from app.database import db

#Metodo para insertar una nueva de credito en bd
def insert_notacredito(cod_fuente, nro_notacredito, fecha, hora, cod_fte_factura, factura, fe_uuid, motivo_notacredito):
    conn = db.connection()
    query =  """ INSERT INTO notas_credito (cod_fuente, nro_notacredito, fecha, hora, cod_fte_factura, factura, fe_uuid, motivo_notacredito)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (cod_fuente, nro_notacredito, fecha, hora, cod_fte_factura, factura, fe_uuid, motivo_notacredito)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todas las notas de credito
def listar_notascredito():
    notas = []
    conn = db.connection()
    query = """ SELECT concat(fc.prefijo,'-',fc.cod_fuente) Fuente, nc.nro_notacredito Nota, nc.cod_fte_factura, nc.factura Factura, nc.nc_uuid
                FROM fuentes_contables fc , notas_credito nc
                WHERE fc.cod_fuente = 4"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            notas.append({'fuente': row[0], 'numero': row[1], 'fte_factura': row[2], 'factura': row[3], 'UUID': row[4]})

    conn.close()
    return notas

#Metodo para generar json de emisión de nota de credito
def json_notacredito(nro_notacredito):
    conn = db.connection()
    query = """ SELECT rf.account_id, nc.fe_uuid as invoice_id, concat(DATE_FORMAT(nc.fecha, "%d/%m/%Y"),' ',nc.hora) as issue_date ,nc.motivo_notacredito as reason, nc.nro_notacredito as number,
                fc.prefijo as prefix, df.cod_serv as sku, f.valor_neto as price, df.cantidad as quantity, df.nom_serv as description
                FROM notas_credito nc 
                join resfacturacion rf
                left join fuentes_contables fc on fc.cod_fuente = nc.cod_fuente
                left join facturas f on f.nro_factura = nc.factura
                left join detalle_facturas df on df.numero_fact = nc.factura
                WHERE nc.nro_notacredito = %s """
    
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query, (nro_notacredito, ))
            rows = cursor.fetchall()

        if not rows:
            return None

        base = rows[0]
        items = []

        for row in rows:
            items.append({
                "sku": row["sku"],
                "price": int(row["price"]),
                "quantity": row["quantity"],
                "description": row["description"]
            })    

        json = {
            "actions": {
                "send_dian": True,
                "send_email": False
            },
            "credit_note": {
                "dataico_account_id": base["account_id"],
                "invoice_id": base["invoice_id"],
                "issue_date": base["issue_date"],
                "reason": base["reason"],
                "number": base["number"],
                "numbering": {
                    "prefix": base["prefix"],
                    "flexible": True
                },
                "items": items
            }
        }

        return json

    except Exception as ex:
        print(f"Se presentó un error inesperado generando el JSON de la Nota Credito {nro_notacredito}. \n {ex}") 
        return None
    finally:
        conn.close()

#Metodo para actualizar datos de FE en BD post emitida factura Estatus 200
def update_campos_nc(nc_uuid, nc_cufe, nc_issue_date, nc_pdf_url, nc_xml_url, nro_notacredito):
    conn = db.connection()
    query = """ UPDATE notas_credito SET nc_uuid = %s, nc_cufe = %s, nc_issue_date = %s, nc_pdf_url = %s,
                nc_xml_url = %s where nro_notacredito = %s """
    
    params = (nc_uuid, nc_cufe, nc_issue_date, nc_pdf_url, nc_xml_url, nro_notacredito)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()        