from app.database import db

#Metodo Insertar Referencia
def insert_referencia(cod_referencia, nom_referencia, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
                      forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
                      regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
                      stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento):
    
    conn = db.connection()
    query = """ INSERT INTO referencias(cod_referencia, nom_referencia, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
                      forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
                      regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
                      stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento) 
                      VALUES
                      (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (cod_referencia, nom_referencia, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
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
def update_referencia(nom_referencia, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
              forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
              regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
              stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento, cod_referencia):
    
    conn = db.connection()
    query = """ UPDATE referencias SET nom_referencia = %s, principio_activo = %s, nom_comercial_ref = %s, unidad_medida = %s, concentracion = %s,
                forma_farm = %s, forma_farm_ihce = %s, laboratorio = %s, presentacion = %s, grupo_referencia = %s, registro_invima = %s, tipo_referencia = %s,
                regulado = %s, serie_referencia = %s, expediente_sanitario = %s, consecutivo_exp = %s, codigo_atc = %s, codigo_cum = %s, codigo_rips = %s,
                stock_minimo = %s, stock_maximo = %s, dispensacion_minima = %s, dispensacion_maxima = %s, cantidad = %s, iva = %s, descuento = %s WHERE cod_referencia = %s"""
    
    params = (nom_referencia, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
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