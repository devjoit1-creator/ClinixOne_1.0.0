from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import fuentes_service, consecutivo_service
import mysql.connector.errors as error

bp_fuentes = Blueprint('fuentes', __name__)

@bp_fuentes.get('/fuentes')
def fuentes():
    fuentes = fuentes_service.listar_fuentes()
    return render_template('temp_fuentes/fuentes.html', fuentes = fuentes)

@bp_fuentes.get('/edit_fuente/<int:cod>')
def edit_fuente(cod):
    fuente = fuentes_service.listar_fuente_codigo(cod)
    """  consecutivo = None
    if(fuente[0] == 6):
        consecutivo = consecutivo_service.listar_consecutivo_fev() """
    
    return render_template('temp_fuentes/edit_fuente.html', fuente = fuente)

@bp_fuentes.post('/f_updateFuente')
def f_updateFuente():
    try:
        """ Request para actualizar los datos de la fuente """
        nom_fuente = request.form["nom_fuente"]
        prefijo = request.form["prefijo"]
        consecutivo = request.form["consecutivo"]
        cod_fuente = request.form["cod_fuente"]

        fuentes_service.update_fuente(nom_fuente, prefijo, consecutivo, cod_fuente)
        
        """ Request para actualizar el consecutivo de la fuente """     
        """ consecutivo = request.form["consecutivo"]
        consecutivo_service.update_consecutivo_fev(consecutivo) """
            
        flash("Fuente Actualizada Exitosamente","success")
        return redirect(url_for('fuentes.fuentes'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('fuentes.fuentes'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('fuentes.fuentes'))