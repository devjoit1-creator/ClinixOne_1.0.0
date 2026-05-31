from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import fuentes_service, consecutivo_service, bodegas_service, terceros_service, referencias_service, entradas_farmacia_service
import mysql.connector.errors as error

#Blueprint
bp_entradasFarmacia = Blueprint("entradasFarmacia", __name__)

#Ruta Ventana Entradas de Farmacia
@bp_entradasFarmacia.get('/entradas_farmacia')
def entradas_farmacia():
    return render_template('temp_entradas_farmacia/entradas_farmacia.html')

#Ruta Ventana Nueva Entrada de Farmacia
@bp_entradasFarmacia.get('/add_entrada')
def add_entrada():
    fuentes = fuentes_service.listar_fuente_ef()
    consecutivo = consecutivo_service.listar_consecutivo_ef()
    bodegas = bodegas_service.listar_bodegas()
    terceros = terceros_service.listar_terceros()
    referencias = referencias_service.listar_referencias_entrada()
    return render_template('temp_entradas_farmacia/add_entrada.html', fuentes = fuentes, consecutivo = consecutivo, bodegas = bodegas, terceros = terceros, referencias = referencias)