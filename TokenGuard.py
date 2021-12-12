##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

import os
from ctypes import *
from ctypes.wintypes import *
import threading

from PySide6 import QtGui
import systrayicon
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from py_toggle import *
import sys
import time
import shared_variables
import requests
import webbrowser

version = "1.0.0"
try:
    latestversion = str(requests.get("https://raw.githubusercontent.com/ZaikoARG/TokenGuard/main/version").text).strip()
except:
    latestversion = version


# Define Notifications

Notifications = {
    "MinimizedApp": ["The application was sent to the background", "Background"],
    "MaximizedApp": ["The application was sent to the foreground", "Foreground"],
    "Thanks": ["Thank you very much for using TokenGuard", "Thanks for Using"],
    "WaitingDiscord": ["Please open Discord to start protection", "Waiting Discord Process"],
    "DiscordError": ["The Discord process has been closed. Please turn on again and restart protection", "Discord Error"]
}


class MainWindow(QMainWindow): # TokenGuard GUI
    def __init__(self):
        self.mainwindow = QMainWindow.__init__(self)

        self.resize(789, 411)
        self.setMaximumSize(QSize(789, 411))
        self.setMinimumSize(QSize(789, 411))


        QtGui.QFontDatabase.addApplicationFont(shared_variables.config_path + r"\resources\Mitr-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(shared_variables.config_path + r"\resources\Montserrat-SemiBold.ttf")
        QtGui.QFontDatabase.addApplicationFont(shared_variables.config_path + r"\resources\Montserrat-SemiBoldItalic.ttf")

        self.setWindowIcon(QPixmap(shared_variables.config_path + r"\resources\TokenGuard.ico"))

        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("""
        #container { 
        background-color: #2F3441;}""")
        self.container.setGeometry(QRect(0, 0, 789, 411))

        self.layout = QVBoxLayout(self.container)
        self.layout.setSpacing(0)

        self.dropShadowFrame = QFrame(self.container)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setEnabled(True)
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setGeometry(QRect(0, 0, 789, 411))
        

        self.toggle = PyToggle()
        self.toggle.setParent(self.dropShadowFrame)
        self.toggle.setGeometry(QRect(364, 270, 0, 0))
        self.label = QLabel(self.dropShadowFrame)
        self.label.setText("TokenGuard")
        self.label.setFont(QFont("Arial", 40))
        self.label.setContentsMargins(0,0,0,0)
        self.label.setGeometry(QRect(295, 70, 331, 41))
        self.label.setStyleSheet("color: white; font-family: Mitr;")


        self.label = QLabel(self.dropShadowFrame)
        self.label.setText(f"Version {version}")
        self.label.setFont(QFont("Arial", 8))
        self.label.setGeometry(QRect(700, 380, 75, 16))
        self.label.setStyleSheet("color: white; font-family: Montserrat Semibold; font-style: italic;")
    


        self.logo = QLabel(self.dropShadowFrame)
        self.logo.setPixmap(QPixmap(shared_variables.config_path + r"\resources\logo.png"))
        self.logo.setContentsMargins(0,0,0,0)
        self.logo.setGeometry(163, 30, 111, 111)


        self.pages = QStackedWidget()
        

        
        self.layout.addWidget(self.dropShadowFrame)
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        

        if version != latestversion:
            dd = DownloadDialog()
            dd.exec_()



        self.show()
        listener = threading.Thread(target=self.listener)
        listener.start()
        

    def closeEvent(self, event: QCloseEvent) -> None:
        st.notify(Notifications["Thanks"])
        os.kill(os.getpid(), 9)

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if event.oldState() == Qt.WindowNoState or self.windowState() == Qt.WindowMaximized:
                self.hidden = True
                self.hideappEvent()

    def listener(self):
        # Listener for all events in the program (Minimize, Errors, etc..)
        self.hidden = False
        WaitingPass = False
        while 1:
            time.sleep(1)
            if self.hidden == True and shared_variables.WindowHide == False:
                self.hidden = False
                shared_variables.WindowHide = True
                self.showappEvent()
            elif shared_variables.DiscordError == True:
                self.toggle.Error()
                st.notify(Notifications["DiscordError"])
                shared_variables.DiscordError = False
            elif shared_variables.WaitingDiscord == True and WaitingPass == False:
                WaitingPass = True
                st.notify(Notifications["WaitingDiscord"])

    def hideappEvent(self):
        time.sleep(1)
        self.hide()
        self.setWindowFlag(Qt.ToolTip, True)
        st.notify(Notifications["MinimizedApp"])
        st.remove_notify(2)
    
    def showappEvent(self):
        time.sleep(1)
        self.setWindowFlag(Qt.ToolTip, False)
        self.showNormal()
        self.activateWindow()
        st.notify(Notifications["MaximizedApp"])

        
class DownloadDialog(QDialog): # New Version Message Box
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("New Version Available")
        self.setWindowIcon(QIcon(shared_variables.config_path + r"\resources\logo.png"))
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.redirect)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("New Version of TokenGuard Available. Do you want Download Now ?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def redirect(self):
        webbrowser.open("https://github.com/ZaikoARG/TokenGuard/releases")
        self.reject()



if "__main__" == __name__:
    # Define SysTrayIcon Thread
    st = systrayicon.SysTrayIcon()
    # Initialize SysTrayIcon
    st.start()
    # Define the App
    app = QApplication(sys.argv)
    # Define the MainWindow
    window = MainWindow()
    # Start App
    sys.exit(app.exec())