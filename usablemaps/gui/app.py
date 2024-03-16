import logging
import PyQt5
import tempfile
from api.maps import get_map
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/MapInterface.ui', self)
        self.setWindowTitle("MapSMTH")
        self.pixmap = None
        self.mapView.installEventFilter(self)
        self.mapView.setMinimumSize(1, 1)
        self.mapView.setFocusPolicy(Qt.NoFocus)
        self.showButton.clicked.connect(lambda e: self.do_map())
        self.scale = 0
        self.cord_x = -1
        self.cord_y = -1

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
        # Приближение/Отдаление
        if event.key() == Qt.Key_PageUp and self.scale:
            self.scale = min(self.scale + 1, 20)
            self.do_map(changes=True)

        if event.key() == Qt.Key_PageDown and self.scale:
            self.scale = max(self.scale - 1, 1)
            self.do_map(changes=True)

        # Перемещение на стрелочки
        if event.key() == Qt.Key_W:
            self.cord_y = min(self.cord_y + 1, 80)
            self.do_map(changes=True)

        if event.key() == Qt.Key_S:
            self.cord_y = max(self.cord_y - 1, -80)
            self.do_map(changes=True)

        if event.key() == Qt.Key_D:
            self.cord_x = min(self.cord_x + 1, 180)
            self.do_map(changes=True)

        if event.key() == Qt.Key_A:
            self.cord_x = max(self.cord_x - 1, -180)
            self.do_map(changes=True)


    def do_map(self, changes=None):
        if changes is None:
            try:
                self.cord_x = float(self.LE_Coordinates1.text())
                self.cord_y = float(self.LE_Coordinates2.text())
                self.scale = int(self.LE_Scale.text())

                if self.scale < 1 or self.scale > 20:
                    raise ValueError

                if abs(self.cord_x) > 180:
                    raise ValueError

                if abs(self.cord_y) > 80:
                    raise ValueError

            except ValueError:
                self.mapView.setText('Неправильный ввод')
                return
        else:
            if self.cord_x:
                self.LE_Coordinates1.setText(str(self.cord_x))
                #self.LE_Coordinates1.setText('')
            if self.cord_y:
                self.LE_Coordinates2.setText(str(self.cord_y))
                #self.LE_Coordinates2.setText('')
            if self.scale:
                self.LE_Scale.setText(str(self.scale))
                self.LE_Scale.setText('')

        with tempfile.NamedTemporaryFile() as file:
            cont = get_map((self.cord_x, self.cord_y), self.scale)

            if cont:
                file.write(cont)
            else:
                self.mapView.setText('Что-то пошло не так')
                return

            self.ChangeMapImage(file.name)

        logging.debug('Done!')

    ########ДЛЯ#СМЕНЫ#КАРТИНКИ#КАРТЫ########
    def ChangeMapImage(self, filename):
        self.pixmap = QPixmap(filename)
        self.mapView.setPixmap(self.pixmap.scaled(
            self.mapView.size(), PyQt5.QtCore.Qt.KeepAspectRatio,
            PyQt5.QtCore.Qt.SmoothTransformation))
        self.mapView.show()
