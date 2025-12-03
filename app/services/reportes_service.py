from app.database import db

def listar_datos_entidad():
    datos_entidad = None
    conn = db.connection()
    query = "SELECT CONCAT(nit_entidad,'-',digito_nit), nom_entidad, dir_entidad, tel_entidad, \
            correo_entidad, cod_habilitacion, logo_entidad FROM entidad"

    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        datos_entidad = result

    conn.close()
    return datos_entidad            