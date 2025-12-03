from flask import Blueprint, render_template, redirect, request, url_for, flash
from app.services import tarifas_services
import mysql.connector.errors

bp_tarifas = Blueprint('tarifas', __name__)
error = mysql.connector.errors

@bp_tarifas.get('/tarifas')
def tarifas():
    try:
        tarfs = tarifas_services.listar_tarifas() 
        return render_template('temp_tarifas/tarifas.html', tarfs = tarfs)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('tarifas.tarifas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('tarifas.tarifas'))

@bp_tarifas.get('/add_tarifa')
def add_tarifa():
    try:
        return render_template('temp_tarifas/add_tarifa.html')

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('tarifas.tarifas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('tarifas.tarifas'))
    
@bp_tarifas.post('/f_addTarifa')
def f_addTarifa():
    try:
        if request.method == 'POST':
            nom_tarifa = request.form["nom_tarifa"]
            base_tarifa = request.form["base_tarifa"]

            tarifas_services.insert_tarifa(nom_tarifa,base_tarifa)
            flash("Tarifa agregada exitosamente", "success")
            return redirect(url_for('tarifas.tarifas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('tarifas.tarifas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('tarifas.tarifas'))

@bp_tarifas.route('/drop_tarifa/<int:id>')
def drop_tarifa(id):
    try:
        tarifas_services.delete_tarifa(id)
        flash("Tarifa eliminada exitosamente", "success")
        return redirect(url_for('tarifas.tarifas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('tarifas.tarifas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('tarifas.tarifas'))

@bp_tarifas.get('/edit_tarifa/<int:id>')
def edit_tarifa(id):
    try:
        tarf = tarifas_services.listar_tarifa_id(id)
        return render_template('temp_tarifas/edit_tarifa.html', tarf = tarf)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('tarifas.tarifas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('tarifas.tarifas'))
        
@bp_tarifas.post('/f_updateTarifa')
def f_updateTarifa():
    try:
        if request.method == 'POST':
            nom_tarifa = request.form["nom_tarifa"]
            base_tarifa = request.form["base_tarifa"]
            id_tarifa = request.form["id_tarifa"]

            tarifas_services.update_tarifa(nom_tarifa,base_tarifa,id_tarifa)
            flash("Tarifa modificada exitosamente", "success")
            return redirect(url_for('tarifas.tarifas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('tarifas.tarifas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('tarifas.tarifas'))           