from app.database import db

def listar_etnias():
    etnias = []
    conn = db.connection()
    query = "SELECT id_etnia, nom_etnia FROM etnia"
    with conn.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchall():
            etnias.append({"id_etnia": row[0], "nom_etnia": row[1]})

    conn.close()
    return etnias        