from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

class Register(QWidget):
    def __init__(self, main_w, db):
        super(Register,self).__init__()
        self.ui = uic.loadUi('reg.ui', self)
        self.log = 0
        self.passwd = 0
        self.username = 0
        self.main_w = main_w
        self.obj = db
        self.ui.button_reg.clicked.connect(self.registration)

    def registration(self):
        self.username = self.ui.ent_username.text()
        self.log = self.ui.ent_login.text()
        self.passwd = self.ui.ent_passwd.text()
        cur = self.obj.cursor()
        cur.execute('select * from users where login = \'{}\' and passwd = \'{}\' and username = \'{}\''.format(self.log, self.passwd, self.username))
        res = cur.fetchone()
        print(res)
        try:
            if res[2] == self.log and res[3] == self.passwd and res[1] == self.username:
                QMessageBox.warning(self,'Сообщение', 'Такой пользователь уже существует')
        except:
            val = (self.username, self.log, self.passwd)
            sql = 'INSERT INTO users (username, login, passwd) VALUES(%s,%s,%s)'
            cur.execute(sql, val)
            self.obj.commit()
            QMessageBox.information(self, 'Сообщение', 'Пользователь успешно создан')
        finally:
            cur.close()



