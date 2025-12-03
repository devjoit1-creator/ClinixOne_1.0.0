from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app.services import hospitalizacion_service, consecutivo_service, paciente_service, administradoras_service, causas_service, medico_service, ufuncionales_service, habitaciones_service, diagnosticos_cie10, servicios_service, reportes_service, fuentes_service
from flask_weasyprint import render_pdf, HTML
from io import BytesIO
import base64
import mysql.connector.errors as error

bp_hospitalizacion = Blueprint('hospitalizacion', __name__)

#Ruta Principal Hospitalizacion
@bp_hospitalizacion.get('/hospitalizacion')
def hospitalizacion():
    hospitalizaciones = hospitalizacion_service.listar_hospitalizaciones()
    return render_template('temp_hospitalizacion/hospitalizacion.html', hospitalizaciones = hospitalizaciones)

#Ruta Formulario Nueva Hospitalizacion
@bp_hospitalizacion.get('/add_hospitalizacion')
def add_hospitalizacion():
    atencion = consecutivo_service.listar_consecutivo_atencion()
    pacientes = paciente_service.listar_pacientes_modal()
    remitidos = hospitalizacion_service.listar_remitidos()
    administradoras = administradoras_service.listar_administradoras_modal()
    causas = causas_service.listar_causas()
    medicos = medico_service.listar_medicos()
    unidades = ufuncionales_service.listar_ufuncionales()
    diagnosticos = diagnosticos_cie10.listar_diagnosticos()
    return render_template('temp_hospitalizacion/add_hospitalizacion.html', atencion = atencion, pacientes = pacientes, remitidos = remitidos, administradoras = administradoras, causas = causas, medicos = medicos,
                           unidades = unidades, diagnosticos = diagnosticos)    

#Ruta Post Guardar Nueva Hospitalización
@bp_hospitalizacion.post('/f_addHospitalizacion')
def f_addHospitalizacion():
    try:
        atencion = request.form["atencion"]
        codigo = request.form["codigo"]
        fecha_ingreso = request.form["fecha_ingreso"]
        hora_ingreso = request.form["hora_ingreso"]
        plan_beneficios = request.form["plan_beneficios"]
        concepto_recaudo = request.form["concepto_recaudo"]
        cod_admin = request.form["cod_admin"]
        nit_admin = request.form["nit_admin"]
        via_ingreso = request.form["via_ingreso"]
        remitido = request.form["remitido"]
        causa_externa = request.form["causa_externa"]
        finalidad = request.form["finalidad"]
        medico = request.form["medico"]
        und_funcional = request.form["und_funcional"]
        habitacion = request.form["habitacion"]
        cod_diag1 = request.form["cod_diag1"]
        nom_diag1 = request.form["nom_diag1"]
        cod_diag2 = request.form["cod_diag2"]
        nom_diag2 = request.form["nom_diag2"]
        cod_diag3 = request.form["cod_diag3"]
        nom_diag3 = request.form["nom_diag3"]
        cod_diag4 = request.form["cod_diag4"]
        nom_diag4 = request.form["nom_diag4"]
        tipo_diag = request.form["tipo_diag"]
        observaciones = request.form["observaciones"]
        usuario_ingreso = request.form["usuario"]

        hospitalizacion_service.insert_hospitalizacion(atencion, codigo, fecha_ingreso, hora_ingreso, plan_beneficios, concepto_recaudo, cod_admin, nit_admin, via_ingreso, remitido, causa_externa,
                                                        finalidad, medico, und_funcional, habitacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3,
                                                        cod_diag4, nom_diag4, tipo_diag, observaciones, usuario_ingreso)
        
        habitaciones_service.update_ocupar_habitacion(habitacion)
        flash("Ingreso a Hospitalización Habilitado. El paciente puede ser atendido","success")
        return redirect(url_for('hospitalizacion.hospitalizacion'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))

#Ruta Generar PDF Orden Ingreso Hospitalización    
@bp_hospitalizacion.get('/orden_ingreso/<int:id>')
def orden_ingreso(id):
    #Datos de entidad
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    #Datos de Registro Hospitalizacion
    registro = hospitalizacion_service.orden_ingreso_hosp(id)    

    html = render_template('temp_hospitalizacion/rp_orden_ingreso.html', entidad = entidad, logo = logo, registro = registro)
    return render_pdf(HTML(string = html))

#Ruta Formulario Nueva Egreso Hospitalizacion
@bp_hospitalizacion.get('/add_egreso_hosp/<int:id>')
def add_egreso_hosp(id):
    registro = hospitalizacion_service.listar_hospitalizacion_id(id)
    paciente = paciente_service.listar_paciente_doc(registro[2])
    administradora = administradoras_service.listar_administradora_id(registro[7])
    unidad = ufuncionales_service.listar_ufuncional_id(registro[14])
    unidades = ufuncionales_service.listar_ufuncionales()
    diagnosticos = diagnosticos_cie10.listar_diagnosticos()
    return render_template('temp_hospitalizacion/add_egreso_hosp.html', registro = registro, paciente = paciente, administradora = administradora, unidad = unidad, unidades = unidades,
                           diagnosticos = diagnosticos)

#Ruta Post Actualizar Datos Egreso Hospitalización
@bp_hospitalizacion.post('/f_addEgresoHosp')
def f_addEgresoHosp():
    try:
        #Request para actualizar los datos de egreso de hospitalizacion
        fecha_salida = request.form["fecha_salida"]
        hora_salida = request.form["hora_salida"]
        und_funcional_salida = request.form["und_funcional_salida"]
        dias_estancia = request.form["dias_estancia"]
        estado_salida = request.form["estado_salida"]
        cod_diag_salida = request.form["cod_diag_salida"]
        nom_diag_salida = request.form["nom_diag_salida"]
        cod_diag_muerte = request.form["cod_diag_muerte"]
        nom_diag_muerte = request.form["nom_diag_muerte"]
        remitido_salida = request.form["remitido_salida"]
        usuario_salida = request.form["usuario"]
        id_hospitalizacion = request.form["atencion"]

        hospitalizacion_service.update_egreso_hosp(fecha_salida, hora_salida, und_funcional_salida, dias_estancia, estado_salida, cod_diag_salida,
                                                    nom_diag_salida, cod_diag_muerte, nom_diag_muerte, remitido_salida, usuario_salida, id_hospitalizacion)

        #Request para Liberar Habitación al generar egreso
        habitacion = request.form["habitacion"]
        habitaciones_service.update_liberar_habitacion(habitacion)

        flash("Egreso de Paciente Generado Exitosamente", "success")
        return redirect(url_for('hospitalizacion.hospitalizacion'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))

#Ruta Generar PDF Orden Egreso Hospitalización   
@bp_hospitalizacion.get('/orden_egreso/<int:id>')
def orden_egreso(id):
    #Datos de entidad
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    registro = hospitalizacion_service.orden_egreso_hosp(id)
    html = render_template('temp_hospitalizacion/rp_orden_egreso.html', entidad = entidad, logo = logo, registro = registro)
    return render_pdf(HTML(string = html))

#Ruta para Anular ingreso de hospitalización  
@bp_hospitalizacion.get('/drop_hospitalizacion/<int:id>')
def drop_hospitalizacion(id):
    try:
        hospitalizacion_service.delete_hospitalizacion(id)
        flash("Ingreso Anulado Exitosamente", "success")
        return redirect(url_for('hospitalizacion.hospitalizacion'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))

#Ruta para Anular Egreso de Hospitalizacion
@bp_hospitalizacion.get('/anular_egreso_hosp/<int:id>')
def anular_egreso_hosp(id):
    try:
        #Ocupar Cama Nuevamente
        registro = hospitalizacion_service.listar_hospitalizacion_id(id)
        habitaciones_service.update_ocupar_habitacion(registro[13])

        hospitalizacion_service.update_anular_egreso(id)
        flash("Egreso Anulado Exitosamente", "success")
        return redirect(url_for('hospitalizacion.hospitalizacion'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))
    
#Ruta Ventana para Cargar Autorización y Servicios medicos a facturar
@bp_hospitalizacion.get('/cargue_servicios_hosp/<int:id>')
def cargue_servicios_hosp(id):
    atencion = hospitalizacion_service.listar_hospitalizacion_id(id)
    servicios = servicios_service.listar_servicios()
    return render_template('temp_hospitalizacion/cargue_servicios_hosp.html', atencion=atencion, servicios=servicios)

#Ruta Metodo para guardar detalle de servicios liquidados de hospitalizacion
@bp_hospitalizacion.post('/f_cargueServiciosHosp')
def f_cargueServiciosHosp():
    try:
        if request.method == 'POST':
            atencion = request.form["atencion"]
            nro_autorizacion = request.form["nro_autorizacion"]
            total_servicios = request.form["total_servicios"]

            hospitalizacion_service.update_aut_hosp(nro_autorizacion, total_servicios, atencion)
            """ Request para insert de detalle servicios de la consulta """
            data = request.form.get("data")
            filas = data.split(';')
            for fila in filas:
                if fila.strip():
                    u_funcional, cod_serv, nom_serv, valor_serv, cantidad, total_serv, nro_aut = fila.split('-')
                    u_funcional_fila = u_funcional.strip()
                    cod_serv_fila = cod_serv.strip()
                    nom_serv_fila = nom_serv.strip()
                    valor_serv_fila = valor_serv.strip()
                    cantidad_fila = cantidad.strip()
                    total_serv_fila = total_serv.strip()
                    nro_aut_fila = nro_aut.strip()
                    hospitalizacion_service.insert_detalle_hospitalizacion(u_funcional_fila, cod_serv_fila, nom_serv_fila, valor_serv_fila, cantidad_fila, total_serv_fila, nro_aut_fila, atencion)
            
            flash(f"Servicios/Procedimientos de la atencion {atencion} Cargados Exitosamente","success")
            return redirect(url_for('hospitalizacion.hospitalizacion'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))
    
#Ruta Generar PDF Orden Hoja Admisión Finalidad
@bp_hospitalizacion.get('/hoja_admision/<int:id>')
def hoja_admision(id):
    #Datos de entidad
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    html = render_template('temp_hospitalizacion/rp_hoja_finalidad.html', entidad = entidad, logo = logo)
    return render_pdf(HTML(string = html))
            
#Ruta Ventana para generar factura hospitalizacion
@bp_hospitalizacion.get('/generar_factura_hosp/<int:id>')
def generar_factura_hosp(id):
    fuentes = fuentes_service.listar_fuente_fe()
    consecutivo = consecutivo_service.listar_consecutivo_fev()
    atencion = hospitalizacion_service.listar_hospitalizacion_id(id)
    dato_pac = paciente_service.listar_paciente_doc(atencion[2])
    administradora = administradoras_service.listar_administradora_id(atencion[7])
    servicios = hospitalizacion_service.listar_detalle_hospitalizacion_id(id)
    return render_template('temp_hospitalizacion/generar_factura_hosp.html', fuentes = fuentes, consecutivo = consecutivo, atencion = atencion, dato_pac = dato_pac, administradora = administradora, servicios = servicios)