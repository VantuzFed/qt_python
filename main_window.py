from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = uic.loadUi('main.ui', self)