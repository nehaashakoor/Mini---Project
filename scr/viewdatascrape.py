from PyQt5 import QtWidgets
import sys
from firebase_config import db
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class ViewScrapedData(QtWidgets.QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Scraped Data")
        self.resize(1200, 700)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
                stop:0 #000000, stop:1 #008080);
            }
            QTableWidget {
background-color: transparent; 
color: white;  
border: 2px solid #444;  
font-size: 14px;
            }
            QHeaderView::section {
background-color: #005f5f;
color: white;
padding: 5px;
font-weight: bold;
border: 1px solid #004040;
            }
            QTableWidget::item {
                padding: 5px;
            }
""")

       
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(50, 50, 1100, 600)
        self.load_data()

    def load_data(self):
        data = list(db.scraped_data.find({"user_email": self.user_id})) 

        if not data:
            return

        headers = list(data[0].keys())
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)
        self.table_widget.setRowCount(len(data))

        for row, item in enumerate(data):
           for col, key in enumerate(headers):
               self.table_widget.setItem(row, col, QTableWidgetItem(str(item.get(key, "N/A"))))

        self.table_widget.horizontalHeader().setStretchLastSection(True)

