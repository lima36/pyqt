import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading
import time


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer_slot)

    def timer_slot(self):
        name = threading.currentThread().getName()
        print(f"timer slot is called by {name}")
        print("before sleep")
        time.sleep(5)
        print("after sleep")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()