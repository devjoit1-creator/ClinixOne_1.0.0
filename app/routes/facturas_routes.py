from flask import Blueprint, render_template, request, redirect, url_for, flash, make_response, jsonify
from app.services import facturas_service, consultas_service, fuentes_service, consecutivo_service, terceros_service, servicios_service, reportes_service, paciente_service, hospitalizacion_service, resfacturacion_service
from flask_weasyprint import render_pdf, HTML
from io import BytesIO
from datetime import datetime
import base64
import mysql.connector.errors as error
import requests
import json

bp_facturas = Blueprint('facturas', __name__)

#Ruta Ventana Principal de Facturas
@bp_facturas.get('/facturas')
def facturas():
    registros = facturas_service.listar_facturas()
    return render_template('temp_facturas/facturas.html', registros = registros)

#Ruta Ventana Nueva Factura General (En Proceso)
@bp_facturas.get('/add_factura')
def add_factura():
    fuentes = fuentes_service.listar_fuente_fe()
    consecutivo = consecutivo_service.listar_consecutivo_fev()
    terceros = terceros_service.listar_terceros()
    servicios = servicios_service.listar_servicios()
    return render_template('temp_facturas/add_factura.html', fuentes = fuentes, consecutivo = consecutivo, terceros = terceros, servicios = servicios)

#Ruta POST para procesar formulario de agregar nueva factura en bd desde Consulta.
@bp_facturas.post('/f_addFacturaConsulta')
def f_addFacturaConsulta():
    try:
        if request.method == 'POST':
            """ Request para insert de la factura """
            ambito_factura = request.form["ambito_factura"]
            cod_fuente = request.form["cod_fuente"]
            nro_factura = request.form["nro_factura"]
            fecha = request.form["fecha"]
            hora = request.form["hora"]
            codigo = request.form["codigo"]
            nombre = request.form["nombre"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            correo = request.form["correo"]
            atencion = request.form["atencion"]
            cod_admin = request.form["cod_admin"]
            nit_admin = request.form["nit_admin"]
            nom_admin = request.form["nom_admin"]
            observacion = request.form["observacion"]
            valor_bruto = request.form["valor_bruto"]
            descuento = request.form["descuento"]
            copago = request.form["copago"]
            subtotal_factura = request.form["subtotal_factura"]
            iva = request.form["iva"]
            valor_neto = request.form["valor_neto"]
            usuario = request.form["usuario"]

            facturas_service.insert_factura(ambito_factura, cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo, atencion, cod_admin, nit_admin,
                                            nom_admin, observacion, valor_bruto, descuento, copago, subtotal_factura, iva, valor_neto, usuario)

            """ Request para insert de los servicios/detalles de la factura """
            numero_fact = request.form["nro_factura"]
            data = request.form.get("data")
            filas = data.split(';')
            for fila in filas:
                if fila.strip():
                    u_funcional, cod_serv, nom_serv, valor_serv, cantidad, total_serv = fila.split('-')
                    u_funcional_fila = u_funcional.strip()
                    cod_serv_fila = cod_serv.strip()
                    nom_serv_fila = nom_serv.strip()
                    valor_serv_fila = valor_serv.strip()
                    cantidad_fila = cantidad.strip()
                    total_serv_fila = total_serv.strip()

                    facturas_service.insert_detalle_factura_consulta(u_funcional_fila, cod_serv_fila, nom_serv_fila, valor_serv_fila, cantidad_fila, total_serv_fila, numero_fact)

            """ Request para actualizar datos de factura en tabla consultas """
            consultas_service.update_datosFactura_consulta(cod_fuente, numero_fact, valor_neto, atencion)

            flash(f"Factura No. {nro_factura} Generada Exitosamente", "success")
            return redirect(url_for('consultas.consultas'))     

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('consultas.consultas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('consultas.consultas'))

#Ruta POST para procesar formulario de agregar nueva factura en bd desde Hospitalización.
@bp_facturas.post('/f_addFacturaHosp')
def f_addFacturaHosp():
    try:
        if request.method == 'POST':
            """ Request para insert de la factura """
            ambito_factura = request.form["ambito_factura"]
            cod_fuente = request.form["cod_fuente"]
            nro_factura = request.form["nro_factura"]
            fecha = request.form["fecha"]
            hora = request.form["hora"]
            codigo = request.form["codigo"]
            nombre = request.form["nombre"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            correo = request.form["correo"]
            atencion = request.form["atencion"]
            cod_admin = request.form["cod_admin"]
            nit_admin = request.form["nit_admin"]
            nom_admin = request.form["nom_admin"]
            observacion = request.form["observacion"]
            valor_bruto = request.form["valor_bruto"]
            descuento = request.form["descuento"]
            copago = request.form["copago"]
            subtotal_factura = request.form["subtotal_factura"]
            iva = request.form["iva"]
            valor_neto = request.form["valor_neto"]
            usuario = request.form["usuario"]

            facturas_service.insert_factura(ambito_factura, cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo, atencion, cod_admin, nit_admin,
                                            nom_admin, observacion, valor_bruto, descuento, copago, subtotal_factura, iva, valor_neto, usuario)

            """ Request para insert de los servicios/detalles de la factura """
            numero_fact = request.form["nro_factura"]
            data = request.form.get("data")
            filas = data.split(';')
            for fila in filas:
                if fila.strip():
                    u_funcional, cod_serv, nom_serv, valor_serv, cantidad, total_serv = fila.split('-')
                    u_funcional_fila = u_funcional.strip()
                    cod_serv_fila = cod_serv.strip()
                    nom_serv_fila = nom_serv.strip()
                    valor_serv_fila = valor_serv.strip()
                    cantidad_fila = cantidad.strip()
                    total_serv_fila = total_serv.strip()

                    facturas_service.insert_detalle_factura_consulta(u_funcional_fila, cod_serv_fila, nom_serv_fila, valor_serv_fila, cantidad_fila, total_serv_fila, numero_fact)

            """ Request para actualizar datos de factura en tabla consultas """
            hospitalizacion_service.update_datosFactura_hospitalizacion(cod_fuente, numero_fact, valor_neto, atencion)

            flash(f"Factura No. {nro_factura} Generada Exitosamente", "success")
            return redirect(url_for('hospitalizacion.hospitalizacion'))     

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('hospitalizacion.hospitalizacion'))


#Ruta POST para procesar formulario de agregar nueva factura en bd desde Facturas. (En proceso)
@bp_facturas.post('/f_addFactura')
def f_addFactura():
    try:
        if request.method == 'POST':
            """ Request para insert de la factura """
            cod_fuente = request.form["cod_fuente"]
            fecha = request.form["fecha"]
            hora = request.form["hora"]
            codigo = request.form["codigo"]
            nombre = request.form["nombre"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            correo = request.form["correo"]
            valor_bruto = request.form["valor_bruto"]
            descuento = request.form["descuento"]
            subtotal_factura = request.form["subtotal_factura"]
            iva = request.form["iva"]
            valor_neto = request.form["valor_neto"]
            usuario = request.form["usuario"]

            facturas_service.insert_factura_bd(cod_fuente, fecha, hora, codigo, nombre, direccion, telefono, correo,
                                             valor_bruto, descuento, subtotal_factura, iva, valor_neto, usuario)
            

            """ Request para insert de los servicios/detalles de la factura """
            id_factura = request.form["id_factura"]
            data = request.form.get("data")
            filas = data.split(';')
            for fila in filas:
                if fila.strip():
                    cod_serv, nom_serv, valor_serv, cantidad, total_serv = fila.split('-')
                    cod_serv_fila = cod_serv.strip()
                    nom_serv_fila = nom_serv.strip()
                    valor_serv_fila = valor_serv.strip()
                    cantidad_fila = cantidad.strip()
                    total_serv_fila = total_serv.strip()

                    facturas_service.insert_detalle_factura(cod_serv_fila, nom_serv_fila, valor_serv_fila, cantidad_fila, total_serv_fila, id_factura)

            flash(f"Factura {cod_fuente} {id_factura} Generada Exitosamente", "success")
            return redirect(url_for('facturas.facturas')) 

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('facturas.facturas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('facturas.facturas'))

#Ruta Reporte PDF factura Interno (Esbozo)    
@bp_facturas.get('/reporte_factura/<int:id>')
def reporte_factura(id):
    #Herencia encabezado reportes
    entidad = reportes_service.listar_datos_entidad()

    #Datos de Factura
    factura = facturas_service.listar_factura_id(id)
    #Datos de detalle de la Factura
    detalle = facturas_service.listar_detalle_factura_id(id)
    
    imagen = BytesIO(entidad[6])
    if imagen:
        logo = base64.b64encode(imagen.read()).decode('utf-8')

    html = render_template('temp_facturas/rp_factura.html', entidad = entidad, logo = logo, factura = factura, detalle = detalle)
    return render_pdf(HTML(string = html))

#Ruta Ventana Emitir Facturación Electronica Masiva
@bp_facturas.get('/emitir_facturas')
def emitir_facturas():
    return render_template('temp_facturas/emitir_facturas.html')

#Ruta AJAX para obtener facturas para emitir
@bp_facturas.post('/get_facturas')
def get_facturas():
    data = request.get_json()
    fecha_inicio = data.get("fecha_inicio", "")
    fecha_fin = data.get("fecha_fin", "")
    facturas = facturas_service.listar_facturas_fechas(fecha_inicio, fecha_fin)
    
    if facturas:
        return jsonify(facturas)
    
    else: 
        return jsonify({"Error": "No se encontraron facturas."})

#Ruta Prueba EndPoint GET
@bp_facturas.get('/getAPI/<int:id>')
def getAPI(id):
    resultado = facturas_service.json_factura(id)    
    return json.dumps(resultado, indent=2)
    

#Ruta Prueba EndPoint Dataico Prueba 1
@bp_facturas.post('/pruebaAPI/<int:id>')
def pruebaAPI(id):
    try:
        url_ex = "https://api.dataico.com/direct/dataico_api/v2/invoices"
        payload = facturas_service.json_factura(id)
        resolucion = resfacturacion_service.listar_resfacturacion_fe()
        headers = {
            "Content-Type": "application/json",
            "Auth-token": resolucion[0]
        }
        
        respuesta = requests.post(url_ex, json=payload, headers=headers)

        return jsonify({
            "estado": respuesta.status_code,
            "respuesta": respuesta.json()
        })

    except requests.exceptions.RequestException as error:
        return jsonify({'error': f'Error en la solicitud externa: {str(error)}'}), 500
    
    except Exception as ex: 
        return jsonify({"error": str(ex)}), 500
    
# Ruta AJAX Endpoint Dataico Prueba 2
@bp_facturas.post('/send_facturas')
def send_facturas():
    data = request.get_json()
    nro_factura = data.get("id", "")
    try:
        url_ex = "https://api.dataico.com/direct/dataico_api/v2/invoices"
        payload = facturas_service.json_factura(nro_factura)
        resolucion = resfacturacion_service.listar_resfacturacion_fe()
        headers = {
            "Content-Type": "application/json",
            "Auth-token": resolucion[0]
        }
        
        respuesta = requests.post(url_ex, json=payload, headers=headers)

        if respuesta.status_code == 201:
            data_fe = respuesta.json()
            """ Formatear fecha json """
            fecha_json = data_fe.get("issue_date")
            fecha_objeto = datetime.strptime(fecha_json, "%d/%m/%Y %H:%M:%S")
            """ Update datos FE """
            fe_uuid = data_fe.get("uuid")
            fe_cufe = data_fe.get("cufe")
            fe_issue_date = fecha_objeto.strftime("%Y-%m-%d")
            fe_issue_time = fecha_objeto.strftime("%H:%M")
            fe_pdf_url = data_fe.get("pdf_url")
            fe_xml_url = data_fe.get("xml_url")
            facturas_service.update_campos_fe(fe_uuid, fe_cufe, fe_issue_date, fe_issue_time, fe_pdf_url, fe_xml_url, nro_factura)

        return jsonify({
            "estado": respuesta.status_code,
            "respuesta": respuesta.json()                
        }), respuesta.status_code

    except requests.exceptions.RequestException as error:
        return jsonify({'error': f'Error en la solicitud externa: {str(error)}'}), 500
    
    except Exception as ex: 
        return jsonify({"error": str(ex)}), 500