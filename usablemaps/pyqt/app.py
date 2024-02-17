import os

from PyQt5 import uic
<<<<<<< HEAD
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog
=======
from PyQt5.QtWidgets import QApplication, QMainWindow, QKeyEvent, QGraphicsView, QPushButton
>>>>>>> 3c3d94c1dc896ea1e0196c555b289b0655b2a569

cwd = os.getcwd()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'MapInterface.ui', self)
        self.setWindowTitle("MapSMTH")


<<<<<<< HEAD
    def ChangeMapImage(self):
        pass

=======
#############БИНДЫ#ДЛЯ#КЛАВИШ###########
    def keyPressEvent(self):
        #Приближение/Отдаление
        if event.key() == Qt.Key_PgUp:
            pass

        if event.key() == Qt.Key_PgDown:
            pass

        #Перемещение на стрелочки
        if event.key() == Qt.Key_Up:
            pass

        if event.key() == Qt.Key_Down:
            pass

        if event.key() == Qt.Key_Left:
            pass

        if event.key() == Qt.Key_Right:
            pass

        #Для нажатий мышкой
        #if event.buttons() == Qt.LeftButton:
        #    x = event.pos().x()
        #    y = event.pos().y()


########ДЛЯ#СМЕНЫ#КАРТИНКИ#КАРТЫ########
    def ChangeMapImage(self):
        pass


########################################
>>>>>>> 3c3d94c1dc896ea1e0196c555b289b0655b2a569
