from flask import Blueprint, render_template, request, jsonify, send_file
from app.services import administradoras_service, rips_service
import mysql.connector.errors as error
from io import BytesIO
import zipfile
import json

bp_rips = Blueprint('rips', __name__)

#Ruta Ventana Generar Rips
@bp_rips.get('/rips')
def rips():
    admin = administradoras_service.listar_administradoras_modal();
    return render_template('temp_rips/generar_rips.html', admin = admin)

#Ruta AJAX para obtener las facturas para generar rips
@bp_rips.post('/get_facturas_rips')
def get_facturas_rips():
    data = request.get_json()
    fecha_inicio = data.get("fecha_inicio", "")
    fecha_fin = data.get("fecha_fin", "") 
    administradora = data.get("administradora", "")
    facturas = rips_service.listar_facturas_rips(fecha_inicio, fecha_fin, administradora)
    
    if facturas:
        return jsonify(facturas)
    
    else: 
        return jsonify({"Error": "No se encontraron facturas."})
    
#Ruta Prueba Obtener JSON del RIPS
@bp_rips.get('/get_json_rips/<nro_factura>')
def get_json_rips(nro_factura):
    json_rips = rips_service.json_rips(nro_factura)
    return jsonify(json_rips) #json.dumps(json_rips, indent=2)

#Ruta Para generar archivos .json rips
""" @bp_rips.post('/send_json_rips')
def send_json_rips():
    data = request.get_json()
    nro_factura = data.get("id", "")
    try:
        json_rips = rips_service.json_rips(nro_factura)
        response = make_response(json.dumps(json_rips, indent=2))
        #Encabezados
        response.headers['Content-Type'] = "application/json"
        response.headers['Content-Disposition'] = f"attachment; filename=FE{nro_factura}.json"

        return response

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500 """
    
#Ruta para generar archivos .json y comprimirlos en .zip
@bp_rips.post('/send_json_rips')
def send_json_rips():
    data = request.get_json()
    facturas = data.get("ids", [])
    try:
        #Buffer para los .zip
        zip_buffer = BytesIO()

        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for nro_factura in facturas:
                json_rips = rips_service.json_rips(nro_factura)
                json_bytes = json.dumps(json_rips, indent=2).encode("utf-8")
                filename = f"FE{nro_factura}.json"
                zip_file.writestr(filename, json_bytes)

        zip_buffer.seek(0)

        return send_file(zip_buffer, mimetype="applitation/zip", as_attachment=True, download_name="RIPS_facturas.zip")
    
    except Exception as ex:
        return jsonify({"error", str(ex)}), 500