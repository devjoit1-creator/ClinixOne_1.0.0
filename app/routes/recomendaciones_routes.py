from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_weasyprint import HTML, render_pdf
from io import BytesIO
from app.services import recomendaciones_service, reportes_service, paciente_service, medico_service
import base64
import mysql.connector.errors as error

bp_recomendaciones = Blueprint('recomendaciones', __name__)

@bp_recomendaciones.get('/recomendaciones/<atencion>/<paciente>')
def recomendaciones(atencion, paciente):
    medico = session['document']
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    recomendaciones = recomendaciones_service.listar_recomendaciones_med(paciente, medico)
    return render_template('temp_recomendaciones/recomendaciones.html', atencion = atencion, paciente = paciente,  dato_pac = dato_pac, recomendaciones = recomendaciones)

@bp_recomendaciones.get('/add_recomendacion/<atencion>/<paciente>')
def add_recomendacion(atencion, paciente):
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    return render_template('temp_recomendaciones/add_recomendacion.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac)

@bp_recomendaciones.post('/f_addRecomendacion')
def f_addRecomendacion():
    try:
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        paciente = request.form["codigo"]
        medico = request.form["medico"]
        detalle = request.form["detalle"]
        atencion = request.form["atencion"]

        recomendaciones_service.insert_recomendacion(fecha, hora, paciente, medico, detalle, atencion)
        flash(f"Receta Medica asociada exitosamente a la atención: {atencion}","success")
        return redirect(url_for('recomendaciones.recomendaciones', atencion = atencion, paciente = paciente))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('recomendaciones.recomendaciones', atencion = atencion, paciente = paciente))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('recomendaciones.recomendaciones', atencion = atencion, paciente = paciente))
    
@bp_recomendaciones.get('/view_recomendacion/<int:id>')
def view_recomendacion(id):
    recomendacion = recomendaciones_service.listar_recomendacion_id(id)
    dato_pac = paciente_service.listar_paciente_doc(recomendacion[3])
    return render_template('temp_recomendaciones/view_recomendacion.html', recomendacion = recomendacion, dato_pac = dato_pac)

@bp_recomendaciones.get('/hc_recomendacion/<idpac>/<int:id>/<idmed>')
def hc_recomendacion(idpac, id, idmed):
    #Herencia encabezado reportes
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    #Datos de paciente
    paciente = paciente_service.listar_paciente_doc(idpac)
    #Datos de recomendación
    recomendacion = recomendaciones_service.listar_recomendacion_id(id)
    #Datos Medico Profesional     
    medico = medico_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('temp_recomendaciones/hc_recomendacion.html', entidad = entidad, logo = logo, paciente = paciente, recomendacion = recomendacion, medico = medico, firma = firma)
    return render_pdf(HTML(string = html))