import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui',self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.titles = None
        self.update_result()

    def update_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("Select * from Info").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())