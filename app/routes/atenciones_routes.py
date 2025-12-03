from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import consultas_service, hospitalizacion_service, ufuncionales_service
import mysql.connector.errors as error

bp_atenciones = Blueprint('atenciones', __name__)

""" @bp_atenciones.get('/atenciones/<medico>')
def atenciones(medico):
    try:
        atenciones = consultas_service.listar_consultas_med(medico)
        return render_template('temp_atenciones/atenciones.html', atenciones = atenciones)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('atenciones.atenciones'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('atenciones.atenciones')) """

@bp_atenciones.get('/atenciones')
def atenciones():
    return render_template('temp_atenciones/atenciones.html')

#Ruta AJAX para traer todas las atenciones por medico y fecha
@bp_atenciones.post('/get_atenciones')
def ajax():
    if request.method == 'POST':
        medico = request.form["medico"]
        fecha_atencion = request.form["fecha_atencion"]
        
        atenciones = consultas_service.listar_consultas_med(medico, fecha_atencion)
        return render_template('temp_atenciones/tabla_atenciones.html', atenciones = atenciones)

@bp_atenciones.get('/atenciones_hosp')
def atenciones_hosp():
    unidades = ufuncionales_service.listar_ufuncionales()
    return render_template('temp_atenciones/atenciones_hosp.html', unidades = unidades)

#Ruta AJAX para traer todas las atenciones por unidad funcional Hosp.
@bp_atenciones.post('/get_atenciones_hosp')
def get_atenciones_hosp():
    if request.method == 'POST':
        un_funcional = request.form["un_funcional"]

        atenciones = hospitalizacion_service.listar_atenciones_hosp(un_funcional)
        return render_template('temp_atenciones/tabla_atenciones_hosp.html', atenciones = atenciones)