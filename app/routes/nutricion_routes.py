from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_weasyprint import HTML, render_pdf
from app.services import nutricion_service, paciente_service, medico_service, diagnosticos_cie10, reportes_service
from io import BytesIO
import base64
import mysql.connector.errors as error

bp_nutricion = Blueprint('nutricion', __name__)

@bp_nutricion.get('/nutricion/<atencion>/<paciente>')
def nutricion(atencion, paciente):
    medico = session['document']
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    registros = nutricion_service.listar_hc_nutricion(paciente, medico)
    return render_template('temp_nutricion/nutricion.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, registros = registros)

@bp_nutricion.get('/add_regnutricion/<atencion>/<paciente>')
def add_regnutricion(atencion, paciente):
    dato_pac = paciente_service.listar_paciente_doc(paciente)
    diagnosticos = diagnosticos_cie10.listar_diagnosticos()
    return render_template('temp_nutricion/add_regnutricion.html', atencion = atencion, paciente = paciente, dato_pac = dato_pac, diagnosticos = diagnosticos)

@bp_nutricion.post('/f_addRegNutricion')
def f_addRegNutricion():
    try:
        paciente = request.form["codigo"]
        medico = request.form["medico"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        motivo_consulta = request.form["motivo_consulta"]
        enf_actual = request.form["enf_actual"]
        antper_diarrea = request.form["antper_diarrea"]
        antper_estrenimiento = request.form["antper_estrenimiento"]
        antper_gastritis = request.form["antper_gastritis"]
        antper_ulcera = request.form["antper_ulcera"]
        antper_nausea = request.form["antper_nausea"]
        antper_pirosis = request.form["antper_pirosis"]
        antper_vomito = request.form["antper_vomito"]
        antper_colitis = request.form["antper_colitis"]
        antper_otro = request.form["antper_otro"]
        antper_otro_cual = request.form["antper_otro_cual"]
        antper_dentadura = request.form["antper_dentadura"]
        antper_protesis = request.form["antper_protesis"]
        antper_observaciones = request.form["antper_observaciones"]
        padece_enf = request.form["padece_enf"]
        padece_enf_cual = request.form["padece_enf_cual"]
        enf_importante = request.form["enf_importante"]
        enf_importante_cual = request.form["enf_importante_cual"]
        toma_medicamento = request.form["toma_medicamento"]
        toma_medicamento_cual = request.form["toma_medicamento_cual"]
        toma_medicamento_dosis = request.form["toma_medicamento_dosis"]
        toma_laxantes = request.form["toma_laxantes"]
        toma_diureticos = request.form["toma_diureticos"]
        toma_antiacidos = request.form["toma_antiacidos"]
        toma_analgesicos = request.form["toma_analgesicos"]
        practica_cirugia = request.form["practica_cirugia"]
        practica_cirugia_cual = request.form["practica_cirugia_cual"]
        antfam_obesidad = request.form["antfam_obesidad"]
        antfam_obesidad_parent = request.form["antfam_obesidad_parent"]
        antfam_diabetes = request.form["antfam_diabetes"]
        antfam_diabetes_parent = request.form["antfam_diabetes_parent"]
        antfam_cancer = request.form["antfam_cancer"]
        antfam_cancer_parent = request.form["antfam_cancer_parent"]
        antfam_hta = request.form["antfam_hta"]
        antfam_hta_parent = request.form["antfam_hta_parent"]
        antfam_hipercolesterolemia = request.form["antfam_hipercolesterolemia"]
        antfam_hipercolesterolemia_parent = request.form["antfam_hipercolesterolemia_parent"]
        antfam_hipertrigliceridemia = request.form["antfam_hipertrigliceridemia"]
        antfam_hipertrigliceridemia_parent = request.form["antfam_hipertrigliceridemia_parent"]
        desayuno_alimentos = request.form["desayuno_alimentos"]
        desayuno_tiempo = request.form["desayuno_tiempo"]
        mediamanana_alimentos = request.form["mediamanana_alimentos"]
        mediamanana_tiempo = request.form["mediamanana_tiempo"]
        almuerzo_alimentos = request.form["almuerzo_alimentos"]
        almuerzo_tiempo = request.form["almuerzo_tiempo"]
        mediatarde_alimentos = request.form["mediatarde_alimentos"]
        mediatarde_tiempo = request.form["mediatarde_tiempo"]
        cena_alimentos = request.form["cena_alimentos"]
        cena_tiempo = request.form["cena_tiempo"]
        aerobicos = request.form["aerobicos"]
        aerobicos_frecuencia = request.form["aerobicos_frecuencia"]
        aerobicos_duracion = request.form["aerobicos_duracion"]
        anaerobicos = request.form["anaerobicos"]
        anaerobicos_frecuencia = request.form["anaerobicos_frecuencia"]
        anaerobicos_duracion = request.form["anaerobicos_duracion"]
        musculatura = request.form["musculatura"]
        musculatura_frecuencia = request.form["musculatura_frecuencia"]
        musculatura_duracion = request.form["musculatura_duracion"]
        alcohol = request.form["alcohol"]
        alcohol_frecuencia = request.form["alcohol_frecuencia"]
        alcohol_cantidad = request.form["alcohol_cantidad"]
        tabaco = request.form["tabaco"]
        tabaco_frecuencia = request.form["tabaco_frecuencia"]
        tabaco_cantidad = request.form["tabaco_cantidad"]
        cafe = request.form["cafe"]
        cafe_frecuencia = request.form["cafe_frecuencia"]
        cafe_cantidad = request.form["cafe_cantidad"]
        signo_cabello = request.form["signo_cabello"]
        signo_ojos = request.form["signo_ojos"]
        signo_piel = request.form["signo_piel"]
        signo_unas = request.form["signo_unas"]
        signo_labios = request.form["signo_labios"]
        signo_encias = request.form["signo_encias"]
        alimentos_preferidos = request.form["alimentos_preferidos"]
        alimentos_noagradan = request.form["alimentos_noagradan"]
        alimentos_malestar = request.form["alimentos_malestar"]
        alergico = request.form["alergico"]
        alergico_cual = request.form["alergico_cual"]
        peso_habitual = request.form["peso_habitual"]
        peso_actual = request.form["peso_actual"]
        estatura = request.form["estatura"]
        imc = request.form["imc"]
        circunferencia_brazo = request.form["circunferencia_brazo"]
        circunferencia_cintura = request.form["circunferencia_cintura"]
        cod_diag1 = request.form["cod_diag1"]
        nom_diag1 = request.form["nom_diag1"]
        cod_diag2 = request.form["cod_diag2"]
        nom_diag2 = request.form["nom_diag2"]
        cod_diag3 = request.form["cod_diag3"]
        nom_diag3 = request.form["nom_diag3"]
        cod_diag4 = request.form["cod_diag4"]
        nom_diag4 = request.form["nom_diag4"]
        plan_trata = request.form["plan_trata"]
        atencion = request.form["atencion"]

        nutricion_service.insert_hcnutricion(paciente, medico, fecha, hora, motivo_consulta, enf_actual, antper_diarrea, antper_estrenimiento, antper_gastritis,
                                                antper_ulcera, antper_nausea, antper_pirosis, antper_vomito, antper_colitis, antper_otro, antper_otro_cual, antper_dentadura,
                                                antper_protesis, antper_observaciones, padece_enf, padece_enf_cual, enf_importante, enf_importante_cual, toma_medicamento, toma_medicamento_cual,
                                                toma_medicamento_dosis, toma_laxantes, toma_diureticos, toma_antiacidos, toma_analgesicos, practica_cirugia, practica_cirugia_cual, antfam_obesidad,
                                                antfam_obesidad_parent, antfam_diabetes, antfam_diabetes_parent, antfam_cancer, antfam_cancer_parent, antfam_hta, antfam_hta_parent,
                                                antfam_hipercolesterolemia, antfam_hipercolesterolemia_parent, antfam_hipertrigliceridemia, antfam_hipertrigliceridemia_parent, desayuno_alimentos, desayuno_tiempo,
                                                mediamanana_alimentos, mediamanana_tiempo, almuerzo_alimentos, almuerzo_tiempo, mediatarde_alimentos, mediatarde_tiempo, cena_alimentos, cena_tiempo,
                                                aerobicos, aerobicos_frecuencia, aerobicos_duracion, anaerobicos, anaerobicos_frecuencia, anaerobicos_duracion, musculatura, musculatura_frecuencia,
                                                musculatura_duracion, alcohol, alcohol_frecuencia, alcohol_cantidad, tabaco, tabaco_frecuencia, tabaco_cantidad, cafe, cafe_frecuencia, cafe_cantidad,
                                                signo_cabello, signo_ojos, signo_piel, signo_unas, signo_labios, signo_encias, alimentos_preferidos, alimentos_noagradan, alimentos_malestar, alergico,
                                                alergico_cual, peso_habitual, peso_actual, estatura, imc, circunferencia_brazo, circunferencia_cintura, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3,
                                                cod_diag4, nom_diag4, plan_trata, atencion)
        
        flash(f"Historia Clinica de Nutrición asociada exitosamente a la atención: {atencion}", "success")
        return redirect(url_for('nutricion.nutricion', atencion = atencion, paciente = paciente))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('nutricion.nutricion', atencion = atencion, paciente = paciente))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('nutricion.nutricion', atencion = atencion, paciente = paciente))
    
@bp_nutricion.get('/view_regnutricion/<int:id>/')
def view_regnutricion(id):
    registro = nutricion_service.listar_hc_nutricion_id(id)
    dato_pac = paciente_service.listar_paciente_doc(registro[1])
    return render_template('temp_nutricion/view_regnutricion.html', registro = registro, dato_pac = dato_pac)

@bp_nutricion.get('/hc_nutricion/<idpac>/<int:id>/<idmed>')
def hc_nutricion(idpac, id, idmed):
     #Herencia encabezado reportes
    entidad = reportes_service.listar_datos_entidad()
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    #Datos de paciente
    paciente = paciente_service.listar_paciente_doc(idpac)
    #Datos de Atención por Nutricion
    registro = nutricion_service.listar_hc_nutricion_id(id)
    #Datos Medico Profesional     
    medico = medico_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('temp_nutricion/hc_nutricion.html', entidad = entidad, logo = logo, paciente = paciente, registro = registro, medico = medico, firma = firma)
    return render_pdf(HTML(string = html))     