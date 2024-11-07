from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

class Login(QWidget):
    def __init__(self, main_w, db):
        super(Login,self).__init__()
        self.ui = uic.loadUi('log.ui',self)
        self.log = 0
        self.passwd = 0
        self.main_w = main_w
        self.obj = db
        self.ui.button_log.clicked.connect(self.login)

    def login(self):
        self.log = self.ui.ent_login.text()
        self.passwd = self.ui.ent_passwd.text()
        cur = self.obj.cursor()
        cur.execute('select * from users where login = \'{}\' and passwd = \'{}\''.format(self.log, self.passwd))
        res = cur.fetchone()
        try:
            if res[2] == self.log and res[3] == self.passwd:
                QMessageBox.information(self,'Сообщение', 'Авторизация прошла успешно')
        except:
            QMessageBox.warning(self,'Предупреждение', 'Неверное имя пользователя или пароль')
        cur.close()
