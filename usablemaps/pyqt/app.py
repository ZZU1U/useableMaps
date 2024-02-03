import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QKeyEvent, QGraphicsView, QPushButton

cwd = os.getcwd()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'MapInterface.ui', self)
        self.setWindowTitle("MapSMTH")


#############БИНДЫ#ДЛЯ#КЛАВИШ###########
    def keyPressEvent(self):
        if event.key() == Qt.Key_Up:
            pass

        if event.key() == Qt.Key_Down:
            pass

        #Для нажатий мышкой
        #if event.buttons() == Qt.LeftButton:
        #    x = event.pos().x()
        #    y = event.pos().y()


########ДЛЯ#СМЕНЫ#КАРТИНКИ#КАРТЫ########
    def ChangeMapImage(self):
        pass


########################################