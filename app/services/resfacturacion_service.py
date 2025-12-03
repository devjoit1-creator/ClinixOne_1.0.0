from app.database import db

#Metodo Insert Nueva Resolución de Facturación Electronica
def insert_resfacturacion(nombre, tipo_documento, estado_res, account_id, auth_token, texto_encabezado, numero_resolucion, fecha_inicio, fecha_fin,
                          prefijo, numero_inicio, numero_fin, encabezado):
    
    conn = db.connection()
    query = """ INSERT INTO resfacturacion (nombre, tipo_documento, estado_res, account_id, auth_token, texto_encabezado, numero_resolucion, fecha_inicio, fecha_fin,
                          prefijo, numero_inicio, numero_fin, encabezado) VALUES
                          (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
    
    params = (nombre, tipo_documento, estado_res, account_id, auth_token, texto_encabezado, numero_resolucion, fecha_inicio, fecha_fin,
              prefijo, numero_inicio, numero_fin, encabezado)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar las resoluciones de facturación y notas electronicas
def listar_resfacturacion():        
    resoluciones = []
    conn = db.connection()
    query = """ SELECT id_resfacturacion, nombre, numero_resolucion, fecha_inicio, fecha_fin, prefijo, numero_inicio, numero_fin, 
                CASE 
                    WHEN estado_res = 0 THEN 'Inactivo'
                    WHEN estado_res = 1 THEN 'Activo'
                END    
                FROM resfacturacion """

    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            resoluciones.append({'id': row[0], 
                                 'nombre': row[1], 
                                 'nro_res': row[2], 
                                 'inicio': row[3], 
                                 'fin': row[4], 
                                 'prefijo': row[5],
                                 'nro_inicio': row[6],
                                 'nro_fin': row[7],
                                 'estado': row[8]})

    conn.close()
    return resoluciones                                      

#Metodo para listar resolución de factura, notas por id
def listar_resfacturacion_id(id_resfacturacion):
    resolucion = None
    conn = db.connection()
    query = """ SELECT * FROM resfacturacion WHERE id_resfacturacion = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_resfacturacion, ))
        result = cursor.fetchone()
        resolucion = result

    conn.close()
    return resolucion    

#Metodo para Listar resolución de Factura Electronica Activa
def listar_resfacturacion_fe():
    resolucion = []
    conn = db.connection()
    query = """ SELECT auth_token FROM resfacturacion WHERE tipo_documento = 1 and estado_res = 1 """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            resolucion.append(row[0])

    conn.close()
    return resolucion

#Metodo para actualizar resolución de factura electronica
def update_resfacturacion(nombre, tipo_documento, estado_res, account_id, auth_token, texto_encabezado, numero_resolucion, fecha_inicio, fecha_fin,
                          prefijo, numero_inicio, numero_fin, encabezado, id_resfacturacion):
    conn = db.connection()
    query = """ UPDATE resfacturacion SET nombre = %s, tipo_documento = %s, estado_res = %s, account_id = %s, auth_token = %s, texto_encabezado = %s,
                numero_resolucion = %s, fecha_inicio = %s, fecha_fin = %s,  prefijo = %s, numero_inicio = %s, numero_fin = %s, encabezado = %s 
                WHERE id_resfacturacion = %s """
    
    params = (nombre, tipo_documento, estado_res, account_id, auth_token, texto_encabezado, numero_resolucion, fecha_inicio, fecha_fin,
              prefijo, numero_inicio, numero_fin, encabezado, id_resfacturacion)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()