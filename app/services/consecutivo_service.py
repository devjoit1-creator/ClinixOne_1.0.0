from app.database import db

database_name = "sias"
#Metodo para obtener el consecutivo de fuente de facturación electronica
def listar_consecutivo_fev():
    consecutivo = None
    conn = db.connection()
    query = "SELECT consecutivo from fuentes_contables where cod_fuente = 6"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        consecutivo = result

    conn.close()
    return consecutivo

#Metodo para obtener el consecutivo de fuente de nota credito a clientes/terceros
def listar_coonsecutivo_ncc():
    consecutivo = None
    conn = db.connection()
    query = "SELECT consecutivo from fuentes_contables where cod_fuente = 4"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        consecutivo = result

    conn.close()
    return consecutivo    

""" Consecutivos de Tablas de Atencion """
#Metodo para obtener el consecutivo de atenciones
def listar_consecutivo_atencion():
    consecutivo = None
    conn = db.connection()
    query = """ SELECT numeracion FROM consecutivos WHERE cod_consecutivo = 'AT' """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        consecutivo = result

    conn.close()
    return consecutivo

#Metodo para obtener el consecutivo de fuente entrada de almacen
def listar_consecutivo_ef():
    consecutivo = None
    conn = db.connection()
    query = """ SELECT consecutivo FROM fuentes_contables WHERE cod_fuente = 7 """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        consecutivo = result

    conn.close()
    return consecutivo