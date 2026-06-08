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

#Ruta Metodo guardar nueva entrada de farmacia
@bp_entradasFarmacia.post('/f_addEntrada')
def f_addEntrada():
    #try:
        cod_fuente = request.form["cod_fuente"]
        nro_entrada = request.form["nro_entrada"]
        fecha_entrada = request.form["fecha_entrada"]
        hora_entrada = request.form["hora_entrada"]
        fecha_vencimiento = request.form["fecha_vencimiento"]
        concepto = request.form["concepto"]
        cod_tercero = request.form["cod_tercero"]
        nom_tercero = request.form["nom_tercero"]
        prefijo_remision = request.form["prefijo_remision"]
        nro_remision = request.form["nro_remision"]
        valor_neto = request.form["total"]
        usuario = request.form["usuario"]

        entradas_farmacia_service.insert_entrada(cod_fuente, nro_entrada, fecha_entrada, hora_entrada, fecha_vencimiento, concepto, cod_tercero,
                                                 nom_tercero, prefijo_remision, nro_remision, valor_neto, usuario)
        
        #Detalle Entrada de farmacia
        numero_ent = request.form["nro_entrada"]
        data = request.form.get("data")
        filas = data.split(';')
        for fila in filas:
            if fila.strip():
                bodega, cod_referencia, nom_referencia, registro_invima, lote, cantidad, vlr_unitario, vlr_subtotal, ref_vencimiento, temperatura, riesgo, condicion = fila.split('|')
                bodega_fila = bodega.strip()
                cod_referencia_fila = cod_referencia.strip()
                nom_referencia_fila = nom_referencia.strip()
                registro_invima_fila = registro_invima.strip()
                lote_fila = lote.strip()
                cantidad_fila = cantidad.strip()
                vlr_unitario_fila = vlr_unitario.strip()
                vlr_subtotal_fila = vlr_subtotal.strip()
                ref_vencimiento_fila = ref_vencimiento.strip()
                temperatura_fila = temperatura.strip()
                riesgo_fila = riesgo.strip()
                condicion_fila = condicion.strip()

                entradas_farmacia_service.insert_detalle_entrada(bodega_fila, cod_referencia_fila, nom_referencia_fila, registro_invima_fila, lote_fila,
                                                                 cantidad_fila, vlr_unitario_fila, vlr_subtotal_fila, ref_vencimiento_fila, temperatura_fila, riesgo_fila, condicion_fila, numero_ent)

        flash(f"Entrada de Farmacia No. {nro_entrada} Generada Exitosamente", "success")
        return redirect(url_for('entradasFarmacia.entradas_farmacia'))
    
    #except error.Error as e:
        #flash(f"Se presentó un error ineperado: {e.msg}", "error")
        #return redirect(url_for('entradasFarmacia.entradas_farmacia'))
    
    #except Exception as ex:
        #flash(f"Se presentó un error ineperado: {ex}", "error")
        #return redirect(url_for('entradasFarmacia.entradas_farmacia'))

