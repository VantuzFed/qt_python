from mysql.connector import connect, Error
class Con_base():
    def __init__(self):
        self.con = 0

    def connection(self):
        try:
            self.con = connect(
                user='root',
                host='127.0.0.1',
                db='server_db',
                password='123'
            )
            print('Connection successful')
            return self.con
        except Error as e:
            print(e)
