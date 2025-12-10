from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import paciente_service, anexos_service
from io import BytesIO
import mysql.connector.errors as error

#Blueprint
bp_anexos = Blueprint('anexos', __name__)

#Ruta Ventana Anexos
@bp_anexos.get('/anexos')
def anexos():
    return render_template('temp_anexos/anexos.html')

#Ruta Ventana Nuevo Anexo
@bp_anexos.get('/nuevo_anexo')
def nuevo_anexo():
    pacientes = paciente_service.listar_pacientes_modal()
    tipos = anexos_service.listar_tipos_anexos()
    return render_template('temp_anexos/nuevo_anexo.html', pacientes = pacientes, tipos = tipos)

#Ruta Guardar Anexo
@bp_anexos.post('/add_anexo')
def add_anexo():
    try:
        codigo = request.form["codigo"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        tipo_documento = request.form["tipo_documento"]
        descripcion = request.form["descripcion"]
        documento_obj = request.files["documento"]

        if documento_obj:
            documento = documento_obj.read()

        anexos_service.insert_anexo(codigo, fecha, hora, tipo_documento, descripcion, documento)
        flash("Anexo Guardado Exitosamente", "success")
        return redirect(url_for('anexos.anexos'))    

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('anexos.anexos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('anexos.anexos'))