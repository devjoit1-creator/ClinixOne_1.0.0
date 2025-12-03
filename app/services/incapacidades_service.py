from app.database import db

#Metodo para Insertar Nuevo Registros Incapacidad
def insert_incapacidad(codigo, medico, fecha, hora, grupo_ser, origen, cod_diag, nom_diag, cod_diag2, nom_diag2, fecha_inicio, fecha_fin, dias, tipo,
                       modalidad, retroactiva, causa, observacion, id_atencion):
    
    conn = db.connection()
    query = "INSERT INTO incapacidades (codigo, medico, fecha, hora, grupo_ser, origen, cod_diag, nom_diag, cod_diag2, nom_diag2, fecha_inicio, fecha_fin, dias, tipo, \
                         modalidad, retroactiva, causa, observacion, id_atencion) \
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    params = (codigo, medico, fecha, hora, grupo_ser, origen, cod_diag, nom_diag, cod_diag2, nom_diag2, fecha_inicio, fecha_fin, dias, tipo,
              modalidad, retroactiva, causa, observacion, id_atencion)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todos los registros de incapacidades por medico y paciente
def listar_incapacidades(paciente, medico):
    incapacidades = []
    conn = db.connection()
    query = "SELECT i.id_incapacidad, i.fecha, i.hora, i.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre), i.id_atencion \
             FROM incapacidades i INNER JOIN pacientes p ON p.num_doc = i.codigo WHERE i.codigo = %s AND i.medico = %s"
    params = (paciente, medico)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            incapacidades.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'codigo': row[3] ,'paciente': row[4], 'atencion': row[5]})

    conn.close()
    return incapacidades

#Metodo para listar datos de incapacidad por ID
def listar_incapacidad_id(id_incapacidad):
    incapacidad = None
    conn = db.connection()
    query = "SELECT * FROM incapacidades WHERE id_incapacidad = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_incapacidad, ))
        result = cursor.fetchone()
        incapacidad = result        

    conn.close()
    return incapacidad            