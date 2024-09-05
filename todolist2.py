from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QDate
import sys
from PyQt5.QtGui import QTextCharFormat
from  PyQt5 import QtCore
import sqlite3
import json

tasks = ["write email", "finish feature", "watch tutorial"]
# class Window(QWidget):
class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        # loadUi('Main_ToDo1.ui', self)
        loadUi('calendar6.ui', self)

        fm = QTextCharFormat()
        fm.setForeground(Qt.red)
        fm.setBackground(Qt.yellow)

        self.todayDate = QDate.currentDate()
        self.whatday.setText(str(self.todayDate.toString("yyyyMMdd")))

        with open('holiday.json', 'r', encoding='UTF-8') as f:
            self.data = json.load(f)

        for bday in self.data.keys():
            dday = QDate.fromString(bday, "yyyyMMdd")
            self.calendarWidget.setDateTextFormat(dday, fm)
            if dday == self.todayDate:
                self.whatday.setText(self.data[dday])

        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.SaveButton.clicked.connect(self.SaveChanges)
        self.addButton.clicked.connect(self.addTask)
        self.check_AOD.stateChanged.connect(self.AOD)
        self.horizontalSlider.valueChanged.connect(self.slot_x_changed)
        self.horizontalSlider.setValue(99)
        

        
            

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        dateSelected2=self.calendarWidget.selectedDate().toString("yyyyMMdd")
        print("Date selected:", dateSelected, dateSelected2)
        self.updateTasklist(dateSelected)

        if dateSelected2 in self.data.keys():
            print(self.data[dateSelected2]['name'])
            self.whatday.setText(dateSelected2 + ":" + self.data[dateSelected2]['name'])
        else:
            self.whatday.setText(dateSelected2)


    def updateTasklist(self, date):
        self.listWidget.clear()
        db = sqlite3.connect("data2.db")
        cursor = db.cursor()

        query = "SELECT task, completed from tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall()

        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            
            self.listWidget.addItem(item)

    def SaveChanges(self):
        db = sqlite3.connect("data2.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            task = str(item.text())
            print(task)
            if item.checkState() == QtCore.Qt.Checked:
                print("checked")
                query = "UPDATE tasks SET completed = 'YES' WHERE task=? AND date = ?"
            else:
                print("unchecked")
                query = "UPDATE tasks SET completed = 'NO' WHERE task=? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)

        db.commit()

        messageBox = QMessageBox()
        messageBox.setText("Cahnges Saved")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addTask(self):
        db = sqlite3.connect("data2.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()

        newTask=self.lineEdit.text()
        query = "INSERT INTO tasks(task, completed, date) VALUES(?,?,?)"
        row = (newTask, "NO", date)

        cursor.execute(query, row)
        db.commit()

        self.lineEdit.clear()
        self.updateTasklist(date)

    def AOD(self):
        print(self.check_AOD.checkState())
        if self.check_AOD.checkState():
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            self.show()

    def slot_x_changed(self, data):
        print(data)
        rate = int(data)/100
        self.setWindowOpacity(rate)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()