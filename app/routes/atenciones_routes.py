from flask import Blueprint, render_template, request, jsonify
from app.services import consultas_service, hospitalizacion_service, ufuncionales_service
import mysql.connector.errors as error

bp_atenciones = Blueprint('atenciones', __name__)

""" @bp_atenciones.get('/atenciones/<medico>')
def atenciones(medico):
    try:
        atenciones = consultas_service.listar_consultas_med(medico)
        return render_template('temp_atenciones/atenciones.html', atenciones = atenciones)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('atenciones.atenciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('atenciones.atenciones')) """

@bp_atenciones.get('/atenciones')
def atenciones():
    return render_template('temp_atenciones/atenciones.html')

#Ruta AJAX para traer todas las atenciones por medico y fecha (Jquery)
""" @bp_atenciones.post('/get_atenciones')
def ajax():
    if request.method == 'POST':
        medico = request.form["medico"]
        fecha_atencion = request.form["fecha_atencion"]
        
        atenciones = consultas_service.listar_consultas_med(medico, fecha_atencion)
        return render_template('temp_atenciones/tabla_atenciones.html', atenciones = atenciones) """

#Ruta AJAX para traer todas las atenciones por medico y fecha
@bp_atenciones.post('/getAtencionesConsulta')
def getAtencionesConsulta():
    try:
        data = request.get_json()
        medico = data.get("medico")
        fecha_atencion = data.get("fecha_atencion")
        atenciones = consultas_service.listar_consultas_med(medico, fecha_atencion)
        if(atenciones):
            return jsonify(atenciones), 200
        else:
            return jsonify({"Error": "No se encontraron registros."}), 200
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500

    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500    

@bp_atenciones.get('/atenciones_hosp')
def atenciones_hosp():
    unidades = ufuncionales_service.listar_ufuncionales_hosp()
    return render_template('temp_atenciones/atenciones_hosp.html', unidades = unidades)

#Ruta AJAX para traer todas las atenciones por unidad funcional Hosp. (JQuery)
""" @bp_atenciones.post('/get_atenciones_hosp')
def get_atenciones_hosp():
    if request.method == 'POST':
        un_funcional = request.form["un_funcional"]

        atenciones = hospitalizacion_service.listar_atenciones_hosp(un_funcional)
        return render_template('temp_atenciones/tabla_atenciones_hosp.html', atenciones = atenciones) """

#Ruta AJAX para traer todas las atenciones por und. funcional Hosp. (API Fetch)
@bp_atenciones.post('/getAtencionesHosp')
def getAtencionesHosp():
    try:
        data = request.get_json()
        un_funcional = data.get("un_funcional")
        atenciones = hospitalizacion_service.listar_atenciones_hosp(un_funcional)
        if atenciones:
            return jsonify(atenciones), 200
        else:
            return jsonify({"Error": "No se encontraron registros."}), 200

    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500
    
    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500