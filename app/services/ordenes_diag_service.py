from app.database import db

#Metodo para obtener el consecutivo de la tabla de ordenes diagnosticas
def listar_consecutivo_od():
    consecutivo = None
    conn = db.connection()
    query = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'sias' AND TABLE_NAME = 'ordenes_diagnosticas';"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        consecutivo = result

    conn.close()
    return consecutivo       

#Metodo para insertar nueva orden diagnostica en la bd
def insert_orden_diag(codigo, medico, fecha, hora, id_atencion):
    conn = db.connection()
    query = "INSERT INTO ordenes_diagnosticas(codigo, medico, fecha, hora, id_atencion) VALUES (%s, %s, %s, %s, %s)"
    params = (codigo, medico, fecha, hora, id_atencion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para insertar detalle de la nueva orden diagnostica en la bd
def insert_detalle_orden(cod_servicio, servicio, justificacion, id_orden):
    conn = db.connection()
    query = "INSERT INTO detalle_ordenes_diagnosticas(cod_servicio, servicio, justificacion, orden) VALUES (%s, %s, %s, %s)"
    params = (cod_servicio, servicio, justificacion, id_orden)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()        


#Metodo para listar todos los registros de Ordenes diagnosticas por medico y paciente
def listar_ordenes_diagnosticas(paciente, medico):
    ordenes = []
    conn = db.connection()
    query = "SELECT od.id_orden, od.fecha, od.hora, od.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre), od.id_atencion \
             FROM ordenes_diagnosticas od INNER JOIN pacientes p ON p.num_doc = od.codigo WHERE od.codigo = %s AND od.medico = %s"
    params = (paciente, medico)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            ordenes.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'codigo': row[3] ,'paciente': row[4], 'atencion': row[5]})

    conn.close()
    return ordenes

#Metodo para listar registro de orden diagnostica por id
def listar_odiag_id(id_orden):
    orden = None
    conn = db.connection()
    query = "SELECT * FROM ordenes_diagnosticas WHERE id_orden = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_orden, ))
        result = cursor.fetchone()
        orden = result

    conn.close()
    return orden

#Metodo para listar el detalle de la orden diagnostica por id
def listar_detalle_odiag_id(id_orden):
    detalle = []
    conn = db.connection()
    query = "SELECT cod_servicio, servicio, justificacion FROM detalle_ordenes_diagnosticas WHERE orden = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_orden, ))
        result = cursor.fetchall()
        for row in result:
            detalle.append({'cod_servicio': row[0], 'servicio': row[1], 'justificacion': row[2]})

    conn.close()
    return detalle