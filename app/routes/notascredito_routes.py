from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import fuentes_service, consecutivo_service, facturas_service, notascredito_service, resfacturacion_service
import mysql.connector.errors as error
import json
import requests
import datetime

bp_notascredito = Blueprint('notascredito', __name__)

#Ruta Ventana Principal de Notas de Credito
@bp_notascredito.get('/notas_credito')
def notas_credito():
    notas = notascredito_service.listar_notascredito()
    return render_template('temp_notascredito/notas_credito.html', notas = notas)

#Ruta Ventana Nueva Nota de Credito
@bp_notascredito.get('/add_notacredito')
def add_notacredito():
    fuentes = fuentes_service.listar_fuente_nc()
    consecutivo = consecutivo_service.listar_coonsecutivo_ncc()
    return render_template('temp_notascredito/add_notacredito.html', fuentes = fuentes, consecutivo = consecutivo)

#Ruta AJAX para obtener factura a la que se aplicará la nota de Credito
@bp_notascredito.post('/get_factura_nc')
def get_factura_nc():
    data = request.get_json()
    nro_factura = data.get("nro_factura", "")
    factura = facturas_service.listar_factura_nc(nro_factura)

    if factura:
        return jsonify(factura)
    
#Ruta Metodo para Guardar la nota de credito en bd
@bp_notascredito.post('/f_addNotaCredito')
def f_addNotaCredito():
    try:
        #Request para los datos de la nota de credito
        cod_fuente = request.form["cod_fuente"]
        nro_notacredito = request.form["nro_notacredito"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        cod_fte_factura = request.form["cod_fte_factura"]
        factura = request.form["nro_factura"]
        fe_uuid = request.form["fe_uuid"]
        motivo_notacredito = request.form["motivo_notacredito"]

        #Llamado al controlador del Insert de nota de credito en bd
        notascredito_service.insert_notacredito(cod_fuente, nro_notacredito, fecha, hora, cod_fte_factura, factura, fe_uuid, motivo_notacredito)
        
        flash(f"Nota Credito No. {nro_notacredito} creada exitosamente.", "success")
        return redirect(url_for('notascredito.notas_credito'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('notascredito.notas_credito'))
    
    except Exception as ex:
       flash(f"Se presentó un error inesperado: {ex}", "error")
       return redirect(url_for('notascredito.notas_credito'))
    
#Ruta Prueba Obtener JSON de nota credito
@bp_notascredito.get('/get_json_notacredito/<nro_notacredito>')
def get_json_notacredito(nro_notacredito):
    json_notacredito = notascredito_service.json_notacredito(nro_notacredito)
    return json.dumps(json_notacredito, indent=2)

#Ruta AJAX Prueba Emitir Nota de Credito Consumo API
@bp_notascredito.post('/send_notacredito')
def send_notacredito():
    data = request.get_json()
    nro_notacredito = data.get("nro_notacredito")
    try:
        url_ex = "https://api.dataico.com/direct/dataico_api/v2/credit_notes"
        payload = notascredito_service.json_notacredito(nro_notacredito)
        resolucion = resfacturacion_service.listar_resfacturacion_fe()
        headers = {
            "Content-Type": "application/json",
            "Auth-token": resolucion[0]
        }

        respuesta = requests.post(url_ex, json=payload, headers=headers)

        if respuesta.status_code == 201:
            data_nc = respuesta.json()
            #Formatear fecha json
            fecha_json = data_nc.get("issue_date")
            #fecha_objeto = datetime.strptime(fecha_json, "%d/%m/%Y %H:%M:%S")
            #Update datos FE
            nc_uuid = data_nc.get("uuid")
            nc_cufe = data_nc.get("cufe")
            nc_issue_date = data_nc.get("issue_date")
            nc_pdf_url = data_nc.get("pdf_url")
            nc_xml_url = data_nc.get("xml_url")
            notascredito_service.update_campos_nc(nc_uuid, nc_cufe, nc_issue_date, nc_pdf_url, nc_xml_url, nro_notacredito)

        return jsonify({
            "estado": respuesta.status_code,
            "respuesta": respuesta.json()                
        }), respuesta.status_code
    
    except requests.exceptions.RequestException as error:
        return jsonify({'error': f'Error en la solicitud externa: {str(error)}'}), 500

    except Exception as ex: 
        return jsonify({"error": str(ex)}), 500