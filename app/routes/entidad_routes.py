from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import entidad_service
import mysql.connector.errors
from io import BytesIO
import base64

bp_entidad = Blueprint('entidad', __name__)
error = mysql.connector.errors

#Ruta ventana Datos de entidad
@bp_entidad.get('/entidad')
def entidad():
    try:
        ent = entidad_service.listar_entidad_arr()
        return render_template('temp_entidad/entidad.html', ent = ent)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('entidad.entidad'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('entidad.entidad'))
    
#Ruta ventana agregar datos en entidad
@bp_entidad.get('/add_entidad')
def add_entidad():
    try:
        return render_template('temp_entidad/add_entidad.html')

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('entidad.entidad'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('entidad.entidad'))
    
#Ruta POST para insertar datos de entidad en base de datos
@bp_entidad.post('/f_addEntidad')
def f_addEntidad():
    try:
        nit_entidad = request.form["nit_entidad"]
        digito_nit = request.form["digito_nit"]
        nom_entidad = request.form["nom_entidad"]
        dir_entidad = request.form["dir_entidad"]
        tel_entidad = request.form["tel_entidad"]
        correo_entidad = request.form["correo_entidad"]
        pais_entidad = request.form["pais_entidad"]
        depto_entidad = request.form["depto_entidad"]
        mun_entidad = request.form["mun_entidad"]
        cod_habilitacion = request.form["cod_habilitacion"]
        gerente = request.form["gerente"]
        revisor = request.form["revisor"]
        resolucion_dian = request.form["resolucion_dian"]
        logo_entidad = request.files["logo_entidad"]
        if logo_entidad:
            img_data = logo_entidad.read()
    
        entidad_service.insert_entidad(nit_entidad, digito_nit, nom_entidad, dir_entidad, tel_entidad, correo_entidad,
                                            pais_entidad, depto_entidad, mun_entidad, cod_habilitacion, gerente, revisor, resolucion_dian, img_data)
        flash("Datos de Entidad agregados exitosamente","success")
        return redirect(url_for('entidad.entidad'))                                 

    except error.Error as e:
        flash(f"Se presentó un erro inesperado: {e.msg}","error")
        return redirect(url_for('entidad.entidad'))
    
    except Exception as ex: 
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('entidad.entidad'))

#Ruta GET para modificar datos de entidad    
@bp_entidad.get('/edit_entidad/<nit>')
def edit_entidad(nit):
    try:
        et = entidad_service.listar_entidad_nit(nit)
        imagen = BytesIO(et[13])
        if imagen:
            logo = base64.b64encode(imagen.read()).decode('utf-8')

        return render_template('temp_entidad/edit_entidad.html', et = et, logo = logo)

    except error.Error as e: 
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('entidad.entidad'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('entidad.entidad'))

#Ruta POST para actualizar datos de entidad en base de datos
@bp_entidad.post('/f_updateEntidad')
def f_updateEntidad():
    try:
        nit_entidad = request.form["nit_entidad"]
        digito_nit = request.form["digito_nit"]
        nom_entidad = request.form["nom_entidad"]
        dir_entidad = request.form["dir_entidad"]
        tel_entidad = request.form["tel_entidad"]
        correo_entidad = request.form["correo_entidad"]
        pais_entidad = request.form["pais_entidad"]
        depto_entidad = request.form["depto_entidad"]
        mun_entidad = request.form["mun_entidad"]
        cod_habilitacion = request.form["cod_habilitacion"]
        gerente = request.form["gerente"]
        revisor = request.form["revisor"]
        resolucion_dian = request.form["resolucion_dian"]
        n_entidad = request.form["n_entidad"]
        logo_entidad = request.files["logo_entidad"]
        if logo_entidad:
            img_data = logo_entidad.read()

        entidad_service.update_entidad(nit_entidad, digito_nit, nom_entidad, dir_entidad, tel_entidad, correo_entidad,
                                        pais_entidad, depto_entidad, mun_entidad, cod_habilitacion, gerente, revisor,
                                        resolucion_dian, img_data, n_entidad)
        flash("Datos de Entidad actualizado exitosamente","success")
        return redirect(url_for('entidad.entidad'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('entidad.entidad'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('entidad.entidad'))


               