from app.database import db

#Listar todos los tipos de anexos
def listar_tipos_anexos():
    tipos_anexo = []
    conn = db.connection()
    query = """ SELECT id_tipoanexo, nom_tipoanexo FROM tipos_anexo """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                tipos_anexo.append({'ID': row[0], 'nombre': row[1]})

    except Exception as ex:
        print(f"Error Inesperado: {ex}")
        conn.rollback()

    finally:
        conn.close()

    return tipos_anexo

#Insert Nuevo Anexo
def insert_anexo(codigo, fecha, hora, tipo_documento, descripcion, documento):
    conn = db.connection()
    query = """ INSERT INTO anexos (codigo, fecha, hora, tipo_documento, descripcion, documento) 
                VALUES (%s, %s, %s, %s, %s, %s) """
    
    params = (codigo, fecha, hora, tipo_documento, descripcion, documento)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()