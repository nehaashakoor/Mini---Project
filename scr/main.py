import sys
from PyQt5 import QtWidgets
from homepage import homepage
from Signinpage import Signin
from Loginpage import Login
from dashboard import Dashboard



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = homepage()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()