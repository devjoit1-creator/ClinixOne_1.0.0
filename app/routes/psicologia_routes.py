from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_weasyprint import HTML, render_pdf
from app.services import psicologia_service, paciente_service, diagnosticos_cie10, medico_service, reportes_service
from io import BytesIO
import base64
import mysql.connector.errors as error

bp_psicologia = Blueprint('psicologia', __name__)

@bp_psicologia.get('/psicologia/<atencion>/<paciente>')
def psicologia(atencion, paciente):
    medico = session['document']
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    registros = psicologia_service.listar_hc_psicologia(paciente, medico)
    return render_template('temp_psicologia/psicologia.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, registros = registros)

@bp_psicologia.get('/add_regpsicologia/<atencion>/<paciente>')
def add_regpsicologia(atencion, paciente):
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    diagnosticos = diagnosticos_cie10.listar_diagnosticos()
    return render_template('temp_psicologia/add_regpsicologia.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, diagnosticos = diagnosticos)

@bp_psicologia.post('/f_addRegPsicologia')
def f_addRegPsicologia():
    try:
        paciente = request.form["codigo"]
        medico = request.form["medico"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        motivo_consulta = request.form["motivo_consulta"]
        enf_actual = request.form["enf_actual"]
        antper_diabetes = request.form["antper_diabetes"]
        antper_hta = request.form["antper_hta"]
        antper_dislipidemia = request.form["antper_dislipidemia"]
        antper_cancer = request.form["antper_cancer"]
        antper_asma = request.form["antper_asma"]
        antper_epilepsia = request.form["antper_epilepsia"]
        antper_tuberculosis = request.form["antper_tuberculosis"]
        antper_violencia = request.form["antper_violencia"]
        antper_otro = request.form["antper_otro"] 
        antper_otro_cual = request.form["antper_otro_cual"]
        antper_observaciones = request.form["antper_observaciones"]
        practica_cirugia = request.form["practica_cirugia"]
        practica_cirugia_cual = request.form["practica_cirugia_cual"]
        padece_enf = request.form["padece_enf"]
        padece_enf_cual = request.form["padece_enf_cual"]
        practica_tratamiento = request.form["practica_tratamiento"]
        practica_tratamiento_cual = request.form["practica_tratamiento_cual"]
        toma_medicamento = request.form["toma_medicamento"]
        toma_medicamento_cual = request.form["toma_medicamento_cual"]
        toma_medicamento_dosis = request.form["toma_medicamento_dosis"]
        antfam_alergia = request.form["antfam_alergia"]
        antfam_alergia_parent = request.form["antfam_alergia_parent"]
        antfam_diabetes = request.form["antfam_diabetes"]
        antfam_diabetes_parent = request.form["antfam_diabetes_parent"]
        antfam_cancer = request.form["antfam_cancer"]
        antfam_cancer_parent = request.form["antfam_cancer_parent"]
        antfam_hta = request.form["antfam_hta"]
        antfam_hta_parent = request.form["antfam_hta_parent"]
        antfam_respiratoria = request.form["antfam_respiratoria"]
        antfam_respiratoria_parent = request.form["antfam_respiratoria_parent"]
        antfam_asma = request.form["antfam_asma"]
        antfam_asma_parent = request.form["antfam_asma_parent"]
        antfam_epilepsia = request.form["antfam_epilepsia"]
        antfam_epilepsia_parent = request.form["antfam_epilepsia_parent"]
        antfam_ceguera = request.form["antfam_ceguera"]
        antfam_ceguera_parent = request.form["antfam_ceguera_parent"]
        antfam_dislipidemia = request.form["antfam_dislipidemia"]
        antfam_dislipidemia_parent = request.form["antfam_dislipidemia_parent"]
        antfam_alcoholismo = request.form["antfam_alcoholismo"]
        antfam_alcoholismo_parent = request.form["antfam_alcoholismo_parent"]
        antfam_tabaquismo = request.form["antfam_tabaquismo"]
        antfam_tabaquismo_parent = request.form["antfam_tabaquismo_parent"]
        antfam_drogadiccion = request.form["antfam_drogadiccion"]
        antfam_drogadiccion_parent = request.form["antfam_drogadiccion_parent"]
        antfam_tuberculosis = request.form["antfam_tuberculosis"]
        antfam_tuberculosis_parent = request.form["antfam_tuberculosis_parent"]
        antfam_violencia = request.form["antfam_violencia"]
        antfam_violencia_parent = request.form["antfam_violencia_parent"]
        aspfam_vive = request.form["aspfam_vive"]
        aspfam_relacion = request.form["aspfam_relacion"]
        aspfam_hecho = request.form["aspfam_hecho"]
        aspper_estudio = request.form["aspper_estudio"]
        aspper_social = request.form["aspper_social"]
        aspper_orientacion = request.form["aspper_orientacion"]
        aspper_conducta = request.form["aspper_conducta"]
        estado_sueno = request.form["estado_sueno"]
        estado_concentracion = request.form["estado_concentracion"]
        estado_juicio = request.form["estado_juicio"]
        estado_intelectual = request.form["estado_intelectual"]
        estado_orientacion = request.form["estado_orientacion"]
        estado_sensopercepcion = request.form["estado_sensopercepcion"]
        estado_conciencia = request.form["estado_conciencia"]
        estado_memoria = request.form["estado_memoria"]
        estado_pensamiento = request.form["estado_pensamiento"]
        estado_afecto = request.form["estado_afecto"]
        estado_higiene = request.form["estado_higiene"]
        estado_postura = request.form["estado_postura"]
        estado_expresion = request.form["estado_expresion"]
        estado_alimentacion = request.form["estado_alimentacion"]
        cod_diag1 = request.form["cod_diag1"]
        nom_diag1 = request.form["nom_diag1"]
        cod_diag2 = request.form["cod_diag2"]
        nom_diag2 = request.form["nom_diag2"]
        cod_diag3 = request.form["cod_diag3"]
        nom_diag3 = request.form["nom_diag3"]
        cod_diag4 = request.form["cod_diag4"]
        nom_diag4 = request.form["nom_diag4"]
        tipo_diag = request.form["tipo_diag"]  
        plan_trata = request.form["plan_trata"]
        atencion = request.form["atencion"]

        psicologia_service.insert_hcpsicologia(paciente, medico, fecha, hora, motivo_consulta, enf_actual, antper_diabetes, antper_hta, antper_dislipidemia, antper_cancer,
                                                antper_asma, antper_epilepsia, antper_tuberculosis, antper_violencia, antper_otro, antper_otro_cual, antper_observaciones,
                                                practica_cirugia, practica_cirugia_cual, padece_enf, padece_enf_cual, practica_tratamiento, practica_tratamiento_cual, toma_medicamento,
                                                toma_medicamento_cual, toma_medicamento_dosis, antfam_alergia, antfam_alergia_parent, antfam_diabetes, antfam_diabetes_parent, antfam_cancer,
                                                antfam_cancer_parent, antfam_hta, antfam_hta_parent, antfam_respiratoria, antfam_respiratoria_parent, antfam_asma, antfam_asma_parent,
                                                antfam_epilepsia, antfam_epilepsia_parent, antfam_ceguera, antfam_ceguera_parent, antfam_dislipidemia, antfam_dislipidemia_parent,
                                                antfam_alcoholismo, antfam_alcoholismo_parent, antfam_tabaquismo, antfam_tabaquismo_parent, antfam_drogadiccion, antfam_drogadiccion_parent,
                                                antfam_tuberculosis, antfam_tuberculosis_parent, antfam_violencia, antfam_violencia_parent, aspfam_vive, aspfam_relacion, aspfam_hecho,
                                                aspper_estudio, aspper_social, aspper_orientacion, aspper_conducta, estado_sueno, estado_concentracion, estado_juicio, estado_intelectual,
                                                estado_orientacion, estado_sensopercepcion, estado_conciencia, estado_memoria, estado_pensamiento, estado_afecto, estado_higiene, estado_postura,
                                                estado_expresion, estado_alimentacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, cod_diag4, nom_diag4, tipo_diag, 
                                                plan_trata, atencion)

        flash(f"Historia Clinica de Psicología asociada exitosamente a la atención: {atencion}", "success")
        return redirect(url_for('psicologia.psicologia', atencion = atencion, paciente = paciente))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('psicologia.psicologia', atencion = atencion, paciente = paciente))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('psicologia.psicologia', atencion = atencion, paciente = paciente))

@bp_psicologia.get('/view_regpsicologia/<int:id>')
def view_repsicologia(id):
    registro = psicologia_service.listar_hc_psicologia_id(id)
    dato_pac = paciente_service.listar_paciente_doc(registro[1])
    return render_template('temp_psicologia/view_regpsicologia.html', dato_pac = dato_pac, registro = registro)

@bp_psicologia.get('/hc_psicologia/<idpac>/<int:id>/<idmed>')
def hc_psicologia(idpac, id, idmed):
 #Herencia encabezado reportes
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    #Datos de paciente
    paciente = paciente_service.listar_paciente_doc(idpac)
    #Datos de Atención por Psicología
    registro = psicologia_service.listar_hc_psicologia_id(id)
    #Datos Medico Profesional     
    medico = medico_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('temp_psicologia/hc_psicologia.html', entidad = entidad, logo = logo, paciente = paciente, registro = registro, medico = medico, firma = firma)
    return render_pdf(HTML(string = html)) 
