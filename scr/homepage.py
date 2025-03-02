from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from firebase_config import auth, db
from Signinpage import Signin  
from Loginpage import Login
from dashboard import Dashboard 
from viewdatascrape import ViewScrapedData

class homepage(QtWidgets.QWidget): 
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(500, 598)
        self.setStyleSheet("QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 rgba(0, 0, 0, 255),  /* Top - Black */\n"
"                                stop:1 rgba(0, 128, 128, 255)); /* Bottom - Teal */\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 120, 251, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Times New Roman\";\n"
"background-color:None\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 260, 131, 31))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"color:rgb(0, 0, 0);\n"
"font: 14pt \"Times New Roman\";\n"
"border-radius: 5px;\n"
"border-color:rgb(176, 176, 176);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton#puchButton:pressed{\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"background-color:rgb(170, 255, 255);\n"
"}")
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 330, 131, 31))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"color :rgb(0, 0, 0);\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"background-color:rgb(170, 255, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(150, 150, 201, 16))
        self.line.setStyleSheet("background-color:None\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Firebase - Authentication"))
        self.pushButton.setText(_translate("Form", "Sign-In"))
        self.pushButton.clicked.connect(self.open_signin)
        self.pushButton_2.setText(_translate("Form", "Log-In"))
        self.pushButton_2.clicked.connect(self.open_login)


    def open_signin(self):
        self.signin_window = Signin()
        self.signin_window.show()


    def open_login(self):
        self.login_window = Login()
        self.login_window.show()
        

    def open_dashboard(self, user_email):
        self.dashboard_window = Dashboard(user_email)
        self.dashboard_window.show()


    def view_scraped_data(self):
        self.view_window = ViewScrapedData(self.user_id)
        self.view_window.show()


    