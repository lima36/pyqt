import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)
    

    def mouseMoveEvent(self, e):
        painter = QPainter(self.label.pixmap())
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.update()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()