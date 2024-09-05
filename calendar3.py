import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QCalendarWidget, QStyle, QItemDelegate, QCalendarWidget, QTableView, QWidget, QMenu
from PyQt5.QtCore import Qt, QDate

class CalendarItemDelegate(QItemDelegate):
    def __int__(self):
        super().__init__()

    def paint(self, painter, option, index):
        # Dates are row and column cells greater than zero
        painter._date_flag = index.row() > 0 and index.column() > 0
        super().paint(painter, option, index)

    def drawDisplay(self, painter, option, rect, text):
        if painter._date_flag:
            text += "\n머냐?"
            option.displayAlignment = QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft
        super().drawDisplay(painter, option, rect, text)

    def drawFocus(self, painter, option, rect):
        super().drawFocus(painter, option, rect)
        if option.state & QStyle.State_Selected:
            painter.save()
            painter.setPen(Qt.red)
            painter.drawRect(rect.adjusted(0, 0, -1, -1))
            painter.restore()

    def paintCell(self, painter, rect, date):
        print("paintCell")
        super().paintCell(painter, rect, date)

    

class MyWindow(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200, 800, 600)

        self.qt_calendar_calendarview = self.findChild(QTableView, "qt_calendar_calendarview")
        qt_calendar_delegate = CalendarItemDelegate(self.qt_calendar_calendarview)
        self.qt_calendar_calendarview.setItemDelegate(qt_calendar_delegate)

        self.events = {
            QDate(2024, 8, 24): ["Bob's birthday"],
            QDate(2024, 8, 19): ["Alice's birthday"]
        }

        self.show()

    def contextMenuEvent(self,event):
        print("contextMenuEvent")
        cmenu = QMenu(self)
        AodAct = cmenu.addAction("AlwaysOn")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()
        elif action == AodAct:
            on = bool(win.windowFlags() & Qt.WindowStaysOnTopHint)
            win.setWindowFlag(Qt.WindowStaysOnTopHint, not on)
            win.show()

        

    def eventFilter(self, object,event):
        print("eventFilter")
        return False

    def mouseDoubleClickEvent(self, event):
        print("Double clicked")

    def mousePressEvent(self, event):
        print("mousePressEvent")

    def paintCell(self, painter, rect, date):
        print("paintCell")
        super().paintCell(painter, rect, date)

        if date in self.events:
            painter.setBrush(Qt.red)
            painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 3, 3)

    def drawDisplay(self, painter, option, rect, text):
        print("Draw Display")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())