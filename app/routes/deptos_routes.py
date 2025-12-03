from flask import Blueprint, jsonify, request
from app.services import departamentos
import mysql.connector.errors as error

bp_deptos = Blueprint('deptos', __name__)

#Ruta AJAX Fetch para Obtener los departamentos
@bp_deptos.get('/get_deptos')
def get_deptos():
    try:
        deptos = departamentos.listar_departamentos()
        if deptos:
            return jsonify(deptos)

    except Exception as ex:
        return jsonify(ex)
    
#Ruta AJAX Fetch para Obtener los municipios
@bp_deptos.post('/get_municipios')
def get_municipios():
    try:
        data = request.get_json()
        cod_depto = data.get("codDepto")
        municipios = departamentos.listar_municipios(cod_depto)
        if municipios:
            return jsonify(municipios)
        
    except Exception as ex:
        return jsonify(ex)    