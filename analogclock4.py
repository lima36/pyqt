import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class WidgetOne(QtWidgets.QWidget):
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.red)
        painter.setBrush(QtCore.Qt.green)

    def minimumSizeHint(self):
        return QtCore.QSize(1000, 1000)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)

        widget_one = WidgetOne()
        # or
        # widget_one.setFixedSize(1000, 1000)
        # or
        # widget_one.setMinimumSize(1000, 1000)
        scroll = QtWidgets.QScrollArea(widgetResizable=True)
        scroll.setWidget(widget_one)

        layout.addWidget(scroll, 0, 0)
        # layout.addWidget(WidgetTwo(), 1, 1)
        self.setCentralWidget(widget)
        self.resize(500, 500)


def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication([])

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()