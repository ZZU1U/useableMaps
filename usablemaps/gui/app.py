import os
import PyQt5
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog, QGraphicsView, QPushButton)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/MapInterface.ui', self)
        self.setWindowTitle("MapSMTH")
        self.pixmap = None
        self.mapView.installEventFilter(self)
        self.mapView.setMinimumSize(1, 1)

    # https://stackoverflow.com/questions/43569167/pyqt5-resize-label-to-fill-the-whole-window
    def eventFilter(self, source, event):
        if source is self.mapView and self.pixmap and event.type() == PyQt5.QtCore.QEvent.Resize:
            self.mapView.setPixmap(self.pixmap.scaled(
                self.mapView.size(), PyQt5.QtCore.Qt.KeepAspectRatio,
                PyQt5.QtCore.Qt.SmoothTransformation))
            self.mapView.show()
        return super(MyWidget, self).eventFilter(source, event)

    #############БИНДЫ#ДЛЯ#КЛАВИШ###########
    def keyPressEvent(self, event):
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
    def ChangeMapImage(self, filename):
        self.pixmap = QPixmap(filename)
        self.mapView.setPixmap(self.pixmap.scaled(
            self.mapView.size(), PyQt5.QtCore.Qt.KeepAspectRatio,
            PyQt5.QtCore.Qt.SmoothTransformation))
        self.mapView.show()
