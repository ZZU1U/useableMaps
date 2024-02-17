import tempfile
import sys
from PyQt5.QtWidgets import QApplication
from gui.app import MyWidget
from api.maps import get_map

cords = list(map(int, input().split()))

scale = float(input())

app = QApplication(sys.argv)
window = MyWidget()

with tempfile.NamedTemporaryFile() as file:
    cont = get_map(cords, scale)

    if cont:
        file.write(cont)
    else:
        print('Произошла ошибка!')
        sys.exit(1)

    window.ChangeMapImage(file.name)

window.show()

sys.exit(app.exec_())
