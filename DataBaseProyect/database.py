import pyodbc

class ConectionDatabase:

    def __init__ (self): 
        self.driver = "{ODBC Driver 17 for SQL Server}"
        self.server = "server"
        self.database = "database" 
        self.username = "username"
        self.pwd = "pwd"
        
    def getConnection(self):
        connection = pyodbc.connect("DRIVER=" + self.driver
                       + ";SERVER=" + self.server
                       + ";DATABASE=" + self.database
                       + ";UID=" + self.username
                       + ";PWD=" + self.pwd)
        self.connection = connection
        
    

