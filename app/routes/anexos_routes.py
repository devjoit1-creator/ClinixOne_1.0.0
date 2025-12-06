from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import paciente_service, anexos_service
from io import BytesIO
import mysql.connector.errors as error

#Blueprint
bp_anexos = Blueprint('anexos', __name__)

#Ruta Ventana Anexos
@bp_anexos.get('/anexos')
def anexos():
    pacientes = paciente_service.listar_pacientes_modal()
    tipos = anexos_service.listar_tipos_anexos()
    return render_template('temp_anexos/anexos.html', pacientes = pacientes, tipos = tipos)