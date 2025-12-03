from app.database import db

def listar_finalidad_consulta():
    finalidades = []
    conn = db.connection()
    query = """ SELECT cod_finalidad, nom_finalidad FROM finalidad_consulta """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            finalidades.append({'cod_finalidad': row[0], 'nom_finalidad': row[1]})

    conn.close()
    return finalidades        
        