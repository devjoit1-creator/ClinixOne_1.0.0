from app.database import db

#Metodo para Insertar Nuevo Registros Receta medica (Recomendaciones)
def insert_recomendacion(fecha, hora, codigo, medico, detalle, id_atencion):
    conn = db.connection()
    query = "INSERT INTO recomendaciones (fecha, hora, codigo, medico, detalle, id_atencion) VALUES (%s, %s, %s, %s, %s, %s)"
    params = (fecha, hora, codigo, medico, detalle, id_atencion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todos los registros de R. Medica por medico y paciente
def listar_recomendaciones_med(paciente, medico):
    recomendaciones = []
    conn = db.connection()
    query = "SELECT r.id_recomendacion, r.fecha, r.hora, r.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre), r.id_atencion \
             FROM recomendaciones r INNER JOIN pacientes p ON p.num_doc = r.codigo WHERE r.codigo = %s AND r.medico = %s"
    params = (paciente, medico)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            recomendaciones.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'codigo': row[3] ,'paciente': row[4], 'atencion': row[5]})

    conn.close()
    return recomendaciones

#Metodo para listar datos de R. medica por ID
def listar_recomendacion_id(id_recomendacion):
    recomendacion = None
    conn = db.connection()
    query = "SELECT * FROM recomendaciones WHERE id_recomendacion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_recomendacion, ))
        result = cursor.fetchone()
        recomendacion = result        

    conn.close()
    return recomendacion        