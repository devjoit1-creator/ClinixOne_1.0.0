from flask import Flask, request, session, flash, render_template
from flask_bcrypt import Bcrypt

# Importando los Blueprints
from app.routes.index_routes import bp_index
from app.routes.deptos_routes import bp_deptos

# Importando los Blueprints Parametrización
from app.routes.entidad_routes import bp_entidad
from app.routes.usuario_routes import bp_usuario
from app.routes.ufuncionales_routes import bp_ufuncionales
from app.routes.tarifas_routes import bp_tarifas
from app.routes.gruposervicios_routes import bp_gruposervicios
from app.routes.servicios_routes import bp_servicios
from app.routes.administradoras_routes import bp_administradoras
from app.routes.medico_routes import bp_medicos
from app.routes.habitaciones_routes import bp_habitaciones
from app.routes.resfacturacion_routes import bp_resfacturacion

# Importando los Blueprints Gestión Medica
from app.routes.paciente_routes import bp_pacientes
from app.routes.consultas_routes import bp_consultas
from app.routes.hospitalizacion_routes import bp_hospitalizacion
from app.routes.anexos_routes import bp_anexos

# Importando los Blueprints Atención Medica
from app.routes.atenciones_routes import bp_atenciones
from app.routes.ordenes_diag_routes import bp_ordenesDiagnosticas
from app.routes.recomendaciones_routes import bp_recomendaciones
from app.routes.incapacidades_routes import bp_incapacidades
from app.routes.interconsultas_routes import bp_interconsultas
from app.routes.nutricion_routes import bp_nutricion
from app.routes.psicologia_routes import bp_psicologia

# Importando los Blueprints Financiero
from app.routes.facturas_routes import bp_facturas
from app.routes.terceros_routes import bp_terceros
from app.routes.plancuentas_routes import bp_plancuentas
from app.routes.fuentes_routes import bp_fuentes
from app.routes.rips_routes import bp_rips
from app.routes.notascredito_routes import bp_notascredito

#BluePrints Pendientes
""" from app.routes.prevaloraciones_routes import prevaloraciones_blueprint

from app.routes.reportes_routes import reportes_blueprint """

# Configuración de la Aplicación
app = Flask(__name__, template_folder='templates')
app.secret_key = 'My_S3cr3t_Key_SIAS'
bcrypt = Bcrypt(app)

# Registro de Blueprint Principal
app.register_blueprint(bp_index)
app.register_blueprint(bp_deptos)

# Registro Blueprints Parametrización
app.register_blueprint(bp_entidad)
app.register_blueprint(bp_usuario)
app.register_blueprint(bp_ufuncionales)
app.register_blueprint(bp_tarifas)
app.register_blueprint(bp_gruposervicios)
app.register_blueprint(bp_servicios)
app.register_blueprint(bp_administradoras)
app.register_blueprint(bp_medicos)
app.register_blueprint(bp_habitaciones)
app.register_blueprint(bp_resfacturacion)

# Registro Blueprints Gestión Medica
app.register_blueprint(bp_pacientes)
app.register_blueprint(bp_consultas)
app.register_blueprint(bp_hospitalizacion)
app.register_blueprint(bp_anexos)

# Registro Blueprints Atención Medica
app.register_blueprint(bp_atenciones)
app.register_blueprint(bp_ordenesDiagnosticas)
app.register_blueprint(bp_recomendaciones)
app.register_blueprint(bp_incapacidades)
app.register_blueprint(bp_interconsultas)
app.register_blueprint(bp_nutricion)
app.register_blueprint(bp_psicologia)

# Registro Blueprints Financiero
app.register_blueprint(bp_facturas)
app.register_blueprint(bp_terceros)
app.register_blueprint(bp_plancuentas)
app.register_blueprint(bp_fuentes)
app.register_blueprint(bp_rips)
app.register_blueprint(bp_notascredito)


#Blueprints Pendientes
""" app.register_blueprint(prevaloraciones_blueprint) """
""" app.register_blueprint(reportes_blueprint) """

#Ruta Metodo para verificar las URL y Redireccionar al Login
@app.before_request
def verificar_peticion():
    ruta = request.path
    if not 'name' in session and ruta != "/" and ruta != "/login_access" and not ruta.startswith("/static"):
        flash("Debe Iniciar Sesión","warning")
        return render_template(('login.html'))

#Instacia de metodo main
if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=5010)
    app.run(debug=True)