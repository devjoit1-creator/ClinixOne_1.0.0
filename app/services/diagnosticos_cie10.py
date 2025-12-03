from app.database import db

# Listar todos los diagnosticos de la bd
def listar_diagnosticos():
    diagnosticos = []
    conn = db.connection()
    query = "SELECT cod_diagnostico, nom_diagnostico FROM diagnosticos_cie10"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            diagnosticos.append({'codigo': row[0], 'nombre': row[1]})

    conn.close()
    return diagnosticos        