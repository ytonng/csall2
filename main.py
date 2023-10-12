import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream


from sidebar_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)


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

    def on_trip_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_trip_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_favourite_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_favourite_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_booking_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_booking_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_deal_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_deal_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_customerservice_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_customerservice_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_feedback_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_feedback_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    ## loading style file, Example 2
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())


    window = MainWindow()
    window.show()

    sys.exit(app.exec())



