from flask import Blueprint, request, jsonify
import requests

bp_rda = Blueprint('rda', __name__)

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