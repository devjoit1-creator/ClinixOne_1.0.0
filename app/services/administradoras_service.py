from app.database import db

#Función para listar todas las administradoras eapbs
def listar_administradoras():
    administradoras = []
    conn = db.connection()
    query = "SELECT cod_administradora, CONCAT(nit_administradora,'-',digito_verificacion), convenio, nom_administradora FROM administradoras"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            administradoras.append({'codigo': row[0], 'nit': row[1], 'convenio': row[2], 'nombre': row[3]})

    conn.close()
    return administradoras

#Función para listar la administradora eapb por codigo para modificar
def listar_administradora_id(cod_administradora):
    administradora = None
    conn = db.connection()
    query = "SELECT * FROM administradoras WHERE cod_administradora = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_administradora, ))
        result = cursor.fetchone()
        administradora = result

    conn.close()
    return administradora

#Función para listar administradoras en modal
def listar_administradoras_modal():
    administradoras = []
    conn = db.connection()
    query = "SELECT cod_administradora, nit_administradora, nom_administradora FROM administradoras"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            administradoras.append({'codigo': row[0], 'nit': row[1], 'nombre': row[2]})

    conn.close()
    return administradoras        

#Función para insertar la administradora eapb en bd
def insert_administradora(cod_administradora, nit_administradora, digito_verificacion, convenio, nom_administradora,
                          dir_administradora, tel_administradora, cod_rips_adm, tipo_convenio, vigencia_convenio, fecha_inicio_conv,
                          fecha_fin_conv, forma_pago, poblacion, tarifa_adm, plan, plan_beneficios, concepto_recaudo, modalidad_pago):
    
    conn = db.connection()
    query = "INSERT INTO administradoras (cod_administradora, nit_administradora, digito_verificacion, convenio, nom_administradora, \
                          dir_administradora, tel_administradora, cod_rips_adm, tipo_convenio, vigencia_convenio, fecha_inicio_conv, \
                          fecha_fin_conv, forma_pago, poblacion, tarifa_adm, plan, plan_beneficios, concepto_recaudo, modalidad_pago) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    params = (cod_administradora, nit_administradora, digito_verificacion, convenio, nom_administradora,
              dir_administradora, tel_administradora, cod_rips_adm, tipo_convenio, vigencia_convenio, fecha_inicio_conv,
              fecha_fin_conv, forma_pago, poblacion, tarifa_adm, plan, plan_beneficios, concepto_recaudo, modalidad_pago)

    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Función para eliminar la administradora eapb en bd
def delete_administradora(cod_administradora):
    conn = db.connection()
    query = "DELETE FROM administradoras WHERE cod_administradora = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_administradora,))
        conn.commit()
        conn.close()

#Función para actualizar la administradora eapb en bd
def update_administradora(cod_administradora, nit_administradora, digito_verificacion, convenio, nom_administradora,
              dir_administradora, tel_administradora, cod_rips_adm, tipo_convenio, vigencia_convenio, fecha_inicio_conv,
              fecha_fin_conv, forma_pago, poblacion, tarifa_adm, plan, plan_beneficios, concepto_recaudo, modalidad_pago, c_administradora):

    conn = db.connection()
    query = "UPDATE administradoras SET cod_administradora = %s, nit_administradora = %s, digito_verificacion = %s, convenio = %s, \
             nom_administradora = %s, dir_administradora = %s,  tel_administradora = %s, cod_rips_adm = %s, tipo_convenio = %s, vigencia_convenio = %s, \
             fecha_inicio_conv = %s, fecha_fin_conv = %s, forma_pago = %s, poblacion = %s, tarifa_adm = %s, plan = %s, plan_beneficios = %s, concepto_recaudo = %s, modalidad_pago = %s WHERE cod_administradora = %s"

    params = (cod_administradora, nit_administradora, digito_verificacion, convenio, nom_administradora,
              dir_administradora, tel_administradora, cod_rips_adm, tipo_convenio, vigencia_convenio, fecha_inicio_conv,
              fecha_fin_conv, forma_pago, poblacion, tarifa_adm, plan, plan_beneficios, concepto_recaudo, modalidad_pago, c_administradora)

    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()                          
