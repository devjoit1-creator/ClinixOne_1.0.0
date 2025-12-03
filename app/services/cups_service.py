from app.database import db

#Listar todos los servicios y procedimientos de la tabla cups 
def listar_cups():
    cups = []
    conn = db.connection()
    query = "SELECT id_cups, nom_cups FROM cups"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            cups.append({'id': row[0], 'nombre': row[1]})

    conn.close()
    return cups
