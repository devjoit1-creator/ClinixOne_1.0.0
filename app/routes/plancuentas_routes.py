from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services import plancuentas_service
from flask_weasyprint import HTML, render_pdf
import mysql.connector.errors as error

bp_plancuentas = Blueprint('plancuentas', __name__)

@bp_plancuentas.get('/plancuentas')
def plancuentas():
    cuentas = plancuentas_service.listar_cuentas()
    return render_template('temp_plancuentas/plancuentas.html', cuentas = cuentas)

@bp_plancuentas.get('/add_cuenta')
def add_cuenta():
    return render_template('temp_plancuentas/add_cuenta.html')

@bp_plancuentas.post('/f_addCuenta')
def f_addCuenta():
    try:
        cod_cuenta = request.form["cod_cuenta"]
        nom_cuenta = request.form["nom_cuenta"]
        clasificacion = request.form["clasificacion"]
        naturaleza = request.form["naturaleza"]

        plancuentas_service.insert_cuenta(cod_cuenta, nom_cuenta, clasificacion, naturaleza)
        flash("Cuenta creada exitosamente en el PUC","success")
        return redirect(url_for('plancuentas.plancuentas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('plancuentas.plancuentas'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('plancuentas.plancuentas'))

@bp_plancuentas.get('/edit_cuenta/<cod_cuenta>')
def edit_cuenta(cod_cuenta):
    cuenta = plancuentas_service.listar_cuenta(cod_cuenta)
    return render_template('temp_plancuentas/edit_cuenta.html', cuenta = cuenta)

@bp_plancuentas.post('/f_updateCuenta')
def f_updateCuenta():
    try:
        cod_cuenta = request.form["cod_cuenta"]
        nom_cuenta = request.form["nom_cuenta"]
        clasificacion = request.form["clasificacion"]
        naturaleza = request.form["naturaleza"]

        plancuentas_service.update_cuenta(nom_cuenta, clasificacion, naturaleza, cod_cuenta)
        flash("Cuenta Actualizada", "success")
        return redirect(url_for('plancuentas.plancuentas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('plancuentas.plancuentas'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('plancuentas.plancuentas'))    

@bp_plancuentas.get('/drop_cuenta/<cod_cuenta>')
def drop_cuenta(cod_cuenta):
    plancuentas_service.delete_cuenta(cod_cuenta)
    flash("Cuenta Eliminada", "success")
    return redirect(url_for('plancuentas.plancuentas'))
            