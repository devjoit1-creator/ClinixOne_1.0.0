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