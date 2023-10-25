import database
import pyodbc

connection = database.ConectionDatabase()
connection.getConnection()
cursor = connection.connection.cursor()

link = "https://mx.linkedin.com/in/queso_pluma"

cursor.execute("INSERT INTO dbo.LinkEgresados VALUES (?)", link)

cursor.commit()
connection.closeConnection()


    
    
    
