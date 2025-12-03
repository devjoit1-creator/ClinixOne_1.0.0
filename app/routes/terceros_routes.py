from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import terceros_service, departamentos
import mysql.connector.errors as error

bp_terceros = Blueprint('terceros', __name__)

@bp_terceros.get('/terceros')
def terceros():
    terceros = terceros_service.listar_terceros()
    return render_template('temp_terceros/terceros.html', terceros = terceros)

@bp_terceros.get('/add_tercero')
def add_tercero():
    deptos = departamentos.listar_departamentos()
    return render_template('temp_terceros/add_tercero.html', deptos = deptos)

@bp_terceros.post('/f_addTercero')
def f_addTercero():
    try:
        tipo_idf = request.form["tipo_idf"]
        identificacion = request.form["identificacion"]
        digito_verf = request.form["digito_verf"]
        nom_tercero = request.form["nom_tercero"]
        dir_tercero = request.form["dir_tercero"]
        tel_tercero = request.form["tel_tercero"]
        tipo_tercero = request.form["tipo_tercero"]
        correo = request.form["correo"]
        cod_depto_tercero = request.form["cod_depto_tercero"]
        nom_depto_tercero = request.form["nom_depto_tercero"]
        cod_munic_tercero = request.form["cod_munic_tercero"]
        nom_munic_tercero = request.form["nom_munic_tercero"]

        terceros_service.insert_tercero(tipo_idf, identificacion, digito_verf, nom_tercero, dir_tercero, tel_tercero, tipo_tercero, correo, cod_depto_tercero, 
                                        nom_depto_tercero, cod_munic_tercero, nom_munic_tercero)
        flash("Tercero Agregado Exitosamente", "success")
        return redirect(url_for('terceros.terceros'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('terceros.terceros'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('terceros.terceros'))
    
@bp_terceros.get('/edit_tercero/<int:id>')
def edit_tercero(id):
    tercero = terceros_service.listar_tercero_id(id)
    deptos = departamentos.listar_departamentos()
    return render_template('temp_terceros/edit_tercero.html', tercero = tercero, deptos = deptos)

@bp_terceros.post('/f_updateTercero')
def f_updateTercero():
    try:
        tipo_idf = request.form["tipo_idf"]
        identificacion = request.form["identificacion"]
        digito_verf = request.form["digito_verf"]
        nom_tercero = request.form["nom_tercero"]
        dir_tercero = request.form["dir_tercero"]
        tel_tercero = request.form["tel_tercero"]
        tipo_tercero = request.form["tipo_tercero"]
        correo = request.form["correo"]
        cod_depto_tercero = request.form["cod_depto_tercero"]
        nom_depto_tercero = request.form["nom_depto_tercero"]
        cod_munic_tercero = request.form["cod_munic_tercero"]
        nom_munic_tercero = request.form["nom_munic_tercero"]
        id_tercero = request.form["id_tercero"]

        terceros_service.update_tercero(tipo_idf, identificacion, digito_verf, nom_tercero, dir_tercero, tel_tercero,  tipo_tercero, correo, 
                                        cod_depto_tercero, nom_depto_tercero, cod_munic_tercero, nom_munic_tercero, id_tercero)
        
        flash(f"Tercero Actualizado Exitosamente", "success")
        return redirect(url_for('terceros.terceros'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('terceros.terceros'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('terceros.terceros'))
    
@bp_terceros.get('/drop_tercero/<int:id>')
def delete_tercero(id):
    try:
        terceros_service.delete_tercero(id)
        flash("Tercero Eliminado", "success")
        return redirect(url_for('terceros.terceros'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('terceros.terceros'))
    
#Ruta Ajax Para obtener datos del tercero como cliente (Facturación)
@bp_terceros.post('/get_tercero')
def get_tercero():
    data = request.get_json()
    nit_admin = data.get("nit_admin")
    #nit_admin = request.form["nit_admin"] jquery
    
    tercero = terceros_service.listar_tercero_nit(nit_admin)
    if tercero:
        return jsonify(tercero)

#Ruta Ajax para Listar Departamentos y Municipios
@bp_terceros.get('/get_deptos')
def get_deptos():
    deptos = departamentos.listar_departamentos()
    if deptos:
        return jsonify(deptos)
    
@bp_terceros.post('/get_municipios')
def get_municipios():
    data = request.get_json()
    cod_depto = data.get("codDepto", "")
    municipios = departamentos.listar_municipios(cod_depto)
    if municipios:
        return jsonify(municipios)    