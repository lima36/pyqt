from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

from analogclock import PyAnalogClock

form_ui = uic.loadUiType('test.ui')[0]

class MyMainWindow(QMainWindow, form_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    # win.setupUi(slf)
    win.show()
    app.exec_()