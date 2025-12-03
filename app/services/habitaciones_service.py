from app.database import db

def listar_habitaciones():
    habitaciones = []
    conn = db.connection()
    query = "SELECT id_habitacion, cod_habitacion, nom_habitacion, c_ufuncional, \
            CASE \
                WHEN reservada = 0 THEN 'Disponible' \
                WHEN reservada = 1 THEN 'Ocupada' \
            END disponibilidad \
            FROM habitaciones"
    
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            habitaciones.append({"id_habitacion": row[0], "cod_habitacion": row[1], "nom_habitacion": row[2], "c_ufuncional": row[3], "disponibilidad": row[4]})

    conn.close()
    return habitaciones

def listar_habitacion_id(id_habitacion):
    habitacion = None
    conn = db.connection()
    query = "SELECT * FROM habitaciones WHERE id_habitacion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_habitacion, ))
        result = cursor.fetchone()
        habitacion = result

    conn.close()
    return habitacion

def listar_habitaciones_modal(c_ufuncional):
    habitaciones = []
    conn = db.connection()
    query = "SELECT cod_habitacion, nom_habitacion FROM habitaciones WHERE reservada = 0 and c_ufuncional = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (c_ufuncional, ))
        result = cursor.fetchall()
        for row in result:
            habitaciones.append({'codigo': row[0], 'nombre': row[1]})

    conn.close()
    return habitaciones        

def insertar_habitacion(cod_habitacion, nom_habitacion, c_ufuncional, reservada):
    conn = db.connection()
    query = "INSERT INTO habitaciones (cod_habitacion, nom_habitacion, c_ufuncional, reservada) VALUES (%s, %s, %s, %s)"
    params = (cod_habitacion, nom_habitacion, c_ufuncional, reservada)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def delete_habitacion(id_habitacion):
    conn = db.connection()
    query = "DELETE FROM habitaciones WHERE id_habitacion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_habitacion, ))
        conn.commit()
        conn.close()

def update_habitacion(cod_habitacion, nom_habitacion, c_ufuncional, reservada, id_habitacion):
    conn = db.connection()
    query = "UPDATE habitaciones SET cod_habitacion = %s, nom_habitacion = %s, c_ufuncional = %s, reservada = %s WHERE id_habitacion = %s"
    params = (cod_habitacion, nom_habitacion, c_ufuncional, reservada, id_habitacion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def update_ocupar_habitacion(cod_habitacion):
    conn = db.connection()
    query = "UPDATE habitaciones SET reservada = 1 WHERE cod_habitacion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_habitacion, ))
        conn.commit()
        conn.close()

def update_liberar_habitacion(cod_habitacion):
    conn = db.connection()
    query = "UPDATE habitaciones SET reservada = 0 WHERE cod_habitacion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_habitacion, ))
        conn.commit()
        conn.close()                