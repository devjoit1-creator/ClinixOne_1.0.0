from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import paciente_service, epicrisis_service
import mysql.connector.errors as error

bp_epicrisis = Blueprint('epicrisis', __name__)

#Ruta Ventana Epicrisis
@bp_epicrisis.get('/epicrisis')
def epicrisis():
    return render_template('temp_epicrisis/epicrisis.html')

#Ruta Ventana Nueva Epicrisis
@bp_epicrisis.get('/add_epicrisis')
def add_epicrisis():
    pacientes = paciente_service.listar_pacientes_modal()
    return render_template('temp_epicrisis/add_epicrisis.html', pacientes = pacientes)

#Ruta Ajax para obtener las atenciones de consulta por paciente y medico
@bp_epicrisis.post('/getAtencionesConsultaEpicrisis')
def getAtencionesConsultaEpicrisis():
    try:
        data = request.get_json()
        paciente = data.get("paciente")
        medico = data.get("medico")
        atenciones = epicrisis_service.listar_atenciones_consulta_epicrisis(paciente, medico)
        if atenciones:
            return jsonify(atenciones), 200
        else:
            return jsonify({"Error": "No se encontraron registros."}), 200
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500

    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500 
    

#Ruta Ajax para obtener las atenciones de hosp. por paciente y medico
@bp_epicrisis.post('/getAtencionesHospEpicrisis')
def getAtencionesHospEpicrisis():
    try:
        data = request.get_json()
        paciente = data.get("paciente")
        medico = data.get("medico")
        atenciones = epicrisis_service.listar_atenciones_hosp_epicrisis(paciente, medico)
        if atenciones:
            return jsonify(atenciones), 200
        else:
            return jsonify({"Error": "No se encontraron registros."}), 200
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500

    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500
    
#Ruta Post para insertar nueva epicrisis
@bp_epicrisis.post('/f_addEpicrisis')
def f_addEpicrisis():
    try:
        codigo = request.form["codigo"]
        medico = request.form["medico"]
        atencion = request.form["atencion"]
        fecha_ingreso = request.form["fecha_ingreso"]
        hora_ingreso = request.form["hora_ingreso"]
        servicio_ingreso = request.form["servicio_ingreso"]
        fecha_salida = request.form["fecha_salida"]
        hora_salida = request.form["hora_salida"]
        servicio_salida = request.form["servicio_salida"]
        motivo_consulta = request.form["motivo_consulta"]
        enf_actual = request.form["enf_actual"]
        antecedentes = request.form["antecedentes"]
        examen_fisico = request.form["examen_fisico"]
        cod_diag_ingreso = request.form["cod_diag_ingreso"]
        nom_diag_ingreso = request.form["nom_diag_ingreso"]
        conducta = request.form["conducta"]
        cambio = request.form["cambio"]
        procedimientos = request.form["procedimientos"]
        justificacion = request.form["justificacion"]
        cod_diag_egreso = request.form["cod_diag_egreso"]
        nom_diag_egreso = request.form["nom_diag_egreso"]
        plan_manejo = request.form["plan_manejo"]
        estado_salida = request.form["estado_salida"]
        remitido_a = request.form["remitido_a"]

        epicrisis_service.insert_epriciris(codigo, medico, atencion, fecha_ingreso, hora_ingreso, servicio_ingreso, fecha_salida, hora_salida, servicio_salida,
                                           motivo_consulta, enf_actual, antecedentes, examen_fisico, cod_diag_ingreso, nom_diag_ingreso, conducta, cambio, procedimientos,
                                           justificacion, cod_diag_egreso, nom_diag_egreso, plan_manejo, estado_salida, remitido_a)

        flash("Epicrisis Creada Exitosamente", "success")
        return redirect(url_for('epicrisis.epicrisis'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('epicrisis.epicrisis'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('epicrisis.epicrisis'))