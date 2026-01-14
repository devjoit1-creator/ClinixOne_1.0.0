from app.database import db

#Función para listar todas las u. funcionales 
def listar_ufuncionales():
    ufuncionales = []
    conn = db.connection()
    query = "SELECT cod_ufuncional, nom_ufuncional FROM unidades_funcionales"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            ufuncionales.append({"cod_ufuncional": row[0], "nom_ufuncional": row[1]})

    conn.close()
    return ufuncionales

def listar_ufuncionales_hosp():
    ufuncionales = []
    conn = db.connection()
    query = """ SELECT cod_ufuncional, nom_ufuncional FROM unidades_funcionales WHERE cod_ufuncional NOT IN ("CE") """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            ufuncionales.append({"cod_ufuncional": row[0], "nom_ufuncional": row[1]})

    conn.close()
    return ufuncionales        

#Función para listar la u. funcional por codigo
def listar_ufuncional_id(id_ufuncional):
    ufuncional = None
    conn = db.connection()
    query = "SELECT * FROM unidades_funcionales WHERE cod_ufuncional = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_ufuncional,))
        result = cursor.fetchone()
        ufuncional = result

    conn.close()
    return ufuncional                

#Función para insertar u. funcional en bd
def insertar_ufuncional(cod_ufuncional, nom_ufuncional):
    conn = db.connection()
    query = "INSERT INTO unidades_funcionales (cod_ufuncional, nom_ufuncional) VALUES (%s, %s)"
    params = (cod_ufuncional, nom_ufuncional)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Función para eliminar u. funcional en bd
def delete_ufuncional(id_ufuncional):
    conn = db.connection()
    query = "DELETE FROM unidades_funcionales WHERE cod_ufuncional = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_ufuncional, ))
        conn.commit()
        conn.close()

#Función para actualizar u. funcional en bd
def update_ufuncional(cod_ufuncional, nom_ufuncional, cufuncional):        
    conn = db.connection()
    query = "UPDATE unidades_funcionales SET cod_ufuncional=%s, nom_ufuncional=%s WHERE cod_ufuncional=%s"
    params = (cod_ufuncional, nom_ufuncional, cufuncional)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()
