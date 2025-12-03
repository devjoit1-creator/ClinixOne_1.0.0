from app.database import db

def listar_tarifas():
    tarifas = []
    conn = db.connection()
    query = "SELECT id_tarifa, nom_tarifa, \
             CASE \
                 WHEN base_tarifa = 1 THEN 'UVR' \
                 WHEN base_tarifa = 2 THEN 'UVR-S' \
                 WHEN base_tarifa = 3 THEN 'GRUPO' \
                 WHEN base_tarifa = 4 THEN 'ECOPETROL' \
             END base FROM tarifas"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            tarifas.append({"id_tarifa": row[0], "nom_tarifa": row[1], "base": row[2]})

    conn.close()
    return tarifas

def listar_tarifa_id(id_tarifa):
    tarifa = None
    conn = db.connection()
    query = "SELECT * FROM tarifas WHERE id_tarifa = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_tarifa,))
        result = cursor.fetchone()
        tarifa = result

    conn.close()
    return tarifa

def insert_tarifa(nom_tarifa, base_tarifa):
    conn = db.connection()
    query = "INSERT INTO tarifas (nom_tarifa, base_tarifa) VALUES (%s, %s)"
    params = (nom_tarifa, base_tarifa)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def delete_tarifa(id_tarifa):
    conn = db.connection()
    query = "DELETE FROM tarifas WHERE id_tarifa = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_tarifa,))
        conn.commit()
        conn.close()

def update_tarifa(nom_tarifa, base_tarifa, id_tarifa):
    conn = db.connection()
    query = "UPDATE tarifas SET nom_tarifa = %s, base_tarifa = %s WHERE id_tarifa = %s"
    params = (nom_tarifa, base_tarifa, id_tarifa)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()