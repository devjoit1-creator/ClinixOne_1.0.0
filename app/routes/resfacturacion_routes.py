from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import resfacturacion_service
import mysql.connector.errors as error
import json

bp_resfacturacion = Blueprint('resfacturacion', __name__)

#Ruta Ventana Principal Resoluciones de FE SS
@bp_resfacturacion.get('/resfacturacion')
def resfacturacion():
    resoluciones = resfacturacion_service.listar_resfacturacion()
    return render_template('temp_resfacturacion/resfacturacion.html', resoluciones = resoluciones)

#Ruta Ventana Nueva Resolución FE SS
@bp_resfacturacion.get('/add_resfacturacion')
def add_resfacturacion():
    return render_template('temp_resfacturacion/add_resfacturacion.html')

#Ruta POST Guardar Nueva Res. FE SS
@bp_resfacturacion.post('/f_addResFacturacion')
def f_addResFacturacion():
    try:
        nombre = request.form["nombre"]
        tipo_documento = request.form["tipo_documento"]
        estado_res = request.form["estado_res"]
        account_id = request.form["account_id"]
        auth_token = request.form["auth_token"]
        texto_encabezado = request.form["texto_encabezado"]
        numero_resolucion = request.form["numero_resolucion"]
        fecha_inicio = request.form["fecha_inicio"]
        fecha_fin = request.form["fecha_fin"]
        prefijo = request.form["prefijo"]
        numero_inicio = request.form["numero_inicio"]
        numero_fin = request.form["numero_fin"]
        encabezado = request.form["encabezado"]

        resfacturacion_service.insert_resfacturacion(nombre, tipo_documento, estado_res, account_id, auth_token, texto_encabezado, numero_resolucion, fecha_inicio, fecha_fin,
                                                        prefijo, numero_inicio, numero_fin, encabezado)
        
        flash("Resolución de Facturación Electronica Guardada Exitosamente", "success")
        return redirect(url_for('resfacturacion.resfacturacion'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('resfacturacion.resfacturacion'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('resfacturacion.resfacturacion'))

#Ruta Ventana Modificar Resolución FE SS
@bp_resfacturacion.get('/edit_resfacturacion/<int:id>')
def edit_resfacturacion(id):
    resolucion = resfacturacion_service.listar_resfacturacion_id(id)
    return render_template('temp_resfacturacion/edit_resfacturacion.html', resolucion = resolucion)

#Ruta POST Actualizar Res. FE SS
@bp_resfacturacion.post('/f_updateResFacturacion')
def f_updateResFacturacion():
    try:
        nombre = request.form["nombre"]
        tipo_documento = request.form["tipo_documento"]
        estado_res = request.form["estado_res"]
        account_id = request.form["account_id"]
        auth_token = request.form["auth_token"]
        texto_encabezado = request.form["texto_encabezado"]
        numero_resolucion = request.form["numero_resolucion"]
        fecha_inicio = request.form["fecha_inicio"]
        fecha_fin = request.form["fecha_fin"]
        prefijo = request.form["prefijo"]
        numero_inicio = request.form["numero_inicio"]
        numero_fin = request.form["numero_fin"]
        encabezado = request.form["encabezado"]
        id_resfacturacion = request.form["id_resfacturacion"]

        resfacturacion_service.update_resfacturacion(nombre, tipo_documento, estado_res, account_id, auth_token, texto_encabezado, numero_resolucion, fecha_inicio, fecha_fin,
                                                     prefijo, numero_inicio, numero_fin, encabezado, id_resfacturacion)
        
        flash("Resolución de Facturación Electronica Guardada Exitosamente", "success")
        return redirect(url_for('resfacturacion.resfacturacion'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: \n{e.msg}", "error")
        return redirect(url_for('resfacturacion.resfacturacion'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: \n{ex}", "error")
        return redirect(url_for('resfacturacion.resfacturacion'))

@bp_resfacturacion.get('/get_token_resf')
def get_token_resf():
    resolucion = resfacturacion_service.listar_resfacturacion_fe()
    json_headers = {
        "Content-Type": "application/json",
        "Auth-token": resolucion[0]
    }
    return json.dumps(json_headers, indent=2)