from app.database import db

#Metodo para insertar un nuevo tercero en bd
def insert_tercero(tipo_idf, identificacion, digito_verf, nom_tercero, dir_tercero, tel_tercero, tipo_tercero, correo, cod_depto_tercero, nom_depto_tercero,
                   cod_munic_tercero, nom_munic_tercero):
    conn = db.connection()
    query = """ INSERT INTO terceros (tipo_idf, identificacion, digito_verf, nom_tercero, dir_tercero, tel_tercero, tipo_tercero, correo, cod_depto_tercero, 
                nom_depto_tercero, cod_munic_tercero, nom_munic_tercero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
    params = (tipo_idf, identificacion, digito_verf, nom_tercero, dir_tercero, tel_tercero, tipo_tercero, correo, cod_depto_tercero, nom_depto_tercero, 
              cod_munic_tercero, nom_munic_tercero)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para actualizar datos del tercero en la bd
def update_tercero(tipo_idf, identificacion, digito_verf, nom_tercero, dir_tercero, tel_tercero, tipo_tercero, correo, cod_depto_tercero, 
                   nom_depto_tercero, cod_munic_tercero, nom_munic_tercero, id_tercero):
    conn = db.connection()
    query = """ UPDATE terceros SET tipo_idf = %s, identificacion = %s, digito_verf = %s, nom_tercero = %s, dir_tercero = %s, tel_tercero = %s, tipo_tercero = %s ,correo = %s, 
    cod_depto_tercero = %s, nom_depto_tercero = %s, cod_munic_tercero = %s, nom_munic_tercero = %s WHERE id_tercero = %s """
    params = (tipo_idf, identificacion, digito_verf, nom_tercero, dir_tercero, tel_tercero, tipo_tercero, correo, 
              cod_depto_tercero, nom_depto_tercero, cod_munic_tercero, nom_munic_tercero, id_tercero)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para eliminar tercero de la bd
def delete_tercero(id_tercero):
    conn = db.connection()
    query = "DELETE FROM terceros WHERE id_tercero = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_tercero, ))
        conn.commit()
        conn.close()        

#Metodo para listar todos los terceros en la bd
def listar_terceros():
    terceros = []
    conn = db.connection()
    query = "SELECT id_tercero, tipo_idf, concat(identificacion,'-',digito_verf), nom_tercero, dir_tercero, tel_tercero, correo FROM terceros"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            terceros.append({'id_tercero': row[0], 'tipo_idf': row[1], 'identificacion': row[2], 'nom_tercero': row[3], 'dir_tercero': row[4], 'tel_tercero': row[5], 'correo': row[6]})

    conn.close()
    return terceros

#Metodo para listar tercero por id
def listar_tercero_id(id_tercero):
    tercero = None
    conn = db.connection()
    query = "SELECT * FROM terceros WHERE id_tercero = %s"
    with conn.cursor() as cursor: 
        cursor.execute(query, (id_tercero, ))
        result = cursor.fetchone()
        tercero = result

    conn.close()
    return tercero      

#Metodo para listar tercero por nit
def listar_tercero_nit(identificacion):
    tercero = None
    conn = db.connection()
    query = "SELECT * FROM terceros WHERE identificacion = %s"
    with conn.cursor() as cursor: 
        cursor.execute(query, (identificacion, ))
        result = cursor.fetchone()
        tercero = result

    conn.close()
    return tercero                  