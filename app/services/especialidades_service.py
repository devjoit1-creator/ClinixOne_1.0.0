from app.database import db

#Listar todas las especialidades
def listar_especialidades():
    especialidades = []
    conn = db.connection()
    query = "SELECT cod_especialidad, nom_especialidad FROM especialidades"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            especialidades.append({'codigo': row[0], 'nombre': row[1] })

    conn.close()
    return especialidades        