from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from PyQt6 import uic

class Table(QWidget):
    def __init__(self, main_w, obj):
        super(Table,self).__init__()
        self.ui = uic.loadUi('table.ui',self)
        self.main_w = main_w
        self.obj = obj
        self.ui.but_cle.clicked.connect(self.table.clear)
        self.ui.but_ent.clicked.connect(self.insert_in_table)

    def insert_in_table(self):
        cur = self.obj.cursor()
        cur.execute('SELECT * FROM users')
        data = cur.fetchall()
        field_names = [i[0] for i in cur.description]
        self.ui.table.setRowCount(len(data))
        self.ui.table.setColumnCount(len(data[1]))
        self.ui.table.setHorizontalHeaderLabels(field_names)
        for i in range(len(data)):
            for j in range(len(data[1])):
                cell = QTableWidgetItem('' if data[i][j] is None else str(data[i][j]))
                self.ui.table.setItem(i, j, cell)

