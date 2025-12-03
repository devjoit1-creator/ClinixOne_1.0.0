from app.database import db

#Metodo para insertar nueva cuenta contable en bd
def insert_cuenta(cod_cuenta, nom_cuenta, clasificacion, naturaleza):
    conn = db.connection()
    query = "INSERT INTO cuentas (cod_cuenta, nom_cuenta, clasificacion, naturaleza) VALUES (%s, %s, %s, %s)"
    params = (cod_cuenta, nom_cuenta, clasificacion, naturaleza)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para actualizar datos de cuenta contable en bd
def update_cuenta(nom_cuenta, clasificacion, naturaleza, cod_cuenta):
    conn = db.connection()
    query = "UPDATE cuentas SET nom_cuenta = %s, clasificacion = %s, naturaleza = %s WHERE cod_cuenta = %s"
    params = (nom_cuenta, clasificacion, naturaleza, cod_cuenta)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para eliminar cuenta contable en bd
def delete_cuenta(cod_cuenta):
    conn = db.connection()
    query = "DELETE FROM cuentas WHERE cod_cuenta = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_cuenta, ))
        conn.commit()
        conn.close() 

#Metodo para listar todas las cuentas contables en la bd
def listar_cuentas():
    cuentas = []
    conn = db.connection()
    query = "SELECT cod_cuenta, nom_cuenta, clasificacion, naturaleza FROM cuentas"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            cuentas.append({'cod_cuenta':row[0], 'nom_cuenta':row[1], 'clasificacion':row[2], 'naturaleza':row[3]})

    conn.close()
    return cuentas

#Metodo para listar datos de cuenta contable por codigo 
def listar_cuenta(cod_cuenta):
    cuenta = None
    conn = db.connection()
    query = "SELECT * FROM cuentas WHERE cod_cuenta = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_cuenta, ))
        result = cursor.fetchone()
        cuenta = result

    conn.close()
    return cuenta                                   