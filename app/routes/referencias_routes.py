from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import formas_farmihce_service, referencias_service
import mysql.connector.errors as error

bp_referencias = Blueprint('referencias', __name__)

#Ruta Ventana Referencias
@bp_referencias.get('/referencias')
def referencias():
    return render_template('temp_referencias/referencias.html')

#Ruta Ventana Nueva Referencia
@bp_referencias.get('/add_referencia')
def add_referencia():
    formas = formas_farmihce_service.listar_formas_ihce()
    return render_template('temp_referencias/add_referencia.html', formas = formas)

#Ruta Metodo Guardar Referencia
@bp_referencias.post('/f_addReferencia')
def f_addReferencia():
    try:
        cod_referencia = request.form["cod_referencia"]
        nom_referencia = request.form["nom_referencia"]
        principio_activo = request.form["principio_activo"]
        nom_comercial_ref = request.form["nom_comercial_ref"]
        unidad_medida = request.form["unidad_medida"]
        concentracion = request.form["concentracion"]
        forma_farm = request.form["forma_farm"]
        forma_farm_ihce = request.form["forma_farm_ihce"]
        laboratorio = request.form["laboratorio"]
        presentacion = request.form["presentacion"]
        grupo_referencia = request.form["grupo_referencia"]
        registro_invima = request.form["registro_invima"]
        tipo_referencia = request.form["tipo_referencia"]
        regulado = request.form["regulado"]
        serie_referencia = request.form["serie_referencia"]
        expediente_sanitario = request.form["expediente_sanitario"]
        consecutivo_exp = request.form["consecutivo_exp"]
        codigo_atc = request.form["codigo_atc"]
        codigo_cum = request.form["codigo_cum"]
        codigo_rips = request.form["codigo_rips"]
        stock_minimo = request.form["stock_minimo"]
        stock_maximo = request.form["stock_maximo"]
        dispensacion_minima = request.form["dispensacion_minima"]
        dispensacion_maxima = request.form["dispensacion_maxima"]
        cantidad = request.form["cantidad"]
        iva = request.form["iva"]
        descuento = request.form["descuento"]

        referencias_service.insert_referencia(cod_referencia, nom_referencia, principio_activo, nom_comercial_ref, unidad_medida, concentracion,
                                              forma_farm, forma_farm_ihce, laboratorio, presentacion, grupo_referencia, registro_invima, tipo_referencia,
                                              regulado, serie_referencia, expediente_sanitario, consecutivo_exp, codigo_atc, codigo_cum, codigo_rips,
                                              stock_minimo, stock_maximo, dispensacion_minima, dispensacion_maxima, cantidad, iva, descuento)
        
        flash("Referencia Creada Exitosamente", "success")
        return redirect(url_for('referencias.referencias'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('referencias.referencias'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('referencias.referencias'))