from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from app.services import habitaciones_service, ufuncionales_service
import mysql.connector.errors

bp_habitaciones = Blueprint('habitaciones', __name__)
error = mysql.connector.errors

@bp_habitaciones.get('/habitaciones')
def habitaciones():
    try: 
        habs = habitaciones_service.listar_habitaciones()
        return render_template('temp_habitaciones/habitaciones.html', habs = habs)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('habitaciones.habitaciones'))

@bp_habitaciones.get('/add_habitacion')
def add_habitacion():
    try:
        uf = ufuncionales_service.listar_ufuncionales()
        return render_template('temp_habitaciones/add_habitacion.html', uf = uf)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('habitaciones.habitaciones'))

@bp_habitaciones.post('/f_addHabitacion')
def f_addHabitacion():
    try:
        cod_habitacion = request.form["cod_habitacion"]
        nom_habitacion = request.form["nom_habitacion"]
        c_ufuncional = request.form["c_ufuncional"]
        reservada = request.form["reservada"]

        habitaciones_service.insertar_habitacion(cod_habitacion,nom_habitacion,c_ufuncional,reservada)
        flash("Habitación agregada exitosamente", "success")
        return redirect(url_for('habitaciones.habitaciones'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
@bp_habitaciones.route('/drop_Habitacion/<int:id>')
def drop_habitacion(id):
    try:
        habitaciones_service.delete_habitacion(id)
        flash("Habitación eliminada exitosamente", "success")
        return redirect(url_for('habitaciones.habitaciones'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('habitaciones.habitaciones'))

@bp_habitaciones.get('/edit_Habitacion/<int:id>')
def edit_Habitacion(id):
    try:
        hab = habitaciones_service.listar_habitacion_id(id)
        uf = ufuncionales_service.listar_ufuncionales()
        return render_template('temp_habitaciones/edit_habitacion.html', hab = hab, uf = uf)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('habitaciones.habitaciones'))

@bp_habitaciones.post('/f_updateHabitacion')
def f_updateHabitacion():
    try:
        cod_habitacion = request.form["cod_habitacion"]
        nom_habitacion = request.form["nom_habitacion"]
        c_ufuncional = request.form["c_ufuncional"]
        reservada = request.form["reservada"]
        id_habitacion = request.form["id_habitacion"]

        habitaciones_service.update_habitacion(cod_habitacion,nom_habitacion,c_ufuncional,reservada,id_habitacion)
        flash("Habitación actualizada exitosamente", "success")
        return redirect(url_for('habitaciones.habitaciones'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('habitaciones.habitaciones'))
    
""" Ruta AJAX para llamar habitaciones en Modal """
@bp_habitaciones.post('/get_habitaciones')
def get_habitaciones():
    data = request.get_json()
    ufuncional_modal = data.get("undFuncional")
    habitaciones = habitaciones_service.listar_habitaciones_modal(ufuncional_modal)

    if habitaciones:
        return jsonify(habitaciones)
    
    #ufuncional_modal = request.form["ufuncional_modal"] jquery
    #return render_template('temp_habitaciones/tabla_habitaciones.html', habitaciones = habitaciones) jquery