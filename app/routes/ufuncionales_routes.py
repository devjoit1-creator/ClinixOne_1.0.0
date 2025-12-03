from flask import Blueprint, render_template, redirect, request, url_for, flash
from app.services import ufuncionales_service
import mysql.connector.errors

bp_ufuncionales = Blueprint('ufuncionales', __name__)
error = mysql.connector.errors

#Ruta ventana de u. funcionales
@bp_ufuncionales.get('/ufuncionales')
def ufuncionales():
    ufunc = ufuncionales_service.listar_ufuncionales()
    return render_template('temp_ufuncionales/ufuncionales.html', ufunc = ufunc)

#Ruta ventana nueva u. funcional
@bp_ufuncionales.get('/add_ufuncional')
def add_ufuncional():
    return render_template('temp_ufuncionales/add_ufuncional.html')

#Ruta POST insertar u. funcional
@bp_ufuncionales.post('/f_addUfuncional')
def f_addUfuncional():
    try:
        cod_ufuncional = request.form["cod_ufuncional"]
        nom_ufuncional = request.form["nom_ufuncional"]

        ufuncionales_service.insertar_ufuncional(cod_ufuncional,nom_ufuncional)
        flash("Unidad Funcional Creada Exitosamente", "success")
        return redirect(url_for('ufuncionales.ufuncionales'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))

#Ruta GET eliminar u. funcional
@bp_ufuncionales.route('/drop_ufuncional/<cod>')
def drop_ufuncional(cod):
    try:
        ufuncionales_service.delete_ufuncional(cod)
        flash("Unidad Funcional Eliminada Exitosamente", "success")
        return redirect(url_for('ufuncionales.ufuncionales'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))

#Ruta GET actualizar u. funcional    
@bp_ufuncionales.get('/edit_ufuncional/<cod>')
def edit_ufuncional(cod):
    try:
        ufunc = ufuncionales_service.listar_ufuncional_id(cod)
        return render_template('temp_ufuncionales/edit_ufuncional.html', ufunc = ufunc)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))

#Ruta POST actualizar u. funcional    
@bp_ufuncionales.post('/f_updateUfuncional')
def f_updateUfuncional():
    try:
        cod_ufuncional = request.form["cod_ufuncional"]
        nom_ufuncional = request.form["nom_ufuncional"]
        cufuncional = request.form["cufuncional"]

        ufuncionales_service.update_ufuncional(cod_ufuncional,nom_ufuncional,cufuncional)
        flash("Unidad Funcional Actualizada Exitosamente", "success")
        return redirect(url_for('ufuncionales.ufuncionales'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('ufuncionales.ufuncionales'))
