from app.database import db

#Metodo para listar todas las formas farmaceuticas para ihce rda
def listar_formas_ihce():
    formas = []
    conn = db.connection()
    query = """ SELECT cod_forma, nom_forma FROM formas_farm_ihce """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                formas.append({'codigo': row[0], 'nombre': row[1]})

        return formas
    
    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()