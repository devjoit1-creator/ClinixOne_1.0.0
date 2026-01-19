from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import paciente_service
import mysql.connector.errors as error

bp_epicrisis = Blueprint('epicrisis', __name__)

#Ruta Ventana Epicrisis
@bp_epicrisis.get('/epicrisis')
def epicrisis():
    return render_template('temp_epicrisis/epicrisis.html')

#Ruta Ventana Nueva Epicrisis
@bp_epicrisis.get('/add_epicrisis')
def add_epicrisis():
    pacientes = paciente_service.listar_pacientes_modal()
    return render_template('temp_epicrisis/add_epicrisis.html', pacientes = pacientes)