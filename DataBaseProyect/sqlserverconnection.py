import database
import pyodbc

connection = database.ConectionDatabase()
connection.getConnection()
cursor = connection.connection.cursor()

for row in cursor.execute("select * from prueba where Id = '3'"):
    print(row.Id, row.Nombre, row.Edad)
    
    
