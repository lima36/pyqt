import sys
from PyQt5.QtWidgets import QWidget, QSizePolicy, QApplication
# from PyQt5.QtCore import Signal, Qt, QTimer, QTime, QPoint, QRectF, QSize
from PyQt5.QtCore import pyqtSignal, Qt, QTimer, QTime, QPoint, QRectF, QSize
from PyQt5.QtGui import QPainter,QColor, QRadialGradient, QPen

class AnalogClock(QWidget):
    updated = pyqtSignal(QTime)   #updated(QTime currentTime);
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.backgroundColor = Qt.yellow
        self.timeZoneOffset = 0
        self.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        # self.setWindowFlag(Qt.FramelessWindowHint)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

    def sizeHint(self):
        return QSize(200,200)

    def setBgColor(self,newColor):
        self.backgroundColor = newColor

    def setTimeZone(self,hourOffset):
        self.timeZoneOffset = min(max(-12,hourOffset),12)*3600
        self.update()

    def paintEvent(self,event):
        hourHand   = [QPoint(7,8), QPoint(-7,8), QPoint(0,-40)]
        minuteHand = [QPoint(7,8), QPoint(-7,8), QPoint(0,-70)]
        secondHand = [QPoint(0,8),QPoint(0,-80)]

        hourColor   = QColor(127,   0, 127)
        minuteColor = QColor(  0, 127, 127, 191)
        secondColor = QColor(255,   0,   0, 191)

        side = min(self.width(),self.height())
        time = QTime.currentTime()   # static function
        time = time.addSecs(self.timeZoneOffset)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing,True)
        painter.translate(self.width()/2, self.height()/2)
        painter.scale(side/200.0,side/200.0)

        # Draw circle
        radialGradient = QRadialGradient(0,0,100,-40,-40) # center, radius, focalPoint
        radialGradient.setColorAt(0.0,Qt.white)
        radialGradient.setColorAt(1.,self.backgroundColor)


        painter.setBrush(radialGradient)
        painter.setPen(QPen(Qt.darkGray,0))  # darkGray cosmetic pen
        painter.drawEllipse(QRectF(-97,-97,194,194))

        return

        # Draw minute tick
        painter.setPen(minuteColor)
        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92,0,96,0)
            painter.rotate(6.0)

        # draw hour hand
        painter.setPen(Qt.NoPen)
        painter.setBrush(hourColor)

        painter.save()
        painter.rotate(30.0*((time.hour()+time.minute()/60.0)))
        painter.drawConvexPolygon(hourHand)
        painter.restore()

        # draw hour tick
        painter.setPen(hourColor)
        for i in range(12):
            painter.drawLine(88,0,96,0)
            painter.rotate(30.0)

        # draw mimute hand
        painter.setPen(Qt.NoPen)
        painter.setBrush(minuteColor)

        painter.save()
        painter.rotate(6.8*(time.minute()+time.second()/60.0))
        painter.drawConvexPolygon(minuteHand)
        painter.restore()

        # Draw second hand
        painter.setPen(secondColor)

        painter.save()
        painter.rotate(6.0*time.second())
        painter.drawLine(secondHand[0],secondHand[1])
        painter.restore()

        self.updated.emit(time)



if __name__ == "__main__":
    app = QApplication(sys.argv)    

    clock = AnalogClock()
    clock.setWindowTitle("Clock")
    clock.resize(100,100)
    clock.show()

    app.exec_()