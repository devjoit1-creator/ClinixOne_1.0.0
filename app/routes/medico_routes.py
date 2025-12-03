from flask import Blueprint, render_template, redirect, request, flash, url_for
from app.services import medico_service
import mysql.connector.errors
from io import BytesIO
import base64

bp_medicos = Blueprint('medicos', __name__)
error = mysql.connector.errors

#Ruta Blueprint para mostrar todos los médicos listados en template
@bp_medicos.get('/medicos')
def medicos():
    try:
        meds = medico_service.listar_medicos()
        return render_template('temp_medicos/medicos.html', meds = meds)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('medicos.medicos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('medicos.medicos'))

#Ruta Blueprint para mostrar formulario para agregar un nuevo medico
@bp_medicos.get('/add_medico')
def add_medico():
    try:
        #Lista de Cargos Asistenciales llamado desde el service
        cargos = medico_service.listar_cargos_asistenciales()
        return render_template('temp_medicos/add_medico.html', cargos = cargos)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('medicos.medicos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('medicos.medicos'))

#Ruta Blueprint para procesar formulario de agregar un nuevo medico y guardarlo en la base de datos
@bp_medicos.post('/f_addMedico')
def f_addMedico():
    try:
        tipo_doc = request.form["tipo_doc"]
        num_doc = request.form["num_doc"]
        p_nombre = request.form["p_nombre"]
        s_nombre = request.form["s_nombre"]
        p_apellido = request.form["p_apellido"]
        s_apellido = request.form["s_apellido"]
        nombre_completo = request.form["nombre_completo"]
        dir_medico = request.form["dir_medico"]
        tel_medico = request.form["tel_medico"]
        id_cargo_asis = request.form["id_cargo_asis"]
        cargo_asis = request.form["cargo_asis"]
        registro_medico = request.form["registro_medico"]
        consultorio = request.form["consultorio"]
        firma_medico = request.files["firma_medico"]
        if firma_medico:
            img_data = firma_medico.read()

        medico_service.insert_medico(tipo_doc, num_doc, p_nombre, s_nombre, p_apellido, s_apellido, nombre_completo, 
                                        dir_medico, tel_medico, id_cargo_asis, cargo_asis, registro_medico, consultorio, img_data)
        flash("Médico agregado exitosamente","success")
        return redirect(url_for('medicos.medicos'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('medicos.medicos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('medicos.medicos'))

#Ruta Blueprint para eliminar medicos de la base de datos 
@bp_medicos.route('/drop_Medico/<int:id>')
def drop_Medico(id):
    try:
        medico_service.delete_medico(id)
        flash("Médico eliminado","success")
        return redirect(url_for('medicos.medicos'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('medicos.medicos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('medicos.medicos'))

#Ruta Blueprint para mostrar formulario para editar un medico
@bp_medicos.get('/edit_medico/<int:id>')
def edit_medico(id):
    try:
        med = medico_service.listar_medico_id(id)
        imagen = BytesIO(med[14]) 
        if imagen: 
            firma = base64.b64encode(imagen.read()).decode('utf-8')

        cargos = medico_service.listar_cargos_asistenciales()
        return render_template('temp_medicos/edit_medico.html', med = med, cargos = cargos, firma = firma)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('medicos.medicos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('medicos.medicos'))
    
#Ruta Blueprint para procesar formulario de edición de medico y actualizarlo en la base de datos
@bp_medicos.post('/f_updateMedico')
def f_updateMedico():
    try:
        tipo_doc = request.form["tipo_doc"]
        num_doc = request.form["num_doc"]
        p_nombre = request.form["p_nombre"]
        s_nombre = request.form["s_nombre"]
        p_apellido = request.form["p_apellido"]
        s_apellido = request.form["s_apellido"]
        nombre_completo = request.form["nombre_completo"]
        dir_medico = request.form["dir_medico"]
        tel_medico = request.form["tel_medico"]
        id_cargo_asis = request.form["id_cargo_asis"]
        cargo_asis = request.form["cargo_asis"]
        registro_medico = request.form["registro_medico"]
        consultorio = request.form["consultorio"]
        firma_medico = request.files["firma_medico"]
        idMedico = request.form["idMedico"]
        if firma_medico:
            img_data = firma_medico.read()

            medico_service.update_medico(tipo_doc, num_doc, p_nombre, s_nombre, p_apellido, s_apellido, nombre_completo, 
                                        dir_medico, tel_medico, id_cargo_asis, cargo_asis, registro_medico, consultorio, img_data, idMedico)
        flash("Médico actualizado exitosamente","success")
        return redirect(url_for('medicos.medicos'))    
            
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('medicos.medicos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('medicos.medicos'))