import os
import sqlite3


class DataBase():
    def __init__(self) -> None:
        self.connection = sqlite3.connect(
            os.path.join(os.getcwd(), 'database.sqlite3'))
        self.create_table()

    def create_table(self):
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS FACES(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP);
        ''')

    def _get_face(self, name):
        try:
            c = self.connection.cursor()
            c.execute("select * FROM FACES where name =?", (name,))
            data = c.fetchone()
            if data:
                return data[0]
            else:
                return None

        except Exception as e:
            print(str(e))

    def get_face_name(self, id):
        try:
            c = self.connection.cursor()
            c.execute("select * FROM FACES where id =?", (id,))
            data = c.fetchone()
            if data:
                return data[1]
            else:
                return None

        except Exception as e:
            print(str(e))

    def _add_face(self, name):
        try:
            self.connection.execute(
                "INSERT INTO FACES (name) VALUES(?)", (name,))
            self.connection.commit()
        except Exception as e:
            print(str(e))

    def add_or_get_face(self, name) -> int:
        """"""
        try:
            face_id = self._get_face(name)
            if face_id:
                return face_id
            else:
                self._add_face(name)
                return self._get_face(name)
        except Exception as e:
            print(str(e))
