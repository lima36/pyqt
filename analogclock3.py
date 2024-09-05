from PyQt5.QtCore import QEvent, QSize, Qt, QTime, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import QPoint, QRect, QDate
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QPolygon
import PyQt5
class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initial_pos = None
        title_bar_layout = QHBoxLayout(self)
        # title_bar_layout.setContentsMargins(1, 1, 1, 1)
        # title_bar_layout.setSpacing(2)
        self.title = QLabel(f"{self.__class__.__name__}", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet(
            """
        QLabel { text-transform: uppercase; font-size: 10pt; margin-left: 0px; color:red }
        """
        )

        if title := parent.windowTitle():
            self.title.setText(title)
        title_bar_layout.addWidget(self.title)
        # Min button
        # self.min_button = QToolButton(self)
        # min_icon = QIcon()
        # min_icon.addFile("min.svg")
        # self.min_button.setIcon(min_icon)
        # self.min_button.clicked.connect(self.window().showMinimized)

        # Max button
        # self.max_button = QToolButton(self)
        # max_icon = QIcon()
        # max_icon.addFile("max.svg")
        # self.max_button.setIcon(max_icon)
        # self.max_button.clicked.connect(self.window().showMaximized)

        # Close button
        self.close_button = QToolButton(self)
        close_icon = QIcon()
        close_icon.addFile("close.svg")  # Close has only a single state.
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        # Normal button
        # self.normal_button = QToolButton(self)
        # normal_icon = QIcon()
        # normal_icon.addFile("normal.svg")
        # self.normal_button.setIcon(normal_icon)
        # self.normal_button.clicked.connect(self.window().showNormal)
        # self.normal_button.setVisible(False)
        # Add buttons
        buttons = [
            # self.min_button,
            # self.normal_button,
            # self.max_button,
            self.close_button,
        ]
        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(16, 16))
            button.setStyleSheet(
                """QToolButton {
                    border: none;
                    padding: 2px;
                }
                """
            )
            title_bar_layout.addWidget(button)

    def window_state_changed(self, state):
        if state == Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.max_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.max_button.setVisible(True)

week = {1:"월", 2:"화",3:"수", 4:"목", 5:"금", 6:"토", 7:"일"}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mydate = QDate.currentDate()
        print(mydate)
        myweek = QDate()

        print(mydate.weekNumber()[0])
        # myweek = QDate.dayOfWeek()
        # print(myweek)
        self.setWindowTitle(str(mydate.toString('MM/dd/ddd/w')) + str(mydate.weekNumber()[0]))
        self.timeZoneOffset = 0
        self.resize(200, 200)
        timer = QTimer(self)
        # adding action to the timer
        # update the whole code
        timer.timeout.connect(self.update)
        # setting start time of timer i.e 1 second
        timer.start(1000)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.hourHand = QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -40)
        ])
        self.minuteHand = QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -70)
        ])

        self.hourColor = QColor(0, 127, 0)
        self.minuteColor = QColor(0, 127, 127, 191)
        # self.setGeometry(300, 300, 400, 400)
        central_widget = QWidget()
        # This container holds the window contents, so we can style it.
        central_widget.setObjectName("Container")
        # central_widget.setStyleSheet(
        #     """#Container {
        #     background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f);
        #     border-radius: 5px;
        # }"""
        # )
        # setting background color to the window
        # self.setStyleSheet("background : black;")
 
        # creating hour hand
        self.hPointer = QPolygon([QPoint(6, 7),
                                        QPoint(-6, 7),
                                        QPoint(0, -50)])
 
        # creating minute hand
        self.mPointer = QPolygon([QPoint(6, 7),
                                  QPoint(-6, 7),
                                  QPoint(0, -70)])
 
        # creating second hand
        self.sPointer = QPolygon([QPoint(1, 1),
                                  QPoint(-1, 1),
                                  QPoint(0, -90)])
        # colors
        # color for minute and hour hand
        self.bColor = Qt.green
 
        # color for second hand
        self.sColor = Qt.red

        self.title_bar = CustomTitleBar(self)

        work_space_layout = QVBoxLayout()
        work_space_layout.setContentsMargins(11, 11, 11, 11)
        # work_space_layout.addWidget(QLabel("Hello, World!", self))

        centra_widget_layout = QVBoxLayout()
        centra_widget_layout.setContentsMargins(0, 0, 0, 0)
        centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        centra_widget_layout.addWidget(self.title_bar)
        centra_widget_layout.addLayout(work_space_layout)

        central_widget.setLayout(centra_widget_layout)
        self.setCentralWidget(central_widget)

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()

    def window_state_changed(self, state):
        self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
        self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.pos()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None:
            delta = event.pos() - self.initial_pos
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y(),
            )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()

    # def paintEvent(self, event):
    #     qp = QPainter(self)
    #     print("paintEvent", event)
    #     self.drawRect(event, qp)
     # method for paint event
    def paintEvent(self, event):
 
        # getting minimum of width and height
        # so that clock remain square
        rec = min(self.width(), self.height())
 
        # getting current time
        tik = QTime.currentTime()
 
        # creating a painter object
        painter = QPainter(self)

        # method to draw the hands
        # argument : color rotation and which hand should be pointed
        def drawPointer(color, rotation, pointer):
 
            # setting brush
            painter.setBrush(QBrush(color))
 
            # saving painter
            painter.save()
 
            # rotating painter
            painter.rotate(rotation)
 
            # draw the polygon i.e hand
            painter.drawConvexPolygon(pointer)
 
            # restore the painter
            painter.restore()
 
 
        # tune up painter
        painter.setRenderHint(QPainter.Antialiasing)
 
        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)
 
        # scale the painter
        painter.scale(rec / 300, rec / 300)
        # set current pen as no pen
        painter.setPen(Qt.NoPen)
 
        # draw each hand
        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)

        # drawing background
        painter.setPen(QPen(self.bColor))
 
        # for loop
        for i in range(0, 60):
            # drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87, 0, 97, 0)
                painter.drawRect(87, 0, 10,10)
            # rotating the painter
            painter.rotate(6)
 
        # ending the painter
        painter.end()

    def paintEvent2(self, event):
        side = min(self.width(), self.height())
        time = QTime.currentTime()
        time = time.addSecs(self.timeZoneOffset * 3600)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.hourColor))

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(self.hourHand)
        painter.restore()

        painter.setPen(self.hourColor)

        for i in range(0, 12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.minuteColor))

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(self.minuteHand)
        painter.restore()

        painter.setPen(QPen(self.minuteColor))

        for j in range(0, 60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.end()

    # def drawRect(self, event, painter):
    #     print("drawRect")
    #     painter.setPen(QColor(255, 0, 0))
    #     painter.setBrush(QColor(255, 0, 0))
    #     painter.drawRect(QRect(80, 20, 40, 100))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
