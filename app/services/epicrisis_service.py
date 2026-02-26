from app.database import db

#Listar todas las atenciones de consulta por documento paciente y documento medico
def listar_atenciones_consulta_epicrisis(paciente, medico):
    atenciones = []
    conn = db.connection()
    query = """ select c.atencion atencion, c.fecha_atencion ingreso, c.hora_atencion hora_ingreso, c.fecha_salida egreso, 
                c.hora_salida hora_egreso, uf.nom_ufuncional servicio
                from consultas c
                left join pacientes p on p.num_doc = c.codigo
                left join medicos m on m.num_documento = c.medico
                left join unidades_funcionales uf on uf.cod_ufuncional = c.und_funcional
                where p.num_doc = %s and m.num_documento = %s """
    params = (paciente, medico)
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            for row in result:
                atenciones.append({'atencion': row[0], 'ingreso': row[1].strftime("%Y-%m-%d"),  'hora_ingreso': row[2], 'salida': row[3].strftime("%Y-%m-%d"),  'hora_salida': row[4],'servicio': row[5]})

        return atenciones        

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex 

    finally:
        conn.close()

#Listar todas las atenciones de Hospitalizacion por documento paciente y documento medico
def listar_atenciones_hosp_epicrisis(paciente, medico):
    atenciones = []
    conn = db.connection()
    query = """ select h.atencion atencion, h.fecha_ingreso ingreso, h.hora_ingreso hora_ingreso, h.fecha_salida egreso, 
                h.hora_salida hora_salida, uf.nom_ufuncional servicio
                from hospitalizacion h 
                left join pacientes p on p.num_doc = h.codigo
                left join medicos m on m.num_documento = h.medico
                left join unidades_funcionales uf on uf.cod_ufuncional = h.und_funcional
                where p.num_doc = %s and m.num_documento = %s """
    params = (paciente, medico)
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            for row in result:
                atenciones.append({'atencion': row[0], 'ingreso': row[1].strftime("%Y-%m-%d"),  'hora_ingreso': row[2], 'salida': row[3].strftime("%Y-%m-%d"),  'hora_salida': row[4],'servicio': row[5]})

        return atenciones

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex
    
    finally:
        conn.close()

#Insertar Nueva Epicrisis
def insert_epriciris(fecha_registro, hora_registro, codigo, medico, atencion, fecha_ingreso, hora_ingreso, servicio_ingreso, fecha_salida, hora_salida, servicio_salida,
                     motivo_consulta, enf_actual, antecedentes, examen_fisico, cod_diag_ingreso, nom_diag_ingreso, conducta,
                     cambio, procedimientos, justificacion, cod_diag_egreso, nom_diag_egreso, plan_manejo, estado_salida, remitido_a):
    
    conn = db.connection()
    query = """ INSERT INTO epicrisis 
                (fecha_registro, hora_registro, codigo, medico, atencion, fecha_ingreso, hora_ingreso, servicio_ingreso, fecha_salida, hora_salida, servicio_salida,
                motivo_consulta, enf_actual, antecedentes, examen_fisico, cod_diag_ingreso, nom_diag_ingreso, conducta,
                cambio, procedimientos, justificacion, cod_diag_egreso, nom_diag_egreso, plan_manejo, estado_salida, remitido_a) 
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
    
    params = (fecha_registro, hora_registro, codigo, medico, atencion, fecha_ingreso, hora_ingreso, servicio_ingreso, fecha_salida, hora_salida, servicio_salida,
              motivo_consulta, enf_actual, antecedentes, examen_fisico, cod_diag_ingreso, nom_diag_ingreso, conducta,
              cambio, procedimientos, justificacion, cod_diag_egreso, nom_diag_egreso, plan_manejo, estado_salida, remitido_a)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Listar todas las epicrisis por medico y paciente
def listar_epicrisis(paciente, medico):
    registros = []
    conn = db.connection()
    query = """ SELECT e.id_epicrisis ID, e.atencion ATENCION, e.codigo DOCUMENTO, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre) PACIENTE,
                e.fecha_registro, e.hora_registro 
                FROM epicrisis e 
                LEFT JOIN pacientes p ON p.num_doc = e.codigo
                LEFT JOIN medicos m ON m.num_documento = e.medico   
                WHERE e.codigo = %s and e.medico = %s """
    params = (paciente, medico)
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            for row in result:
                registros.append({'ID': row[0], 'atencion': row[1], 'documento': row[2], 'paciente': row[3], 'fecha': row[4].strftime("%Y-%m-%d"), 'hora': row[5]})

        return registros        

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex
    
    finally:
        conn.close()

#Listar Datos de Epicrisis por ID        
def listar_epicrisis_id(id):
    epicrisis = None
    conn = db.connection()
    query = """ SELECT * FROM epicrisis WHERE id_epicrisis = %s """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (id, ))
            result = cursor.fetchone()
            epicrisis = result

        return epicrisis

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex

    finally:
        conn.close()    