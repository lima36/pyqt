import sys
from PyQt5.QtCore    import Qt, QRectF, QDate
from PyQt5.QtGui     import QPainter, QColor, QFont
from PyQt5.QtWidgets import QCalendarWidget, QApplication

class CalendarWidget(QCalendarWidget):

    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        if date == QDate(2024, 8, 15):
            painter.save()
            painter.drawRect(rect)
            painter.setPen(QColor(168, 34, 3))
            painter.setFont(QFont('Decorative', 8))            
            painter.drawText(QRectF(rect), Qt.TextSingleLine|Qt.AlignTop, str(date.day()))
            painter.drawText(rect, Qt.AlignTop| Qt.AlignHCenter, '광복절') 

            painter.restore()
        else:
            QCalendarWidget.paintCell(self, painter, rect, date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CalendarWidget()
    w.show()
    sys.exit(app.exec_())