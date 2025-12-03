from app.database import db

#Metodo para insertar nueva interconsulta en la bd.
def insert_interconsulta(codigo, medico, fecha, hora, cod_especialidad, nom_especialidad, detalle, id_atencion):
    conn = db.connection()
    query = "INSERT INTO interconsultas (codigo, medico, fecha, hora, cod_especialidad, nom_especialidad, detalle, id_atencion) \
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    
    params = (codigo, medico, fecha, hora, cod_especialidad, nom_especialidad, detalle, id_atencion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todos los registros de incapacidades por medico y paciente
def listar_interconsultas(paciente, medico):
    interconsultas = []
    conn = db.connection()
    query = "SELECT i.id_interconsulta, i.fecha, i.hora, i.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre), i.id_atencion \
             FROM interconsultas i INNER JOIN pacientes p ON p.num_doc = i.codigo WHERE i.codigo = %s AND i.medico = %s"
    params = (paciente, medico)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            interconsultas.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'codigo': row[3] ,'paciente': row[4], 'atencion': row[5]})

    conn.close()
    return interconsultas

#Metodo para listar interconsulta individual
def listar_interconsulta_id(id_interconsulta):
    interconsulta = None
    conn = db.connection()
    query = "SELECT * FROM interconsultas WHERE id_interconsulta = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_interconsulta, ))
        result = cursor.fetchone()
        interconsulta = result

    conn.close()
    return interconsulta            