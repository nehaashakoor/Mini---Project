import pyrebase
from firebase_admin import credentials
import firebase_admin
import pymongo


firebaseConfig = {
    "apiKey": "AIzaSyC0iPEnlFS8JSHLp_VMDzLkG61mruZ9nGQ",
    "authDomain": "new-project-88982.firebaseapp.com",
    "projectId": "new-project-88982",
    "storageBucket": "new-project-88982.firebasestorage.app",
    "messagingSenderId": "1010621333",
    "appId": "1:1010621333:web:1bb5166cbbebb03ed8b49c",
    "measurementId": "G-M5BYSLBWBV",
    "databaseURL": " "
}


firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db = firebase.database()

cred = credentials.Certificate("C:/Users/hp/Desktop/Selenium OV/MongoDB PYQT5/serviceAccountKey.json.json")
firebase_admin.initialize_app(cred)


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["daraz_db"]


class FirebaseAuth:
    @staticmethod
    def signup_user(email, password):
        try:
            auth.create_user_with_email_and_password(email, password)
            return email
        except Exception as e:
            return str(e)

    @staticmethod
    def login_user(email, password):
        try:
            auth.sign_in_with_email_and_password(email, password)
            return email 
        except Exception as e:
            return str(e)