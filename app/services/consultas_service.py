from app.database import db

#Metodo para obtener el consecutivo de la tabla de consultas
def listar_consecutivo_consulta():
    consecutivo = None
    conn = db.connection()
    query = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'sias' AND TABLE_NAME = 'consultas';"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        consecutivo = result

    conn.close()
    return consecutivo 

#Listar todas las consultas
def listar_consultas():
    consultas = []
    conn = db.connection()
    query = "SELECT c.atencion, c.fecha_atencion, c.hora_atencion, CONCAT(p.num_doc,'-',CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre)), \
            CONCAT(m.num_documento,'-',m.nombre_completo), c.nro_autorizacion, c.numero_fact \
            FROM consultas c, pacientes p, medicos m WHERE c.codigo = p.num_doc and c.medico = m.num_documento"
    
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            consultas.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'paciente': row[3], 'medico': row[4], 'aut': row[5], 'numero_fact': row[6]})

    conn.close()
    return consultas

#Listar Datos de Consulta por Numero de Atención
def listar_consultas_atencion(atencion):
    consultas = []
    conn = db.connection()
    query = """ SELECT c.atencion, c.fecha_atencion, c.hora_atencion, CONCAT(p.num_doc,'-',CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre)), \
                CONCAT(m.num_documento,'-',m.nombre_completo), c.nro_autorizacion, c.numero_fact
                FROM consultas c, pacientes p, medicos m 
                WHERE c.codigo = p.num_doc and c.medico = m.num_documento AND c.atencion = %s """
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (atencion, ))
            result = cursor.fetchall()
            for row in result:
                consultas.append({'id': row[0], 'fecha': row[1].strftime("%Y-%m-%d"), 'hora': row[2], 'paciente': row[3], 'medico': row[4], 'aut': row[5], 'numero_fact': row[6]})

        return consultas

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        return None
    
    finally:
        conn.close()

#Listar todas las consultas activas por medico y fecha
def listar_consultas_med(medico, fecha):
    atenciones = []
    conn = db.connection()
    query = "SELECT c.atencion, c.fecha_atencion, c.hora_atencion, c.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre) \
             FROM consultas c, pacientes p WHERE c.codigo = p.num_doc and c.medico = %s and c.fecha_atencion = %s"

    params = (medico, fecha)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            atenciones.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'documento': row[3], 'paciente': row[4]})

    conn.close()
    return atenciones

#listar consulta por ID
def listar_consultas_id(id_consulta):
    consulta = None
    conn = db.connection()
    query = "SELECT * FROM consultas WHERE atencion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_consulta, ))
        result = cursor.fetchone()
        consulta = result

    conn.close()
    return consulta                    

#Insertar Nueva Consulta
def insert_consulta(atencion, codigo, fecha_atencion, hora_atencion, fecha_salida, hora_salida, cod_admin, nit_admin, plan_beneficios, concepto_recaudo,
                    via_ingreso, causa_externa, finalidad_consulta, clase_consulta, medico, und_funcional, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3,
                    nom_diag3, cod_diag4, nom_diag4, tipo_diag, modalidad, servicio_consulta, nro_autorizacion, total_servicios, usuario):
    
    conn = db.connection()
    query = "INSERT INTO consultas (atencion, codigo, fecha_atencion, hora_atencion, fecha_salida, hora_salida, cod_admin, nit_admin, plan_beneficios, concepto_recaudo, \
            via_ingreso, causa_externa, finalidad_consulta, clase_consulta, medico, und_funcional, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, \
            cod_diag4, nom_diag4, tipo_diag, modalidad, servicio_consulta, nro_autorizacion, total_servicios, usuario) VALUES \
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    params = (atencion, codigo, fecha_atencion, hora_atencion, fecha_salida, hora_salida, cod_admin, nit_admin, plan_beneficios, concepto_recaudo,
              via_ingreso, causa_externa, finalidad_consulta, clase_consulta, medico, und_funcional, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3,
              nom_diag3, cod_diag4, nom_diag4, tipo_diag, modalidad, servicio_consulta, nro_autorizacion, total_servicios, usuario)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para insertar detalle de los servicios de la consulta en la bd
def insert_detalle_consulta(und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, nro_autorizacion, id_atencion):
    conn = db.connection()
    query = "INSERT INTO detalle_consultas(und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, nro_autorizacion, id_atencion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    params = (und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, nro_autorizacion, id_atencion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para eliminar consulta de la bd
def delete_consulta(atencion):
    conn = db.connection()
    query = """ DELETE FROM consultas WHERE atencion = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (atencion, ))
        conn.commit()
        conn.close()

#Metodo para eliminar detalles de consultas de la bd
def delete_detalle_consulta(atencion):
    conn = db.connection()
    query = """ DELETE FROM detalle_consultas WHERE id_atencion = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (atencion, ))
        conn.commit()
        conn.close()

#Metodo para actualizar datos de factura en tb consultas
def update_datosFactura_consulta(fuente_fact, numero_fact, total_fact, atencion):
    conn = db.connection()
    query = "UPDATE consultas SET fuente_fact = %s, numero_fact = %s, total_fact = %s WHERE atencion = %s"
    params = (fuente_fact, numero_fact, total_fact, atencion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()        

#Metodo para listar todos los servicios detalle de la consulta para generar factura
def listar_detalle_consulta_id(id_consulta):
    detalle = []
    conn = db.connection()
    query = "SELECT und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total FROM detalle_consultas WHERE id_atencion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_consulta, ))
        result = cursor.fetchall()
        for row in result:
            detalle.append({'und_funcional': row[0], 'cod_serv': row[1], 'nom_serv': row[2], 'valor_serv': row[3], 'cantidad': row[4], 'total': row[5]})

    conn.close()
    return detalle                           