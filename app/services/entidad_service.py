from app.database import db

#Metodo para listar el arreglo de la entidad 
def listar_entidad_arr():
    entidad_arr = []
    conn = db.connection()
    query = "SELECT nit_entidad, nom_entidad FROM entidad"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            entidad_arr.append({'nit': row[0], 'nombre': row[1]})

    conn.close()
    return entidad_arr

#Metodo para listar la entidad por el nit
def listar_entidad_nit(nit_entidad):
    entidad = None
    conn = db.connection()
    query = "SELECT * FROM entidad WHERE nit_entidad = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (nit_entidad, ))
        result = cursor.fetchone()
        entidad = result

    conn.close()
    return entidad    

#Metodo para crear una nueva entidad en la bd
def insert_entidad(nit_entidad, digito_nit, nom_entidad, dir_entidad, tel_entidad, correo_entidad,
                     pais_entidad, depto_entidad, mun_entidad, cod_habilitacion, gerente, revisor, resolucion_dian, logo_entidad):
    
    conn = db.connection()
    query = "INSERT INTO entidad (nit_entidad, digito_nit, nom_entidad, dir_entidad, tel_entidad, correo_entidad, \
             pais_entidad, depto_entidad, mun_entidad, cod_habilitacion, gerente, revisor, resolucion_dian, logo_entidad) \
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    params = (nit_entidad, digito_nit, nom_entidad, dir_entidad, tel_entidad, correo_entidad,
              pais_entidad, depto_entidad, mun_entidad, cod_habilitacion, gerente, revisor, resolucion_dian, logo_entidad)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para actualizar los datos de la entidad en bd
def update_entidad(nit_entidad, digito_nit, nom_entidad, dir_entidad, tel_entidad, correo_entidad,
                   pais_entidad, depto_entidad, mun_entidad, cod_habilitacion, gerente, revisor, resolucion_dian, logo_entidad, n_entidad):

    conn = db.connection()
    query = "UPDATE entidad SET nit_entidad = %s, digito_nit = %s, nom_entidad = %s, dir_entidad = %s, tel_entidad = %s, correo_entidad = %s, \
             pais_entidad = %s, depto_entidad = %s, mun_entidad = %s, cod_habilitacion = %s, gerente = %s, revisor = %s, resolucion_dian = %s, \
             logo_entidad = %s WHERE nit_entidad = %s"
    params = (nit_entidad, digito_nit, nom_entidad, dir_entidad, tel_entidad, correo_entidad,
              pais_entidad, depto_entidad, mun_entidad, cod_habilitacion, gerente, revisor, resolucion_dian, logo_entidad, n_entidad)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()         