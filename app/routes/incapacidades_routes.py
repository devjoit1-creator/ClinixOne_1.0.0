from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_weasyprint import HTML, render_pdf
from app.services import incapacidades_service, paciente_service, medico_service, entidad_service, diagnosticos_cie10, reportes_service
from io import BytesIO
import base64
import mysql.connector.errors as error

bp_incapacidades = Blueprint('incapacidades', __name__)

@bp_incapacidades.get('/incapacidades/<atencion>/<paciente>')
def incapacidades(atencion, paciente):
    medico = session['document']
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    incapacidades = incapacidades_service.listar_incapacidades(paciente, medico)
    return render_template('temp_incapacidades/incapacidades.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, incapacidades = incapacidades)

@bp_incapacidades.get('/add_incapacidad/<atencion>/<paciente>')
def add_incapacidad(atencion, paciente):
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    diagnosticos = diagnosticos_cie10.listar_diagnosticos()
    return render_template('temp_incapacidades/add_incapacidad.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, diagnosticos = diagnosticos)   

@bp_incapacidades.post('/f_addIncapacidad')
def f_addIncapacidad():
    try:
        paciente = request.form["codigo"]
        medico = request.form["medico"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        grupo_ser = request.form["grupo_ser"]
        origen = request.form["origen"]
        cod_diag = request.form["cod_diag"]
        nom_diag = request.form["nom_diag"]
        cod_diag2 = request.form["cod_diag2"]
        nom_diag2 = request.form["nom_diag2"]
        fecha_inicio = request.form["fecha_inicio"]
        fecha_fin = request.form["fecha_fin"]
        dias = request.form["dias"]
        tipo = request.form["tipo"]
        modalidad = request.form["modalidad"]
        retroactiva = request.form["retroactiva"]
        causa = request.form["causa"]
        observacion = request.form["observacion"]
        atencion = request.form["atencion"]

        incapacidades_service.insert_incapacidad(paciente, medico, fecha, hora, grupo_ser, origen, cod_diag, nom_diag, cod_diag2, nom_diag2, fecha_inicio, fecha_fin,
                                                    dias, tipo, modalidad, retroactiva, causa, observacion, atencion)
        
        flash(f"Incapacidad asociada exitosamente a la atención: {atencion}","success")
        return redirect(url_for('incapacidades.incapacidades', atencion = atencion, paciente = paciente))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('incapacidades.incapacidades', atencion = atencion, paciente = paciente))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('incapacidades.incapacidades', atencion = atencion, paciente = paciente))
    
@bp_incapacidades.get('/view_incapacidad/<int:id>/')
def view_incapacidad(id):
    incapacidad = incapacidades_service.listar_incapacidad_id(id)
    dato_pac = paciente_service.listar_paciente_doc(incapacidad[1])
    return render_template('temp_incapacidades/view_incapacidad.html', incapacidad = incapacidad, dato_pac = dato_pac)

@bp_incapacidades.get('/hc_incapacidad/<idpac>/<int:id>/<idmed>')
def hc_incapacidad(idpac, id, idmed):
    #Herencia encabezado reportes
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')    

    #Datos de paciente
    paciente = paciente_service.listar_paciente_doc(idpac)
    #Datos de Incapacidad
    incapacidad = incapacidades_service.listar_incapacidad_id(id)
    #Datos Medico Profesional     
    medico = medico_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('temp_incapacidades/hc_incapacidad.html', entidad = entidad, logo = logo, paciente = paciente, incapacidad = incapacidad, medico = medico, firma = firma)
    return render_pdf(HTML(string = html))      