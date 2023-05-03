import sqlite3


class Task:
    def __init__(self, title, desc, date, time):
        self.title = title
        self.desc = desc
        self.date = date
        self.time = time

    def __str__(self):
        return f'{self.title} : {self.desc} : {self.date} : {self.time}'


class DBHandler:
    def __init__(self):
        self.con = sqlite3.connect("TaskDB.db")
        try:
            self.con.execute("CREATE TABLE IF NOT EXISTS taskHandler(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT,"
                             "Description TEXT, Date TEXT, Time TEXT)")
            self.con.commit()
        except Exception as e:
            print(e)

    def insertTask(self, t):
        listTask = [t.title, t.desc, t.date, t.time]
        try:
            self.con.execute("INSERT INTO taskHandler(Title, Description, Date, Time) VALUES(?,?,?,?)", listTask)
            self.con.commit()
        except Exception as e:
            print(e)

    def getTask(self, date):
        cursor = self.con.cursor()
        rows = cursor.execute("SELECT * FROM taskHandler WHERE date='" + date + "'")
        return rows

    def deleteTasks(self, del_row):
        self.con.cursor()
        self.con.execute("DELETE FROM taskHandler WHERE Title ='" + del_row + "'")
        self.con.commit()


