
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(881, 590)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, -10, 890, 609))
        self.widget.setStyleSheet(u"background-color: #FFFFFF")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(90, 90, 711, 431))
        self.widget_2.setStyleSheet(u"background-color: #BBBFC0; ")
        self.Name_teatcher = QLabel(self.widget_2)
        self.Name_teatcher.setObjectName(u"Name_teatcher")
        self.Name_teatcher.setGeometry(QRect(10, 20, 691, 41))
        font = QFont()
        font.setFamilies([u"Tlwg Typist"])
        self.Name_teatcher.setFont(font)
        self.Name_teatcher.setStyleSheet(u"color: black; font-size: 20px; border: 3px  solid grey")
        self.Name_teatcher.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font3);
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font1);
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 80, 621, 141))
        self.tableWidget.setStyleSheet(u"background-color: #D3D3D3; \n"
"border: 1px solid #A9A9A9; \n"
"border-radius: 10px;\n"
"selection-background-color: #6B8E23;"
"color: black")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.Return_uttom = QPushButton(self.widget_2)
        self.Return_uttom.setObjectName(u"Return_uttom")
        self.Return_uttom.setGeometry(QRect(10, 390, 341, 28))
        self.Return_uttom.setStyleSheet(u"padding: 0px; border-radius: 5px; color: black;background-color: #9B9F9F")
        self.exit_buttom = QPushButton(self.widget_2)
        self.exit_buttom.setObjectName(u"exit_buttom")
        self.exit_buttom.setGeometry(QRect(370, 390, 331, 28))
        self.exit_buttom.setStyleSheet(u"padding: 0px; border-radius: 5px; color: black;background-color: #9B9F9F")
        self.matriculation_code_input = QLineEdit(self.widget_2)
        self.matriculation_code_input.setObjectName(u"matriculation_code_input")
        self.matriculation_code_input.setGeometry(QRect(130, 230, 271, 31))
        font4 = QFont()
        font4.setFamilies([u"URW Bookman [urw]"])
        font4.setBold(True)
        font4.setItalic(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.matriculation_code_input.setFont(font4)
        self.matriculation_code_input.setStyleSheet(u"color: black; \n"
"padding: 6px;\n"
"\n"
"")
        self.search_buttom = QPushButton(self.widget_2)
        self.search_buttom.setObjectName(u"search_buttom")
        self.search_buttom.setGeometry(QRect(440, 230, 131, 31))
        self.search_buttom.setStyleSheet(u"padding: 0px; border-radius: 5px; color: black;background-color: #9B9F9F")
        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setPlaceholderText("Select The Grade Category")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 290, 211, 31))
        self.comboBox.setStyleSheet(u"color: black; background-color: #9B9F9F;selection-color: #9B9F9F; ")
        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 60, 661, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 70, 20, 301))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(670, 70, 31, 301))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(self.widget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(20, 270, 661, 20))
        self.line_4.setStyleSheet(u"")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5 = QFrame(self.widget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(20, 370, 661, 20))
        self.line_5.setStyleSheet(u"")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.grade_input = QLineEdit(self.widget_2)
        self.grade_input.setObjectName(u"grade_input")
        self.grade_input.setGeometry(QRect(220, 340, 81, 31))
        self.grade_input.setStyleSheet(u"color: black")
        self.set_grade_buttom = QPushButton(self.widget_2)
        self.set_grade_buttom.setObjectName(u"set_grade_buttom")
        self.set_grade_buttom.setGeometry(QRect(320, 340, 131, 31))
        self.set_grade_buttom.setStyleSheet(u"padding: 0px; border-radius: 5px; color: black;background-color: #9B9F9F")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Name_teatcher.setText(QCoreApplication.translate("Form", u"Welcome ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        self.tableWidget.setColumnWidth(0,120)
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Math", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"English", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Science", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Art", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Music", None));
        self.Return_uttom.setText(QCoreApplication.translate("Form", u"Return", None))
        self.exit_buttom.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.matriculation_code_input.setText("")
        self.matriculation_code_input.setPlaceholderText(QCoreApplication.translate("Form", u"Insert the student registration code", None))
        self.matriculation_code_input.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.search_buttom.setText(QCoreApplication.translate("Form", u"Search", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Math", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"English", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Science", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Art", None))
        self.comboBox.setStyleSheet("selection-color: black; color: black")
        self.set_grade_buttom.setText(QCoreApplication.translate("Form", u"Set Grade", None))
    # retranslateUi
