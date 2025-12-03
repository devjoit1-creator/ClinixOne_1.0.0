import mysql.connector

def connection():
    user = 'root'
    password = ''
    host = 'localhost'
    database = 'sias'
    port = 3306
    conexion = mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        database = database,
        port = port
    )
    return conexion