from flask import Blueprint, render_template, redirect, request, url_for, flash
from app.services import gruposervicios_service
import mysql.connector.errors

bp_gruposervicios = Blueprint('gruposervicios', __name__)
error = mysql.connector.errors

@bp_gruposervicios.get('/gruposervicios')
def gruposervicios():
    try:
        gservs = gruposervicios_service.listar_gruposervicios()
        return render_template('temp_gruposervicios/gruposervicios.html', gservs = gservs)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

@bp_gruposervicios.get('/add_gruposervicio')
def add_gruposervicio():
    try:
        return render_template('temp_gruposervicios/add_gruposervicio.html')

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

@bp_gruposervicios.post('/f_addGrupoServicio')
def f_addGrupoServicio():
    try:
        cod_grupo_servicio = request.form["cod_grupo_servicio"]
        nom_grupo_servicio = request.form["nom_grupo_servicio"]

        gruposervicios_service.insert_gruposervicio(cod_grupo_servicio,nom_grupo_servicio)
        flash("Grupo de Servicios agregado exitosamente","success")
        return redirect(url_for('gruposervicios.gruposervicios'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

@bp_gruposervicios.route('/drop_gruposervicio/<id>')
def drop_gruposervicio(id):
    try:
        gruposervicios_service.delete_gruposervicio(id)
        flash("Grupo de Servicios eliminado exitosamente", "success")
        return redirect(url_for('gruposervicios.gruposervicios'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

@bp_gruposervicios.get('/update_gruposervicio/<id>')
def update_gruposervicio(id):
    try:
        gserv = gruposervicios_service.listar_gruposervicio_id(id)
        return render_template('temp_gruposervicios/edit_gruposervicio.html', gserv = gserv)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

@bp_gruposervicios.post('/f_updateGrupoServicio')
def f_updateGrupoServicio():
    try:
        cod_grupo_servicio = request.form["cod_grupo_servicio"]
        nom_grupo_servicio = request.form["nom_grupo_servicio"]
        cgrupo_servicio = request.form["cgrupo_servicio"]

        gruposervicios_service.update_gruposervicio(cod_grupo_servicio,nom_grupo_servicio,cgrupo_servicio)
        flash("Grupo de Servicios actualizado exitosamente", "success")
        return redirect(url_for('gruposervicios.gruposervicios'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('gruposervicios.gruposervicios'))