##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

import threading
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import tokenprotection
import shared_variables

class PyToggle(QCheckBox):
    # Toggle Check Widget for GUI
    def __init__(
        self, 
        witdth = 60, 
        bg_color = "#777", 
        circle_color = "#DDD", 
        active_color = "#599afe", 
        animation_curve = QEasingCurve.Type.OutBounce
    ):
        QCheckBox.__init__(self)

        self.parentWidget()

        self.setFixedSize(witdth, 28)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.bg_color = bg_color
        self.circle_color = circle_color
        self.active_color = active_color

        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)


        self.stateChanged.connect(self.start_transition)
    

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()


    def Error(self):
        self.setCheckState(Qt.Unchecked)
        self.start_transition


    
    def start_transition(self, value):
        self.animation.stop()

        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)

        self.animation.start()

        if self.isChecked() == True and shared_variables.Protection_Status == False:
            tp = threading.Thread(target=tokenprotection.TokenProtection().start, args=[])
            tp.start()
        elif self.isChecked() == False and shared_variables.Protection_Status == True:
            tokenprotection.TokenProtection().stop()



    def hitButton(self, pos: QPoint) -> bool:
        return self.contentsRect().contains(pos)

    def paintEvent(self, e) -> None:
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        p.setPen(Qt.PenStyle.NoPen)
        
        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            p.setBrush(QColor(self.bg_color))
            p.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self.circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            p.setBrush(QColor(self.active_color))
            p.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self.circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)

        p.end()