import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog

cwd = os.getcwd()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'MapInterface.ui', self)
        self.setWindowTitle("MapSMTH")


    def ChangeMapImage(self):
        pass

