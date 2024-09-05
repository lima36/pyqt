import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint, QRect

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        qp = QPainter(self)
        print("paintEvent", event)
        self.drawLine(event,qp)
        self.drawRect(event, qp)

    def drawLine(self,event,painter):
        painter.setPen(QColor(255, 0, 0))
        painter.drawLine(QPoint(85, 10), QPoint(85, 90))

    def drawRect(self, event, painter):
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(QRect(80, 20, 10, 60))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()