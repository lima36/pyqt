import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QTextCharFormat
from PyQt5 import QtCore
import json

form_class = uic.loadUiType("calendar2.ui")[0]

holidays = {'20240805':'그냥', '20240815':'광복절', '20240820':'테스트', '20240825':'그냥2', '20240830':'마지막날'}
todo = {}
# class WindowClass(QMainWindow, form_class) :
class WindowClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # self.setWindowOpacity(0.5)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setStyleSheet("background:transparent;")

        #QCalendarWidget의 시그널
        self.calendarWidget_Test.clicked.connect(self.calendarClicked)
        self.calendarWidget_Test.currentPageChanged.connect(self.calendarPageChanged)
        self.calendarWidget_Test.selectionChanged.connect(self.calendarSelectionChanged)        

        #QCalendarWidget이 자동으로 오늘 날짜가 있는 달력을 보여주게 설정
        self.todayDate = QDate.currentDate()
        self.calendarWidget_Test.setCurrentPage(self.todayDate.year(), self.todayDate.month())

        fm = QTextCharFormat()
        fm.setForeground(Qt.red)
        fm.setBackground(Qt.yellow)

        with open('holiday.json', 'r', encoding='UTF-8') as f:
            self.data = json.load(f)

        for bday in self.data.keys():
            dday = QDate.fromString(bday, "yyyyMMdd")
            self.calendarWidget_Test.setDateTextFormat(dday, fm)
        # for holiday in self.data:
        #     if holiday['kind'] == "휴일":
        #         dday = QDate.fromString(str(holiday['date']), "yyyyMMdd")
        #         self.calendarWidget_Test.setDateTextFormat(dday, fm)


        # for dday, name in holidays.items():
        #     dday2 = QDate.fromString(dday, "yyyyMMdd")          
        #     self.calendarWidget_Test.setDateTextFormat(dday2, fm)

        #버튼에 기능 연결
        self.btn_prevMonth.clicked.connect(self.prevMonth)
        self.btn_nextMonth.clicked.connect(self.nextMonth)
        self.btn_today.clicked.connect(self.today)
        self.check_AOD.stateChanged.connect(self.AOD)
        self.horizontalSlider.valueChanged.connect(self.slot_x_changed)
        self.horizontalSlider.setValue(99)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):                                 # +
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()        


    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        openAct = cmenu.addAction("AlwaysOn")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()
        elif action == openAct:
            self.AOD()

    def AOD(self):
        print(self.check_AOD.checkState())
        if self.check_AOD.checkState():
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            self.show()

    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        print(date)
        if date == QDate(2024, 8, 15):
            painter.save()
            painter.drawRect(rect)
            painter.setPen(QColor(168, 34, 3))
            painter.setFont(QFont('Decorative', 7))            
            painter.drawText(QRectF(rect), Qt.TextSingleLine|Qt.AlignCenter, str(date.day()))
            painter.drawText(rect, Qt.AlignTop| Qt.AlignHCenter, '광복절') 

            painter.restore()
        else:
            QCalendarWidget.paintCell(self, painter, rect, date)

    def slot_x_changed(self, data):
        print(data)
        rate = int(data)/100
        self.setWindowOpacity(rate)

    #CalendarWidget의 시그널에 연결된 함수들
    def calendarClicked(self) :
        selected=self.calendarWidget_Test.selectedDate().toString("yyyyMMdd")
        print(self.calendarWidget_Test.selectedDate().toString("yyyyMMdd"))
        self.listWidget.clear()
        self.listWidget.addItem(selected)

        if selected in self.data.keys():
            self.listWidget.addItem(self.data[selected]['name'])

    def calendarPageChanged(self) :
        self.year = str(self.calendarWidget_Test.yearShown()) + "년"
        self.month = str(self.calendarWidget_Test.monthShown()) + "월"
        self.lbl_currentPage.setText(self.year + " " + self.month)

    def calendarSelectionChanged(self) :
        self.selectedDateVar = self.calendarWidget_Test.selectedDate()
        self.lbl_selectedDate.setText(self.selectedDateVar.toString())

    #버튼에 연결된 함수들
    def prevMonth(self) :
        self.calendarWidget_Test.showPreviousMonth()

    def nextMonth(self) :
        self.calendarWidget_Test.showNextMonth()

    def today(self) :
        self.calendarWidget_Test.showToday()
        self.todayDate = QDate.currentDate()
        self.calendarWidget_Test.setSelectedDate(self.todayDate)
        # self.calendarWidget_Test.setCurrentPage(self.todayDate.year(), self.todayDate.month())
        # self.calendarSelectionChanged()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 