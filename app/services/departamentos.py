from app.database import db

def listar_departamentos():
    departamentos = []
    conn = db.connection()
    query = "SELECT id_depto, nom_depto FROM departamento"
    with conn.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchall():
            departamentos.append({"id_depto": row[0], "nom_depto":row[1]})

    conn.close()
    return departamentos

def listar_municipios(cod_depto):
    municipios = []
    conn = db.connection()
    query = "SELECT m.id_municipio, m.nom_municipio FROM municipio m join departamento d on d.id_depto = m.cod_depto where m.cod_depto = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_depto, ))
        for row in cursor.fetchall():
            municipios.append({"id_municipio": row[0], "nom_municipio": row[1]})

    conn.close()
    return municipios

def listar_paises():
    paises = []
    conn = db.connection()
    query = "SELECT id_pais, nom_pais FROM pais ORDER BY nom_pais ASC"
    with conn.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchall():
            paises.append({"id_pais": row[0], "nom_pais": row[1]})

    conn.close()
    return paises

