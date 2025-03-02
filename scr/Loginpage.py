from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from firebase_config import auth, db
from dashboard import Dashboard
from firebase_config import FirebaseAuth


class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.pushButton.clicked.connect(self.login)
        self.error.setVisible(False)

    def setupUi(self):
        self.setObjectName("Login")
        self.resize(500, 598)
        self.setStyleSheet("QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 rgba(0, 0, 0, 255),  /* Top - Black */\n"
"                                stop:1 rgba(0, 128, 128, 255)); /* Bottom - Teal */\n"
"}\n"
"")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(190, 150, 121, 16))
        self.line.setStyleSheet("background-color:None\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(180, 120, 181, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Times New Roman\";\n"
"background-color:None\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(120, 240, 281, 41))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setTabletTracking(True)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    font: 12pt \"Times New Roman\";\n"
"    color:rgb(255, 255, 255);\n"
"    border: 2px solid rgb(100, 100, 100);\n"
"    border-radius: 20px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    background-color: rgb(34, 34, 34);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(96, 96, 96);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(0, 150, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 320, 281, 41))
        self.lineEdit_2.setMouseTracking(True)
        self.lineEdit_2.setTabletTracking(True)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    font: 12pt \"Times New Roman\";\n"
"    color:rgb(255, 255, 255);\n"
"    border: 2px solid rgb(100, 100, 100);\n"
"    border-radius: 20px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    background-color: rgb(34, 34, 34);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(96, 96, 96);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(0, 150, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(50)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(200, 430, 111, 31))
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
        self.pushButton.setObjectName("pushButton")
        self.error = QtWidgets.QLabel(self)
        self.error.setGeometry(QtCore.QRect(130, 370, 271, 16))
        self.error.setStyleSheet("color:rgb(255, 2, 6);\n"
"background-color:None;\n"
"font: 75 11pt \"Times New Roman\";")
        self.error.setObjectName("error")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Log-In Account"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Your Mail ..."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Your Password ..."))
        self.pushButton.setText(_translate("Form", "Log-In"))
        self.pushButton.clicked.connect(self.open_dashboard)
        
    def login(self):
        email = self.lineEdit.text().strip()  
        password = self.lineEdit_2.text().strip()   
    
        if not email or not password:
           self.error.setText("Enter Your Email and Password")
           self.error.setVisible(True)
           return

        try:
            firebase_response = auth.sign_in_with_email_and_password(email, password)
            user_email = firebase_response.get("email", "unknown_user")
            self.error.setText("Logged in successfully!")
            self.error.setVisible(True)  
            self.close()  
            self.open_dashboard(user_email)
        except Exception as e:
            error_message = str(e)
            if "EMAIL_NOT_FOUND" in error_message:
               self.error.setText("Enter Your Mail")
            elif "INVALID_PASSWORD" in error_message:
               self.error.setText("Enter Your Password")
            else:
                self.error.setText("Failed to log In")

            self.error.setVisible(True)

    def open_dashboard(self, user_email):
        self.dashboard_window = Dashboard(user_email)
        self.dashboard_window.show()
