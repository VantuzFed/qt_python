from PyQt6.QtWidgets import QApplication
from window_1 import Register
from window_2 import Login
from table import Table
from main_window import MainWindow
import sys
from sql import Con_base

class Control:
    def __init__(self,w, bd_obj):
        self.bd_obj = bd_obj
        self.w1 = Register(w, self.bd_obj)
        self.w2 = Login(w, self.bd_obj)
        self.tw = Table(w, self.bd_obj)
        self.w = w
        self.w.button_1.clicked.connect(self.show_window_2)
        self.w.button_2.clicked.connect(self.show_window_1)
        self.w.but_tab.clicked.connect(self.show_table)


    # registration
    def show_window_1(self):
        self.w1.button.clicked.connect(self.show_main)
        self.w.hide()
        self.w1.show()


    # login
    def show_window_2(self):
        self.w.hide()
        self.w2.button.clicked.connect(self.show_main)
        self.w2.show()

    def show_main(self):
        self.tw.hide()
        self.w1.hide()
        self.w2.hide()
        self.w.show()

    def show_table(self):
        self.w.hide()
        self.tw.but_back.clicked.connect(self.show_main)
        self.tw.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    bd_obj = Con_base().connection()
    c = Control(w, bd_obj)
    sys.exit(app.exec())