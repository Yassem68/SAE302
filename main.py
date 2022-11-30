from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()