from app.database import db
import base64

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

#Listar Anexos por documento
def list_anexos_doc(codigo):
    anexos = []
    conn = db.connection()
    query = """ SELECT a.id_anexo, a.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre) nombre, a.fecha, ta.nom_tipoanexo tipo,
                a.documento
                FROM anexos a
                LEFT JOIN pacientes p on p.num_doc = a.codigo
                LEFT JOIN tipos_anexo ta on ta.id_tipoanexo = a.tipo_documento 
                WHERE a.codigo = %s
                ORDER BY a.fecha DESC """
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (codigo, ))
            result = cursor.fetchall()
            for row in result:
                documento = row[5]
                anexos.append({'ID': row[0], 'codigo': row[1], 'nombre': row[2], 'fecha': row[3].strftime("%Y-%m-%d"), 'tipo': row[4], 'base64': base64.b64encode(documento).decode('utf-8') })

        return anexos        

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        return None
    
    finally:
        conn.close()
         