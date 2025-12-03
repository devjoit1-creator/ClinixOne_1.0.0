from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_bcrypt import Bcrypt
from app.services import usuario_service, medico_service
import mysql.connector.errors

bp_usuario = Blueprint('usuarios', __name__)
bcrypt = Bcrypt()
error = mysql.connector.errors

#Ruta Blueprint para mostrar todos los usuarios listados en template
@bp_usuario.get('/usuarios')
def usuarios():
    try:
        usu = usuario_service.listar_usuarios()
        return render_template('temp_usuarios/usuarios.html', usu = usu)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))

#Ruta Blueprint para mostrar formulario para agregar un nuevo usuario
@bp_usuario.get('/add_usuario')
def add_usuario():
    try:
        perf = usuario_service.listar_perfiles_usuario()
        med = medico_service.listar_medicos()
        return render_template('temp_usuarios/add_usuario.html', perf = perf, med = med)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))

#Ruta Blueprint para procesar formulario de agregar un nuevo usuario y guardarlo en la base de datos    
@bp_usuario.post('/f_addUsuario')
def f_addUsuario():
    try:
        doc_usuario = request.form["doc_usuario"]
        nombre_completo = request.form["nombre_completo"]
        usuario = request.form["usuario"]
        password = bcrypt.generate_password_hash(request.form["password"])
        perfil = request.form["perfil"]

        usuario_service.insert_usuario(doc_usuario,nombre_completo, usuario, password, perfil)
        flash("Usuario Creado Exitosamente", "success")
        return redirect(url_for('usuarios.usuarios'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
@bp_usuario.route('/drop_Usuario/<usuario>')
def drop_usuario(usuario):
    try:
        usuario_service.delete_usuario(usuario)
        flash("Usuario Eliminado Exitosamente", "success")
        return redirect(url_for('usuarios.usuarios'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))    


#Ruta Blueprint para mostrar formulario para editar un usuario
@bp_usuario.get('/edit_usuario/<usuario>')
def edit_usuario(usuario):
    try:
        usu = usuario_service.listar_usuario_nombre(usuario)
        perf = usuario_service.listar_perfiles_usuario()
        med = medico_service.listar_medicos()
        return render_template('temp_usuarios/edit_usuario.html', usu = usu ,perf = perf, med = med)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))

@bp_usuario.post('/f_updateUsuario')
def f_updateUsuario():
    try:
        doc_usuario = request.form["doc_usuario"]
        nombre_completo = request.form["nombre_completo"]
        usuario = request.form["usuario"]
        password = bcrypt.generate_password_hash(request.form["password"])
        perfil = request.form["perfil"]

        usuario_service.update_usuario(doc_usuario,nombre_completo, usuario, password, perfil)
        flash("Usuario Actualizado Exitosamente", "success")
        return redirect(url_for('usuarios.usuarios'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))            
   