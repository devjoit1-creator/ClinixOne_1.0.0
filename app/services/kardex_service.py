from app.database import db

#Metodo para insertar movimiento de entrada en kardex
def insert_entrada_kardex(movimiento, cod_fuente, nro_fuente, fecha, bodega, cod_referencia, nom_referencia, cant_entrada):
    conn = db.connection()
    query = """ INSERT INTO kardex (movimiento, cod_fuente, nro_fuente, fecha, bodega, cod_referencia, nom_referencia, cant_entrada)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (movimiento, cod_fuente, nro_fuente, fecha, bodega, cod_referencia, nom_referencia, cant_entrada)
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

#Metodo para insertar movimiento de salida en kardex
def insert_salida_kardex(movimiento, cod_fuente, nro_fuente, fecha, bodega, cod_referencia, nom_referencia, cant_salida):
    conn = db.connection()
    query = """ INSERT INTO kardex (movimiento, cod_fuente, nro_fuente, fecha, bodega, cod_referencia, nom_referencia, cant_salida)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (movimiento, cod_fuente, nro_fuente, fecha, bodega, cod_referencia, nom_referencia, cant_salida)
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