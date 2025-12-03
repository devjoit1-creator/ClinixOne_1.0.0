from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import tarifas_services, administradoras_service, cobertura_adm_service
import mysql.connector.errors

bp_administradoras = Blueprint('administradoras', __name__)
error = mysql.connector.errors

#Ruta ventana administradoras
@bp_administradoras.get('/administradoras')
def administradoras():
    try:
        admins = administradoras_service.listar_administradoras()
        return render_template('temp_administradoras/administradoras.html', admins = admins)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('administradoras.administradoras'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('administradoras.administradoras'))

#Ruta ventana nueva administradora    
@bp_administradoras.get('/add_administradora')
def add_administradora():
    try:
        tarfs = tarifas_services.listar_tarifas()
        coberturas = cobertura_adm_service.listar_coberturas()
        conceptos = cobertura_adm_service.listar_conceptos()
        modalidades = cobertura_adm_service.listar_modalidades()
        return render_template('temp_administradoras/add_administradora.html', tarfs = tarfs, coberturas = coberturas, conceptos = conceptos, modalidades = modalidades)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('administradoras.administradoras'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('administradoras.administradoras'))

#Ruta POST insertar nueva administradora
@bp_administradoras.post('/f_addAdministradora')
def f_addAdministradora():
    try:
        cod_administradora = request.form["cod_administradora"]
        nit_administradora = request.form["nit_administradora"]
        digito_verificacion = request.form["digito_verificacion"]
        convenio = request.form["convenio"]
        nom_administradora = request.form["nom_administradora"]
        dir_administradora = request.form["dir_administradora"]
        tel_administradora = request.form["tel_administradora"]
        cod_rips_adm = request.form["cod_rips_adm"]
        tipo_convenio = request.form["tipo_convenio"]
        vigencia_convenio = request.form["vigencia_convenio"]
        fecha_inicio_conv = request.form["fecha_inicio_conv"]
        fecha_fin_conv = request.form["fecha_fin_conv"]
        forma_pago = request.form["forma_pago"]
        poblacion = request.form["poblacion"]
        tarifa_adm = request.form["tarifa_adm"]
        plan = request.form["plan"]
        plan_beneficios = request.form["plan_beneficios"]
        concepto_recaudo = request.form["concepto_recaudo"]
        modalidad_pago = request.form["modalidad_pago"]

        administradoras_service.insert_administradora(cod_administradora,nit_administradora,digito_verificacion,convenio,nom_administradora,
                                                        dir_administradora,tel_administradora,cod_rips_adm,tipo_convenio,vigencia_convenio,fecha_inicio_conv,
                                                        fecha_fin_conv,forma_pago,poblacion,tarifa_adm,plan, plan_beneficios, concepto_recaudo, modalidad_pago)
        
        flash("E.A.P.B.- Administradora creada exitosamente", "success")
        return redirect(url_for('administradoras.administradoras'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('administradoras.administradoras'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('administradoras.administradoras'))

#Ruta GET Eliminar administradora    
@bp_administradoras.route('/drop_administradora/<codigo>')
def drop_administradora(codigo):
    try:
        administradoras_service.delete_administradora(codigo)
        flash("E.A.P.B.- Administradora eliminada exitosamente", "success")
        return redirect(url_for('administradoras.administradoras'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('administradoras.administradoras'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('administradoras.administradoras'))

#Ruta GET Actualizar administradora    
@bp_administradoras.get('/update_administradora/<codigo>')
def update_administradora(codigo):
    try:
        admin = administradoras_service.listar_administradora_id(codigo)
        tarfs = tarifas_services.listar_tarifas()
        coberturas = cobertura_adm_service.listar_coberturas()
        conceptos = cobertura_adm_service.listar_conceptos()
        modalidades = cobertura_adm_service.listar_modalidades()
        return render_template('temp_administradoras/edit_administradora.html', admin = admin, tarfs = tarfs, coberturas = coberturas, conceptos = conceptos, modalidades = modalidades)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('administradoras.administradoras'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('administradoras.administradoras'))

#Ruta POST Actualizar administradora    
@bp_administradoras.post('/f_updateAdministradora')
def f_updateAdministradora():
    try:
        cod_administradora = request.form["cod_administradora"]
        nit_administradora = request.form["nit_administradora"]
        digito_verificacion = request.form["digito_verificacion"]
        convenio = request.form["convenio"]
        nom_administradora = request.form["nom_administradora"]
        dir_administradora = request.form["dir_administradora"]
        tel_administradora = request.form["tel_administradora"]
        cod_rips_adm = request.form["cod_rips_adm"]
        tipo_convenio = request.form["tipo_convenio"]
        vigencia_convenio = request.form["vigencia_convenio"]
        fecha_inicio_conv = request.form["fecha_inicio_conv"]
        fecha_fin_conv = request.form["fecha_fin_conv"]
        forma_pago = request.form["forma_pago"]
        poblacion = request.form["poblacion"]
        tarifa_adm = request.form["tarifa_adm"]
        plan = request.form["plan"]
        plan_beneficios = request.form["plan_beneficios"]
        concepto_recaudo = request.form["concepto_recaudo"]
        modalidad_pago = request.form["modalidad_pago"]
        c_administradora = request.form["c_administradora"]

        administradoras_service.update_administradora(cod_administradora, nit_administradora, digito_verificacion, convenio, nom_administradora,
                                                        dir_administradora, tel_administradora, cod_rips_adm, tipo_convenio, vigencia_convenio, fecha_inicio_conv, fecha_fin_conv,
                                                        forma_pago, poblacion, tarifa_adm, plan, plan_beneficios, concepto_recaudo, modalidad_pago, c_administradora)
        
        flash("E.A.P.B.- Administradora actualizada exitosamente", "success")
        return redirect(url_for('administradoras.administradoras'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('administradoras.administradoras'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('administradoras.administradoras'))
    
#Ruta Metodo AJAX para cargar dato de cobertura por codigo de administradora
@bp_administradoras.post('/get_cobertura_administradora')
def get_cobertura_administradora():
    data = request.get_json()
    cod_admin = data.get("cod_admin", "")
    cobertura = cobertura_adm_service.listar_cobertura_admin(cod_admin)
    if cobertura:
        return jsonify(cobertura)
        
#Ruta Metodo AJAX para cargar dato de concepto recaudo por codigo de administradora
@bp_administradoras.post('/get_concepto_administradora')
def get_concepto_administradora():
    data = request.get_json()
    cod_admin = data.get("cod_admin", "")
    concepto = cobertura_adm_service.listar_concepto_admin(cod_admin)
    if concepto:
        return jsonify(concepto)