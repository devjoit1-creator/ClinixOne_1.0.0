from app.database import db

#Metodo Insertar Referencia
def insert_referencia(cod_referencia, nom_referencia, cod_principio, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
                      forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
                      regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
                      stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento):
    
    conn = db.connection()
    query = """ INSERT INTO referencias(cod_referencia, nom_referencia, cod_principio, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
                      forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
                      regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
                      stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento) 
                      VALUES
                      (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (cod_referencia, nom_referencia, cod_principio, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
              forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
              regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
              stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento)
    
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

#Metodo Actualizar Referencia
def update_referencia(nom_referencia, cod_principio, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
              forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
              regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
              stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento, cod_referencia):
    
    conn = db.connection()
    query = """ UPDATE referencias SET nom_referencia = %s, cod_principio = %s, principio_activo = %s, nom_comercial_ref = %s, unidad_medida = %s, concentracion = %s,
                forma_farm = %s, forma_farm_ihce = %s, laboratorio = %s, presentacion = %s, grupo_referencia = %s, registro_invima = %s, tipo_referencia = %s,
                regulado = %s, serie_referencia = %s, expediente_sanitario = %s, consecutivo_exp = %s, codigo_atc = %s, codigo_cum = %s, codigo_rips = %s,
                stock_minimo = %s, stock_maximo = %s, dispensacion_minima = %s, dispensacion_maxima = %s, cantidad = %s, iva = %s, descuento = %s WHERE cod_referencia = %s"""
    
    params = (nom_referencia, cod_principio, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
              forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
              regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
              stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento, cod_referencia)
    
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

#Metodo Eliminar Referencia
def delete_referencia(cod_referencia):
    conn = db.connection()
    query = """ DELETE FROM referencias WHERE cod_referencia = %s """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (cod_referencia, ))
            conn.commit()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()

#Metodo Listar Referencias
def listar_referencias():
    referencias = []
    conn = db.connection()
    query = """ SELECT cod_referencia, nom_referencia, cod_principio, principio_activo FROM referencias """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                referencias.append({'codigo': row[0], 'nombre': row[1], 'codprin': row[2], 'principio': row[3]})

        return referencias
    
    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()

#Metodo Listar Referencia por codigo
def listar_referencia_codigo(cod_referencia):
    referencia = None
    conn = db.connection()
    query = """ SELECT * FROM referencias WHERE cod_referencia = %s """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (cod_referencia, ))
            result = cursor.fetchone()
            referencia = result

        return referencia
    
    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally: 
        conn.close()

#Metodo Listar referencias busqueda Entrada de Almacen
def listar_referencias_entrada():
    referencias = []
    conn = db.connection()
    query = """ SELECT cod_referencia, nom_referencia, registro_invima FROM referencias """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                referencias.append({'codigo': row[0], 'nombre': row[1], 'invima': row[2]})

        return referencias
    
    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()