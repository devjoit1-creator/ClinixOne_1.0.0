from app.database import db

#Metodo Listar todos los parametros RDA montados
def listar_parametrosrda():
    parametros = []
    conn = db.connection()
    query = """ SELECT id_parametro, ambiente FROM parametros_rda """
    try: 
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                parametros.append({'id': row[0], 'ambiente': row[1]})

        return parametros

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex

    finally:
        conn.close()

def listar_parametrosrda_prueba():
    parametro = None
    conn = db.connection()
    query =  """ SELECT clientid, clientsecret, tenantid, scope, subskey FROM parametros_rda WHERE id_parametro = 1 """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        parametro = result

    conn.close
    return parametro        

#Metodo Insert Nuevo Parametro RDA
def insert_parametrorda(ambiente, clientid, clientsecret, tenantid, scope, subskey):
    conn = db.connection()
    query = """ INSERT INTO parametros_rda (ambiente, clientid, clientsecret, tenantid, scope, subskey) VALUES (%s, %s, %s, %s, %s, %s) """
    params = (ambiente, clientid, clientsecret, tenantid, scope, subskey)
    try: 
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            conn.close()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex
    
    finally:
        conn.close()

#Metodo Update Parametro RDA
def update_parametrorda(ambiente, clientid, clientsecret, tenantid, scope, subskey, id):
    conn = db.connection()
    query = """ UPDATE parametros_rda SET ambiente = %s, clientid = %s, clientsecret= %s,  tenantid = %s, scope = %s, subskey = %s WHERE id_parametro = %s """
    params = (ambiente, clientid, clientsecret, tenantid, scope, subskey, id)
    try: 
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            conn.close()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex
    
    finally:
        conn.close()

#Metodo Delete Parametro RDA
def delete_parametrorda(id):
    conn = db.connection()
    query = """ DELETE FROM parametros_rda WHERE id_parametro = %s """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (id, ))
            conn.commit()
            conn.close()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise ex
    
    finally:
        conn.close()