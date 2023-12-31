import mysql.connector
import hashlib
import test_rc,re
from PyQt5 import QtCore, QtGui, QtWidgets

def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shoutaaoi4968",
            database="tourism information kiosk"
        )
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1021, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-image: url(:/newPrefix/tourism kiosk/penang tour.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 60, 381, 461))
        self.frame.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:0, stop:0.511364 rgba(0, 156, 221, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 60px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.welcomeLabel = QtWidgets.QLabel(self.frame)
        self.welcomeLabel.setGeometry(QtCore.QRect(20, 10, 231, 101))
        self.welcomeLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.usernameEntry = QtWidgets.QLineEdit(self.frame)
        self.usernameEntry.setGeometry(QtCore.QRect(40, 140, 301, 41))
        self.usernameEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 20px;\n"
"")
        self.usernameEntry.setText("")
        self.usernameEntry.setObjectName("usernameEntry")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(130, 320, 111, 51))
        self.loginButton.setStyleSheet("/* Set the button\'s style */\n"
"QPushButton {\n"
"    background-color: rgb(88, 145, 167); \n"
"    font: 14pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 132);\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 110, 121, 21))
        self.usernameLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setGeometry(QtCore.QRect(40, 220, 121, 21))
        self.passwordLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.passwordLabel.setObjectName("passwordLabel")
        self.forgetPasswordButton = QtWidgets.QPushButton(self.frame)
        self.forgetPasswordButton.setGeometry(QtCore.QRect(250, 290, 91, 21))
        self.forgetPasswordButton.setStyleSheet("/* Set the button\'s style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color:rgb(0, 0, 0) ;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {    \n"
"    color:rgb(255, 0, 0) ;\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"")
        self.forgetPasswordButton.setObjectName("forgetPasswordButton")
        self.passwordEntry = QtWidgets.QLineEdit(self.frame)
        self.passwordEntry.setGeometry(QtCore.QRect(40, 250, 301, 41))
        self.passwordEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 20px;\n"
"")
        self.passwordEntry.setText("")
        self.passwordEntry.setObjectName("passwordEntry")
        self.errorMessageLabel = QtWidgets.QLabel(self.frame)
        self.errorMessageLabel.setGeometry(QtCore.QRect(40, 380, 300, 31))
        self.errorMessageLabel.setStyleSheet("background-color: transparent;\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "font: 10pt \"Arial Rounded MT Bold\";")
        self.errorMessageLabel.setObjectName("errorMessageLabel")
        # Center-align the text
        self.errorMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registrationButton = QtWidgets.QPushButton(self.frame)
        self.registrationButton.setGeometry(QtCore.QRect(90, 410, 191, 31))
        self.registrationButton.setStyleSheet("/* Set the button\'s style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    font: 14pt \"Arial\";\n"
"    color:rgb(0, 0, 0) ;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {    \n"
"    color:rgb(255, 0, 0) ;\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"")
        self.registrationButton.setObjectName("registrationButton")
        self.showPasswordButton = QtWidgets.QPushButton(self.frame)
        self.showPasswordButton.setGeometry(QtCore.QRect(280, 250, 51, 41))
        self.showPasswordButton.setStyleSheet("/* Set the button\'s style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:pressed {\n"
"    ;\n"
"}\n"
"\n"
"\n"
"")
        self.showPasswordButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showPasswordButton.setIcon(icon)
        self.showPasswordButton.setIconSize(QtCore.QSize(35, 35))
        self.showPasswordButton.setObjectName("showPasswordButton")
        self.passwordEntry.raise_()
        self.welcomeLabel.raise_()
        self.usernameEntry.raise_()
        self.loginButton.raise_()
        self.usernameLabel.raise_()
        self.passwordLabel.raise_()
        self.forgetPasswordButton.raise_()
        self.errorMessageLabel.raise_()
        self.registrationButton.raise_()
        self.showPasswordButton.raise_()
        self.penangimg = QtWidgets.QPushButton(self.centralwidget)
        self.penangimg.setGeometry(QtCore.QRect(810, 470, 201, 101))
        self.penangimg.setStyleSheet("background-color: transparent;")
        self.penangimg.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/letstravel.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.penangimg.setIcon(icon2)
        self.penangimg.setIconSize(QtCore.QSize(200, 200))
        self.penangimg.setObjectName("penangimg")
        self.planeimg = QtWidgets.QPushButton(self.centralwidget)
        self.planeimg.setGeometry(QtCore.QRect(830, 30, 171, 101))
        self.planeimg.setStyleSheet("background-color: transparent;")
        self.planeimg.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/travelplane.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.planeimg.setIcon(icon1)
        self.planeimg.setIconSize(QtCore.QSize(150, 150))
        self.planeimg.setObjectName("planeimg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcomeLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Hi, Welcome !</span></p></body></html>"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.usernameLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Username</span></p></body></html>"))
        self.passwordLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Password</span></p></body></html>"))
        self.forgetPasswordButton.setText(_translate("MainWindow", "Forget password?"))
        self.errorMessageLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.registrationButton.setText(_translate("MainWindow", "Register an account"))
        # Connect the showPasswordButton's clicked signal to the toggleShowPassword method
        self.showPasswordButton.clicked.connect(self.toggleShowPassword)

    def toggleShowPassword(self):
        # Toggle the password visibility when the button is clicked
        is_password_visible = self.passwordEntry.echoMode() == QtWidgets.QLineEdit.Normal

        if is_password_visible:
            # Change the icon and set the password mode to Password
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.showPasswordButton.setIcon(icon)
            self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            # Change the icon and set the password mode to Normal
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.showPasswordButton.setIcon(icon)
            self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Normal)



class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(1020, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegistrationWindow.sizePolicy().hasHeightForWidth())
        RegistrationWindow.setSizePolicy(sizePolicy)
        RegistrationWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1021, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-image: url(:/newPrefix/tourism kiosk/penang tour.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 60, 381, 461))
        self.frame.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:0, stop:0.511364 rgba(0, 156, 221, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 60px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.emailEntry = QtWidgets.QLineEdit(self.frame)
        self.emailEntry.setGeometry(QtCore.QRect(40, 140, 301, 31))
        self.emailEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.emailEntry.setText("")
        self.emailEntry.setObjectName("emailEntry")
        self.signupButton = QtWidgets.QPushButton(self.frame)
        self.signupButton.setGeometry(QtCore.QRect(130, 350, 111, 51))
        self.signupButton.setStyleSheet("/* Set the button\'s style */\n"
"QPushButton {\n"
"    background-color: rgb(88, 145, 167); \n"
"    font: 14pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 132);\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"\n"
"")
        self.signupButton.setObjectName("signupButton")
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 30, 111, 31))
        self.usernameLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setGeometry(QtCore.QRect(40, 190, 111, 21))
        self.passwordLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.passwordLabel.setObjectName("passwordLabel")
        self.errorMessageLabel = QtWidgets.QLabel(self.frame)
        self.errorMessageLabel.setGeometry(QtCore.QRect(30, 410, 320, 31))
        self.errorMessageLabel.setStyleSheet("background-color: transparent;\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "font: 10pt \"Arial Rounded MT Bold\";")
        self.errorMessageLabel.setObjectName("errorMessageLabel")
        # Center-align the text
        self.errorMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.emailLabel = QtWidgets.QLabel(self.frame)
        self.emailLabel.setGeometry(QtCore.QRect(30, 110, 91, 31))
        self.emailLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.emailLabel.setObjectName("emailLabel")
        self.usernameEntry = QtWidgets.QLineEdit(self.frame)
        self.usernameEntry.setGeometry(QtCore.QRect(40, 60, 301, 31))
        self.usernameEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.usernameEntry.setText("")
        self.usernameEntry.setObjectName("usernameEntry")
        self.passwordEntry = QtWidgets.QLineEdit(self.frame)
        self.passwordEntry.setGeometry(QtCore.QRect(40, 220, 301, 31))
        self.passwordEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.passwordEntry.setText("")
        self.passwordEntry.setObjectName("passwordEntry")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(30, 270, 71, 21))
        self.cityLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.cityLabel.setObjectName("cityLabel")
        self.cityEntry = QtWidgets.QLineEdit(self.frame)
        self.cityEntry.setGeometry(QtCore.QRect(40, 300, 301, 31))
        self.cityEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.cityEntry.setText("")
        self.cityEntry.setObjectName("cityEntry")
        self.planeimg = QtWidgets.QPushButton(self.centralwidget)
        self.planeimg.setGeometry(QtCore.QRect(830, 30, 171, 101))
        self.planeimg.setStyleSheet("background-color: transparent;")
        self.planeimg.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/travelplane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.planeimg.setIcon(icon)
        self.planeimg.setIconSize(QtCore.QSize(150, 150))
        self.planeimg.setObjectName("planeimg")
        self.penangimg = QtWidgets.QPushButton(self.centralwidget)
        self.penangimg.setGeometry(QtCore.QRect(810, 470, 201, 101))
        self.penangimg.setStyleSheet("background-color: transparent;")
        self.penangimg.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/letstravel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.penangimg.setIcon(icon1)
        self.penangimg.setIconSize(QtCore.QSize(200, 200))
        self.penangimg.setObjectName("penangimg")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(40, 20, 51, 51))
        self.backButton.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 0, 127);\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"")
        self.backButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon2)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setObjectName("backButton")
        RegistrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "RegistrationWindow"))
        self.signupButton.setText(_translate("RegistrationWindow", "Signup"))
        self.usernameLabel.setText(_translate("RegistrationWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Username</span></p></body></html>"))
        self.passwordLabel.setText(_translate("RegistrationWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Password</span></p></body></html>"))
        self.errorMessageLabel.setText(_translate("RegistrationWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.emailLabel.setText(_translate("RegistrationWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Email</span></p></body></html>"))
        self.cityLabel.setText(_translate("RegistrationWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">City</span></p></body></html>"))

class Ui_ForgetPasswordWindow(object):
    def setupUi(self, ForgetPasswordWindow):
        ForgetPasswordWindow.setObjectName("ForgetPasswordWindow")
        ForgetPasswordWindow.resize(1020, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ForgetPasswordWindow.sizePolicy().hasHeightForWidth())
        ForgetPasswordWindow.setSizePolicy(sizePolicy)
        ForgetPasswordWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(ForgetPasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1021, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-image: url(:/newPrefix/tourism kiosk/penang tour.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 60, 381, 461))
        self.frame.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:0, stop:0.511364 rgba(0, 156, 221, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 60px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.emailEntry = QtWidgets.QLineEdit(self.frame)
        self.emailEntry.setGeometry(QtCore.QRect(40, 70, 301, 31))
        self.emailEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.emailEntry.setText("")
        self.emailEntry.setObjectName("emailEntry")
        self.saveButton = QtWidgets.QPushButton(self.frame)
        self.saveButton.setGeometry(QtCore.QRect(130, 370, 111, 41))
        self.saveButton.setStyleSheet("/* Set the button\'s style */\n"
"QPushButton {\n"
"    background-color: rgb(88, 145, 167); \n"
"    font: 14pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 132);\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"\n"
"")
        self.saveButton.setObjectName("saveButton")
        self.verificationLabel = QtWidgets.QLabel(self.frame)
        self.verificationLabel.setGeometry(QtCore.QRect(40, 120, 181, 31))
        self.verificationLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.verificationLabel.setObjectName("verificationLabel")
        self.errorMessageLabel = QtWidgets.QLabel(self.frame)
        self.errorMessageLabel.setGeometry(QtCore.QRect(30, 421, 321, 41))
        self.errorMessageLabel.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 0, 0);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.errorMessageLabel.setObjectName("errorMessageLabel")
        self.emailLabel = QtWidgets.QLabel(self.frame)
        self.emailLabel.setGeometry(QtCore.QRect(30, 40, 91, 31))
        self.emailLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.emailLabel.setObjectName("emailLabel")
        self.verificationEntry = QtWidgets.QLineEdit(self.frame)
        self.verificationEntry.setGeometry(QtCore.QRect(40, 150, 211, 31))
        self.verificationEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.verificationEntry.setText("")
        self.verificationEntry.setObjectName("verificationEntry")
        self.newpasswordLabel = QtWidgets.QLabel(self.frame)
        self.newpasswordLabel.setGeometry(QtCore.QRect(30, 190, 181, 51))
        self.newpasswordLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.newpasswordLabel.setObjectName("newpasswordLabel")
        self.newpasswordEntry = QtWidgets.QLineEdit(self.frame)
        self.newpasswordEntry.setGeometry(QtCore.QRect(40, 230, 301, 31))
        self.newpasswordEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.newpasswordEntry.setText("")
        self.newpasswordEntry.setObjectName("newpasswordEntry")
        self.sendButton = QtWidgets.QPushButton(self.frame)
        self.sendButton.setGeometry(QtCore.QRect(270, 150, 71, 31))
        self.sendButton.setStyleSheet("/* Set the button\'s style */\n"
"QPushButton {\n"
"    background-color: rgb(88, 145, 167); \n"
"    font: 12pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 13px;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 132);\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"\n"
"")
        self.sendButton.setObjectName("sendButton")
        self.confirmpasswordLabel = QtWidgets.QLabel(self.frame)
        self.confirmpasswordLabel.setGeometry(QtCore.QRect(20, 280, 231, 31))
        self.confirmpasswordLabel.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.confirmpasswordLabel.setObjectName("confirmpasswordLabel")
        self.confirmpasswordEntry = QtWidgets.QLineEdit(self.frame)
        self.confirmpasswordEntry.setGeometry(QtCore.QRect(40, 310, 301, 31))
        self.confirmpasswordEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial\";\n"
"border-radius: 11px;\n"
"")
        self.confirmpasswordEntry.setText("")
        self.confirmpasswordEntry.setObjectName("confirmpasswordEntry")
        self.planeimg = QtWidgets.QPushButton(self.centralwidget)
        self.planeimg.setGeometry(QtCore.QRect(830, 30, 171, 101))
        self.planeimg.setStyleSheet("background-color: transparent;")
        self.planeimg.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/travelplane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.planeimg.setIcon(icon)
        self.planeimg.setIconSize(QtCore.QSize(150, 150))
        self.planeimg.setObjectName("planeimg")
        self.penangimg = QtWidgets.QPushButton(self.centralwidget)
        self.penangimg.setGeometry(QtCore.QRect(810, 470, 201, 101))
        self.penangimg.setStyleSheet("background-color: transparent;")
        self.penangimg.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/letstravel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.penangimg.setIcon(icon1)
        self.penangimg.setIconSize(QtCore.QSize(200, 200))
        self.penangimg.setObjectName("penangimg")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(40, 20, 51, 51))
        self.backButton.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"/* Change the cursor when hovering */\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 0, 127);\n"
"    cursor: pointer; /* Change cursor to a pointing hand */\n"
"}\n"
"")
        self.backButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\s\\Desktop\\tourism kiosk/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon2)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setObjectName("backButton")
        ForgetPasswordWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ForgetPasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(ForgetPasswordWindow)

    def retranslateUi(self, ForgetPasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        ForgetPasswordWindow.setWindowTitle(_translate("ForgetPasswordWindow", "Forget Password"))
        self.saveButton.setText(_translate("ForgetPasswordWindow", "Save"))
        self.verificationLabel.setText(_translate("ForgetPasswordWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Verification code</span></p></body></html>"))
        self.errorMessageLabel.setText(_translate("ForgetPasswordWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.emailLabel.setText(_translate("ForgetPasswordWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Email</span></p></body></html>"))
        self.newpasswordLabel.setText(_translate("ForgetPasswordWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">New Password</span></p></body></html>"))
        self.sendButton.setText(_translate("ForgetPasswordWindow", "Send"))
        self.confirmpasswordLabel.setText(_translate("ForgetPasswordWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Confirm Password</span></p></body></html>"))

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the login button to the login function
        self.ui.loginButton.clicked.connect(self.login)

        self.ui.forgetPasswordButton.clicked.connect(self.show_forgetpassword_window)

        # Connect the registration button to show the registration window
        self.ui.registrationButton.clicked.connect(self.show_registration_window)

    def login(self):
        # Implement your login logic here
        # You can access the entered username and password like this:
        username = self.ui.usernameEntry.text()
        password = self.ui.passwordEntry.text()

        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shoutaaoi4968",
            database="tourism information kiosk"
        )

        cursor = db_connection.cursor()

        # Hash the entered password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Execute a query to check if the provided username and hashed password match any records
        query = "SELECT * FROM User WHERE user_name = %s AND Password = %s"
        cursor.execute(query, (username, hashed_password))
        user = cursor.fetchone()

        if user is not None:
            # Clear the error message if credentials are valid
            self.ui.errorMessageLabel.setText("Login successful")
            # Perform any other actions you want upon successful login
        else:
            # Display an error message if credentials are invalid
            error_message = "Invalid username or password. Please try again."
            self.ui.errorMessageLabel.setText(error_message)

    def show_registration_window(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.ui.backButton.clicked.connect(self.close_registration_window)
        self.registration_window.show()
        self.hide()

    def show_forgetpassword_window(self):
        self.forgetpassword_window = ForgetPasswordWindow()
        self.forgetpassword_window.ui.backButton.clicked.connect(self.close_forgetpassword_window)
        self.forgetpassword_window.show()
        self.hide()

    def close_registration_window(self):
        self.registration_window.close()
        self.show()
    def close_forgetpassword_window(self):
        self.forgetpassword_window.close()
        self.show()

class RegistrationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistrationWindow()
        self.ui.setupUi(self)

        # Connect the signup button to the registration function
        self.ui.signupButton.clicked.connect(self.register)

    def username_exists(self, username):  # Updated method signature
        db_connection = connect_to_database()
        if db_connection:
            try:
                cursor = db_connection.cursor()
                query = "SELECT COUNT(*) FROM User WHERE user_name = %s"
                cursor.execute(query, (username,))
                result = cursor.fetchone()[0]
                return result > 0
            except mysql.connector.Error as err:
                print(f"Error checking username existence: {err}")
            finally:
                cursor.close()
                db_connection.close()
        return False

    def email_exists(self, email):  # Updated method signature
        db_connection = connect_to_database()
        if db_connection:
            try:
                cursor = db_connection.cursor()
                query = "SELECT COUNT(*) FROM User WHERE email = %s"
                cursor.execute(query, (email,))
                result = cursor.fetchone()[0]
                return result > 0
            except mysql.connector.Error as err:
                print(f"Error checking email existence: {err}")
            finally:
                cursor.close()
                db_connection.close()
        return False

    def perform_registration(self, username, password, email, city):  # Updated method signature
        db_connection = connect_to_database()
        if db_connection:
            try:
                cursor = db_connection.cursor()
                # Hash the password
                hashed_password = hashlib.sha256(password.encode()).hexdigest()

                # Insert the user data into the User table
                query = "INSERT INTO User (user_name, Password, email, city) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (username, hashed_password, email, city))

                # Commit the changes to the database
                db_connection.commit()

                return True  # Registration successful
            except mysql.connector.Error as err:
                print(f"Error performing registration: {err}")
            finally:
                cursor.close()
                db_connection.close()
        return False  # Registration failed

    def register(self):
        # Access user input
        username = self.ui.usernameEntry.text()
        password = self.ui.passwordEntry.text()
        email = self.ui.emailEntry.text()
        city = self.ui.cityEntry.text()

        # Validate inputs
        if not username or not password or not email or not city:
            self.ui.errorMessageLabel.setText("Please fill in all the fields.")
        elif not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email):
            self.ui.errorMessageLabel.setText("Invalid email address.")
        elif len(password) <= 8:
            self.ui.errorMessageLabel.setText("Password must be longer than 8 characters.")
        elif self.username_exists(username):
            self.ui.errorMessageLabel.setText("Username already exists.")
        elif self.email_exists(email):
            self.ui.errorMessageLabel.setText("Email already registered.")
        else:
            # Perform the actual registration process
            if self.perform_registration(username, password, email, city):
                self.ui.errorMessageLabel.setText("Registration successful!")
            else:
                self.ui.errorMessageLabel.setText("Registration failed. Please try again later.")

class ForgetPasswordWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ForgetPasswordWindow()
        self.ui.setupUi(self)
        self.verification_code = None
        self.ui.sendButton.clicked.connect(self.send)
        self.ui.saveButton.clicked.connect(self.save)

    def send(self):
        email = self.ui.emailEntry.text()

        if not email:
            # If the email field is empty, show an error message
            self.ui.errorMessageLabel.setText("Please enter your email.")
            return  # Don't proceed further

        from google_auth_oauthlib.flow import InstalledAppFlow
        from email.mime.text import MIMEText
        import base64
        import random
        import string

        # Define the scopes
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']

        # Load credentials from the client_secret.json file
        flow = InstalledAppFlow.from_client_secrets_file(
            r"C:\Users\s\Downloads\client_secret_379816141851-frjap9raqtnjcn5t8t97v51vmum6te8e.apps.googleusercontent.com.json",
            SCOPES)

        # Run the OAuth flow
        credentials = flow.run_local_server(port=0)

        from googleapiclient.discovery import build

        def send_verification_email(to, subject):
            service = build('gmail', 'v1', credentials=credentials)
            verification_code = ''.join(random.choice(string.digits) for _ in range(6))
            message = create_message('me', to, subject, f'Your verification code is: {verification_code}')
            send_message(service, 'me', message)
            self.verification_code = verification_code

        def create_message(sender, to, subject, message_text):
            message = MIMEText(message_text)
            message['to'] = to
            message['subject'] = subject
            return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        def send_message(service, user_id, message):
            try:
                message = service.users().messages().send(userId=user_id, body=message).execute()
                print(f"Message sent. Message Id: {message['id']}")
            except Exception as e:
                print(f"An error occurred: {e}")

        # Example usage:

        send_verification_email('usermapping1@gmail.com', 'Password Reset')
        # Implement code to send a verification code to the provided email address
        # You can add logic to handle successful or failed sending of the code.

        # Clear any previous error messages
        self.ui.errorMessageLabel.setText("")

    def save(self):
        newpassword = self.ui.newpasswordEntry.text()
        confirmpassword = self.ui.confirmpasswordEntry.text()

        if newpassword == confirmpassword:
            # Passwords match, you can proceed to reset the password.

            # Establish a database connection
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="shoutaaoi4968",
                database="tourism information kiosk"
            )

            # Check if the connection was successful
            if db_connection:
                try:
                    cursor = db_connection.cursor()
                    email = self.ui.emailEntry.text()

                    # Hash the new password
                    hashed_password = hashlib.sha256(confirmpassword.encode()).hexdigest()

                    # Update the user's password in the database
                    update_query = "UPDATE user SET Password = %s WHERE email = %s"
                    cursor.execute(update_query, (hashed_password, email))
                    db_connection.commit()

                    # Close the cursor and database connection
                    cursor.close()
                    db_connection.close()

                    # Set a success message in your UI
                    self.ui.errorMessageLabel.setText(f"Password successfully reset. ")
                except mysql.connector.Error as err:
                    print(f"Error updating the password in the database: {err}")
            else:
                self.ui.errorMessageLabel.setText("Database connection failed.")
        else:
            # Passwords do not match, show an error message to the user.
            self.ui.errorMessageLabel.setText("Passwords do not match.")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())