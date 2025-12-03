from app.database import db

def listar_causas():
    causas = []
    conn = db.connection()
    query = "SELECT cod_causa, nom_causa FROM causa_externa_at"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            causas.append({'codigo': row[0], 'nombre': row[1]})

    conn.close()
    return causas        