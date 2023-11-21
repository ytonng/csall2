import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout,QDateEdit,QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from functools import partial
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime
common_font = QFont("Arial", 12)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, user_id=7):
        super(MainWindow, self).__init__()
        self.user_id = user_id
        self.ui = Ui_MainWindow(self, user_id)
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

    def set_user_id(self, user_id):
        self.user_id = user_id
        print(f"User ID set to: {user_id}")

    def open_booking_page_2(self):
        # Set the current index of stackedWidget to 8 (page_9)
        self.ui.stackedWidget.setCurrentIndex(8)

    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex()
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    ## functions for changing menu page
    def on_attraction_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_attraction_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_profile_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_profile_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_history_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_history_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_booking_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_booking_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_deal_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_deal_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_chatbot_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_chatbot_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_feedback_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_feedback_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_map_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_map_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_quiz_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def on_quiz_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(9)

class Ui_MainWindow(object):
    def __init__(self, MainWindow, user_id):
        self.user_id = user_id
        self.MainWindow = MainWindow

    def set_user_id(self, user_id):
        self.user_id = user_id
        print(f"User ID set to: {user_id}")

    def setupUi(self, MainWindow):
        print(f"User ID set to: {self.user_id}")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setStyleSheet("")
        self.logo_label_1.setText("")
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 30, -1, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.attraction_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.attraction_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("attraction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attraction_btn_1.setIcon(icon)
        self.attraction_btn_1.setCheckable(True)
        self.attraction_btn_1.setAutoExclusive(True)
        self.attraction_btn_1.setObjectName("attraction_btn_1")
        self.verticalLayout.addWidget(self.attraction_btn_1)
        self.profile_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.profile_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_btn_1.setIcon(icon1)
        self.profile_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.profile_btn_1.setCheckable(True)
        self.profile_btn_1.setAutoExclusive(True)
        self.profile_btn_1.setObjectName("profile_btn_1")
        self.verticalLayout.addWidget(self.profile_btn_1)
        self.history_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.history_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.history_btn_1.setIcon(icon2)
        self.history_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.history_btn_1.setCheckable(True)
        self.history_btn_1.setAutoExclusive(True)
        self.history_btn_1.setObjectName("history_btn_1")
        self.verticalLayout.addWidget(self.history_btn_1)
        self.booking_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.booking_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("booking.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.booking_btn_1.setIcon(icon3)
        self.booking_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.booking_btn_1.setCheckable(True)
        self.booking_btn_1.setAutoExclusive(True)
        self.booking_btn_1.setObjectName("booking_btn_1")
        self.verticalLayout.addWidget(self.booking_btn_1)
        self.deals_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.deals_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("deal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deals_btn_1.setIcon(icon4)
        self.deals_btn_1.setCheckable(True)
        self.deals_btn_1.setAutoExclusive(True)
        self.deals_btn_1.setObjectName("deals_btn_1")
        self.verticalLayout.addWidget(self.deals_btn_1)
        self.chatbot_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.chatbot_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("cus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chatbot_btn_1.setIcon(icon5)
        self.chatbot_btn_1.setCheckable(True)
        self.chatbot_btn_1.setAutoExclusive(True)
        self.chatbot_btn_1.setObjectName("chatbot_btn_1")
        self.verticalLayout.addWidget(self.chatbot_btn_1)
        self.feedback_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.feedback_btn_1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.feedback_btn_1.setIcon(icon6)
        self.feedback_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.feedback_btn_1.setCheckable(True)
        self.feedback_btn_1.setAutoExclusive(True)
        self.feedback_btn_1.setObjectName("feedback_btn_1")
        self.verticalLayout.addWidget(self.feedback_btn_1)
        self.map_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.map_btn_1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.map_btn_1.setIcon(icon7)
        self.map_btn_1.setCheckable(True)
        self.map_btn_1.setAutoExclusive(True)
        self.map_btn_1.setObjectName("map_btn_1")
        self.verticalLayout.addWidget(self.map_btn_1)
        self.quiz_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.quiz_btn_1.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("game.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quiz_btn_1.setIcon(icon8)
        self.quiz_btn_1.setCheckable(True)
        self.quiz_btn_1.setAutoExclusive(True)
        self.quiz_btn_1.setObjectName("quiz_btn_1")
        self.verticalLayout.addWidget(self.quiz_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("exit1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon9)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(80, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.attraction_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.attraction_btn_2.setFont(font)
        self.attraction_btn_2.setCheckable(True)
        self.attraction_btn_2.setAutoExclusive(True)
        self.attraction_btn_2.setObjectName("attraction_btn_2")
        self.verticalLayout_2.addWidget(self.attraction_btn_2)
        self.profile_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_btn_2.sizePolicy().hasHeightForWidth())
        self.profile_btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.profile_btn_2.setFont(font)
        self.profile_btn_2.setMouseTracking(False)
        self.profile_btn_2.setStyleSheet("border-color: rgb(170, 0, 0);")
        self.profile_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.profile_btn_2.setCheckable(True)
        self.profile_btn_2.setAutoExclusive(True)
        self.profile_btn_2.setObjectName("profile_btn_2")
        self.verticalLayout_2.addWidget(self.profile_btn_2)
        self.history_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.history_btn_2.setFont(font)
        self.history_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.history_btn_2.setCheckable(True)
        self.history_btn_2.setAutoExclusive(True)
        self.history_btn_2.setObjectName("history_btn_2")
        self.verticalLayout_2.addWidget(self.history_btn_2)
        self.booking_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.booking_btn_2.setFont(font)
        self.booking_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.booking_btn_2.setCheckable(True)
        self.booking_btn_2.setAutoExclusive(True)
        self.booking_btn_2.setObjectName("booking_btn_2")
        self.verticalLayout_2.addWidget(self.booking_btn_2)
        self.deal_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.deal_btn_2.setFont(font)
        self.deal_btn_2.setCheckable(True)
        self.deal_btn_2.setAutoExclusive(True)
        self.deal_btn_2.setObjectName("deal_btn_2")
        self.verticalLayout_2.addWidget(self.deal_btn_2)
        self.chatbot_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.chatbot_btn_2.setFont(font)
        self.chatbot_btn_2.setCheckable(True)
        self.chatbot_btn_2.setAutoExclusive(True)
        self.chatbot_btn_2.setObjectName("chatbot_btn_2")
        self.verticalLayout_2.addWidget(self.chatbot_btn_2)
        self.feedback_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.feedback_btn_2.setFont(font)
        self.feedback_btn_2.setCheckable(True)
        self.feedback_btn_2.setAutoExclusive(True)
        self.feedback_btn_2.setObjectName("feedback_btn_2")
        self.verticalLayout_2.addWidget(self.feedback_btn_2)
        self.map_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setBold(False)
        font.setWeight(50)
        self.map_btn_2.setFont(font)
        self.map_btn_2.setCheckable(True)
        self.map_btn_2.setAutoExclusive(True)
        self.map_btn_2.setObjectName("map_btn_2")
        self.verticalLayout_2.addWidget(self.map_btn_2)
        self.quiz_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.quiz_btn_2.setFont(font)
        self.quiz_btn_2.setCheckable(True)
        self.quiz_btn_2.setAutoExclusive(True)
        self.quiz_btn_2.setObjectName("quiz_btn_2")
        self.verticalLayout_2.addWidget(self.quiz_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.exit_btn_2.setFont(font)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(-70, 0, 1222, 3022))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setMinimumSize(QtCore.QSize(1200, 3000))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.search_btn_3 = QtWidgets.QPushButton(self.frame_2)
        self.search_btn_3.setGeometry(QtCore.QRect(840, 0, 31, 31))
        self.search_btn_3.setStyleSheet("\n"
                                        "background-color: rgb(255, 255, 255);")
        self.search_btn_3.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("serach1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn_3.setIcon(icon11)
        self.search_btn_3.setObjectName("search_btn_3")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setStyleSheet("\n"
"background-color: rgb(228, 242, 253);\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.change_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("navigationmanual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon10)
        self.change_btn.setIconSize(QtCore.QSize(20, 20))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setStyleSheet("\n"
"background-color: rgb(228, 242, 253);\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(self.page_8)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1222, 3022))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_8)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(30)
        self.profile_frame_middle = QtWidgets.QFrame(self.page_1)
        self.profile_frame_middle.setFrameShape(QtWidgets.QFrame.Box)
        self.profile_frame_middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame_middle.setObjectName("profile_frame_middle")
        self.ProfileSetting = QtWidgets.QLabel(self.profile_frame_middle)
        self.ProfileSetting.setGeometry(QtCore.QRect(20, 10, 221, 41))
        self.ProfileSetting.setFont(font)
        self.ProfileSetting.setObjectName("ProfileSetting")
        self.FirstName_input = QtWidgets.QLineEdit(self.profile_frame_middle)
        self.FirstName_input.setGeometry(QtCore.QRect(20, 110, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FirstName_input.setFont(font)
        self.FirstName_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.FirstName_input.setObjectName("FirstName_input")
        self.LastName_input = QtWidgets.QLineEdit(self.profile_frame_middle)
        self.LastName_input.setGeometry(QtCore.QRect(20, 250, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LastName_input.setFont(font)
        self.LastName_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.LastName_input.setObjectName("LastName_input")
        self.MobileNumber_input = QtWidgets.QLineEdit(self.profile_frame_middle)
        self.MobileNumber_input.setGeometry(QtCore.QRect(510, 110, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.MobileNumber_input.setFont(font)
        self.MobileNumber_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.MobileNumber_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.MobileNumber_input.setObjectName("MobileNumber_input")
        self.Address1_input = QtWidgets.QLineEdit(self.profile_frame_middle)
        self.Address1_input.setGeometry(QtCore.QRect(20, 380, 421, 251))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Address1_input.setFont(font)
        self.Address1_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Address1_input.setText("")
        self.Address1_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Address1_input.setObjectName("Address1_input")
        self.postcode_input = QtWidgets.QLineEdit(self.profile_frame_middle)
        self.postcode_input.setGeometry(QtCore.QRect(510, 250, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.postcode_input.setFont(font)
        self.postcode_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.postcode_input.setText("")
        self.postcode_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.postcode_input.setObjectName("postcode_input")
        self.Area_input = QtWidgets.QLineEdit(self.profile_frame_middle)
        self.Area_input.setGeometry(QtCore.QRect(510, 380, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Area_input.setFont(font)
        self.Area_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Area_input.setText("")
        self.Area_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Area_input.setObjectName("Area_input")
        self.FirstName = QtWidgets.QLabel(self.profile_frame_middle)
        self.FirstName.setGeometry(QtCore.QRect(20, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FirstName.setFont(font)
        self.FirstName.setObjectName("FirstName")
        self.LastName = QtWidgets.QLabel(self.profile_frame_middle)
        self.LastName.setGeometry(QtCore.QRect(20, 230, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LastName.setFont(font)
        self.LastName.setObjectName("LastName")
        self.MobileNumber = QtWidgets.QLabel(self.profile_frame_middle)
        self.MobileNumber.setGeometry(QtCore.QRect(510, 90, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MobileNumber.setFont(font)
        self.MobileNumber.setObjectName("MobileNumber")
        self.Address = QtWidgets.QLabel(self.profile_frame_middle)
        self.Address.setGeometry(QtCore.QRect(20, 360, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Address.setFont(font)
        self.Address.setObjectName("Address")
        self.Postcode = QtWidgets.QLabel(self.profile_frame_middle)
        self.Postcode.setGeometry(QtCore.QRect(510, 230, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Postcode.setFont(font)
        self.Postcode.setObjectName("Postcode")
        self.Area = QtWidgets.QLabel(self.profile_frame_middle)
        self.Area.setGeometry(QtCore.QRect(520, 360, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Area.setFont(font)
        self.Area.setObjectName("Area")
        self.gridLayout_2.addWidget(self.profile_frame_middle, 0, 2, 1, 1)
        self.profile_frame_right = QtWidgets.QFrame(self.page_1)
        self.profile_frame_right.setFrameShape(QtWidgets.QFrame.Box)
        self.profile_frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame_right.setObjectName("profile_frame_right")
        self.save_profile_button = QtWidgets.QPushButton(self.profile_frame_middle)
        self.save_profile_button.setGeometry(QtCore.QRect(910, 570, 181, 51))
        self.save_profile_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.save_profile_button.setObjectName("save_profile_button")
        self.DateOfBirth = QtWidgets.QLabel(self.profile_frame_middle)
        self.DateOfBirth.setGeometry(QtCore.QRect(920, 80, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DateOfBirth.setFont(font)
        self.DateOfBirth.setObjectName("DateOfBirth")
        self.dateEdit = QtWidgets.QDateEdit(self.profile_frame_middle)
        self.dateEdit.setGeometry(QtCore.QRect(920, 110, 131, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.Gender = QtWidgets.QLabel(self.profile_frame_middle)
        self.Gender.setGeometry(QtCore.QRect(920, 230, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Gender.setFont(font)
        self.Gender.setObjectName("Gender")
        self.male_checkBox = QtWidgets.QCheckBox(self.profile_frame_middle)
        self.male_checkBox.setGeometry(QtCore.QRect(920, 280, 81, 20))
        self.male_checkBox.setObjectName("male_checkBox")
        self.female_checkBox = QtWidgets.QCheckBox(self.profile_frame_middle)
        self.female_checkBox.setGeometry(QtCore.QRect(920, 330, 90, 20))
        self.female_checkBox.setObjectName("female_checkBox")
        self.gridLayout_2.addWidget(self.profile_frame_middle, 0, 3, 1, 1)
        self.profile_frame_middle.raise_()
        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.historypage = QtWidgets.QScrollArea(self.page_3)
        self.historypage.setWidgetResizable(True)
        self.historypage.setObjectName("historypage")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1150, 1222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1200))
        self.frame.setStyleSheet("\n"
"background-color: rgb(228, 242, 253);\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setGeometry(QtCore.QRect(40, 90, 971, 192))
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.headerItem().setFont(6, font)
        self.history_label = QtWidgets.QLabel(self.frame)
        self.history_label.setGeometry(QtCore.QRect(40, 10, 301, 71))
        self.history_label.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.history_label.setObjectName("history_label")
        self.verticalLayout_6.addWidget(self.frame)
        self.historypage.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.historypage, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1222, 3022))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.page_5)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1222, 3022))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.dealspage = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.feedbackpage = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.feedbackpage.setFont(font)
        self.feedbackpage.setStyleSheet("\n"
"background-color: rgb(228, 242, 253);\n"
"")
        self.feedbackpage.setAlignment(QtCore.Qt.AlignCenter)
        self.feedbackpage.setObjectName("feedbackpage")
        self.gridLayout_8.addWidget(self.feedbackpage, 0, 0, 1, 1)
        # Create a QWebEngineView widget and set its size and position
        self.webView = QWebEngineView(self.feedbackpage)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1300, 900))  # Adjust the size and position as needed
        self.webView.setObjectName("webView")

        # Load a web page into the QWebEngineView widget
        self.webView.setUrl(QtCore.QUrl(
            "https://docs.google.com/forms/d/e/1FAIpQLSf8kSKHrT5G406KZUg2BzmCkQnBamQ0oBfLN5Ziz_8HxByxdg/viewform"))
        self.stackedWidget.addWidget(self.page_7)
        self.map_page = QtWidgets.QWidget()
        self.map_page.setObjectName("map_page")
        self.stackedWidget.addWidget(self.map_page)

        # Create a QWebEngineView widget and set its size and position
        self.webView = QWebEngineView(self.map_page)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1300, 900))  # Adjust the size and position as needed
        self.webView.setObjectName("webView")

        # Load a web page into the QWebEngineView widget
        self.webView.setUrl(QtCore.QUrl("https://www.google.com/maps"))

        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # Set the geometry here
        self.page_9.setGeometry(QtCore.QRect(0, 0, 1195,699))
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_9)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        # Set the geometry here
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1222,3022))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_3.setMinimumSize(QtCore.QSize(1200, 1200))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.bookingpage_2 = QtWidgets.QFrame(self.frame_3)
        self.bookingpage_2.setGeometry(QtCore.QRect(30, 30, 1200, 3600))
        self.bookingpage_2.setMinimumSize(QtCore.QSize(1200, 3600))
        self.bookingpage_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bookingpage_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bookingpage_2.setObjectName("bookingpage_2")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_5.addWidget(self.scrollArea_3)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.quizpage = QtWidgets.QFrame(self.page_10)
        self.quizpage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quizpage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quizpage.setObjectName("quizpage")
        self.horizontalLayout_9.addWidget(self.quizpage)

        # Create a QWebEngineView widget and set its size and position
        self.webView = QWebEngineView(self.quizpage)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1300, 900))  # Adjust the size and position as needed
        self.webView.setObjectName("webView")

        # Load a web page into the QWebEngineView widget
        self.webView.setUrl(
            QtCore.QUrl("https://quizizz.com/join/quiz/65557246ff6f6a5c40e22251/start?studentShare=true"))


        self.stackedWidget.addWidget(self.page_10)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.profile_btn_1.toggled['bool'].connect(self.profile_btn_2.setChecked) # type: ignore
        self.history_btn_1.toggled['bool'].connect(self.history_btn_2.setChecked) # type: ignore
        self.booking_btn_1.toggled['bool'].connect(self.booking_btn_2.setChecked) # type: ignore
        self.profile_btn_2.toggled['bool'].connect(self.profile_btn_1.setChecked) # type: ignore
        self.history_btn_2.toggled['bool'].connect(self.history_btn_1.setChecked) # type: ignore
        self.booking_btn_2.toggled['bool'].connect(self.booking_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.deals_btn_1.toggled['bool'].connect(self.deal_btn_2.setChecked) # type: ignore
        self.chatbot_btn_1.toggled['bool'].connect(self.chatbot_btn_2.setChecked) # type: ignore
        self.feedback_btn_1.toggled['bool'].connect(self.feedback_btn_2.setChecked) # type: ignore
        self.deal_btn_2.toggled['bool'].connect(self.deals_btn_1.setChecked) # type: ignore
        self.chatbot_btn_2.toggled['bool'].connect(self.chatbot_btn_1.setChecked) # type: ignore
        self.feedback_btn_2.toggled['bool'].connect(self.feedback_btn_1.setChecked) # type: ignore
        self.map_btn_2.toggled['bool'].connect(self.map_btn_1.setChecked) # type: ignore
        self.map_btn_1.toggled['bool'].connect(self.map_btn_2.setChecked) # type: ignore
        self.quiz_btn_2.toggled['bool'].connect(self.quiz_btn_1.setChecked) # type: ignore
        self.quiz_btn_1.toggled['bool'].connect(self.quiz_btn_2.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the chatbot buttons to the corresponding methods
        self.chatbot_btn_1.clicked.connect(self.open_chatbot_page_1)
        self.chatbot_btn_2.clicked.connect(self.open_chatbot_page_1)

        button_size = QtCore.QSize(120, 50)  # Adjust the width and height as needed

        self.attraction_btn_2.setFixedSize(button_size)
        self.profile_btn_2.setFixedSize(button_size)
        self.history_btn_2.setFixedSize(button_size)
        self.booking_btn_2.setFixedSize(button_size)
        self.deal_btn_2.setFixedSize(button_size)
        self.chatbot_btn_2.setFixedSize(button_size)
        self.feedback_btn_2.setFixedSize(button_size)
        self.map_btn_2.setFixedSize(button_size)
        self.quiz_btn_2.setFixedSize(button_size)

        button_size_1 = QtCore.QSize(75, 50)  # Adjust the width and height as needed

        self.attraction_btn_1.setFixedSize(button_size_1)
        self.profile_btn_1.setFixedSize(button_size_1)
        self.history_btn_1.setFixedSize(button_size_1)
        self.booking_btn_1.setFixedSize(button_size_1)
        self.deals_btn_1.setFixedSize(button_size_1)
        self.chatbot_btn_1.setFixedSize(button_size_1)
        self.feedback_btn_1.setFixedSize(button_size_1)
        self.map_btn_1.setFixedSize(button_size_1)
        self.quiz_btn_1.setFixedSize(button_size_1)
        # Create a QCalendarWidget instance for checkin and checkout
        self.save_profile_button.clicked.connect(lambda: self.save_profile())

        self.setup_search_widgets()
        self.fetch_and_populate_data()
        self.history_btn_2.clicked.connect(self.show_booking_history)
        self.search_btn_3.clicked.connect(self.search_attractions)
        self.booking_btn_2.clicked.connect(self.fetch_and_populate_attractions_booking_data)
        # Connect the function to the clicked signal of the profile_button
        self.profile_btn_2.clicked.connect(lambda: self.set_placeholder_text(self.user_id))

    def fetch_user_data_from_database(self, user_id):
        # Connect to the MySQL database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="steven1234",
            database="tourism information kiosk"
        )
        cursor = db_connection.cursor()

        # Define your SQL query to fetch user data based on user_id
        sql_query = "SELECT * FROM user WHERE user_id = %s;"
        cursor.execute(sql_query, (user_id,))
        user_data = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()

        return user_data

    def set_placeholder_text(self, user_id):
        user_data = self.fetch_user_data_from_database(user_id)

        if user_data:
            # Fetch and set the username
            first_name = user_data[2]
            last_name = user_data[3]
            contact_number = user_data[6]
            address = user_data[9]
            postcode = user_data[10]
            area = user_data[8]

            # Set the placeholder text based on user data
            self.FirstName_input.setPlaceholderText(f"{first_name}")
            self.LastName_input.setPlaceholderText(f"{last_name}")
            self.MobileNumber_input.setPlaceholderText(f" {str(contact_number)}")
            self.Address1_input.setPlaceholderText(f" {address}")
            self.postcode_input.setPlaceholderText(f"{str(postcode)}")
            self.Area_input.setPlaceholderText(f" {area}")
        self.stackedWidget.setCurrentIndex(1)

    def fetch_data(self):
        try:
            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Define your base SQL query to fetch data and images by performing a JOIN
            sql_query = """
            SELECT a.attractions_name, a.attractions_price, a.description, a.attractions_address, i.image_data
            FROM attractions AS a
            LEFT JOIN image AS i ON a.attractions_id = i.attractions_id
            WHERE i.image_type='Main'
            """

            cursor.execute(sql_query)
            data = cursor.fetchall()
            # Close the cursor and database connection
            cursor.close()
            db_connection.close()
            return data
        except mysql.connector.Error as err:
            print(f"Error fetching data from the database: {err}")
        return None

    def fetch_search_data(self, search_query=None, selected_category=None):
        try:
            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Define your base SQL query to fetch data and images by performing a JOIN
            sql_query = """
            SELECT a.attractions_name, a.attractions_price, a.description, a.attractions_address, i.image_data
            FROM attractions AS a
            LEFT JOIN image AS i ON a.attractions_id = i.attractions_id
            LEFT JOIN category AS c ON a.category_id = c.category_id
            """

            # Add WHERE clauses to filter based on search_query and selected_category
            if search_query:
                sql_query += f" WHERE a.attractions_name LIKE '%{search_query}%'"
            if selected_category and selected_category.lower() != 'all':
                if 'WHERE' in sql_query:
                    sql_query += f" AND c.category_name = '{selected_category}'"
                else:
                    sql_query += f" WHERE c.category_name = '{selected_category}'"

            # Add additional condition to filter images where image_type is 'Main'
            sql_query += " AND i.image_type = 'Main'"

            cursor.execute(sql_query)
            data = cursor.fetchall()

            # Close the cursor and database connection
            cursor.close()
            db_connection.close()
            return data

        except mysql.connector.Error as err:
            print(f"Error fetching data from the database: {err}")
        return None

    def fetch_category_from_database(self):
        category = ["All"]  # Add "All" as the first option

        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="steven1234",
            database="tourism information kiosk"
        )

        # Create a cursor
        cursor = db_connection.cursor()

        # Define your SQL query to fetch options from another table
        categories_query = "SELECT category_name FROM category"

        # Execute the query
        cursor.execute(categories_query)

        # Fetch all the options
        category_data = cursor.fetchall()

        # If there are options, extract them
        if category_data:
            category.extend([str(option[0]) for option in category_data])

        # Close the cursor
        cursor.close()
        return category

    def setup_search_widgets(self):
        # Create search widgets
        search_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        search_frame.setMinimumSize(QtCore.QSize(300, 50))
        search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        search_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.verticalLayout_6.addWidget(search_frame)

        self.Search_attraction = QtWidgets.QLineEdit(search_frame)
        self.Search_attraction.setGeometry(QtCore.QRect(370, 0, 441, 30))
        self.Search_attraction.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Search_attraction.setObjectName("Search_attraction")
        self.Search_attraction.setFont(QtGui.QFont("Arial", 12))
        self.section = QtWidgets.QComboBox(search_frame)
        self.section.setGeometry(QtCore.QRect(240, 0, 81, 30))
        self.section.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.section.setEditable(False)
        self.section.setObjectName("section")
        font = QtGui.QFont()
        font.setPointSize(10)  # Change 12 to the desired font size
        self.section.setFont(font)
        # Fetch categories and populate the section combo box
        category = self.fetch_category_from_database()  # Use self to call the method

        # Populate the QComboBox with options
        self.section.addItem("All")  # Add "All" option
        for option in category:
            self.section.addItem(option)

        self.search_btn_3 = QtWidgets.QPushButton(search_frame)
        self.search_btn_3.setGeometry(QtCore.QRect(840, 0, 31, 31))
        self.search_btn_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_btn_3.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("serach1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn_3.setIcon(icon11)
        self.search_btn_3.setObjectName("search_btn_3")
        self.verticalLayout_10.addWidget(search_frame)

        # Connect the search button to the search_attractions method
        self.search_btn_3.clicked.connect(self.search_attractions)

    def fetch_and_populate_data(self):
        data = self.fetch_data()
        if data:
            self.display_data(data)

    def search_attractions(self):
        # Get search query and selected category
        search_query = self.Search_attraction.text()
        selected_category = self.section.currentText()
        self.clear_layout(self.verticalLayout_10)

        # Set up search widgets before each search
        self.setup_search_widgets()

        # Fetch data based on search query and category
        data = self.fetch_search_data(search_query, selected_category)

        # Display the new data
        if data:
            self.display_data(data)

    def display_data(self, data):
        for index, (attraction_name, attractions_price, description, attractions_address, image_data) in enumerate(
                data):
            new_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
            new_frame.setFixedSize(1200, 500)
            new_frame.setFrameShape(QtWidgets.QFrame.Box)
            new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_6.setSpacing(0)
            self.verticalLayout_6.addWidget(new_frame)
            image_label = QtWidgets.QLabel(new_frame)
            image_label.setGeometry(QtCore.QRect(30, 40, 441, 391))  # Adjust the position and size as needed
            # Set the image data here (assuming the image_data is a binary image)
            # For example, you can use QPixmap to display the image:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image_data)
            image_label.setPixmap(pixmap)

            name_text_edit = QtWidgets.QTextEdit(new_frame)
            name_text_edit.setGeometry(QtCore.QRect(520, 50, 501, 51))

            # Set the entire text as HTML with bold formatting
            name_text_edit.setHtml(f'<b>Name: {attraction_name}</b>')
            name_text_edit.setObjectName(f"name{index + 1}")

            # Set the QTextEdit field as read-only
            name_text_edit.setReadOnly(True)

            price_text_edit = QtWidgets.QTextEdit(new_frame)
            price_text_edit.setGeometry(QtCore.QRect(1060, 50, 104, 51))

            # Set the entire text as HTML with bold formatting
            price_text_edit.setHtml(f'<b>RM {attractions_price}</b>')
            price_text_edit.setObjectName(f"price{index + 1}")

            # Set the QTextEdit field as read-only
            price_text_edit.setReadOnly(True)

            description_text_edit = QtWidgets.QTextEdit(new_frame)
            description_text_edit.setGeometry(QtCore.QRect(520, 150, 631, 101))
            description_text_edit.setPlainText(description)
            description_text_edit.setHtml(f'<b><u>Description</u></b><br>{description}')
            description_text_edit.setObjectName(f"description{index + 1}")

            # Set the QTextEdit field as read-only
            description_text_edit.setReadOnly(True)

            address_text_edit = QtWidgets.QTextEdit(new_frame)
            address_text_edit.setGeometry(QtCore.QRect(520, 300, 631, 101))
            address_text_edit.setPlainText(attractions_address)
            address_text_edit.setHtml(f'<b><u>Address</u></b><br>{attractions_address}')
            address_text_edit.setObjectName(f"address{index + 1}")
            font = QFont()
            font.setPointSize(12)  # Adjust the font size as needed
            font.setFamily("Arial")  # Adjust the font family as needed

            # Set the font for name_text_edit
            name_text_edit.setFont(font)

            # Set the font for price_text_edit
            price_text_edit.setFont(font)

            # Set the font for description_text_edit
            description_text_edit.setFont(font)

            # Set the font for address_text_edit
            address_text_edit.setFont(font)

            # Set the QTextEdit field as read-only
            address_text_edit.setReadOnly(True)

            self.verticalLayout_10.addWidget(new_frame)

    def clear_layout(self, layout):
        # Clear all widgets from the layout
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def show_booking_data(self):
        # Call the method to fetch and populate data
        self.fetch_and_populate_booking_data()

        # Make the frame visible
        self.frame.setVisible(True)

    def fetch_deals_data(self):
        try:
            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Define your SQL query to fetch data and images by performing a JOIN
            sql_query = """
            SELECT d.deals_name, d.deals_description, d.discount, d.promocode, d.attractions_id, i.image_data
            FROM deals AS d
            LEFT JOIN image AS i ON d.deals_id = i.deals_id
            WHERE i.image_type = 'Main'
            """
            cursor.execute(sql_query)
            data = cursor.fetchall()

            # Close the cursor and database connection
            cursor.close()
            db_connection.close()
            return data

        except mysql.connector.Error as err:
            print(f"Error fetching data from the database: {err}")
        return None

    def fetch_and_populate_deals_data(self):
        self.clear_layout(self.verticalLayout_8)
        data = self.fetch_deals_data()

        if data:
            for index, (deals_name, deals_description, discount, promocode, attractions_id, image_data) in enumerate(
                    data):
                new_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
                new_frame.setFixedSize(1250, 400)
                new_frame.setFrameShape(QtWidgets.QFrame.Box)
                new_frame.setFrameShadow(QtWidgets.QFrame.Raised)

                # Create a new vertical layout for each frame
                new_frame_layout = QtWidgets.QVBoxLayout(new_frame)
                new_frame.setLayout(new_frame_layout)

                # Image Label
                image_label = QtWidgets.QLabel(new_frame)
                image_label.setGeometry(QtCore.QRect(20, 20, 441, 370))  # Adjust the position and size as needed
                pixmap = QtGui.QPixmap()

                if pixmap.loadFromData(image_data):
                    image_label.setPixmap(pixmap)
                    image_label.setScaledContents(True)
                else:
                    print("Failed to load image data.")

                # Deals Name Text Edit
                deals_name_text_edit = QtWidgets.QTextEdit(new_frame)
                deals_name_text_edit.setGeometry(QtCore.QRect(480, 40, 561, 61))
                deals_name_text_edit.setPlainText(deals_name)
                deals_name_text_edit.setHtml(f'<b>Name:{deals_name}</b>')
                deals_name_text_edit.setObjectName(f"deals_name{index + 1}")

                # Deals Price Text Edit
                deals_price_text_edit = QtWidgets.QTextEdit(new_frame)
                deals_price_text_edit.setGeometry(QtCore.QRect(1070, 40, 111, 61))
                deals_price_text_edit.setPlainText(str(discount))
                deals_price_text_edit.setHtml(f'<b>Discount: {discount*100}</b>'+"%")
                deals_price_text_edit.setObjectName(f"discount{index + 1}")

                # Deals Description Text Edit
                deals_description_text_edit = QtWidgets.QTextEdit(new_frame)
                deals_description_text_edit.setGeometry(QtCore.QRect(480, 110, 701, 151))
                deals_description_text_edit.setPlainText(deals_description)
                deals_description_text_edit.setHtml(f'<b>Descriptions: </b>{deals_description}')
                deals_description_text_edit.setObjectName(f"deals_description{index + 1}")

                # Deals Promocode Text Edit
                deals_promocode_text_edit = QtWidgets.QTextEdit(new_frame)
                deals_promocode_text_edit.setGeometry(QtCore.QRect(480, 270, 701, 100))
                deals_promocode_text_edit.setPlainText(promocode)
                deals_promocode_text_edit.setHtml(f'<b>Promocode:</b>{promocode}')
                deals_promocode_text_edit.setObjectName(f"promocode{index + 1}")
                font = QFont()
                font.setPointSize(12)  # Adjust the font size as needed
                font.setFamily("Arial")  # Adjust the font family as needed

                # Set the font for deals_name_text_edit
                deals_name_text_edit.setFont(font)

                # Set the font for deals_price_text_edit
                deals_price_text_edit.setFont(font)

                # Set the font for deals_description_text_edit
                deals_description_text_edit.setFont(font)

                # Set the font for deals_promocode_text_edit
                deals_promocode_text_edit.setFont(font)

                image_label.setVisible(True)
                deals_name_text_edit.setVisible(True)
                deals_description_text_edit.setVisible(True)
                deals_promocode_text_edit.setVisible(True)

                # Set the QTextEdit fields as read-only
                deals_name_text_edit.setReadOnly(True)
                deals_price_text_edit.setReadOnly(True)
                deals_description_text_edit.setReadOnly(True)
                deals_promocode_text_edit.setReadOnly(True)

                # Add the new frame to the main layout
                self.verticalLayout_8.addWidget(new_frame)

    def fetch_booking_data_from_database(self):
        # Connect to the MySQL database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="steven1234",
            database="tourism information kiosk"
        )
        cursor = db_connection.cursor()

        # Define your SQL query to fetch data from the database by performing a JOIN
        sql_query = """
                SELECT
        b.booking_id, b.booking_date, b.status,
        a.attractions_name, a.attractions_price, c.quantities,
        (a.attractions_price * c.quantities) * (1 - d.discount) AS total_amount_with_discount
    FROM booking AS b
    LEFT JOIN booking_details AS c ON b.booking_id = c.booking_id
    LEFT JOIN attractions AS a ON c.attractions_id = a.attractions_id
    LEFT JOIN deals AS d ON c.deals_id = d.deals_id
    WHERE b.user_id = %s;
    """
        cursor.execute(sql_query, (self.user_id,))
        data = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()
        return data

    def show_booking_history(self):
        # Clear the existing items in the treeWidget
        self.treeWidget.clear()

        data = self.fetch_booking_data_from_database()

        if data:
            for row in data:
                item = QtWidgets.QTreeWidgetItem(self.treeWidget)

                # Set the text for each column based on your desired mapping
                item.setText(0, str(row[0]))
                item.setText(1, str(row[3]))
                item.setText(2, str(row[1]))
                item.setText(3, str(row[5]))
                item.setText(4, str(row[4]))
                item.setText(5, str(row[6]))
                item.setText(6, str(row[2]))

                # Add the item to the treeWidget
                self.treeWidget.addTopLevelItem(item)

    def fetch_hotel_data_1_from_database(self):
        try:
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Replace this query with your actual query to fetch hotel data
            query = """
                SELECT attractions_name, description, attractions_address, attractions_price
                FROM attractions
                WHERE attractions_price != '0'
            """
            cursor.execute(query)
            hotel_data = cursor.fetchall()

            return hotel_data
        except Exception as e:
            # Log or raise the exception for better error handling
            print(f"Error fetching attractions data from the database: {e}")
            return None

    def separate_images_by_type(self, attractions_data):
        main_images = []
        details_images = []

        try:
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            for name, description, address, price in attractions_data:
                # Fetch all details images for the current attractions
                details_image_query = f"SELECT image_data FROM image WHERE attractions_id = (SELECT attractions_id FROM attractions WHERE attractions_name = '{name}') AND image_type = 'Details'"
                cursor.execute(details_image_query)
                details_image_data = cursor.fetchall()

                try:
                    if details_image_data:
                        details_images.extend(
                            (name, description, address, price, image_data[0]) for image_data in details_image_data)
                except Exception as e:
                    print(f"An error occurred: {e}")

                # Fetch the main image for the current attractions
                main_image_query = f"SELECT image_data FROM image WHERE attractions_id= (SELECT attractions_id FROM attractions WHERE attractions_name = '{name}') AND image_type = 'Main'"
                cursor.execute(main_image_query)
                main_image_data = cursor.fetchone()

                if main_image_data:
                    main_images.append((name, description, address, price, main_image_data[0]))

        except Exception as e:
            print(f"Error fetching images from the database: {e}")

        return main_images, details_images

    def fetch_and_populate_attractions_booking_data(self, use_first_database=True):

        try:
            if use_first_database:
                attractions_data = self.fetch_hotel_data_1_from_database()
            else:
                return None

            if attractions_data:
                # Clear existing items from the layout
                self.clear_layout(self.verticalLayout_6)

                # Separate data for fetch_and_populate_hotels_data
                main_images, details_images = self.separate_images_by_type(attractions_data)

                # Use main_images for fetch_and_populate_hotels_data
                for index, (
                attractions_name, description, attractions_address, attractions_price, image_data) in enumerate(
                        main_images):
                    new_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
                    new_frame.setFixedSize(1200, 400)
                    new_frame.setFrameShape(QtWidgets.QFrame.Box)
                    new_frame.setFrameShadow(QtWidgets.QFrame.Raised)

                    # Create a new vertical layout for each frame
                    new_frame_layout = QtWidgets.QVBoxLayout(new_frame)
                    new_frame.setLayout(new_frame_layout)

                    book_btn = QtWidgets.QPushButton(new_frame)
                    book_btn.setGeometry(QtCore.QRect(1040, 330, 121, 28))
                    book_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
                    book_btn.setObjectName("book_btn")
                    book_btn.setText("Book Now >")
                    details_data = [details for details in details_images if details[0] == attractions_name]

                    # Inside fetch_and_populate_hotels_data method
                    book_btn.clicked.connect(
                        lambda checked, a_name=attractions_name, a_description=description, a_price=attractions_price,
                               a_image=image_data, d_data=details_data: self.create_booking_page(a_name, a_price,
                                                                                                 d_data))

                    image_label = QtWidgets.QLabel(new_frame)
                    image_label.setGeometry(QtCore.QRect(30, 30, 291, 331))
                    pixmap = QtGui.QPixmap()

                    if pixmap.loadFromData(image_data):
                        image_label.setPixmap(pixmap)
                        image_label.setScaledContents(True)
                    else:
                        print("Failed to load image data.")

                    bookingtitle = QtWidgets.QTextEdit(new_frame)
                    bookingtitle.setGeometry(QtCore.QRect(340, 30, 831, 41))
                    bookingtitle.setPlainText(attractions_name)
                    bookingtitle.setHtml(f'<b>Name:{attractions_name}</b>')
                    bookingtitle.setObjectName(f"hotels_name{index + 1}")

                    booking_price = QtWidgets.QTextEdit(new_frame)
                    booking_price.setGeometry(QtCore.QRect(890, 330, 131, 31))
                    booking_price.setStyleSheet("background-color: rgb(255, 255, 255);")
                    booking_price.setPlainText(str(attractions_price))
                    booking_price.setHtml(f'<b>RM{attractions_price}</b>')
                    booking_price.setObjectName(f"hotels_pricee{index + 1}")

                    booking_address = QtWidgets.QTextEdit(new_frame)
                    booking_address.setGeometry(QtCore.QRect(340, 100, 831, 200))
                    booking_address.setPlainText(attractions_address)
                    booking_address.setHtml(f'<b>Address:</b>{attractions_address}')
                    booking_address.setObjectName(f"hotel_address{index + 1}")

                    font = QFont()
                    font.setFamily("Arial")  # Set the font family (adjust as needed)
                    font.setPointSize(12)
                    book_btn.setFont(font)
                    bookingtitle.setFont(font)
                    booking_price.setFont(font)
                    booking_address.setFont(font)

                    image_label.setVisible(True)
                    bookingtitle.setVisible(True)
                    booking_price.setVisible(True)
                    booking_address.setVisible(True)

                    # Set the QTextEdit fields as read-only
                    bookingtitle.setReadOnly(True)
                    booking_price.setReadOnly(True)
                    booking_address.setReadOnly(True)

                    # Add the new frame to the main layout
                    self.verticalLayout_6.addWidget(new_frame)

                # Update the layout
                self.verticalLayout_6.update()

        except Exception as e:
            print(f"Error in fetch_and_populate_hotels_data: {e}")

    def hide_hotels_data(self):
        # Assuming scrollAreaWidgetContents_3 is the parent widget of fetch_and_populate_hotels_data
        self.scrollAreaWidgetContents_3.setVisible(False)

    def create_booking_page(self, attractions_name, attractions_price, details_data):
        new_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        new_frame.setFixedSize(1150, 650)
        new_frame.setFrameShape(QtWidgets.QFrame.Box)
        new_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Back button
        back_booking = QtWidgets.QPushButton(new_frame)
        back_booking.setGeometry(QtCore.QRect(0, 0, 60, 28))
        back_booking.setStyleSheet("background-color: rgb(255, 255, 255);")
        back_booking.setObjectName("back_booking")
        back_booking.setText("CLOSE")

        # Set the font size to 10
        font = back_booking.font()
        font.setPointSize(10)
        back_booking.setFont(font)

        # Connect the back_booking button to the navigate_to_page_4 method
        back_booking.clicked.connect(new_frame.close)

        # Create a new vertical layout for each frame
        new_frame_layout = QtWidgets.QVBoxLayout(new_frame)
        new_frame.setLayout(new_frame_layout)

        # List to store image labels
        image_labels = []

        # Limit the number of displayed pictures to 4
        num_images_to_display = min(len(details_data), 4)

        # Iterate through details_data and create image labels
        for i in range(num_images_to_display):
            individual_image_data = details_data[i][4]
            image_label = QtWidgets.QLabel(new_frame)

            # Adjusted position for a more visually appealing layout
            image_label.setGeometry(QtCore.QRect(70 + i * 273, 30, 191, 141))

            image_label.setFrameShape(QtWidgets.QFrame.Box)
            image_label.setText("")
            image_label.setObjectName(f"booking_pic_{i + 2}")  # Start from 2 to match the naming convention
            image_labels.append(image_label)

            try:
                # Fetch the actual image data from the database using the size information
                pixmap = QtGui.QPixmap()
                if pixmap.loadFromData(individual_image_data):
                    image_label.setPixmap(pixmap)
                    image_label.setScaledContents(True)
                else:
                    print(f"Failed to load image data for image {i + 2}.")

            except Exception as e:
                print(f"Error loading image data: {e}")
        # Additional code to handle details_description
        details_description_label = QtWidgets.QTextEdit(new_frame)
        details_description_label.setGeometry(QtCore.QRect(0, 261, 1150, 61))  # Adjust the position and size as needed
        if details_data:
            details_description_label.setPlainText(details_data[0][2])  # Assuming address is at index 2
        else:
            print("Details data is empty.")


        details_description_label.setHtml(f'<b>Address:</b> {details_data[0][2]}')
        details_description_label.setObjectName("details_description_label")
        details_description_label.setVisible(True)

        # Booking title
        booking_title_2 = QtWidgets.QTextEdit(new_frame)
        booking_title_2.setGeometry(QtCore.QRect(0, 200, 1150, 61))  # Adjusted position
        booking_title_2.setPlainText(attractions_name)
        booking_title_2.setHtml(f'<b>Name: {attractions_name}</b>')
        booking_title_2.setObjectName("booking_title_2")

        # Booking price
        booking_price_2 = QtWidgets.QTextEdit(new_frame)
        booking_price_2.setGeometry(QtCore.QRect(950, 500, 170, 61))
        booking_price_2.setPlainText(str(attractions_price))
        booking_price_2.setHtml(f'<b>RM {attractions_price}</b>')
        booking_price_2.setObjectName("booking_price_2")

        # Booking description
        booking_description_2 = QtWidgets.QTextEdit(new_frame)
        booking_description_2.setGeometry(QtCore.QRect(0, 322, 1150, 150))
        booking_description_2.setPlainText(details_data[0][1])  # Assuming description is at index 1
        booking_description_2.setHtml(f'<b>Description:</b> {details_data[0][1]}')
        booking_description_2.setObjectName("booking_description_2")

        # ComboBox
        ticket_label = QtWidgets.QLabel(new_frame)
        ticket_label.setGeometry(QtCore.QRect(20, 500, 100, 30))  # Adjusted position
        ticket_label.setObjectName("ticket_label")
        ticket_label.setText("Ticket number:")

        comboBox = QtWidgets.QComboBox(new_frame)
        comboBox.setGeometry(QtCore.QRect(100, 500, 50, 30))  # Adjusted position
        comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        comboBox.setObjectName("comboBox")
        for i in range(1, 21):
            comboBox.addItem(str(i))

        # Check-in date label
        # Check-in date label and calendar text field
        check_in_label = QtWidgets.QLabel(new_frame)
        check_in_label.setGeometry(QtCore.QRect(200, 500, 101, 28))  # Adjusted position
        check_in_label.setObjectName("check_in_label")
        check_in_label.setText("Check-in date:")

        check_in_date = QDateEdit(new_frame)
        check_in_date.setGeometry(QtCore.QRect(320, 500, 191, 28))  # Adjusted position for spacing
        check_in_date.setCalendarPopup(True)
        check_in_date.setObjectName("check_in_date")
        check_in_date.setDate(QtCore.QDate.currentDate())
        check_in_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        check_in_date.calendarWidget().setStyleSheet("background-color: rgb(255, 255, 255);")

        # Check-out date label and calendar text field
        promocode_label = QtWidgets.QLabel(new_frame)
        promocode_label.setGeometry(QtCore.QRect(550, 500, 101, 28))  # Adjusted position with increased spacing
        promocode_label.setObjectName("promocode_label")
        promocode_label.setText("Promocode:")

        promocode_entry = QtWidgets.QTextEdit(new_frame)
        promocode_entry.setGeometry(QtCore.QRect(670, 500, 191, 28))  # Adjusted position for spacing
        promocode_entry.setObjectName("promocode_entry")
        promocode_entry.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Booking button
        booking_btn = QtWidgets.QPushButton(new_frame)
        booking_btn.setGeometry(QtCore.QRect(950, 600, 170, 40))  # Adjusted position
        booking_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        booking_btn.setObjectName("booking_btn")
        booking_btn.setText("Book Now")
        booking_btn.clicked.connect(
            lambda: self.save_booking_data(self.user_id, attractions_name, check_in_date.date().toString(), comboBox,
                                           promocode_entry))
        booking_btn.clicked.connect(
            lambda: self.send_email(attractions_name, check_in_date.date().toString(), comboBox))

        # Set the QTextEdit fields as read-only
        booking_description_2.setReadOnly(True)
        booking_title_2.setReadOnly(True)
        booking_price_2.setReadOnly(True)
        details_description_label.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)

        booking_title_2.setFont(font)
        booking_price_2.setFont(font)
        booking_description_2.setFont(font)
        details_description_label.setFont(font)
        ticket_label.setFont(font)
        check_in_label.setFont(font)
        promocode_label.setFont(font)
        # Assuming scrollAreaWidgetContents_3 is the parent widget of create_booking_page
        self.scrollAreaWidgetContents_3.setVisible(True)

        # Add the new frame to the main layout
        self.horizontalLayout_7.addWidget(new_frame)
        self.horizontalLayout_7.update()

        # Ensure the visibility of the new frame and its ancestors
        ancestor_widget = new_frame.parentWidget()

        while ancestor_widget is not None:
            ancestor_widget.setVisible(True)
            ancestor_widget.raise_()
            ancestor_widget = ancestor_widget.parentWidget()

        # Raise the new frame to the top of the stacking order
        new_frame.raise_()

        # Hide the booking page initially
        new_frame.show()

        print("Booking page shown")
        return new_frame

    def get_attractions_info_from_deals_id(self, deals_id):
        try:
            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Query to retrieve attractions_id and attractions_name based on deals_id
            attractions_query = """
                SELECT a.attractions_id, a.attractions_name
                FROM attractions AS a
                JOIN deals AS d ON a.attractions_id = d.attractions_id
                WHERE d.deals_id = %s;
            """
            cursor.execute(attractions_query, (deals_id,))
            result = cursor.fetchone()

            if result:
                attractions_id, attractions_name = result
                return attractions_id, attractions_name
            else:
                return None

        except Exception as e:
            print(f"Error getting attractions info: {e}")
        finally:
            cursor.close()
            db_connection.close()

    def save_booking_data(self, user_id, attractions_name, check_in_date, comboBox, promocode_entry):
        try:
            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )
            cursor = db_connection.cursor()

            # Convert check_in_date to a datetime object
            check_in_date = datetime.strptime(check_in_date, "%a %b %d %Y").date()

            # Query to retrieve attractions_id and attractions_price based on attractions_name
            attractions_query = "SELECT attractions_id, attractions_price FROM attractions WHERE attractions_name = %s;"
            cursor.execute(attractions_query, (attractions_name,))
            result = cursor.fetchone()

            if result:
                attractions_id, attractions_price = result

                # Retrieve the selected quantity from the QComboBox
                selected_quantity = int(comboBox.currentText())

                if promocode_entry and promocode_entry.toPlainText().strip():
                    entered_promocode = promocode_entry.toPlainText()

                    # Query to check the validity of the promo code and get deals_id
                    promocode_query = "SELECT deals_id FROM deals WHERE promocode = %s ;"
                    cursor.execute(promocode_query, (entered_promocode,))
                    deals_id_result = cursor.fetchone()

                    if deals_id_result:
                        deals_id = deals_id_result[0]

                        # Get attractions information based on deals_id
                        attractions_info = self.get_attractions_info_from_deals_id(deals_id)

                        if attractions_info:
                            promo_attractions_id, promo_attractions_name = attractions_info

                            # Check if attractions from the promo code match the provided attractions on the booking page
                            if promo_attractions_id == attractions_id and promo_attractions_name == attractions_name:
                                # Proceed with booking

                                # Calculate total amount without discount (assuming discount is not used in this case)
                                total_amount = self.calculate_total_amount(attractions_price, selected_quantity, 0)

                                # Insert data into the booking table without a promo code
                                booking_query = "INSERT INTO booking (booking_date, user_id, status) " \
                                                "VALUES (%s, %s, 'Confirmed');"
                                booking_data = (check_in_date, user_id)
                                cursor.execute(booking_query, booking_data)

                                # Retrieve the auto-generated booking_id
                                booking_id = cursor.lastrowid

                                # Insert data into the booking_details table without a promo code
                                details_query = "INSERT INTO booking_details (booking_id, attractions_id, quantities) " \
                                                "VALUES (%s, %s, %s);"
                                details_data = (booking_id, attractions_id, selected_quantity)
                                cursor.execute(details_query, details_data)

                                # Commit the changes
                                db_connection.commit()

                                # Display a message box with the booking details
                                QMessageBox.information(
                                    None,
                                    "Booking Information",
                                    f"Booking Successful!\n\n"
                                    f"Attraction: {attractions_name}\n"
                                    f"Quantity: {selected_quantity}\n"
                                    f"Total Amount: RM {total_amount:.2f}"
                                )
                            else:
                                QMessageBox.warning(
                                    None,
                                    "Mismatched Attractions",
                                    "The attractions from the promo code do not match the provided attractions."
                                )
                        else:
                            QMessageBox.warning(None, "Attractions Info Not Found",
                                                f"No attractions found for the given deals_id: {deals_id}")
                    else:
                        QMessageBox.warning(None, "Invalid Promocode", "The entered promocode is invalid.")
                else:
                    # Calculate total amount without discount
                    total_amount = self.calculate_total_amount(attractions_price, selected_quantity, 0)

                    # Insert data into the booking table without a promo code
                    booking_query = "INSERT INTO booking (booking_date, user_id, status) " \
                                    "VALUES (%s, %s, 'Confirmed');"
                    booking_data = (check_in_date, user_id)
                    cursor.execute(booking_query, booking_data)

                    # Retrieve the auto-generated booking_id
                    booking_id = cursor.lastrowid

                    # Insert data into the booking_details table without a promo code
                    details_query = "INSERT INTO booking_details (booking_id, attractions_id, quantities) " \
                                    "VALUES (%s, %s, %s);"
                    details_data = (booking_id, attractions_id, selected_quantity)
                    cursor.execute(details_query, details_data)

                    # Commit the changes
                    db_connection.commit()

                    # Display a message box with the booking details
                    QMessageBox.information(
                        None,
                        "Booking Information",
                        f"Booking Successful!\n\n"
                        f"Attraction: {attractions_name}\n"
                        f"Quantity: {selected_quantity}\n"
                        f"Total Amount: RM {total_amount:.2f}"
                    )

            else:
                QMessageBox.warning(None, "Attraction Not Found",
                                    f"No attractions found with the name: {attractions_name}")

        except Exception as e:
            print(f"Error saving booking data: {e}")
        finally:
            # Close the cursor and database connection in the finally block to ensure it happens regardless of exceptions
            cursor.close()
            db_connection.close()

    def calculate_total_amount(self, unit_price, quantity, discount_percentage):
        # Calculate total amount with discount
        total_amount = unit_price * quantity * (1 - discount_percentage)
        return total_amount
    def navigate_back(self):
        # Check if self.scrollArea_2 is not in the QStackedWidget, add it
        if self.MainWindow.ui.stackedWidget.indexOf(self.scrollArea_2) == -1:
            self.MainWindow.ui.stackedWidget.addWidget(self.scrollArea_2)

        self.scrollAreaWidgetContents_3.setVisible(True)
        # Set the stacked widget index to show the desired page (self.scrollArea_2)
        index_of_scrollArea_2 = self.MainWindow.ui.stackedWidget.indexOf(self.scrollArea_2)
        self.MainWindow.ui.stackedWidget.setCurrentIndex(index_of_scrollArea_2)

    def send_email(self, hotel_name, check_in_date, comboBox):
        # Load credentials from the client_secret.json file
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']
        flow = InstalledAppFlow.from_client_secrets_file(
            r"C:\Users\s\Downloads\client_secret_379816141851-frjap9raqtnjcn5t8t97v51vmum6te8e.apps.googleusercontent.com.json",
            SCOPES)

        # Run the OAuth flow
        credentials = flow.run_local_server(port=0)

        def create_message(sender, to, subject, message_text):
            message = MIMEMultipart()
            message.attach(MIMEText(message_text, 'plain'))
            message['to'] = to
            message['subject'] = subject
            return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        def send_message(service, user_id, message):
            try:
                message = service.users().messages().send(userId=user_id, body=message).execute()
                print(f"Message sent. Message Id: {message['id']}")
            except Exception as e:
                print(f"An error occurred: {e}")

        service = build('gmail', 'v1', credentials=credentials)
        subject = 'Booking Confirmation: ' + hotel_name
        number_of_tickets = comboBox.currentText()
        message_text = f'Thank you for booking with us!\n\n' \
                       f'Attraction Name: {hotel_name}\n' \
                       f'Check-in Date: {check_in_date}\n' \
                       f'Number of Ticket: {number_of_tickets}\n' \
                       f'We look forward to hosting you.'

        send_message(service, 'me', create_message('me', 'usermapping1@gmail.com', subject, message_text))

    def show_checkin_calendar_2(self, event):
        # Calculate the position to display the check-in calendar
        pos = self.booking_title_2.mapToGlobal(QtCore.QPoint(0, self.booking_title_2.height()))
        self.checkin_calendar.setMinimumDate(QtCore.QDate.currentDate())
        self.checkin_calendar.setSelectedDate(self.checkin_input_2.date())
        self.checkin_calendar.move(pos)
        self.checkin_calendar.show()

        # Connect the dateChanged signal to update the check-in input
        self.checkin_calendar.clicked.connect(self.update_checkin_input_2)

    def update_checkin_input_2(self, date):
        # Update the check-in input date when a date is selected in the calendar
        self.checkin_input_2.setDate(self.checkin_calendar.selectedDate())
        self.checkin_calendar.hide()


    def show_checkin_calendar_2(self, event):
        pos = self.checkin_input_2.mapToGlobal(QtCore.QPoint(0, self.checkin_input_2.height()))
        self.checkin_calendar.setMinimumDate(QtCore.QDate.currentDate())
        self.checkin_calendar.setSelectedDate(self.checkin_input_2.date())
        self.checkin_calendar.move(pos)
        self.checkin_calendar.show()

        self.checkin_calendar.clicked.disconnect()  # Disconnect previous connections
        self.checkin_calendar.clicked.connect(lambda: self.update_checkin_input_2(self.checkin_calendar.selectedDate()))

    def update_checkin_input_2(self, date):
        self.checkin_input_2.setDate(self.checkin_calendar.selectedDate())
        self.checkin_calendar.hide()

    # Create a slot function for saving/updating the user's profile
    def save_profile(self):
        user_id = self.user_id  # Use the user_id from Ui_MainWindow
        print(f"Inside save_profile function for user_id: {user_id}")
        # Retrieve user input from the input fields
        first_name = self.FirstName_input.text()
        last_name = self.LastName_input.text()
        mobile_number = self.MobileNumber_input.text()
        address1 = self.Address1_input.text()
        postcode = self.postcode_input.text()
        area = self.Area_input.text()

        try:
            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="steven1234",
                database="tourism information kiosk"
            )

            cursor = db_connection.cursor()

            # Perform validation (you can add more validation logic)
            if not first_name or not last_name:
                QtWidgets.QMessageBox.warning(self.page_1, "Validation Error", "First name and last name are required.")
                return
            if not mobile_number:
                QtWidgets.QMessageBox.warning(self.page_1, "Validation Error", "Mobile number is required.")
                return
            if not address1:
                QtWidgets.QMessageBox.warning(self.page_1, "Validation Error", "Address is required.")
                return
            if not postcode:
                QtWidgets.QMessageBox.warning(self.page_1, "Validation Error", "Postcode is required.")
                return
            if not area:
                QtWidgets.QMessageBox.warning(self.page_1, "Validation Error", "Area is required.")
                return

            # Additional validation for mobile number (you can customize this)
            if not mobile_number.isdigit():
                QtWidgets.QMessageBox.warning(self.page_1, "Validation Error", "Mobile number must be a number.")
                return
            if len(mobile_number) < 10 or len(mobile_number) > 12:
                QtWidgets.QMessageBox.warning(self.page_1, "Validation Error", "Mobile number must be valid.")
                return
            # Check if the user already exists in the database
            check_user_query = "SELECT * FROM user WHERE user_id = %s"
            cursor.execute(check_user_query, (user_id,))
            existing_user = cursor.fetchone()
            print(f"Existing user for user_id {user_id}: {existing_user}")

            if existing_user:
                # User exists, perform an update query
                update_query = "UPDATE user SET first_name = %s, last_name = %s, contact_number = %s, " \
                               "address = %s, postcode = %s, area = %s WHERE user_id = %s"
                cursor.execute(update_query,
                               (first_name, last_name, mobile_number, address1, postcode, area, user_id))
                db_connection.commit()
                cursor.close()
                # Display a success message
                QtWidgets.QMessageBox.information(self.page_1, "Profile Updated", "Your profile has been updated.")
            else:
                # User doesn't exist, display an error message
                QtWidgets.QMessageBox.warning(self.page_1, "User Not Found", "User does not exist in the database.")

        except mysql.connector.Error as err:

            QtWidgets.QMessageBox.warning(self.page_1, "Database Error", f"Error updating profile data: {err}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.attraction_btn_2.setText(_translate("MainWindow", "Attraction"))
        self.profile_btn_2.setText(_translate("MainWindow", "Profile"))
        self.history_btn_2.setText(_translate("MainWindow", "History"))
        self.booking_btn_2.setText(_translate("MainWindow", "Booking"))
        self.deal_btn_2.setText(_translate("MainWindow", "Deals"))
        self.chatbot_btn_2.setText(_translate("MainWindow", "ChatBot"))
        self.feedback_btn_2.setText(_translate("MainWindow", "Feedback"))
        self.map_btn_2.setText(_translate("MainWindow", "Map"))
        self.quiz_btn_2.setText(_translate("MainWindow", "Quiz"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.ProfileSetting.setText(_translate("MainWindow", "Profile Setting "))
        self.FirstName.setText(_translate("MainWindow", "First Name"))
        self.LastName.setText(_translate("MainWindow", "Last Name"))
        self.MobileNumber.setText(_translate("MainWindow", "Mobile Number"))
        self.Address.setText(_translate("MainWindow", "Address "))
        self.Postcode.setText(_translate("MainWindow", "Postcode"))
        self.Area.setText(_translate("MainWindow", "Area"))
        self.save_profile_button.setText(_translate("MainWindow", "Save Profile"))
        self.DateOfBirth.setText(_translate("MainWindow", "Date Of Birth"))
        self.Gender.setText(_translate("MainWindow", "Gender"))
        self.male_checkBox.setText(_translate("MainWindow", "Male"))
        self.female_checkBox.setText(_translate("MainWindow", "Female"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "BookingID"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Venue"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Date"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Quantities"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Amount per ticket"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "After Discount"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "Status"))
        header = self.treeWidget.header()

        # Set the size for each column
        header.resizeSection(0, 100)  # Adjust the size as needed
        header.resizeSection(1, 300)
        header.resizeSection(2, 100)
        header.resizeSection(3, 100)
        header.resizeSection(4, 150)
        header.resizeSection(5, 150)
        header.resizeSection(6, 90)
        # Assuming self.treeWidget is your QTreeWidget
        self.treeWidget.resize(1000, 400)  # Adjust the width and height as needed
        # Assuming self.treeWidget is your QTreeWidget
        font = QtGui.QFont()  # Create a QFont object
        font.setFamily("Arial")  # Set the font family (adjust as needed)
        font.setPointSize(12)  # Set the font size (adjust as needed)
        self.treeWidget.header().setFont(font)  # Set the font style to italic (adjust as needed)
        self.treeWidget.setFont(font)  # Apply the font to the QTreeWidget
        self.attraction_btn_2.setFont(font)
        self.profile_btn_2.setFont(font)
        self.history_btn_2.setFont(font)
        self.booking_btn_2.setFont(font)
        self.deal_btn_2.setFont(font)
        self.chatbot_btn_2.setFont(font)
        self.feedback_btn_2.setFont(font)
        self.map_btn_2.setFont(font)
        self.quiz_btn_2.setFont(font)
        self.exit_btn_2.setFont(font)
        self.ProfileSetting.setFont(font)
        self.FirstName.setFont(font)
        self.LastName.setFont(font)
        self.MobileNumber.setFont(font)
        self.Address.setFont(font)
        self.Postcode.setFont(font)
        self.Area.setFont(font)
        self.save_profile_button.setFont(font)
        self.DateOfBirth.setFont(font)
        self.Gender.setFont(font)
        self.male_checkBox.setFont(font)
        self.female_checkBox.setFont(font)

        self.history_label.setText(_translate("MainWindow", "Booking History"))
        self.feedbackpage.setText(_translate("MainWindow", "Feedback"))


        # Load icons for checked and unchecked states
        self.change_btn_unchecked_icon = QtGui.QIcon(QtGui.QPixmap("navigationmanual.png"))
        self.change_btn_checked_icon = QtGui.QIcon(QtGui.QPixmap("back.png"))

        # Create a slot method to update the change_btn icon
        def update_change_btn_icon(checked):
            if checked:
                self.change_btn.setIcon(self.change_btn_unchecked_icon)
            else:
                self.change_btn.setIcon(self.change_btn_checked_icon)

        # Connect the change_btn's toggled signal to the slot method
        self.change_btn.toggled.connect(update_change_btn_icon)
        self.deal_btn_2.clicked.connect(self.fetch_and_populate_deals_data)

    def open_chatbot_page_1(self):
        self.chatbot_page_1 = QtWidgets.QMainWindow()

        # Add QWebEngineView to display HTML
        web_view = QWebEngineView(self.chatbot_page_1)
        web_view.setUrl(QtCore.QUrl.fromLocalFile("C:\\Users\\s\\Desktop\\tourism kiosk\\chatbot.html"))

        # Set the QWebEngineView as the central widget
        self.chatbot_page_1.setCentralWidget(web_view)
        self.chatbot_page_1.setGeometry(100, 100, 400, 600)  # Adjust the values as needed

        self.chatbot_page_1.show()

import resource_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()