##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

import pystray
from PIL import Image, ImageDraw
import threading, time, sys
import webbrowser
import os
from shared_variables import config_path
import shared_variables
class SysTrayIcon():
    # Class for create icon in the Taskbar
    def __init__(self) -> None:

        self.icon = pystray.Icon('TokenGuard')
        self.icon.title = "TokenGuard"
        self.icon.icon = self.create_image()
        self.icon.menu = pystray.Menu(
            pystray.MenuItem(
                "Open",
                self.leavebackground
            ),
            pystray.MenuItem(
                "Contact Us",
                self.contactus

            ),
            pystray.MenuItem(
                "Quit",
                self.on_clicked
            )
        )


    def SetWindowHandle(self, windowhandle):
        self.windowhandle = windowhandle

    def on_clicked(self, icon, item):
        os.kill(os.getpid(), 9)

    def contactus(self, icon, item):
        webbrowser.open("https://discord.gg/9jMqbyvMZS")

    def leavebackground(self, icon, item):
        shared_variables.WindowHide = False

    def create_image(self):
        # Open Logo Image
        img = Image.open(config_path +  r"\resources\TokenGuard.ico")
        return img

    def notify(self, data:list):
        self.icon.notify(data[0], data[1])

    def remove_notify(self, waiting_time=None) -> None:
        if waiting_time != None:
            time.sleep(waiting_time)
            self.icon.remove_notification()
            


    def start(self):
        t = threading.Thread(target=self.icon.run)
        t.start() 

    def stop(self):
        self.icon.stop()