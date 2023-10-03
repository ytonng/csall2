# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\s\Desktop\demo1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.errorMessageLabel.setGeometry(QtCore.QRect(90, 380, 200, 31))
        self.errorMessageLabel.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 0, 0);\n"
"font: 10pt \"Arial Rounded MT Bold\";")
        self.errorMessageLabel.setObjectName("errorMessageLabel")
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
        self.loginButton.clicked.connect(self.loginClicked)

    def loginClicked(self):
        # Perform validation of username and password
        username = self.usernameEntry.text()
        password = self.passwordEntry.text()

        if username == "your_valid_username" and password == "your_valid_password":
            # Clear the error message if credentials are valid
            self.errorMessageLabel.setText("")
            # Perform any other actions you want upon successful login
        else:
            # Display an error message if credentials are invalid
            self.errorMessageLabel.setText("Invalid username or password")

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

import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())