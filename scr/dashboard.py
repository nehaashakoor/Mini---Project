from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from firebase_config import auth, db
from Scraper import DarazScraper
from viewdatascrape import ViewScrapedData

class Dashboard(QtWidgets.QWidget):
    def __init__(self,user_email):
        super().__init__()
        self.user_id = user_email
        self.scraper = DarazScraper() 
        self.db = self.scraper.db
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dashboard")
        self.resize(1200, 700)
        self.setStyleSheet("QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 rgba(0, 0, 0, 255),  /* Top - Black */\n"
"                                stop:1 rgba(0, 128, 128, 255)); /* Bottom - Teal */\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(500, 50, 361, 41))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:None;\n"
"font: 75 20pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(370, 230, 161, 41))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:None;\n"
"font: 75 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(280, 320, 261, 41))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:None;\n"
"font: 75 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(530, 80, 201, 16))
        self.line.setStyleSheet("background-color:None\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(560, 230, 301, 41))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    font: 14pt \"Times New Roman\";\n"
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
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 320, 381, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    font: 14pt \"Times New Roman\";\n"
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
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(570, 370, 361, 16))
        self.label_4.setStyleSheet("color:rgb(255, 0, 4);\n"
"background-color:None;\n"
"font: 75 9pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setVisible(False)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(320, 470, 231, 41))
        self.pushButton.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:rgb(170, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";\n"
"border-radius:10px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 470, 231, 41))
        self.pushButton_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:rgb(0, 136, 204);\n"
"font: 75 14pt \"Times New Roman\";\n"
"border-radius:10px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(420, 560, 361, 31))
        self.label_5.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:None;\n"
"font: 75 13pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.label_5.setVisible(False)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Daraz Product Scraper"))
        self.label_2.setText(_translate("Form", "Enter Product Name "))
        self.label_3.setText(_translate("Form", "Enter MongoDB Collection Name"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "Scrape Data"))
        self.pushButton.clicked.connect(self.start_scraping)
        self.pushButton_2.setText(_translate("Form", "View Scrape Data"))
        self.pushButton_2.clicked.connect(self.view_scraped_data)
        self.label_5.setText(_translate("Form", "TextLabel"))


    def scrape_data(self):
        product_name = self.search_input.text()
        scraper = DarazScraper()  
        data = scraper.scrape(product_name) 
        self.label_5.setText("Start Scraping...")
        self.label_5.setVisible(True) 
        if data:
            for item in data:
                item["user_email"] = self.user_email 
            db.scraped_data.insert_many(data)
            self.label_5.setText("Data scraped and saved successfully!")
            self.label_5.setVisible(True)
            
        else:
            self.label_5.setText("No data Found")
            self.label_5.setVisible(True)
            

    def start_scraping(self):
        search_query = self.lineEdit.text().strip()
        collection_name = "scraped data"

        if not search_query:
            self.label_4.setText("Please Enter the product name")
            self.label_4.setVisible(True)
            return

        scraper = DarazScraper()
        data = scraper.scrape(search_query , collection_name)

        if data:
            for item in data:
                item["user_email"] = self.user_id  
            db.scraped_data.insert_many(data)
            self.label_4.setText("Scraping Completed and Data Saved!")
            self.label_4.setVisible(False)

        else:
            self.label_4.setText("No data found!")
            self.label_4.setVisible(True)

        scraper = DarazScraper()
        data = list(db.scraped_data.find({"user_email": self.user_id})) 
        self.label_5.setText("Scraping Completed")
        self.label_5.setVisible(True)

    def view_scraped_data(self):
        self.view_window = ViewScrapedData(self.user_id)
        self.view_window.show()