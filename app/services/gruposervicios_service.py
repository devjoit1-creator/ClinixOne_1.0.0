from app.database import db

def listar_gruposervicios():
    grupos_servicios = []
    conn = db.connection()
    query = "SELECT cod_grupo_servicio, nom_grupo_servicio FROM grupos_servicios"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            grupos_servicios.append({'cod_grupo_servicio': row[0], 'nom_grupo_servicio': row[1]})

    conn.close()
    return grupos_servicios

def listar_gruposervicio_id(cod_grupo_servicio):
    grupo_servicio = None
    conn = db.connection()
    query = "SELECT * FROM grupos_servicios WHERE cod_grupo_servicio = %s"
    with conn.cursor() as cursor: 
         cursor.execute(query, (cod_grupo_servicio, )) 
         result = cursor.fetchone()
         grupo_servicio = result

    conn.close()
    return grupo_servicio

def insert_gruposervicio(cod_grupo_servicio, nom_grupo_servicio):
    conn = db.connection()
    query = "INSERT INTO grupos_servicios (cod_grupo_servicio, nom_grupo_servicio) VALUES (%s, %s)"
    params = (cod_grupo_servicio, nom_grupo_servicio)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def delete_gruposervicio(cod_grupo_servicio):
    conn = db.connection()
    query = "DELETE FROM grupos_servicios WHERE cod_grupo_servicio = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_grupo_servicio, ))
        conn.commit()
        conn.close()

def update_gruposervicio(cod_grupo_servicio, nom_grupo_servicio, cgrupo_servicio):
    conn = db.connection()
    query = "UPDATE grupos_servicios SET cod_grupo_servicio = %s, nom_grupo_servicio = %s WHERE cod_grupo_servicio = %s"
    params = (cod_grupo_servicio, nom_grupo_servicio, cgrupo_servicio)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar Servicios de Grupo Consulta Externa
def listar_serv_ce():
    servicios = []
    conn = db.connection()
    query = """ SELECT cod_servicio, nom_servicio FROM servicios WHERE grupo = '01' """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            servicios.append({'cod_servicio': row[0], 'nom_servicio': row[1]})

    conn.close()
    return servicios        