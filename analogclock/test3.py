import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPainterPath
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle('QPainter를 이용한 그래픽스')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # 그리기 함수의 호출 부분
        # self.drawText(event, qp)
        # self.drawPoints(event, qp)
        # self.drawRectangles(event, qp)
        # self.drawLines(event, qp)
        # self.drawBrushes(event, qp)
        self.drawBezierCurve(event,qp)
        qp.end()
    
    def drawText(self, event, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('나눔명조', 35))
        qp.drawText(event.rect(), Qt.AlignCenter, '스산한 늦가을\n아니.. 초겨울인가?')

    def drawPoints(self, event, qp):
        pen = QPen(Qt.red, 5)
        qp.setPen(pen)
        size = self.size()
        
        for i in range(700):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)  

    def drawRectangles(self, event, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(50, 50, 100, 100)
        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(150, 150, 100, 100)
        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 250, 100, 100)

    def drawLines(self, event, qp):
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(50, 50, 350, 50)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(50, 110, 350, 110)
        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(50, 170, 350, 170)
        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(50, 230, 350, 230)
        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(50, 290, 350, 290)
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(50, 350, 350, 350)

    def drawBrushes(self, event, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 20, 110, 110)
        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(145, 20, 110, 110)
        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(270, 20, 110, 110)
        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 145, 110, 110)
        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(145, 145, 110, 110)
        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(270, 145, 110, 110)
        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 270, 110, 110)
        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(145, 270, 110, 110)
        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(270, 270, 110, 110)

    def drawBezierCurve(self, event, qp):
        pen = QPen(Qt.black, 7)
        qp.setPen(pen)
        path = QPainterPath()
        path.moveTo(50, 50)
        path.cubicTo(200, 50, 50, 350, 350, 350)
        qp.drawPath(path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())