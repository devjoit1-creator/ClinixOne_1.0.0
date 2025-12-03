from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services import paciente_service, medico_service, cups_service, ordenes_diag_service, reportes_service
from flask_weasyprint import render_pdf, HTML
from io import BytesIO
import base64
import mysql.connector.errors as error

bp_ordenesDiagnosticas = Blueprint('ordenes_diag', __name__)

@bp_ordenesDiagnosticas.get('/ordenes_diag/<atencion>/<paciente>')
def ordenes_diag(atencion, paciente):
    medico = session['document']
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    ordenes = ordenes_diag_service.listar_ordenes_diagnosticas(paciente, medico)
    return render_template('temp_ordenes_diag/ordenes_diag.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac ,ordenes = ordenes)

@bp_ordenesDiagnosticas.get('/add_orden_diag/<atencion>/<paciente>')
def add_orden_diag(atencion, paciente):
    consecutivo = ordenes_diag_service.listar_consecutivo_od()
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    cups = cups_service.listar_cups()
    return render_template('temp_ordenes_diag/add_orden_diag.html', atencion = atencion, paciente = paciente, consecutivo = consecutivo, dato_pac = dato_pac, cups = cups)    

@bp_ordenesDiagnosticas.post('/f_addOrdenDiag')
def f_addOrdenDiag():
    try:
        """ Request para Consulta Orden Diagnostica """
        paciente = request.form["codigo"]
        medico = request.form["medico"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        atencion = request.form["atencion"]

        ordenes_diag_service.insert_orden_diag(paciente, medico, fecha, hora, atencion)
        
        """ Request para Consulta Detalle Orden Diagnostica """
        id_orden = request.form["id_orden"]
        data = request.form.get('data')
        filas = data.split(';')
        for fila in filas:
            if fila.strip():
                cod_servicio, servicio, justificacion = fila.split('-')
                cod_servicio_fila = cod_servicio.strip()
                servicio_fila = servicio.strip()
                justificacion_fila = justificacion.strip()           
                ordenes_diag_service.insert_detalle_orden(cod_servicio_fila, servicio_fila, justificacion_fila, id_orden)

        flash(f"Orden Diagnostica asociada exitosamente a la atención: {atencion}", "success")
        return redirect(url_for('ordenes_diag.ordenes_diag', atencion = atencion, paciente = paciente))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('ordenes_diag.ordenes_diag', atencion = atencion, paciente = paciente))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('ordenes_diag.ordenes_diag', atencion = atencion, paciente = paciente))
    

@bp_ordenesDiagnosticas.get('/view_orden_diag/<int:id>')
def view_orden_diag(id):
    orden_diag = ordenes_diag_service.listar_odiag_id(id)
    dato_pac = paciente_service.listar_paciente_doc(orden_diag[1])
    detalle = ordenes_diag_service.listar_detalle_odiag_id(id)
    return render_template('temp_ordenes_diag/view_orden_diag.html', orden_diag = orden_diag, dato_pac = dato_pac, detalle = detalle)

@bp_ordenesDiagnosticas.get('/hc_orden_diag/<idpac>/<int:id>/<idmed>')
def hc_orden_diag(idpac, id, idmed):
    #Herencia encabezado reportes
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    #Datos de paciente
    paciente = paciente_service.listar_paciente_doc(idpac)
    #Datos de orden diagnostica y detalle
    orden_diag = ordenes_diag_service.listar_odiag_id(id)
    detalle = ordenes_diag_service.listar_detalle_odiag_id(id)
    #Datos Medico Profesional     
    medico = medico_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('temp_ordenes_diag/hc_orden_diag.html', entidad = entidad, logo = logo, paciente = paciente, orden_diag = orden_diag, detalle = detalle, medico = medico, firma = firma)
    return render_pdf(HTML(string = html))    