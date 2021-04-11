
import sqlite3



class Connection():

    def __init__(self, username=None, password=None, host=None, port=None, databasename=None):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.databasename = databasename

    def connecting_to_database(self):
        
        self.conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        return self.conn
        
    def createtable_company(self):
        self.conn.execute('''CREATE TABLE COMPANY
         (ID INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')



class MySQLQuerys():

    def __init__(self, conn):
        self.conn = conn

    def insert(self):
        self.conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) VALUES ('Nima', 22, 'California', 20000.00 )")
        self.conn.commit()
        print("Inserted")


    def delete(self):
        pass


    def update(self):
        pass


    def selectall(self):
        pass


    def selectone(self):
        pass

