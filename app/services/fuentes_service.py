from app.database import db

def update_fuente(nom_fuente, prefijo, consecutivo, cod_fuente):
    conn = db.connection()
    query = "UPDATE fuentes_contables SET nom_fuente = %s, prefijo = %s, consecutivo = %s WHERE cod_fuente = %s"
    params = (nom_fuente, prefijo, consecutivo, cod_fuente)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def listar_fuentes():
    fuentes = []
    conn = db.connection()
    query = "SELECT cod_fuente, nom_fuente, prefijo FROM fuentes_contables"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            fuentes.append({'cod_fuente': row[0], 'nom_fuente': row[1], 'prefijo': row[2]})

    conn.close()
    return fuentes

def listar_fuente_codigo(cod_fuente):
    fuente = None
    conn = db.connection()
    query = "SELECT * FROM fuentes_contables WHERE cod_fuente = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_fuente, ))
        result = cursor.fetchone()
        fuente = result

    conn.close()
    return fuente    

def listar_fuente_fe():
    fuentes_fe = []
    conn = db.connection()
    query = " SELECT cod_fuente, prefijo FROM fuentes_contables WHERE nom_fuente LIKE 'FACTURA ELECTRONICA%' "
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            fuentes_fe.append({'cod_fuente': row[0], 'prefijo': row[1]})

    conn.close()
    return fuentes_fe

def listar_fuente_nc():
    fuentes_nc = []
    conn = db.connection()
    query = " SELECT cod_fuente, prefijo FROM fuentes_contables WHERE nom_fuente LIKE 'NOTA CREDITO%' "
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            fuentes_nc.append({'cod_fuente': row[0], 'prefijo': row[1]})

    conn.close()
    return fuentes_nc        