from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QBrush, QColor, QFont, QIcon
from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QHBoxLayout
)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(900, 600)

        # Main Widget
        self.main_widget = QWidget(Form)
        self.main_widget.setObjectName("main_widget")
        self.main_widget.setGeometry(QRect(0, 0, 900, 600))
        self.main_widget.setStyleSheet("background-color: #E0E0E0;")

        # Inner Widget with Border and Rounded Corners
        self.inner_widget = QWidget(self.main_widget)
        self.inner_widget.setObjectName("inner_widget")
        self.inner_widget.setGeometry(QRect(100, 70, 700, 450))
        self.inner_widget.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 25px;
            border: 2px solid #A9A9A9;
        """)

        # Vertical Layout for Inner Widget
        self.verticalLayout = QVBoxLayout(self.inner_widget)

        # Welcome Label
        self.Name_Student = QLabel(self.inner_widget)
        self.Name_Student.setObjectName("Name_Student")
        self.Name_Student.setFont(QFont("Tlwg Typist", 18))
        self.Name_Student.setStyleSheet("color: black;")
        self.Name_Student.setAlignment(Qt.AlignCenter)# type: ignore
        self.verticalLayout.addWidget(self.Name_Student)

        # Table Widget
        self.tableWidget = QTableWidget(self.inner_widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("""
            background-color: #D3D3D3; 
            border: 1px solid #A9A9A9; 
            border-radius: 10px;
            selection-background-color: #6B8E23;
            color: black;
            selection-color: black;
        """)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)# type: ignore
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)# type: ignore
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)# type: ignore
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setTextElideMode(Qt.ElideRight)# type: ignore

        if self.tableWidget.columnCount() < 6:
            self.tableWidget.setColumnCount(6)

        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)# type: ignore
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)

        header_labels = ["Math", "English", "Science", "Art", "Music", "Semester"]
        for i, label in enumerate(header_labels):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)# type: ignore
            item.setFont(font1)
            item.setForeground(brush)
            self.tableWidget.setHorizontalHeaderItem(i, item)

        self.verticalLayout.addWidget(self.tableWidget)

        # Average Grades Label
        self.average_grades_label = QLabel(self.inner_widget)
        self.average_grades_label.setObjectName("average_grades_label")
        self.average_grades_label.setFont(QFont("Tlwg Typist", 18))
        self.average_grades_label.setStyleSheet("color: black;")
        self.average_grades_label.setAlignment(Qt.AlignCenter)# type: ignore
        self.verticalLayout.addWidget(self.average_grades_label)

        # Horizontal Layout for Buttons
        self.button_layout = QHBoxLayout()

        # Return Button
        self.Return_buttom = QPushButton(self.inner_widget)
        self.Return_buttom.setObjectName("Return_buttom")
        self.Return_buttom.setIcon(QIcon("return_icon.png"))  # Add icon path here
        self.Return_buttom.setStyleSheet("""
            padding: 5px; 
            border-radius: 5px; 
            color: black;
            background-color: #9B9F9F;
            font-size: 16px;
        """)
        self.button_layout.addWidget(self.Return_buttom)

        # Exit Button
        self.exit_buttom = QPushButton(self.inner_widget)
        self.exit_buttom.setObjectName("exit_buttom")
        self.exit_buttom.setIcon(QIcon("exit_icon.png"))  # Add icon path here
        self.exit_buttom.setStyleSheet("""
            padding: 5px; 
            border-radius: 5px; 
            color: black;
            background-color: #9B9F9F;
            font-size: 16px;
        """)
        self.button_layout.addWidget(self.exit_buttom)

        self.verticalLayout.addLayout(self.button_layout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.Name_Student.setText(QCoreApplication.translate("Form", "Welcome ", None))
        header_labels = ["Math", "English", "Science", "Art", "Music", "Semester"]
        for i, label in enumerate(header_labels):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(QCoreApplication.translate("Form", label, None))
        self.average_grades_label.setText(QCoreApplication.translate("Form", "The average of your grades is: 34", None))
        self.Return_buttom.setText(QCoreApplication.translate("Form", "Return", None))
        self.exit_buttom.setText(QCoreApplication.translate("Form", "Exit", None))
