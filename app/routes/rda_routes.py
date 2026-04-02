from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, json
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
        clientid = request.form["clientid"]
        clientsecret = request.form["clientsecret"]
        tenantid = request.form["tenantid"]
        scope = request.form["scope"]
        subskey = request.form["subskey"]

        rda_service.insert_parametrorda(ambiente, clientid, clientsecret, tenantid, scope, subskey)
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
        #Obtener datos de parametro
        parametros = rda_service.listar_parametrosrda_prueba()

        #Parametros Consumo API IHCE
        clientid = str(parametros[0])
        clientsecret = str(parametros[1])
        tenantid = str(parametros[2])
        scope = str(parametros[3])
        subskey = str(parametros[4])

        #API IHCE Obtener Token
        ep_token = f"https://login.microsoftonline.com/{tenantid}/oauth2/v2.0/token"
        headers_token = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body_token = {
            "grant_type": "client_credentials",
            "client_id": clientid,
            "client_secret": clientsecret,
            "scope": scope
        }
 
        respuesta_token = requests.post(url=ep_token, headers=headers_token, data=body_token)
        if respuesta_token.status_code != 200:
            return jsonify({
                "Error": "Error al obtener token",
                "Detalle": respuesta_token.text
            }), respuesta_token.status_code
        
        #Parametros Consumo Envio RDA
        data = respuesta_token.json()    
        token = data.get('access_token')
        if not token:
            return jsonify({"Error": "No se obtuvo Token"}), 500
        

        #API IHCE Envio RDA
        ep_envio = "https://vulcano.ihcecol.gov.co/api/Composition/$enviar-rda-paciente"
        headers_envio = {
            "Authorization": f"Bearer {token}",
            "Ocp-Apim-Subscription-Key": subskey,
            "Content-Type": "application/fhir+json"
        }

        payload = {
            "resourceType": "Bundle",
            "type": "document",
            "timestamp": "2026-03-06T15:38:00-05:00",
            "entry": [
                {
                "fullUrl": "urn:uuid:64536675-7461-4649-807c-974242130001",
                "resource": {
                    "resourceType": "Composition",
                    "id": "RDA-2026-001",
                    "status": "final",
                    "type": {
                    "coding": [
                        {
                        "system": "http://loinc.org",
                        "code": "11488-4",
                        "display": "Consultation Note"
                        }
                    ],
                    "text": "Resumen Digital de Atención (RDA)"
                    },
                    "subject": { "reference": "Patient/CC-1140839950" },
                    "date": "2026-03-06T15:38:00-05:00",
                    "author": [
                    {
                        "reference": "Practitioner/CC-72428280",
                        "display": "Darwin Garcia"
                    }
                    ],
                    "title": "Resumen de Atención Médica",
                    "custodian": { "reference": "Organization/NIT-901001375" },
                    "section": [
                    {
                        "title": "Motivo de consulta",
                        "code": {
                        "coding": [{ "system": "http://loinc.org", "code": "46239-0" }]
                        },
                        "text": {
                        "status": "generated",
                        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Paciente refiere dolor abdominal agudo...</div>"
                        }
                    },
                    {
                        "title": "Diagnósticos",
                        "entry": [{ "reference": "Condition/diag-001" }]
                    }
                    ]
                }
                },
                {
                "fullUrl": "urn:uuid:64536675-7461-4649-807c-974242130002",
                "resource": {
                    "resourceType": "Patient",
                    "id": "CC-1140839950",
                    "identifier": [
                    {
                        "use": "official",
                        "type": {
                        "coding": [
                            {
                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                            "code": "CC"
                            }
                        ]
                        },
                        "system": "https://www.sispro.gov.co/get-identificacion-paciente",
                        "value": "1140839950"
                    }
                    ],
                    "name": [{ "family": "Orozco", "given": ["Julio", "Manuel"] }],
                    "gender": "male",
                    "birthDate": "1991-04-20",
                    "address": [{ "city": "Barranquilla", "country": "CO" }]
                }
                },
                {
                "fullUrl": "urn:uuid:64536675-7461-4649-807c-974242130005",
                "resource": {
                    "resourceType": "Practitioner",
                    "id": "CC-72428280",
                    "identifier": [
                    {
                        "system": "https://www.sispro.gov.co/get-identificacion-talento-humano",
                        "value": "72428280"
                    }
                    ],
                    "name": [{ "family": "Garcia", "given": ["Darwin"] }]
                }
                },
                {
                "fullUrl": "urn:uuid:64536675-7461-4649-807c-974242130003",
                "resource": {
                    "resourceType": "Organization",
                    "id": "NIT-901001375",
                    "identifier": [
                    {
                        "system": "https://www.sispro.gov.co/get-identificacion-ips",
                        "value": "901001375"
                    }
                    ],
                    "name": "PROSPERIDAD IPS S.A.S."
                }
                },
                {
                "fullUrl": "urn:uuid:64536675-7461-4649-807c-974242130004",
                "resource": {
                    "resourceType": "Condition",
                    "id": "diag-001",
                    "clinicalStatus": {
                    "coding": [
                        {
                        "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                        "code": "active"
                        }
                    ]
                    },
                    "verificationStatus": {
                    "coding": [
                        {
                        "system": "http://terminology.hl7.org/CodeSystem/condition-verif",
                        "code": "confirmed"
                        }
                    ]
                    },
                    "code": {
                    "coding": [
                        {
                        "system": "http://hl7.org/fhir/sid/icd-10",
                        "code": "K358",
                        "display": "Apendicitis aguda"
                        }
                    ]
                    },
                    "subject": { "reference": "Patient/CC-1140839950" }
                }
                }
            ]
            }

        respuesta_envio = requests.post(url=ep_envio, headers=headers_envio, json=payload, timeout=30)
        try:
            respuesta_final = respuesta_envio.json()
        except Exception:
            respuesta_final = respuesta_envio.text    
    
        return jsonify({
            "estado": respuesta_envio.status_code,
            "resultado": respuesta_final
        }), respuesta_envio.status_code

    except requests.exceptions.RequestException as error:
        return jsonify({"Error": f"Error en la solicitud externa: {str(error)}"}), 500
    
    except Exception as ex:
        return jsonify({"Error": str(ex)}), 500