from app.database import db

def listar_cargos_asistenciales():
    cargos = []
    conn = db.connection()
    query = "SELECT id_cargo_asistencial, nom_cargo_asistencial FROM cargo_asistencial"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            cargos.append({'id_cargo_asistencial': row[0], 'nom_cargo_asistencial': row[1]})

    conn.close()
    return cargos

def listar_medicos():
    medicos = []
    conn = db.connection()
    query = "SELECT * FROM medicos"
    with conn.cursor() as cursor:
        cursor.execute(query)
        resultado = cursor.fetchall()
        for row in resultado:
            medicos.append({'id_medico': row[0], 'tipo_documento': row[1], 'num_documento': row[2], 'nombre_completo': row[7], 'cargo': row[11]})
            
    conn.close()
    return medicos

def listar_medico_id(id_medico):
    medico = None
    conn = db.connection()
    query = "SELECT * FROM medicos WHERE id_medico = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_medico, )) 
        resultado = cursor.fetchone()
        medico = resultado

    conn.close()
    return medico

def listar_medico_firma(num_documento):
    medico = None
    conn = db.connection()
    query = "SELECT firma_medico, nombre_completo, nom_cargo, num_documento, registro_medico FROM medicos WHERE num_documento = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (num_documento, ))
        resultado = cursor.fetchone()
        medico = resultado

    conn.close()
    return medico    

def insert_medico(tipo_documento, num_documento, p_nombre, s_nombre, p_apellido, s_apellido, nombre_completo,
                  direccion, telefono, cod_cargo, nom_cargo, registro_medico, consultorio, firma_medico):
    conn = db.connection()
    query = "INSERT INTO medicos (tipo_documento, num_documento, p_nombre, s_nombre, p_apellido, s_apellido, \
             nombre_completo, direccion, telefono, cod_cargo, nom_cargo, registro_medico, consultorio, firma_medico) \
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    params = (tipo_documento, num_documento, p_nombre, s_nombre, p_apellido, s_apellido, nombre_completo,
              direccion, telefono, cod_cargo, nom_cargo, registro_medico, consultorio, firma_medico)

    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

def delete_medico(id_medico):
    conn = db.connection()
    query = "DELETE FROM medicos WHERE id_medico = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_medico, ))
        conn.commit()
        conn.close()

def update_medico(tipo_documento, num_documento, p_nombre, s_nombre, p_apellido, s_apellido, nombre_completo,
              direccion, telefono, cod_cargo, nom_cargo, registro_medico, consultorio, firma_medico, id_medico):
    
    conn = db.connection()
    query = "UPDATE medicos SET tipo_documento=%s, num_documento=%s, p_nombre=%s, s_nombre=%s, p_apellido=%s, s_apellido=%s, \
             nombre_completo=%s, direccion=%s, telefono=%s, cod_cargo=%s, nom_cargo=%s, registro_medico=%s, consultorio=%s, firma_medico=%s \
             WHERE id_medico = %s "
    
    params = (tipo_documento, num_documento, p_nombre, s_nombre, p_apellido, s_apellido, nombre_completo,
              direccion, telefono, cod_cargo, nom_cargo, registro_medico, consultorio, firma_medico, id_medico)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()