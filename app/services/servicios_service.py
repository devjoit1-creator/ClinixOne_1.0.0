from app.database import db

def listar_servicios():
    servicios = []
    conn = db.connection()
    query = "SELECT id_servicio, cod_servicio, nom_servicio, valor, grupo FROM servicios_proceds_cups"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            servicios.append({'id_servicio': row[0], 'cod_servicio': row[1], 'nom_servicio': row[2], 'valor': row[3], 'grupo': row[4]})

    conn.close()
    return servicios

def listar_servicio_id(id_servicio):
    servicio = None
    conn = db.connection()
    query = "SELECT * FROM servicios_proceds_cups WHERE id_servicio = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_servicio, ))
        result = cursor.fetchone()
        servicio = result

    conn.close()
    return servicio

def insert_servicio(cod_servicio, nom_servicio, valor, tarifa, grupo):
    conn = db.connection()
    query = "INSERT INTO servicios_proceds_cups (cod_servicio, nom_servicio, valor, tarifa, grupo) VALUES (%s, %s, %s, %s, %s)"
    params = (cod_servicio, nom_servicio, valor, tarifa, grupo)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def delete_servicio(id_servicio):
    conn = db.connection()
    query = "DELETE FROM servicios_proceds_cups WHERE id_servicio = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_servicio,))
        conn.commit()
        conn.close()

def update_servicio(cod_servicio, nom_servicio, valor, tarifa, grupo, id_servicio):
    conn = db.connection()
    query = "UPDATE servicios_proceds_cups SET cod_servicio = %s, nom_servicio = %s, valor = %s, tarifa = %s, grupo = %s WHERE id_servicio = %s"
    params = (cod_servicio, nom_servicio, valor, tarifa, grupo, id_servicio)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()