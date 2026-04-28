from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import bodegas_service
import mysql.connector.errors as error

#Blueprint
bp_bodegas = Blueprint('bodegas', __name__)

#Ruta Ventana Bodegas
@bp_bodegas.get('/bodegas')
def bodegas():
    bodegas = bodegas_service.listar_bodegas()
    return render_template('temp_bodegas/bodegas.html', bodegas = bodegas)

#Ruta Ventana Nueva Bodega
@bp_bodegas.get('/add_bodega')
def add_bodega():
    return render_template('temp_bodegas/add_bodega.html')    

#Ruta Metodo Guardar Bodega
@bp_bodegas.post('/f_addBodega')
def f_addBodega():
    try:
        id_bodega = request.form["id_bodega"]
        nom_bodega = request.form["nom_bodega"]
        ubicacion = request.form["ubicacion"]

        bodegas_service.insert_bodega(id_bodega, nom_bodega, ubicacion)
        flash("Bodega Creada Exitosamente", "success")
        return redirect(url_for("bodegas.bodegas"))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for("bodegas.bodegas")), 500
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for("bodegas.bodegas")), 500
    
#Ruta Ventana Actualizar Bodega
@bp_bodegas.get('/edit_bodega/<id>')
def edit_bodega(id):
    bodega = bodegas_service.listar_bodega_id(id)
    return render_template('temp_bodegas/edit_bodega.html', bodega = bodega)

#Ruta Metodo Actualizar Bodega
@bp_bodegas.post('/f_updateBodega')
def f_updateBodega():
    try:
        nom_bodega = request.form["nom_bodega"]
        ubicacion = request.form["ubicacion"]
        id_bodega = request.form["id_bodega"]

        bodegas_service.update_bodega(nom_bodega, ubicacion, id_bodega)
        flash("Bodega Actualizada Exitosamente", "success")
        return redirect(url_for("bodegas.bodegas"))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for("bodegas.bodegas")), 500
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for("bodegas.bodegas")), 500 
    
#Ruta Metodo Eliminar Bodega
@bp_bodegas.get('/drop_bodega/<id>')
def drop_bodega(id):
    try:
        bodegas_service.delete_bodega(id)
        flash("Bodega Eliminada Exitosamente", "success")
        return redirect(url_for("bodegas.bodegas"))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for("bodegas.bodegas")), 500
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for("bodegas.bodegas")), 500