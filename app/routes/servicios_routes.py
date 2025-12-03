from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import servicios_service, tarifas_services, gruposervicios_service
import mysql.connector.errors

bp_servicios = Blueprint("servicios",__name__)
error = mysql.connector.errors

@bp_servicios.get('/servicios')
def servicios():
    try:
        servs = servicios_service.listar_servicios()
        return render_template('temp_servicios/servicios.html', servs = servs)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('servicios.servicios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('servicios.servicios'))

@bp_servicios.get('/add_servicio')
def add_servicio():
    try: 
        tarfs = tarifas_services.listar_tarifas()
        grservs = gruposervicios_service.listar_gruposervicios()
        return render_template('temp_servicios/add_servicio.html', tarfs = tarfs, grservs = grservs)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('servicios.servicios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('servicios.servicios'))

@bp_servicios.post('/f_addServicio')
def f_addServicio():
    try:
        cod_servicio = request.form["cod_servicio"]
        nom_servicio = request.form["nom_servicio"]
        valor = request.form["valor"]
        tarifa = request.form["tarifa"]
        grupo = request.form["grupo"]

        servicios_service.insert_servicio(cod_servicio,nom_servicio,valor,tarifa,grupo)
        flash("Servicio y/o Proced. agregado exitosamente", "success")
        return redirect(url_for('servicios.servicios'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('servicios.servicios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('servicios.servicios'))
    
@bp_servicios.route('/drop_servicio/<int:id>')
def drop_servicio(id):
    try:
        servicios_service.delete_servicio(id)
        flash("Servicio y/o Proced. eliminado exitosamente", "success")
        return redirect(url_for('servicios.servicios'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('servicios.servicios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('servicios.servicios'))

@bp_servicios.get('/update_servicio/<int:id>')
def update_servicio(id):
    try:
        serv = servicios_service.listar_servicio_id(id)
        tarfs = tarifas_services.listar_tarifas()
        grservs = gruposervicios_service.listar_gruposervicios()
        return render_template('temp_servicios/edit_servicio.html', serv = serv, tarfs = tarfs, grservs = grservs)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('servicios.servicios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('servicios.servicios'))
    
@bp_servicios.post('/f_updateServicio')
def f_updateServicio ():
    try:
        cod_servicio = request.form["cod_servicio"]
        nom_servicio = request.form["nom_servicio"]
        valor = request.form["valor"]
        tarifa = request.form["tarifa"]
        grupo = request.form["grupo"]
        id_servicio = request.form["id_servicio"]

        servicios_service.update_servicio(cod_servicio,nom_servicio,valor,tarifa,grupo,id_servicio)
        flash("Servicio y/o Proced. actualizado exitosamente", "success")
        return redirect(url_for('servicios.servicios'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('servicios.servicios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('servicios.servicios'))    