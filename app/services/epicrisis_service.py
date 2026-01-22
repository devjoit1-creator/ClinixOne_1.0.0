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