from app.database import db

#Metodo Insertar Nueva Entrada Farmacia
def insert_entrada(cod_fuente, nro_entrada, fecha_entrada, hora_entrada, fecha_vencimiento, concepto, cod_tercero, nom_tercero,
                   prefijo_remision, nro_remision, valor_neto, usuario):
    
    conn = db.connection()
    query = """ INSERT INTO entradas_farmacia (cod_fuente, nro_entrada, fecha_entrada, hora_entrada, fecha_vencimiento, concepto, cod_tercero, nom_tercero,
                prefijo_remision, nro_remision, valor_neto, usuario) 
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (cod_fuente, nro_entrada, fecha_entrada, hora_entrada, fecha_vencimiento, concepto, cod_tercero, nom_tercero,
             prefijo_remision, nro_remision, valor_neto, usuario)
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()

#Metodo Insertar Detalle Nueva Entrada Farmacia
def insert_detalle_entrada(bodega, cod_referencia, nom_referencia, registro_invima, lote, cantidad, vlr_unitario, vlr_subtotal,
                           ref_vencimiento, temperatura, riesgo, condicion, numero_ent):
    
    conn = db.connection()
    query = """ INSERT INTO detalle_entradas_farmacia (bodega, cod_referencia, nom_referencia, registro_invima, lote, cantidad, vlr_unitario, vlr_subtotal,
                ref_vencimiento, temperatura, riesgo, condicion, numero_ent)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (bodega, cod_referencia, nom_referencia, registro_invima, lote, cantidad, vlr_unitario, vlr_subtotal,
              ref_vencimiento, temperatura, riesgo, condicion, numero_ent)
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()
    
#Metodo listar entradas por numero
def listar_entrada_numero(nro_entrada):
    entradas = []
    conn = db.connection()
    query = """ SELECT cod_fuente, nro_entrada, fecha_entrada, cod_tercero, nom_tercero FROM entradas_farmacia WHERE nro_entrada = %s"""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (nro_entrada, ))
            result = cursor.fetchall()
            for row in result:
                entradas.append({'fuente': row[0], 'numero': row[1], 'fecha': row[2].strftime("%Y-%m-%d"), 'cod_tercero': row[3], 'nom_tercero': row[4]})

        return entradas
    
    except Exception as ex:
        print(f"Se presentó un error inesperado: {ex}")
        conn.rollback()
        raise

    finally:
        conn.close()