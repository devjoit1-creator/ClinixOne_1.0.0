from app.database import db

def listar_educacion():
    niveles = []
    conn = db.connection()
    query = "SELECT id_nivel, nom_nivel FROM nivel_escolaridad"
    with conn.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchall():
            niveles.append({"id_nivel": row[0], "nom_nivel": row[1]})

    conn.close()
    return niveles

def listar_ocupacion():
    ocupaciones = []
    conn = db.connection()
    query = "SELECT id_ocupacion, nom_ocupacion FROM ocupacion"
    with conn.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchall():
            ocupaciones.append({"id_ocupacion": row[0], "nom_ocupacion": row[1]})

    conn.close()
    return ocupaciones                    