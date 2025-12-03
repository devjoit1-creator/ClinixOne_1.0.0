from flask import Blueprint, render_template, redirect, request ,flash, url_for, jsonify
from app.services import paciente_service, departamentos, escolaridad, etnias

import mysql.connector.errors

bp_pacientes = Blueprint('pacientes', __name__)
error = mysql.connector.errors

#Ruta Blueprint para mostrar todos los usuarios listados en template
@bp_pacientes.get('/pacientes')
def pacientes():
    pacs = paciente_service.listar_pacientes()
    return render_template('temp_pacientes/pacientes.html', pacs = pacs)

#Ruta Blueprint para mostrar formulario para agregar un nuevo paciente
@bp_pacientes.get('/add_paciente')
def add_paciente():
    #Listado de Deptos, Municipios, Paises
    deptos = departamentos.listar_departamentos()
    #munic = departamentos.listar_municipios()
    pais = departamentos.listar_paises()

    #Listado de Escolaridad, Ocupación, Etnias
    niveles = escolaridad.listar_educacion()
    ocupaciones = escolaridad.listar_ocupacion()
    etnia = etnias.listar_etnias()

    return render_template('temp_pacientes/add_paciente.html', deptos = deptos, pais = pais, niveles = niveles, ocupaciones = ocupaciones, etnia = etnia )

#Ruta Blueprint para procesar formulario de agregar un nuevo pacciente y guardarlo en la base de datos
@bp_pacientes.post('/f_addPaciente')
def f_addPaciente():
    try:
        tipoDoc = request.form["tipoDoc"]
        numDoc = request.form["numDoc"]
        papellido = request.form["papellido"]
        sapellido = request.form["sapellido"]
        pnombre = request.form["pnombre"]
        snombre = request.form["snombre"]
        fechaNac = request.form["fechaNac"]
        edad = request.form["edad"]
        tipo_edad = request.form["tipo_edad"]
        sexo = request.form["sexo"]
        direccion = request.form["direccion"]
        telefono = request.form["telefono"]
        movil = request.form["movil"]
        barrio = request.form["barrio"]
        zona = request.form["zona"]
        depto = request.form["depto"]
        nom_depto = request.form["nom_depto"]
        munic = request.form["munic"]
        nom_munic = request.form["nom_munic"]
        nacionalidad = request.form["nacionalidad"]
        pais = request.form["pais"]
        paisRes = request.form["paisRes"]
        correo = request.form["correo"]
        estCivil = request.form["estCivil"]
        nivelEdu = request.form["nivelEdu"]
        ocupacion = request.form["ocupacion"]
        acompanante = request.form["acompanante"]
        telAcompanante = request.form["telAcompanante"]
        parentAcompanante = request.form["parentAcompanante"]
        responsable = request.form["responsable"]
        telResponsable = request.form["telResponsable"]
        parentResponsable = request.form["parentResponsable"]
        religion = request.form["religion"]
        etnia = request.form["etnia"]
        regimen = request.form["regimen"]
        afiliacion = request.form["afiliacion"]
        nivel_afi = request.form["nivel_afi"]
        tipo_paciente = request.form["tipo_paciente"]

        paciente_service.insert_paciente(tipoDoc,numDoc,papellido,sapellido,pnombre,snombre,fechaNac,edad,tipo_edad,
                                sexo,direccion,telefono,movil,barrio,zona,depto,nom_depto,munic,nom_munic,nacionalidad,pais,paisRes,correo,estCivil,nivelEdu,ocupacion,
                                acompanante,telAcompanante,parentAcompanante,responsable,telResponsable,parentResponsable,religion,etnia,
                                regimen,afiliacion,nivel_afi,tipo_paciente)
        flash("Paciente Agregado Exitosamente","success")
        return redirect(url_for('pacientes.pacientes'))
    
    except error.Error as e:
        flash(f"Se presentó error: {e.msg}","error")
        return redirect(url_for('pacientes.pacientes'))
    
#Ruta Blueprint para eliminar paciente de la base de datos
@bp_pacientes.route('/drop_Paciente/<int:id>')
def drop_Paciente(id):
    try:
        paciente_service.delete_paciente(id)
        flash("Paciente Eliminado","success")
        return redirect(url_for('pacientes.pacientes'))

    except error.Error as e:
        flash(f"Se presentó un error: {e.msg}", "error")
        return redirect(url_for('pacientes.pacientes'))

#Ruta Blueprint para listar los datos de paciente por ID de la base de datos
@bp_pacientes.get('/edit_paciente/<int:id>')
def edit_paciente(id):
    try:
        pac = paciente_service.listar_paciente_id(id)
        #Listado de Deptos, Municipios, Paises
        deptos = departamentos.listar_departamentos()
        #munic = departamentos.listar_municipios()
        paises = departamentos.listar_paises()

        #Listado de Escolaridad, Ocupación, Etnias
        niveles = escolaridad.listar_educacion()
        ocupaciones = escolaridad.listar_ocupacion()
        etnia = etnias.listar_etnias()
    
        return render_template('temp_pacientes/edit_paciente.html', pac = pac, deptos = deptos, paises = paises, niveles = niveles, ocupaciones = ocupaciones, etnia = etnia)
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('administradoras.administradoras'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('administradoras.administradoras'))    

#Ruta Blueprint para procesar formulario de edición de paciente y actualizarlo en la base de datos
@bp_pacientes.post('/f_updatePaciente')
def f_updatePaciente():
    try:
        tipoDoc = request.form["tipoDoc"]
        numDoc = request.form["numDoc"]
        papellido = request.form["papellido"]
        sapellido = request.form["sapellido"]
        pnombre = request.form["pnombre"]
        snombre = request.form["snombre"]
        fechaNac = request.form["fechaNac"]
        edad = request.form["edad"]
        tipo_edad = request.form["tipo_edad"]
        sexo = request.form["sexo"]
        direccion = request.form["direccion"]
        telefono = request.form["telefono"]
        movil = request.form["movil"]
        barrio = request.form["barrio"]
        zona = request.form["zona"]
        depto = request.form["depto"]
        nom_depto = request.form["nom_depto"]
        munic = request.form["munic"]
        nom_munic = request.form["nom_munic"]
        nacionalidad = request.form["nacionalidad"]
        pais = request.form["pais"]
        paisRes = request.form["paisRes"]
        correo = request.form["correo"]
        estCivil = request.form["estCivil"]
        nivelEdu = request.form["nivelEdu"]
        ocupacion = request.form["ocupacion"]
        acompanante = request.form["acompanante"]
        telAcompanante = request.form["telAcompanante"]
        parentAcompanante = request.form["parentAcompanante"]
        responsable = request.form["responsable"]
        telResponsable = request.form["telResponsable"]
        parentResponsable = request.form["parentResponsable"]
        religion = request.form["religion"]
        etnia = request.form["etnia"]
        regimen = request.form["regimen"]
        afiliacion = request.form["afiliacion"]
        nivel_afi = request.form["nivel_afi"]
        idPaciente = request.form["idPaciente"]

        paciente_service.update_paciente(tipoDoc,numDoc,papellido,sapellido,pnombre,snombre,fechaNac,edad,tipo_edad,
                                sexo,direccion,telefono,movil,barrio,zona,depto,nom_depto,munic,nom_munic,nacionalidad,pais,paisRes,correo,estCivil,nivelEdu,ocupacion,
                                acompanante,telAcompanante,parentAcompanante,responsable,telResponsable,parentResponsable,religion,etnia,
                                regimen,afiliacion,nivel_afi, idPaciente)
        flash("Datos de paciente actualizados exitosamente","success")
        return redirect(url_for('pacientes.pacientes'))
        
    except error.Error as e:
        flash(f"Se presentó un error: {e.msg}", "error")
        return redirect(url_for('pacientes.pacientes'))
    
#Ruta AJAX para obtener el regimen del paciente por documento
@bp_pacientes.post('/get_regimen_paciente')
def get_regimen_paciente():
    try:
        data = request.get_json()
        num_doc = data.get("numDoc")
        regimen = paciente_service.listar_regimen_paciente(num_doc)

        if regimen:
            return jsonify(regimen)

    except error.Error as e:
        return jsonify(e.msg)

    except Exception as ex:
        return jsonify(ex)
    
#Ruta Ajax Para obtener datos del paciente como cliente (Facturación)   
@bp_pacientes.post('/get_paciente')
def get_paciente():
    data = request.get_json()
    cod_paciente = data.get("cod_paciente")
    #cod_paciente = request.form["cod_paciente"] jquery

    paciente = paciente_service.listar_paciente_doc(cod_paciente)
    if paciente:
        return jsonify(paciente)    