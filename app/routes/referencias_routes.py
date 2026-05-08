from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector.errors as error

bp_referencias = Blueprint('referencias', __name__)

#Ruta Ventana Referencias
@bp_referencias.get('/referencias')
def referencias():
    return render_template('temp_referencias/referencias.html')

#Ruta Ventana Nueva Referencia
@bp_referencias.get('/add_referencia')
def add_referencia():
    return render_template('temp_referencias/add_referencia.html')