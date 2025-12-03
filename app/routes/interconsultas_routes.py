from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services import interconsultas_service, especialidades_service, paciente_service, medico_service, entidad_service, reportes_service
from flask_weasyprint import render_pdf, HTML
from io import BytesIO
import mysql.connector.errors as error
import base64

bp_interconsultas = Blueprint('interconsultas', __name__)

@bp_interconsultas.get('/interconsultas/<atencion>/<paciente>')
def interconsultas(atencion, paciente):
    medico = session['document']
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    interconsultas = interconsultas_service.listar_interconsultas(paciente, medico)
    return render_template('temp_interconsultas/interconsultas.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, interconsultas = interconsultas)

@bp_interconsultas.get('/add_interconsulta/<atencion>/<paciente>')
def add_interconsulta(atencion, paciente):
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    especialidades = especialidades_service.listar_especialidades()
    return render_template('temp_interconsultas/add_interconsulta.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, especialidades = especialidades)

@bp_interconsultas.post('/f_addInterconsulta')
def f_addInterconsulta():
    try:
        paciente = request.form["codigo"]
        medico = request.form["medico"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        cod_especialidad = request.form["cod_especialidad"]
        nom_especialidad = request.form["nom_especialidad"]
        detalle = request.form["detalle"]
        atencion = request.form["atencion"]

        interconsultas_service.insert_interconsulta(paciente, medico, fecha, hora, cod_especialidad, nom_especialidad, detalle, atencion)
        flash(f"Interconsulta asociada exitosamente a la atención: {atencion}","success")
        return redirect(url_for('interconsultas.interconsultas', atencion = atencion, paciente = paciente))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('interconsultas.interconsultas', atencion = atencion, paciente = paciente))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('interconsultas.interconsultas', atencion = atencion, paciente = paciente))
    
@bp_interconsultas.get('/view_interconsulta/<int:id>')
def view_interconsulta(id):
    interconsulta = interconsultas_service.listar_interconsulta_id(id)
    dato_pac = paciente_service.listar_paciente_doc(interconsulta[1])
    return render_template('temp_interconsultas/view_interconsulta.html', interconsulta = interconsulta, dato_pac = dato_pac)

@bp_interconsultas.get('/hc_interconsulta/<idpac>/<int:id>/<idmed>')
def hc_interconsulta(idpac, id, idmed):
    #Herencia encabezado reportes
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    #Datos de paciente
    paciente = paciente_service.listar_paciente_doc(idpac)
    #Datos de Incapacidad
    interconsulta = interconsultas_service.listar_interconsulta_id(id)
    #Datos Medico Profesional     
    medico = medico_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('temp_interconsultas/hc_interconsulta.html', entidad = entidad, logo = logo, paciente = paciente, interconsulta = interconsulta, medico = medico, firma = firma)
    return render_pdf(HTML(string = html))         