
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 609)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-50, -40, 961, 681))
        self.widget.setStyleSheet(u"background-color: #FFFFFF")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(280, 130, 461, 361))
        self.widget_2.setStyleSheet(u"background-color: #BBBFC0; padding: 17px")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 241, 16))
        font = QFont()
        font.setFamilies([u"Tlwg Typist"])
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: black; font-size: 20px; padding: 0px")
        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(360, 10, 71, 21))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Matriculation_Code_input = QLineEdit(self.widget_2)
        self.Matriculation_Code_input.setObjectName(u"Matriculation_Code_input")
        self.Matriculation_Code_input.setGeometry(QRect(100, 90, 251, 31))
        font1 = QFont()
        font1.setFamilies([u"URW Bookman [urw]"])
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.Matriculation_Code_input.setFont(font1)
        self.Matriculation_Code_input.setStyleSheet(u"color: black; padding: 6px; ")
        self.Password_input = QLineEdit(self.widget_2)
        self.Password_input.setObjectName(u"Password_input")
        self.Password_input.setGeometry(QRect(100, 150, 251, 31))
        font2 = QFont()
        font2.setFamilies([u"URW Bookman [urw]"])
        font2.setBold(True)
        font2.setItalic(True)
        self.Password_input.setFont(font2)
        self.Password_input.setStyleSheet(u"color: black; padding: 6px")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 70, 211, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: black; font-size: 13px; padding: 0px")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 130, 111, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: black; font-size: 13px; padding: 0px")
        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 10, 91, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 20, 16, 311))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(self.widget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(420, 20, 16, 311))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5 = QFrame(self.widget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(30, 330, 401, 16))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.Login_buttom = QPushButton(self.widget_2)
        self.Login_buttom.setObjectName(u"Login_buttom")
        self.Login_buttom.setGeometry(QRect(180, 270, 91, 28))
        self.Login_buttom.setStyleSheet(u"padding: 0px; border-radius: 5px; color: black;background-color: #9B9F9F")
        self.See_password = QCheckBox(self.widget_2)
        self.See_password.setObjectName(u"See_password")
        self.See_password.setGeometry(QRect(100, 220, 111, 21))
        self.See_password.setStyleSheet(u"padding: 0px; color: black")
        self.See_password.setTristate(False)
        self.Text_error = QLabel(self.widget_2)
        self.Text_error.setObjectName(u"Text_error")
        self.Text_error.setGeometry(QRect(90, 190, 281, 16))
        self.Text_error.setStyleSheet(u"color: #FF4C4C; padding: 0px")
        self.Text_error.setText('')
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"School Access Portal", None))
        self.Matriculation_Code_input.setText("")
        self.Matriculation_Code_input.setPlaceholderText(QCoreApplication.translate("Form", u"Insert your matriculation code", None))
        self.Password_input.setText("")
        self.Password_input.setPlaceholderText(QCoreApplication.translate("Form", u"Insert your Password", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Your Matriculation Code", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Your Password", None))
        self.Login_buttom.setText(QCoreApplication.translate("Form", u"Login", None))
        self.See_password.setText(QCoreApplication.translate("Form", u"See Password", None))
    # retranslateUi