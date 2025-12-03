from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
import mysql.connector.errors as error
from app.services import usuario_service

#Nombramos el Blueprint Principal
bp_index = Blueprint('Index', __name__)
bcrypt = Bcrypt()

#Ruta Ventana Pagina Principal Login
@bp_index.get('/')
def index():
    session.clear()
    return render_template('login.html')

#Ruta Metodo Post Recorrido BD usuarios y perfiles y acceso
@bp_index.post('/login_access')
def login_access():
    try:
        usuario = request.form['userId']
        contrasena = request.form['userPass']

        user = usuario_service.listar_usuario_nombre(usuario)
        candidate = user[3]
    
        """ if usuario == '' or contrasena == '':
            flash('Debe diligenciar su usuario y contraseña','warning')
            return render_template('login.html') """
        
        if len(user)>0:
            if bcrypt.check_password_hash(candidate, contrasena):
                session['name'] = user[2]
                session['profile'] = user[4]
                session['document'] = user[0]

                if session['profile'] != 0:
                    return redirect(url_for('Index.dashboard'))
            else:       
                flash('Contraseña Incorrecta', 'warning')
                return render_template('login.html')
        else: 
            flash('Usuario no existe. Contacte al Administrador del Sistema', 'error')
            return render_template('login.html')
        
    except TypeError:
        flash('Usuario no existe. Contacte al Administrador del Sistema', 'error')
        return render_template('login.html')
    
#Ruta Ventana Retorno Pagina Login    
@bp_index.get('/logout')
def logout():
    session.clear()
    return render_template('login.html')

#Ruta Ventana Pagina Principal Dashboard
@bp_index.get('/dashboard')
def dashboard():
    return render_template('dashboard.html')