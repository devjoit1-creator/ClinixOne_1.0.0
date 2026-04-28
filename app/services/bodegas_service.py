from app.database import db


#Metodo Insertar Bodega
def insert_bodega(id_bodega, nom_bodega, ubicacion):
    conn = db.connection()
    query = """ INSERT INTO bodegas (id_bodega, nom_bodega, ubicacion) VALUES (%s, %s, %s)"""
    params = (id_bodega, nom_bodega, ubicacion)
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()

#Metodo Actualizar Bodega
def update_bodega(nom_bodega, ubicacion, id_bodega):
    conn = db.connection()
    query = """ UPDATE bodegas SET nom_bodega = %s, ubicacion = %s WHERE id_bodega = %s """
    params = (nom_bodega, ubicacion, id_bodega)
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise
    
    finally:
        conn.close()

#Metodo Eliminar Bodega
def delete_bodega(id_bodega):
    conn = db.connection()
    query = """ DELETE FROM bodegas WHERE id_bodega = %s """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (id_bodega, ))
            conn.commit()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise
    
    finally:
        conn.close()

#Metodo Listar Bodegas
def listar_bodegas():
    bodegas = []
    conn = db.connection()
    query = """ SELECT id_bodega, nom_bodega FROM bodegas """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                bodegas.append({'ID': row[0], 'nombre': row[1]})

        return bodegas

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()

#Metodo Listar Bodega por ID
def listar_bodega_id(id_bodega):
    bodega = None
    conn = db.connection()
    query = """ SELECT * FROM bodegas WHERE id_bodega = %s """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (id_bodega, ))
            result = cursor.fetchone()
            bodega = result

        return bodega

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()