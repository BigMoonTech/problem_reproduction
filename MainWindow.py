from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QGridLayout, QTextBrowser


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 515)
        MainWindow.setMinimumSize(QSize(720, 515))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout2 = QVBoxLayout(self.page)
        self.verticalLayout2.setObjectName(u"verticalLayout2")
        self.education_textbox = QTextBrowser(self.page)
        self.education_textbox.setObjectName(u"education_textbox")
        self.verticalLayout2.addWidget(self.education_textbox)


        self.education_textbox.setOpenLinks(False)

        self.stackedWidget.addWidget(self.page)
        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.stackedWidget.setCurrentIndex(0)

