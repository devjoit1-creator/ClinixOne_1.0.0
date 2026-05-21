from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.entradas_farmacia_service import *
import mysql.connector.errors as error

#Blueprint
bp_entradasFarmacia = Blueprint("entradasFarmacia", __name__)

#Ruta Ventana Entradas de Farmacia
@bp_entradasFarmacia.get('/entradas_farmacia')
def entradas_farmacia():
    return render_template('temp_entradas_farmacia/entradas_farmacia.html')