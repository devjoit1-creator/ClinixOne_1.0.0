from app.database import db

def insert_paciente(tipo_doc, num_doc, p_apellido, s_apellido, p_nombre, s_nombre, fecha_nac,
                    edad, tipo_edad, sexo, direccion, telefono, movil, barrio, zona, depto, nom_depto, munic, nom_munic, nacionalidad,
                    pais, pais_res, email, est_civil, nivel_edu ,ocupacion, acompanante, tel_acompanante, parent_acompanante,
                    responsable, tel_responsable, parent_responsable, religion, etnia, regimen, afiliacion, nivel_afil, tipo_paciente):
    conn = db.connection()
    query = "INSERT INTO pacientes (tipo_doc, num_doc, p_apellido, s_apellido, p_nombre, s_nombre, fecha_nac,\
                    edad, tipo_edad, sexo, direccion, telefono, movil, barrio, zona, depto, nom_depto, munic, nom_munic, nacionalidad,\
                    pais, pais_res, email, est_civil, nivel_edu, ocupacion, acompanante, tel_acompanante, parent_acompanante,\
                    responsable, tel_responsable, parent_responsable, religion, etnia, regimen, afiliacion, nivel_afil, tipo_paciente) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    params = (tipo_doc, num_doc, p_apellido, s_apellido, p_nombre, s_nombre, fecha_nac,
              edad, tipo_edad, sexo, direccion, telefono, movil, barrio, zona, depto, nom_depto, munic, nom_munic, nacionalidad,
              pais, pais_res, email, est_civil, nivel_edu ,ocupacion, acompanante, tel_acompanante, parent_acompanante,
              responsable, tel_responsable, parent_responsable, religion, etnia, regimen, afiliacion, nivel_afil, tipo_paciente)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def listar_pacientes():
    pacientes = []
    conn = db.connection()
    query = "SELECT * FROM pacientes"
    with conn.cursor() as cursor:
        cursor.execute(query)
        resultado = cursor.fetchall()
        for row in resultado:
            pacientes.append({'id': row[0],'tipo_doc': row[1], 'num_doc': row[2], 'p_apellido': row[3], 's_apellido': row[4],
                              'p_nombre': row[5], 's_nombre': row[6]})

    conn.close()
    return pacientes

def listar_paciente_id(id):
    paciente = None
    conn = db.connection()
    query = "SELECT * FROM pacientes WHERE id_paciente = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id, )) 
        resultado = cursor.fetchone()
        paciente = resultado
        """ if resultado:
            columns = [desc[0] for desc in cursor.description]
            paciente = dict(zip(columns, resultado))
        else:
            paciente = None """
        
    conn.close()
    return paciente

def listar_paciente_doc(num_doc):
    paciente = None
    conn = db.connection()
    query = "SELECT tipo_doc, num_doc, CONCAT(p_nombre,' ',s_nombre,' ',p_apellido,' ',s_apellido), fecha_nac, \
             CASE \
                WHEN est_civil = 1 THEN 'SOLTERO(A)' \
                WHEN est_civil = 2 THEN 'CASADO(A)' \
                WHEN est_civil = 3 THEN 'SEPARADO(A)' \
                WHEN est_civil = 4 THEN 'VIUDO(A)' \
                WHEN est_civil = 5 THEN 'UNIÓN LIBRE' \
             END, acompanante, \
             CASE \
                WHEN sexo = 1 THEN 'MASCULINO' \
                WHEN sexo = 2 THEN 'FEMENINO' \
                WHEN sexo = 3 THEN 'INDETERMINADO' \
             END, \
             ocupacion, tel_acompanante, direccion, telefono, responsable, nom_munic, parent_acompanante, tel_responsable, email FROM pacientes WHERE num_doc = %s" 
    

    with conn.cursor() as cursor:
        cursor.execute(query, (num_doc, )) 
        resultado = cursor.fetchone()
        paciente = resultado

    conn.close()
    return paciente      

def delete_paciente(id):
    conn = db.connection()
    query = "DELETE FROM pacientes WHERE id_paciente = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id, ))
        conn.commit()
        conn.close()                

def update_paciente(tipo_doc, num_doc, p_apellido, s_apellido, p_nombre, s_nombre, fecha_nac,
              edad, tipo_edad, sexo, direccion, telefono, movil, barrio, zona, depto, nom_depto, munic, nom_munic, nacionalidad,
              pais, pais_res, email, est_civil, nivel_edu ,ocupacion, acompanante, tel_acompanante, parent_acompanante,
              responsable, tel_responsable, parent_responsable, religion, etnia, regimen, afiliacion, nivel_afil, id):
    
    conn = db.connection()
    
    query = "UPDATE pacientes SET tipo_doc = %s, num_doc = %s, p_apellido = %s, s_apellido = %s, p_nombre = %s, s_nombre = %s, fecha_nac = %s, \
                    edad = %s, tipo_edad = %s, sexo = %s, direccion = %s, telefono = %s, movil = %s, barrio = %s, zona = %s, depto = %s, nom_depto = %s, munic = %s, nom_munic = %s, nacionalidad = %s,\
                    pais = %s, pais_res = %s, email = %s, est_civil = %s, nivel_edu = %s, ocupacion = %s, acompanante = %s, tel_acompanante = %s, parent_acompanante = %s,\
                    responsable = %s, tel_responsable = %s, parent_responsable = %s, religion = %s, etnia = %s, regimen = %s, afiliacion = %s, nivel_afil = %s WHERE id_paciente = %s"
    
    params = (tipo_doc, num_doc, p_apellido, s_apellido, p_nombre, s_nombre, fecha_nac,
              edad, tipo_edad, sexo, direccion, telefono, movil, barrio, zona, depto, nom_depto, munic, nom_munic, nacionalidad,
              pais, pais_res, email, est_civil, nivel_edu ,ocupacion, acompanante, tel_acompanante, parent_acompanante,
              responsable, tel_responsable, parent_responsable, religion, etnia, regimen, afiliacion, nivel_afil, id)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def listar_pacientes_modal():
    pacientes = []
    conn = db.connection()
    query = "SELECT tipo_doc, num_doc, CONCAT(p_apellido,' ',s_apellido,' ',p_nombre,' ',s_nombre) FROM pacientes"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            pacientes.append({'tipo': row[0], 'documento': row[1], 'nombre': row[2]})

    conn.close()
    return pacientes

#Metodo para listar regimen de paciente
def listar_regimen_paciente(num_doc):
    regimen = None
    conn = db.connection()
    query = """ SELECT p.regimen as cod_regimen,
                CASE
                    WHEN p.regimen = '01' THEN 'Contributivo cotizante'
                    WHEN p.regimen = '02' THEN 'Contributivo beneficiario'
                    WHEN p.regimen = '03' THEN 'Contributivo adicional'
                    WHEN p.regimen = '04' THEN 'Subsidiado'
                    WHEN p.regimen = '05' THEN 'No afiliado'
                    WHEN p.regimen = '06' THEN 'Especial o Excepcion cotizante'
                    WHEN p.regimen = '07' THEN 'Especial o Excepcion beneficiario'
                    WHEN p.regimen = '08' THEN 'Personas privadas de la libertad a cargo del Fondo Nacional de Salud'
                    WHEN p.regimen = '09' THEN 'Tomador / Amparado ARL'
                    WHEN p.regimen = '10' THEN 'Tomador / Amparado SOAT'
                    WHEN p.regimen = '11' THEN 'Tomador / Amparado Planes voluntarios de salud'
                    WHEN p.regimen = '12' THEN 'Particular'
                    WHEN p.regimen = '13' THEN 'Especial o Exepcion no cotizante Ley 352 de 1997'
                END as nom_regimen
                FROM pacientes p
                WHERE p.num_doc = %s """
    
    with conn.cursor() as cursor:
        cursor.execute(query, (num_doc, ))
        result = cursor.fetchone()
        regimen = result

    conn.close()
    return regimen    