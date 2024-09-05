import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QRegion
from PyQt5.QtCore import Qt

class ui_form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        margin = 10
        Form.resize(500, 500)
        self.mainFrame = QtWidgets.QFrame(Form)
        self.mainFrame.setGeometry(QtCore.QRect(10, 10, 481, 481))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mainFrame.setObjectName("mainFrame")
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        Form.setStyleSheet(
        "QFrame#mainFrame {\n"
        "    border: 5px solid grey;\n"
        "    border-radius: 240px;\n"
        "    background-color: rgba(255, 0, 0, 50);\n"
        "}\n"
        "QWidget#Form {\n"
        "    background-color: rgba(255, 255, 255, 0);\n"
        "    border: 5px solid blue;\n"
        "    border-radius: 250px;\n"
        "}"
        )
        self.mainFrame.mouseDoubleClickEvent = lambda event: QtWidgets.qApp.quit()
        # Form.setWindowOpacity(0.4)
        # self.mainFrame.setWindowOpacity(1)

        
class mywindow(QMainWindow, ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.region_and_mask()

    def region_and_mask(self):
        my_region = QRegion(self.rect(), QRegion.Ellipse)
        self.setMask(my_region)  

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            app.quit()
    
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mywindow()
    win.show()
    app.exec_()