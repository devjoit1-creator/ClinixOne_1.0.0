from app.database import db

#Metodo para Listar todas las coberturas
def listar_coberturas():
    coberturas = []
    conn = db.connection()
    query = """ SELECT cod_cobertura, nom_cobertura FROM cobertura_administradoras """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            coberturas.append({'cod_cobertura': row[0], 'nom_cobertura': row[1]})

    conn.close()
    return coberturas

#Metodo para Listar todas las coberturas por administradora
def listar_cobertura_admin(cod_administradora):
    cobertura = None
    conn = db.connection()
    query = """ SELECT ca.cod_cobertura, ca.nom_cobertura FROM cobertura_administradoras ca, administradoras a WHERE ca.cod_cobertura = a.plan_beneficios 
                AND a.cod_administradora = %s """
    
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_administradora, ))
        result = cursor.fetchone()
        cobertura = result

    conn.close()
    return cobertura

#Metodo para listar todos los conceptos de recaudo
def listar_conceptos():
    conceptos = []
    conn = db.connection()
    query = """ SELECT cod_concepto, nom_concepto FROM concepto_recaudo_administradoras """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            conceptos.append({'cod_concepto': row[0], 'nom_concepto': row[1]})

    conn.close()
    return conceptos

#Metodo para Listar todos los conceptos por administradora
def listar_concepto_admin(cod_administradora):
    concepto = None
    conn = db.connection()
    query = """ SELECT cra.cod_concepto, cra.nom_concepto FROM concepto_recaudo_administradoras cra, administradoras a WHERE cra.cod_concepto = a.concepto_recaudo 
                AND a.cod_administradora = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_administradora, ))
        result = cursor.fetchone()
        concepto = result

    conn.close()
    return concepto

#Metodo para listar todas las modalidades de pago
def listar_modalidades():
    modalidades = []
    conn = db.connection()
    query = """ SELECT cod_modalidad, nom_modalidad FROM modalidad_pago_administradoras """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            modalidades.append({'cod_modalidad': row[0], 'nom_modalidad': row[1]})

    conn.close()
    return modalidades        