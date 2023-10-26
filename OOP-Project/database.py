import pyodbc
import os
from dotenv import load_dotenv


class ConectionDatabase:

    def __init__(self):
        load_dotenv()
        self.driver = os.getenv('DRIVER')
        self.server = os.getenv('SERVER')
        self.database = os.getenv('DATABASE')
        self.username = os.getenv('USERNAME')
        self.pwd = os.getenv('PSWDB')

    def getConnection(self):
        connection = pyodbc.connect("DRIVER=" + self.driver
                                    + ";SERVER=" + self.server
                                    + ";DATABASE=" + self.database
                                    + ";UID=" + self.username
                                    + ";PWD=" + self.pwd)
        self.connection = connection

    def closeConnection(self):
        self.connection.close()
