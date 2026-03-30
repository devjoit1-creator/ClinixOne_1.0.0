from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from app.services import rda_service
import mysql.connector.errors as error
import requests

bp_rda = Blueprint('rda', __name__)

#Ruta Ventana Parametros API RDA
@bp_rda.get('/transmisionRDA')
def transmisionRDA():
    parametros = rda_service.listar_parametrosrda()
    return render_template('temp_rda/parametros.html', parametros = parametros)

#Ruta Ventana Nuevo Parametro Transmisión RDA
@bp_rda.get('/add_parametro')
def add_parametro():
    return render_template('temp_rda/add_parametro.html')

#Ruta Metodo Guardar Nuevo Parametro RDA
@bp_rda.post('/f_addparametro')
def f_addparametro():
    try:
        ambiente = request.form["ambiente"]
        tenantid = request.form["tenantid"]
        scope = request.form["scope"]
        subskey = request.form["subskey"]

        rda_service.insert_parametrorda(ambiente, tenantid, scope, subskey)
        flash("Ambiente para transmisión de RDA Guardado Exitosamente", "success")
        return redirect(url_for('rda.transmisionRDA'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('rda.transmisionRDA'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for("rda.transmisionRDA"))

#Ruta Metodo Eliminar Parametro
@bp_rda.get('/drop_parametro/<int:id>')
def drop_parametro(id):
    try:
        rda_service.delete_parametrorda(id)
        flash("Ambiente para transmisión de RDA Eliminado Exitosamente", "success")
        return redirect(url_for('rda.transmisionRDA'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('rda.transmisionRDA'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('rda.transmisionRDA'))

@bp_rda.post('/enviar_rda_paciente')
def enviar_rda_paciente():
    try:
        endpoint = "https://sandbox.ihcecol.gov.co/ihce"
        headers = {
            "Authorization": "",
            "Ocp-Apim-Subscription-Key": "",
            "Content-Type": "application/fhir+json"
        }

        payload = {
            "resourceType": "Bundle",
            "type": "document",
            "entry": [{
               "resource":  "Patient",
               "identifier": [
                    {
                        "system": "https://registro.nacional/id",
                        "value": "800123456"
                    }
                ]
            }]
        }

        respuesta = requests.post(endpoint, headers=headers, json=payload)

        return jsonify({
            "estado": respuesta.status_code,
            "respuesta": respuesta.json()
        })
    
    except requests.exceptions.RequestException as error:
        return jsonify({"Error": f"Error en la solicitud externa: {str(error)}"}), 500
    
    except Exception as ex:
        return jsonify({"Error": str(ex)}), 500