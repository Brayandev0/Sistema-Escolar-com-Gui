from abc import abstractmethod,ABC
import pymysql
import sys
import hashlib
from PySide6.QtWidgets import QApplication, QWidget,QMainWindow,QStackedWidget,QLineEdit,QCheckBox,QMenuBar,QMessageBox,QTableWidgetItem
from PySide6.QtCore import Signal
import portal_de_acesso
import Painel_de_alunos
import  Painel_dos_professores


class Central_Page(QMainWindow):

     def __init__(self) :
             super().__init__()
             self.setFixedSize(880,609)
             self.menu_bar()
             self.setWindowTitle("School System")
             self.stacked = QStackedWidget()
             self.Login_page = Acess_Portal()
             self.grades_page = Grades_Page()
             self.teatcher_page = Teatcher_Page()
             self.setCentralWidget(self.stacked)
             self.stacked.addWidget(self.Login_page)
             self.stacked.addWidget(self.teatcher_page)
             self.stacked.addWidget(self.grades_page)
             self.stacked.setCurrentWidget(self.Login_page)
             self.Login_page.StudentLoged.connect(lambda : self.setting_student_info())
             self.Login_page.Teatcher_logged.connect(lambda: self.setting_teatcher_info())
             self.grades_page.return_grades.connect(lambda: self.return_to_login())
             self.teatcher_page.return_signal.connect(lambda: self.return_to_login())
     
     def return_to_login(self):
          self.Login_page.clean_inputs()
          self.stacked.setCurrentWidget(self.Login_page)
     def menu_bar(self):
             alert : Qmessage_error = Show_success_alert()
             qmenu = self.menuBar()
             qmenu.setStyleSheet("background-color: #BBBFC0; color:black")
             menu = qmenu.addMenu("Help Menu")
             i_not_know_password = menu.addAction("I do Not Know My Password")
             i_not_know_matriculation = menu.addAction("I do Not know My Matriculation Code")
             i_not_know_password.triggered.connect(lambda: alert.show_message_error('Your Password is your date of birth, in the format dd/mm/year ') )
             i_not_know_matriculation.triggered.connect(lambda: alert.show_message_error('Contact The School Secretary To obtain the registration code') )

     def setting_student_info(self):
          self.grades_page.setter_informations_to_table(self.Login_page.id_to_student)
          self.stacked.setCurrentWidget(self.grades_page)
     def setting_teatcher_info(self):
          self.stacked.setCurrentWidget(self.teatcher_page)
          self.teatcher_page.setter_name_teatcher(self.Login_page.name__user)


class Acess_Portal(QWidget):
    StudentLoged = Signal()
    Teatcher_logged = Signal()

    def __init__(self) :
        super().__init__()
        self.id_to_student = 0
        self.Page = portal_de_acesso.Ui_Form()
        self.db : Mysql_Consult = consult_in_database()
        self.encrypt_data : Encrypter = sha512_encrypt()
        self.show_messages_error : Qmessage_error = Show_alert_error()
        self.Page.setupUi(self)
        self.Page.Password_input.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.Page.See_password.checkStateChanged.connect(lambda: self.See_password_func())
        self.Page.Login_buttom.clicked.connect(lambda: self.Log_in() )
   
    # Displays Password in the window 
    def See_password_func(self):
        if QCheckBox.isChecked(self.Page.See_password):
            self.Page.Password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else: 
            self.Page.Password_input.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
    # execute the Login 

    def Log_in(self):
         print('dgdfgd')
         if self.testing_login_inputs():
              print("entrou_login input")
              if self.search_consult_data():
                    print(self.permission)
                    if self.permission == "Teatcher":
                         self.Teatcher_logged.emit()
                         return True
                    self.StudentLoged.emit()
    # Verify values in Login inputs

    def clean_inputs(self):
         self.Page.Password_input.setText("")
         self.Page.Matriculation_Code_input.setText("")

    def search_consult_data(self):
         print("consulta search def ")
         matriculation_code_criptografy = self.encrypt_data.encript_Data(self.Page.Matriculation_Code_input.text())
         result = self.db.consult_in_db(' SELECT * FROM Students WHERE MatriculationCode = %s AND Birth = %s ',(matriculation_code_criptografy,self.convert_(self.Page.Password_input.text())))
         if result and result != 0:
              self.id_to_student,self.name__user,*args = result[0]
              permission__ = self.db.consult_in_db("SELECT Permission FROM Students WHERE id = %s ",(str(self.id_to_student)))
              self.permission = permission__[0][0] 
              print(self.permission)
              return True
         self.show_messages_error.show_message_error("The informations entered is incorrect")
         return False
    
    def testing_login_inputs(self):
        matriculation_code = self.Page.Matriculation_Code_input.text()
        password = self.Page.Password_input.text()
        length_password = len(password)
        if not matriculation_code or not password:
               self.show_messages_error.show_message_error("The fields are empty")
               return False
        elif len(matriculation_code) < 10 or len(matriculation_code) > 10:
              self.show_messages_error.show_message_error("your school registration code is invalid")
              return False
        elif length_password > 8 or length_password < 8:
             self.show_messages_error.show_message_error("Your Password is invalid ")
             return False
        try:
            int(matriculation_code)
            int(password)
        except ValueError:
            self.show_messages_error.show_message_error("Your Matriculation Code or Your Password of inválid")
            return False
        return True
    def convert_(self,date):
        dia = date[0:2]
        mes = date[2:4]
        mes += '-'
        ano = date[4:8]
        ano += '-'
        return sha512_encrypt().encript_Data(ano + mes + dia)
             

class Grades_Page(QWidget):
     return_grades = Signal()

     def __init__(self) :
          super().__init__()
          self.page = Painel_de_alunos.Ui_Form()

          self.page.setupUi(self)
          self.page.exit_buttom.clicked.connect(lambda: exit(0))
          self.page.Return_buttom.clicked.connect(lambda: self.prepare_return())
     def inserto_to_table(self):
          coluna = 0
          grades = (self.math,self.english,self.science,self.art,self.music,self.semester)
          self.linha = self.page.tableWidget.rowCount()
          self.page.tableWidget.insertRow(self.linha)
          for a in grades:
               self.data = QTableWidgetItem(str(a))
               self.page.tableWidget.setItem(self.linha,coluna,self.data)
               coluna += 1
     def prepare_return(self):
          self.page.tableWidget.removeRow(self.linha)
          self.return_grades.emit()
     def setter_informations_to_table(self,id):
          self.consult_page = consult_in_database()
          data = self.consult_page.consult_in_db('SELECT * FROM Grades WHERE id = %s',(id))
          for a in data:
               *args,self.name,self.math,self.english,self.science,self.art,self.music,self.semester = a
               self.average_total = self.math + self.english + self.science + self.art + self.music
               self.average_total = self.average_total / 5
               print(self.average_total)
          self.page.Name_Student.setText(f"Welcome {self.name}")
          self.page.average_grades_label.setText(f"The Average of your Grades is {self.average_total}  ")
          self.inserto_to_table()


class Teatcher_Page(QWidget):
     return_signal = Signal()
     def __init__(self, ) :
          super().__init__()
          self.linha = 9
          self.log_error : Qmessage_error = Show_alert_error()
          self.page = Painel_dos_professores.Ui_Form()
          self.consult_page : Mysql_Consult = consult_in_database()
          self.page_encript : Encrypter = sha512_encrypt()
          self.page.setupUi(self)
          self.page.search_buttom.clicked.connect(lambda: self.search_user())
          self.page.set_grade_buttom.clicked.connect(lambda: self.setting_new_grades())
          self.page.Return_uttom.clicked.connect(lambda: self.return_signal.emit())
          self.page.exit_buttom.clicked.connect(lambda: exit())
     def setter_name_teatcher(self,name):
          self.page.Name_teatcher.setText(f"Welcome Sr {name}")

     def search_user(self):

          if self.linha == 0:
               self.page.tableWidget.removeRow(self.linha)
          matriculation_encripted = self.page_encript.encript_Data(self.page.matriculation_code_input.text())
          Data_requisition = self.consult_page.consult_in_db('SELECT * FROM Students WHERE MatriculationCode = %s',matriculation_encripted)
          if Data_requisition or Data_requisition != 0:
               for i in Data_requisition:
                    Grades_data = self.consult_page.consult_in_db('SELECT * FROM Grades WHERE id = %s',i[0])
                    for items in Grades_data:
                         print("correto")
                         try:
                              self.id_student,self.name,self.math,self.english,self.science,self.art,self.music,w = items
                              print(self.math)
                         except AttributeError:
                              self.log_error.show_message_error("The Matriculation Code insered not are on student")
                              return False
                         print(self.id_student)
                    self.Insert_data_table()
                    return True
          self.log_error.show_message_error("The Matriculation Code Insered is inválid")
          return False
     def setting_new_grades(self):
          if self.verify_grade_input():
               match self.page.comboBox.currentText():
                    case 'Math':
                         table = 'Mathematics'
                         column = 1
                    case 'English':
                         table = 'English'
                         column = 2
                    case 'Science':
                         table = 'Science'
                         column = 3
                    case 'Art':
                         table = 'Art'
                         column = 4
                    case 'Music':
                         table = 'Music'
                         column = 5
                    case _:
                         self.log_error.show_message_error("Your Not Selected one Category Grade")
                         return False
               a = self.consult_page.consult_in_db(f"UPDATE Grades SET {table} = {self.page.grade_input.text()} WHERE id = %s ",(self.id_student))
               if not a or a == 0:
                    self.log_error.show_message_error("The matriculation Code insered is Incorrect")
                    return False
               item = QTableWidgetItem(self.page.grade_input.text())
               self.page.tableWidget.setItem(0,column,item)


     def verify_grade_input(self):
          grade_input_data = self.page.grade_input.text()
          try: 
               float(grade_input_data)
               self.id_student
               int(self.page.matriculation_code_input.text())
          except ValueError:
               self.log_error.show_message_error("The Grade Insered Is inválid")
               return False
          except AttributeError:
               self.log_error.show_message_error("Your Not selected one Student")
               return False
          if not grade_input_data:
               self.log_error.show_message_error("The field of Grades is empty")
               return False
          if float(grade_input_data) > 100:
               self.log_error.show_message_error("The Grade Insered Is inválid")
               return False
          if not self.page.matriculation_code_input.text():
               self.log_error.show_message_error("your not insered the matriculation code of Student")
          return True
          
               
     def Insert_data_table(self):
          coluna = 0
          try:
               grades = (self.name,self.math,self.english,self.science,self.art,self.music,)
          except AttributeError:
               self.log_error.show_message_error("The matriculation Code insered not are of Student")
               return False
          self.linha = self.page.tableWidget.rowCount()
          print(self.linha)
          self.page.tableWidget.insertRow(self.linha)
          for a in grades:
               a = str(a)
               self.data = QTableWidgetItem(a)
               self.page.tableWidget.setItem(self.linha,coluna,self.data)
               coluna += 1



class  Mysql_Consult(ABC):
     @abstractmethod
     def consult_in_db(self,consulta : str, dados: tuple | str) -> str:
          pass


class consult_in_database(Mysql_Consult):


    def consult_in_db(self,consulta  : str,dados : tuple | str) :
        print("conectou")
        self.mysql_conection = pymysql.connect(host='localhost',
                                                user='root',
                                                password='admin',
                                                database='Banco_de_Dados')
        self.cursor = self.mysql_conection.cursor()
        self.cursor.execute(consulta,(dados))
        self.mysql_conection.commit()
        self.mysql_conection.close()
        self.cursor.close()
        return self.cursor.fetchall()


class Encrypter(ABC):
     @abstractmethod
     def encript_Data(self,data : str) -> str:
          pass
     

class sha512_encrypt(Encrypter) :

     def encript_Data(self,data: str) -> str:
        hash = hashlib.sha512()
        hash.update(data.encode('utf-8'))
        return hash.hexdigest()
     

class Qmessage_error(ABC):
     @abstractmethod
     def show_message_error(self,txt : str):
          pass


class Show_alert_error(Qmessage_error):
    
    def show_message_error(self, txt: str):
          error = QMessageBox()
          error.setText(txt)
          error.setIcon(QMessageBox.Icon.Critical)
          error.setWindowTitle("Error")
          error.exec()


class Show_success_alert(Qmessage_error):
     def show_message_error(self, txt: str):
          error = QMessageBox()
          error.setText(txt)
          error.setIcon(QMessageBox.Icon.Information)
          error.setWindowTitle("Alert")
          error.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Central_Page()
    janela.show()
    app.exec()
