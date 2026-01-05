from app.database import db

#Listar todas las entidades que remiten pacientes
def listar_remitidos():
    remitidos = []
    conn = db.connection()
    query = """ SELECT nom_remitido FROM remitidos """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            remitidos.append({'nombre': row[0]})

    conn.close()
    return remitidos

#Metodo para insertar nueva hospitalizacion en BD
def insert_hospitalizacion(atencion, codigo, fecha_ingreso, hora_ingreso, plan_beneficios, concepto_recaudo, cod_admin, nit_admin, via_ingreso, remitido, causa_externa,
                           finalidad, medico, und_funcional, habitacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, cod_diag4, 
                           nom_diag4, tipo_diag, observaciones, usuario_ingreso):
    
    conn = db.connection()
    query = """ INSERT INTO hospitalizacion (atencion, codigo, fecha_ingreso, hora_ingreso, plan_beneficios, concepto_recaudo, cod_admin, nit_admin, via_ingreso, remitido, causa_externa,
                                            finalidad, medico, und_funcional, habitacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, cod_diag4, 
                                            nom_diag4, tipo_diag, observaciones, usuario_ingreso)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (atencion, codigo, fecha_ingreso, hora_ingreso, plan_beneficios, concepto_recaudo, cod_admin, nit_admin, via_ingreso, remitido, causa_externa,
              finalidad, medico, und_funcional, habitacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, cod_diag4, 
              nom_diag4, tipo_diag, observaciones, usuario_ingreso)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todas las hospitalizaciones
def listar_hospitalizaciones():
    hospitalizaciones = []
    conn = db.connection()
    query = """ SELECT h.atencion, h.fecha_ingreso, h.hora_ingreso, p.num_doc ,CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre),
                h.fecha_salida, h.hora_salida, h.nro_autorizacion, h.numero_fact
                FROM hospitalizacion h,  pacientes p WHERE h.codigo = p.num_doc"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            hospitalizaciones.append({'atencion': row[0], 'fecha_ingreso': row[1], 'hora_ingreso': row[2], 'codigo': row[3], 'paciente': row[4], 'fecha_salida': row[5], 'hora_salida': row[6], 'aut': row[7], 'numero_fact': row[8]})

    conn.close()
    return hospitalizaciones

#Metodo para listar datos de hospitalizacion por numero de atención
def listar_hospitalizacion_atencion(atencion):
    hospitalizaciones = []
    conn = db.connection()
    query = """ SELECT h.atencion, h.fecha_ingreso, h.hora_ingreso, p.num_doc ,CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre),
                h.fecha_salida, h.hora_salida, h.nro_autorizacion, h.numero_fact
                FROM hospitalizacion h,  pacientes p WHERE h.codigo = p.num_doc and h.atencion = %s  """
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (atencion, ))
            result = cursor.fetchall()
            for row in result:
                hospitalizaciones.append({'atencion': row[0], 'fecha_ingreso': row[1].strftime("%Y-%m-%d"), 'hora_ingreso': row[2], 'codigo': row[3], 'paciente': row[4], 'fecha_salida': row[5].strftime("%Y-%m-%d"), 'hora_salida': row[6], 'aut': row[7], 'numero_fact': row[8]})

        return hospitalizaciones

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex
    
    finally:
        conn.close()

#Metodo para listar hospitalizacion por id
def listar_hospitalizacion_id(id_hospitalizacion):
    hospitalizacion = None
    conn = db.connection()
    query = """ SELECT * FROM hospitalizacion WHERE atencion = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_hospitalizacion, ))
        result = cursor.fetchone()
        hospitalizacion = result

    conn.close()
    return hospitalizacion    

#Metodo para listar datos de orden de ingreso de hospitalizacion
def orden_ingreso_hosp(id_hospitalizacion):
    registro = None
    conn = db.connection()
    query = """ SELECT h.fecha_ingreso, h.hora_ingreso, h.atencion,
                concat(p.p_nombre,' ',p.s_nombre,' ',p.p_apellido,' ',p.s_apellido), concat(p.tipo_doc,' ',p.num_doc), p.direccion, p.telefono, p.fecha_nac, floor(datediff(sysdate(), p.fecha_nac)/365),
                p.nom_munic, p.barrio,
                case
                    when p.sexo = '1' then 'MASCULINO'
                    when p.sexo = '2' then 'FEMENINO'
                    when p.sexo = '3' then 'INDETERMINADO'
                end,
                p.ocupacion,
                case 
                    when p.regimen = 1 then 'Contributivo'
                    when p.regimen = 2 then 'Subsidiado'
                    when p.regimen = 3 then 'Particular'
                    when p.regimen = 4 then 'Vinculado'
                    when p.regimen = 5 then 'Reg. Excepción'
                    when p.regimen = 6 then 'Reg. Especial'
                    when p.regimen = 7 then 'Otro'
                    when p.regimen = 8 then 'Sin Regimen'
                end,
                p.acompanante, p.parent_acompanante, p.tel_acompanante, p.responsable, p.parent_responsable, p.tel_responsable,
                a.nit_administradora, a.cod_administradora, a.nom_administradora, a.dir_administradora, a.tel_administradora, a.convenio,
                uf.nom_ufuncional, h.habitacion, h.remitido, concat(m.num_documento,' - ',m.nombre_completo),
                h.cod_diag1, h.nom_diag1, h.cod_diag2, h.nom_diag2, h.cod_diag3, h.nom_diag3, h.cod_diag4, h.nom_diag4, h.observaciones, h.usuario_ingreso
                FROM hospitalizacion h, pacientes p, administradoras a, unidades_funcionales uf, medicos m 
                WHERE p.num_doc = h.codigo AND h.cod_admin = a.cod_administradora AND h.und_funcional = uf.cod_ufuncional
                AND h.medico = m.num_documento AND h.atencion = %s"""
    with conn.cursor() as cursor:
        cursor.execute(query, (id_hospitalizacion, ))
        result = cursor.fetchone()
        registro = result

    conn.close()
    return registro

# Metodo para insertar datos de egreso de hospitalización
def update_egreso_hosp(fecha_salida, hora_salida, und_funcional_salida, dias_estancia, estado_salida, cod_diag_salida, nom_diag_salida,
                       cod_diag_muerte, nom_diag_muerte, remitido_salida, usuario_salida, id_hospitalizacion):
    conn = db.connection()
    query = """ UPDATE hospitalizacion SET fecha_salida = %s, hora_salida = %s, und_funcional_salida = %s, dias_estancia = %s, estado_salida = %s,
                cod_diag_salida = %s, nom_diag_salida = %s, cod_diag_muerte = %s, nom_diag_muerte = %s, remitido_salida = %s, usuario_salida = %s
                WHERE atencion = %s  """
    
    params = (fecha_salida, hora_salida, und_funcional_salida, dias_estancia, estado_salida, cod_diag_salida, nom_diag_salida,
              cod_diag_muerte, nom_diag_muerte, remitido_salida, usuario_salida, id_hospitalizacion)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar datos de orden de egreso de hospitalizacion
def orden_egreso_hosp(id_hospitalizacion):
    registro = None
    conn = db.connection()
    query = """ SELECT h.atencion,
                concat(p.p_nombre,' ',p.s_nombre,' ',p.p_apellido,' ',p.s_apellido), concat(p.tipo_doc,' ',p.num_doc), p.direccion, p.telefono, p.fecha_nac, floor(datediff(sysdate(), p.fecha_nac)/365),
                p.nom_munic, p.barrio,
                case
                    when p.sexo = '1' then 'MASCULINO'
                    when p.sexo = '2' then 'FEMENINO'
                    when p.sexo = '3' then 'INDETERMINADO'
                end,
                p.ocupacion,
                case 
                    when p.regimen = 1 then 'Contributivo'
                    when p.regimen = 2 then 'Subsidiado'
                    when p.regimen = 3 then 'Particular'
                    when p.regimen = 4 then 'Vinculado'
                    when p.regimen = 5 then 'Reg. Excepción'
                    when p.regimen = 6 then 'Reg. Especial'
                    when p.regimen = 7 then 'Otro'
                    when p.regimen = 8 then 'Sin Regimen'
                end,
                p.acompanante, p.parent_acompanante, p.tel_acompanante, p.responsable, p.parent_responsable, p.tel_responsable,
                a.nit_administradora, a.cod_administradora, a.nom_administradora, a.dir_administradora, a.tel_administradora, a.convenio,
                h.fecha_salida, h.hora_salida, uf.nom_ufuncional, h.dias_estancia,
                case 
                    when h.estado_salida = 1 then 'VIVO'
                    when h.estado_salida = 2 then 'MUERTO'
                    when h.estado_salida = 3 then 'VIVO'
                    when h.estado_salida = 4 then 'REFERIDO A OTRA INSTITUCIÓN'
                    when h.estado_salida = 5 then 'VIVO'
                    when h.estado_salida = 6 then 'VIVO'
                    when h.estado_salida = 7 then 'VIVO'
                end,
                h.cod_diag_salida, h.nom_diag_salida, h.cod_diag_muerte, h.nom_diag_muerte, h.remitido_salida, h.usuario_salida
                FROM hospitalizacion h, pacientes p, administradoras a, unidades_funcionales uf
                WHERE p.num_doc = h.codigo AND h.cod_admin = a.cod_administradora AND h.und_funcional = uf.cod_ufuncional
                AND h.atencion = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_hospitalizacion, ))
        result = cursor.fetchone()
        registro = result

    conn.close()
    return registro

#Metodo Para eliminar/anular Ingreso a hospitalización
def delete_hospitalizacion(id_hospitalizacion):
    conn = db.connection()
    query = """ DELETE FROM hospitalizacion WHERE atencion = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_hospitalizacion, ))
        conn.commit()
        conn.close()

#Metodo para anular egreso de hospitalización
def update_anular_egreso(id_hospitalizacion):
    conn = db.connection()
    query = """ UPDATE hospitalizacion SET fecha_salida = NULL, hora_salida = NULL, und_funcional_salida = NULL, dias_estancia = NULL, estado_salida = NULL,
                cod_diag_salida = NULL, nom_diag_salida = NULL, cod_diag_muerte = NULL, nom_diag_muerte = NULL, remitido_salida = NULL, usuario_salida = NULL
                WHERE atencion = %s  """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_hospitalizacion, ))
        conn.commit()
        conn.close()

#Metodo para listar las atenciones por hospitalización
def listar_atenciones_hosp(und_funcional):
    atenciones_hosp = []
    conn = db.connection()
    query = """ SELECT h.atencion, h.fecha_ingreso, h.codigo, concat(p.p_nombre,' ',p.s_nombre,' ',p.p_apellido,' ',p.s_apellido), h.habitacion, a.nom_administradora 
              FROM hospitalizacion h, pacientes p, administradoras a
              WHERE h.codigo = p.num_doc AND h.cod_admin = a.cod_administradora
              AND h.fecha_salida is NULL AND h.und_funcional = %s """
    
    with conn.cursor() as cursor:
        cursor.execute(query, (und_funcional, ))
        result = cursor.fetchall()
        for row in result:
            atenciones_hosp.append({'atencion': row[0], 'fecha': row[1], 'codigo': row[2], 'paciente': row[3], 'habitacion': row[4], 'administradora': row[5]})


    conn.close()
    return atenciones_hosp

#Metodo para actualizar campo autorizacion de tabla hospitalizacion
def update_aut_hosp(nro_autorizacion, total_servicios, id_hospitalizacion):
    conn = db.connection()
    query = """ UPDATE hospitalizacion SET nro_autorizacion = %s, total_servicios = %s WHERE atencion = %s"""
    params =  (nro_autorizacion, total_servicios, id_hospitalizacion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para insertar detalle de los servicios de la hospitalizacion en la bd
def insert_detalle_hospitalizacion(und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, nro_autorizacion, id_atencion):
    conn = db.connection()
    query = """ INSERT INTO detalle_hospitalizacion(und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, nro_autorizacion, id_atencion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
    params = (und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, nro_autorizacion, id_atencion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()


#Metodo para listar todos los servicios detalle de la hospitalizacion para generar factura
def listar_detalle_hospitalizacion_id(id_atencion):
    detalle = []
    conn = db.connection()
    query = "SELECT und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total FROM detalle_hospitalizacion WHERE id_atencion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_atencion, ))
        result = cursor.fetchall()
        for row in result:
            detalle.append({'und_funcional': row[0], 'cod_serv': row[1], 'nom_serv': row[2], 'valor_serv': row[3], 'cantidad': row[4], 'total': row[5]})

    conn.close()
    return detalle

#Metodo para actualizar datos de factura en tb hospitalizacion
def update_datosFactura_hospitalizacion(fuente_fact, numero_fact, total_fact, atencion):
    conn = db.connection()
    query = "UPDATE hospitalizacion SET fuente_fact = %s, numero_fact = %s, total_fact = %s WHERE atencion = %s"
    params = (fuente_fact, numero_fact, total_fact, atencion)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()
