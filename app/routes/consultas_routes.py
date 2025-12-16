from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import paciente_service, administradoras_service, causas_service, finalidadconsulta_service, medico_service, ufuncionales_service, diagnosticos_cie10, gruposervicios_service, servicios_service, consultas_service, fuentes_service, consecutivo_service, terceros_service
import mysql.connector.errors as error

bp_consultas = Blueprint('consultas', __name__)

@bp_consultas.get('/consultas')
def consultas():
    try:
        consultas = consultas_service.listar_consultas()
        return render_template('temp_consultas/consultas.html', consultas = consultas)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('consultas.consultas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('consultas.consultas'))

#Ruta AJAX para obtener los datos de consulta por numero de Atención
@bp_consultas.post('/getAtencionConsulta')
def getAtencionConsulta():
    try:
        data = request.get_json()
        atencion = data.get("atencion")
        consultas = consultas_service.listar_consultas_atencion(atencion)
        if consultas:
            return jsonify(consultas)
        else:
            return jsonify({"Error": "No se encontraron registros."}), 200
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500

    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500    

@bp_consultas.get('/add_consulta')
def add_consulta():
    try:
        atencion = consecutivo_service.listar_consecutivo_atencion()
        consecutivo = consultas_service.listar_consecutivo_consulta()
        pacientes = paciente_service.listar_pacientes_modal()
        administradoras = administradoras_service.listar_administradoras_modal()
        causas = causas_service.listar_causas()
        finalidades = finalidadconsulta_service.listar_finalidad_consulta()
        medicos = medico_service.listar_medicos()
        unidades = ufuncionales_service.listar_ufuncionales()
        diagnosticos = diagnosticos_cie10.listar_diagnosticos()
        servicio_asoc = gruposervicios_service.listar_serv_ce()
        servicios = servicios_service.listar_servicios()
        return render_template('temp_consultas/add_consulta.html', atencion = atencion, consecutivo = consecutivo, pacientes = pacientes, administradoras = administradoras, causas = causas, finalidades = finalidades, medicos = medicos, unidades = unidades, diagnosticos = diagnosticos, servicios = servicios, servicio_asoc = servicio_asoc)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('consultas.consultas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('consultas.consultas'))
    
@bp_consultas.post('/f_addConsulta')
def f_addConsulta():
    try:
        """ Request para insert de la consulta """
        atencion = request.form["atencion"]
        codigo = request.form["codigo"]
        fecha_atencion = request.form["fecha_atencion"]
        hora_atencion = request.form["hora_atencion"]
        fecha_salida = request.form["fecha_salida"]
        hora_salida = request.form["hora_salida"]
        cod_admin = request.form["cod_admin"]
        nit_admin = request.form["nit_admin"]
        plan_beneficios = request.form["plan_beneficios"]
        concepto_recaudo = request.form["concepto_recaudo"]
        via_ingreso = request.form["via_ingreso"]
        causa_externa = request.form["causa_externa"]
        finalidad_consulta = request.form["finalidad_consulta"]
        clase_consulta = request.form["clase_consulta"]
        medico = request.form["medico"]
        und_funcional = request.form["und_funcional"]
        cod_diag1 = request.form["cod_diag1"]
        nom_diag1 = request.form["nom_diag1"]
        cod_diag2 = request.form["cod_diag2"]
        nom_diag2 = request.form["nom_diag2"]
        cod_diag3 = request.form["cod_diag3"]
        nom_diag3 = request.form["nom_diag3"]
        cod_diag4 = request.form["cod_diag4"]
        nom_diag4 = request.form["nom_diag4"]
        tipo_diag = request.form["tipo_diag"]
        modalidad = request.form["modalidad"]
        servicio_consulta = request.form["servicio_consulta"]
        nro_autorizacion = request.form["nro_autorizacion"]
        total_servicios = request.form["total_servicios"]
        usuario = request.form["usuario"]

        consultas_service.insert_consulta(atencion, codigo, fecha_atencion, hora_atencion, fecha_salida, hora_salida, cod_admin, nit_admin, plan_beneficios, concepto_recaudo,
                                            via_ingreso, causa_externa, finalidad_consulta, clase_consulta, medico, und_funcional, cod_diag1, nom_diag1, cod_diag2, nom_diag2,
                                            cod_diag3, nom_diag3, cod_diag4, nom_diag4, tipo_diag, modalidad, servicio_consulta, nro_autorizacion, total_servicios, usuario)
        
        """ Request para insert de detalle servicios de la consulta """
        #id_consulta = request.form["id_consulta"]
        data = request.form.get("data")
        filas = data.split(';')
        for fila in filas:
            if fila.strip():
                u_funcional, cod_serv, nom_serv, valor_serv, cantidad, total_serv, nro_autorizacion = fila.split('-')
                u_funcional_fila = u_funcional.strip()
                cod_serv_fila = cod_serv.strip()
                nom_serv_fila = nom_serv.strip()
                valor_serv_fila = valor_serv.strip()
                cantidad_fila = cantidad.strip()
                total_serv_fila = total_serv.strip()
                nro_autorizacion_fila = nro_autorizacion.strip()
                consultas_service.insert_detalle_consulta(u_funcional_fila, cod_serv_fila, nom_serv_fila, valor_serv_fila, cantidad_fila, total_serv_fila, nro_autorizacion_fila, atencion)
        
        flash(f"Consulta Habilitada. El paciente puede ser atendido","success")
        return redirect(url_for('consultas.consultas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('consultas.consultas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('consultas.consultas'))

@bp_consultas.route('/drop_consulta/<int:atencion>')
def drop_consulta(atencion):
    try:
        consultas_service.delete_consulta(atencion)
        consultas_service.delete_detalle_consulta(atencion)
        flash("Consulta Anulada Exitosamente", "success")
        return redirect(url_for('consultas.consultas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('consultas.consultas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('consultas.consultas'))

@bp_consultas.get('/edit_consulta/<int:id>')
def edit_consulta(id):
    try:
        pacientes = paciente_service.listar_pacientes_modal()
        administradoras = administradoras_service.listar_administradoras_modal()
        causas = causas_service.listar_causas()
        medicos = medico_service.listar_medicos()
        unidades = ufuncionales_service.listar_ufuncionales()
        diagnosticos = diagnosticos_cie10.listar_diagnosticos()
        servicios = servicios_service.listar_servicios()

        consulta = consultas_service.listar_consultas_id(id)
        dato_pac = paciente_service.listar_paciente_doc(consulta[1])
        return render_template('temp_consultas/edit_consulta.html', consulta = consulta, pacientes = pacientes, administradoras = administradoras, causas = causas, medicos = medicos, unidades = unidades, diagnosticos = diagnosticos, servicios = servicios, dato_pac = dato_pac)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}","error")
        return redirect(url_for('consultas.consultas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}","error")
        return redirect(url_for('consultas.consultas'))

#Ruta Ventana para Mostrar Formulario de Generación de Factura por Consulta Externa    
@bp_consultas.get('/generar_factura_consulta/<int:id>')
def generar_factura_consulta(id):
    fuentes = fuentes_service.listar_fuente_fe()
    consecutivo = consecutivo_service.listar_consecutivo_fev()
    consulta = consultas_service.listar_consultas_id(id)
    dato_pac = paciente_service.listar_paciente_doc(consulta[2])
    administradora = administradoras_service.listar_administradora_id(consulta[7])
    servicios = consultas_service.listar_detalle_consulta_id(id)
    return render_template('temp_consultas/generar_factura_consulta.html', fuentes = fuentes, consecutivo = consecutivo, consulta = consulta, dato_pac = dato_pac, administradora = administradora, servicios = servicios)