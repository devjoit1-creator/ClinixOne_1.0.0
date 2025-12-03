from app.database import db

#Metodo para insertar una nueva factura en bd
def insert_factura_bd(cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo,
                    valor_bruto, descuento, subtotal_factura, iva, valor_neto, usuario):

    conn = db.connection()
    query = "INSERT INTO facturas (cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo, valor_bruto, \
                                   descuento, subtotal_factura, iva, valor_neto, usuario) VALUES \
                                  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    params = (cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo, valor_bruto,
              descuento, subtotal_factura, iva, valor_neto, usuario)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para insertar una nueva factura en bd desde consulta
def insert_factura(ambito_factura, cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo, atencion, cod_admin, nit_admin, nom_admin, observacion, valor_bruto,
                   descuento, copago, subtotal_factura, iva, valor_neto, usuario):
    
    conn = db.connection()
    query = "INSERT INTO facturas (ambito_factura, cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo, atencion, cod_admin, nit_admin, nom_admin, observacion, valor_bruto, \
                                   descuento, copago, subtotal_factura, iva, valor_neto, usuario) VALUES \
                                  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    params = (ambito_factura, cod_fuente, nro_factura, fecha, hora, codigo, nombre, direccion, telefono, correo, atencion, cod_admin, nit_admin, nom_admin, observacion, valor_bruto,
              descuento, copago, subtotal_factura, iva, valor_neto, usuario)
              
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()


#Metodo para insertar detalles de nueva factura en bd 
def insert_detalle_factura(cod_serv, nom_serv, valor_serv, cantidad, total, id_factura):
    conn = db.connection()
    query = "INSERT INTO detalle_facturas(cod_serv, nom_serv, valor_serv, cantidad, total, id_factura) VALUES (%s, %s, %s, %s, %s, %s)"
    params = (cod_serv, nom_serv, valor_serv, cantidad, total, id_factura)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()


#Metodo para insertar detalles de nueva factura en bd desde consulta
def insert_detalle_factura_consulta(und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, numero_fact):
    conn = db.connection()
    query = "INSERT INTO detalle_facturas(und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, numero_fact) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    params = (und_funcional, cod_serv, nom_serv, valor_serv, cantidad, total, numero_fact)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todas las facturas
def listar_facturas():
    facturas = []
    conn = db.connection()
    query = """ SELECT concat(fc.prefijo,'-',fc.cod_fuente) Fuente, f.nro_factura Factura, f.codigo Documento, f.nombre Cliente, concat('$', format(f.valor_neto,'2','de_DE')) Total,
                f.fe_uuid UUID, f.fe_pdf_url PDF
                FROM fuentes_contables fc , facturas f
                WHERE fc.cod_fuente = 6 """

    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            facturas.append({'fuente': row[0], 'factura': row[1], 'documento': row[2], 'cliente': row[3], 'total': row[4], 'uuid': row[5], 'pdf': row[6]})

    conn.close()
    return facturas

#Metodo para listar factura por id
def listar_factura_id(id_factura):
    factura = None
    conn = db.connection()
    query = """ SELECT 
                    /* Datos Factura */
                    CONCAT(fc.prefijo, f.nro_factura) AS factura,
                    f.fecha, f.hora, f.codigo, f.nombre, f.direccion, f.telefono, f.atencion, 
                    f.cod_admin, f.nom_admin,
                    /* Datos Paciente */
                    CONCAT(p.p_nombre, ' ', p.s_nombre, ' ', p.p_apellido, ' ', p.s_apellido) AS paciente,
                    CONCAT(p.tipo_doc, ' ', p.num_doc) AS documento,
                    p.direccion, p.telefono, p.fecha_nac,
                    FLOOR(DATEDIFF(SYSDATE(), p.fecha_nac)/365) AS edad,
                    p.nom_munic AS municipio,
                    CASE p.regimen
                        WHEN 1 THEN 'Contributivo'
                        WHEN 2 THEN 'Subsidiado'
                        WHEN 3 THEN 'Particular'
                        WHEN 4 THEN 'Vinculado'
                        WHEN 5 THEN 'Reg. Excepción'
                        WHEN 6 THEN 'Reg. Especial'
                        WHEN 7 THEN 'Otro'
                        WHEN 8 THEN 'Sin Regimen'
                    END AS regimen,
                    /* Autorización */
                    COALESCE(c.nro_autorizacion, h.nro_autorizacion) AS autorizacion,
                    /* Médico */
                    CONCAT(m.num_documento, ' - ', m.nombre_completo) AS medico,
                    /* Fechas de atención */
                    COALESCE(c.fecha_atencion, h.fecha_ingreso) AS ingreso,
                    COALESCE(c.fecha_salida, h.fecha_salida) AS salida,
                    /* Otros datos */
                    f.observacion,
                    CASE a.forma_pago
                        WHEN 1 THEN 'Contado'
                        WHEN 2 THEN 'Credito'
                    END AS forma_pago,
                    FORMAT(f.valor_bruto, 2, 'de_DE') AS valor_bruto,
                    FORMAT(f.descuento, 2, 'de_DE') AS descuento,
                    FORMAT(f.copago, 2, 'de_DE') AS copago,
                    FORMAT(f.subtotal_factura, 2, 'de_DE') AS subtotal_factura,
                    FORMAT(f.iva, 2, 'de_DE') AS iva,
                    FORMAT(f.valor_neto, 2, 'de_DE') AS valor_neto
                FROM facturas f
                JOIN fuentes_contables fc ON f.cod_fuente = fc.cod_fuente
                JOIN administradoras a ON f.cod_admin = a.cod_administradora
                LEFT JOIN consultas c ON f.atencion = c.atencion
                LEFT JOIN hospitalizacion h ON f.atencion = h.atencion
                LEFT JOIN pacientes p ON p.num_doc = COALESCE(c.codigo, h.codigo)
                LEFT JOIN medicos m ON m.num_documento = COALESCE(c.medico, h.medico)
                WHERE f.nro_factura = %s """
    
    with conn.cursor() as cursor:
        cursor.execute(query, (id_factura, ))
        result = cursor.fetchone()
        factura = result

    conn.close()
    return factura


#Metodo para listar el detalle de la factura por id
def listar_detalle_factura_id(nro_factura):
    detalle = []
    conn = db.connection()
    query = "SELECT cod_serv, nom_serv, format(valor_serv,'2','de_DE'), cantidad, format(total,'2','de_DE')  FROM detalle_facturas WHERE numero_fact = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (nro_factura, ))
        result = cursor.fetchall()
        for row in result:
            detalle.append({'cod_serv': row[0], 'nom_serv': row[1], 'valor_serv': row[2], 'cantidad': row[3], 'total': row[4]})

    conn.close()
    return detalle

#Metodo para listar facturas por rango de fecha para emitir
def listar_facturas_fechas(fecha_inicio, fecha_fin):
    facturas = []
    conn = db.connection()
    query = """ select fc.prefijo as prefijo, f.nro_factura as factura, f.codigo as codigo, f.nombre as nombre, DATE_FORMAT(f.fecha, '%d/%m/%Y') as fecha, concat('$', format(f.valor_neto, 2, 'de_DE')) as valor
                from facturas f 
                join fuentes_contables fc on fc.cod_fuente = f.cod_fuente
                where f.fe_uuid is null and fe_cufe is null
                and f.fecha between cast(%s as date) and cast(%s as date)"""
    params = (fecha_inicio, fecha_fin)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            facturas.append({'fuente': row[0],
                             'numero': row[1],
                             'codigo': row[2],
                             'nombre': row[3],
                             'fecha': row[4],
                             'valor': row[5]})

    conn.close()
    return facturas        

#Metodo para generar JSON FE SS CUFE obligatorio
def json_factura(nro_factura):
    conn = db.connection()
    query = """ select f.nro_factura, f.fecha, 
				coalesce(h.fecha_ingreso, c.fecha_atencion) as ingreso, 
				coalesce(h.fecha_salida, c.fecha_salida) as salida,
				case 
					when a.plan_beneficios = '01' then 'PLAN_DE_BENEFICIOS'
					when a.plan_beneficios = '02' then 'PRESUPUESTO_MAXIMO'
					when a.plan_beneficios = '03' then 'PRIMA_NO_ASEGURADO_SOAT'
					when a.plan_beneficios = '04' then 'COBERTURA_SOAT'
					when a.plan_beneficios = '05' then 'COBERTURA_ARL'
					when a.plan_beneficios = '06' then 'COBERTURA_ADRES'
					when a.plan_beneficios = '07' then 'COBERTURA_SALUD_PUBLICA'
					when a.plan_beneficios = '08' then 'COBERTURA_ENTIDAD_RECURSOS_OFERTA'
					when a.plan_beneficios = '09' then 'URGENCIAS_MIGRANTE'
					when a.plan_beneficios = '10' then 'PLAN_COMPLEMENTARIO_SALUD'
					when a.plan_beneficios = '11' then 'PLAN_MEDICINA_PREPAGADA'
					when a.plan_beneficios = '12' then 'OTRAS_POLIZAS_SALUD'
					when a.plan_beneficios = '13' then 'COBERTURA_REGIMEN_ESPECIAL'
					when a.plan_beneficios = '14' then 'COBERTURA_FONDO_NACIONAL_PRIVADAS_LIBERTAD'
					when a.plan_beneficios = '15' then 'PARTICULAR'
				end as cobertura, a.convenio,
                case
					when a.modalidad_pago = '01' then 'PAGO_INDIVIDUAL_POR_CASO_CONJUNTO_INTEGRAL_PAQUETE_CANASTA'
					when a.modalidad_pago = '02' then 'PAGO_GLOBAL_PROSPECTIVO'
					when a.modalidad_pago = '03' then 'PAGO_POR_CAPITACION'
					when a.modalidad_pago = '04' then 'PAGO_POR_EVENTO'
					when a.modalidad_pago = '05' then 'OTRA_MODALIDAD'
				end as modpago,
				df.cod_serv, df.cantidad, df.nom_serv, df.valor_serv, f.descuento,
                a.forma_pago,
                rf.numero_resolucion, fc.prefijo, rf.account_id, 
                coalesce (t.tipo_idf, p.tipo_doc) as tipo_documento, f.codigo, 
                coalesce(t.tipo_tercero, p.tipo_paciente) as tipo_persona, f.nombre, p.p_nombre, p.p_apellido,
                f.correo, f.direccion, f.telefono,
                coalesce(t.cod_depto_tercero, p.depto) as depto_persona,
                coalesce(substring(t.cod_munic_tercero, 3, 3), substring(p.munic, 3, 3)) as munic_persona,
                (select 
                	case 
                		when p.regimen = '01' then 'CONTRIBUTIVO_COTIZANTE'
                		when p.regimen = '02' then 'CONTRIBUTIVO_BENEFICIARIO'
                		when p.regimen = '03' then 'CONTRIBUTIVO_ADICIONAL'
                		when p.regimen = '04' then 'SUBSIDIADO'
                		when p.regimen = '05' then 'NO_AFILIADO'
                		when p.regimen = '06' then 'ESPECIAL_COTIZANTE'
                		when p.regimen = '07' then 'ESPECIAL_BENEFICIARIO'
                		when p.regimen = '08' then 'PERSONA_FONDO_NACIONAL_PRIVADAS_LIBERTAD'
                		when p.regimen = '09' then 'TOMADOR_ARL'
                		when p.regimen = '10' then 'TOMADOR_SOAT'
                		when p.regimen = '11' then 'TOMADOR_PLAN_VOLUNTARIO_SALUD'
                		when p.regimen = '12' then 'PARTICULAR'
                		when p.regimen = '13' then 'ESPECIAL_LEY_352_1997'
                	end
                	from pacientes p where p.num_doc = coalesce(c.codigo, h.codigo)
                ) as regimen,
                coalesce(h.nro_autorizacion, c.nro_autorizacion) as autorizacion,
                (select p.p_nombre from pacientes p where p.num_doc = coalesce(c.codigo, h.codigo)) as primer_nombre,
				(select p.p_apellido from pacientes p where p.num_doc = coalesce(c.codigo, h.codigo)) as primer_apellido,
                (select p.num_doc from pacientes p where p.num_doc = coalesce(c.codigo, h.codigo)) as num_documento,
				(select p.tipo_doc from pacientes p where p.num_doc = coalesce(c.codigo, h.codigo)) as tipo_documento,
                (select pa.nom_pais from pais pa inner join pacientes p on p.pais = pa.id_pais where p.num_doc = coalesce(c.codigo, h.codigo)) as pais_origen
                from facturas f
                join resfacturacion rf
                left join administradoras a on a.cod_administradora = f.cod_admin
                left join hospitalizacion h on h.numero_fact = f.nro_factura
                left join consultas c on c.numero_fact = f.nro_factura
                left join detalle_facturas df on df.numero_fact = f.nro_factura
                left join fuentes_contables fc on fc.cod_fuente = f.cod_fuente
                left join terceros t on t.identificacion = f.codigo
                left join pacientes p on p.num_doc = f.codigo
                where rf.estado_res = 1 and rf.tipo_documento = 1 
                and f.nro_factura = %s  """
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query, (nro_factura,))
            rows = cursor.fetchall()

        if not rows:
            return None

        base = rows[0]
        associated_users = []
        items = []
        recaudos = []

        associated_users.append({
            "contract_number": base["convenio"],
            "provider_code": "PRO222",
            "user_type": base["regimen"],
            "authorization_number": base["autorizacion"],
            "person": {
                "first_name": base["primer_nombre"],
                "last_name": base["primer_apellido"],
                "identification": base["num_documento"],
                #"identification_type": "CEDULA_CIUDADANIA",
                "dian_identification_type": base["tipo_documento"],
                "identification_origin_country": base["pais_origen"]
            }
        })
        for row in rows:
            items.append({
                "sku": row["cod_serv"],
                "quantity": row["cantidad"],
                "description": row["nom_serv"],
                "price": int(row["valor_serv"])
            })

            recaudos.append({
                "amount": int(row["descuento"]),
                "issue_date": row["salida"].strftime("%d/%m/%Y"),
                "medical_fee_code": "NO_APLICA"
            })

        json = {
            "actions": {
                "send_dian": True,
                "send_email": True
            },
            "invoice":{
                "issue_date": base["fecha"].strftime("%d/%m/%Y"),
                "payment_date": base["fecha"].strftime("%d/%m/%Y"),
                "health":{
                    "version": "API_SALUD_V2",
                    "coverage": base["cobertura"],
                    "provider_code": "PRO222",
                    "contract_number": base["convenio"],
                    "payment_modality": base["modpago"],
                    "period_start_date": base["ingreso"].strftime("%d/%m/%Y"),
                    "period_end_date": base["salida"].strftime("%d/%m/%Y"),
                    "associated_users": associated_users,
                    "recaudos": recaudos
                },
                "invoice_type_code": "FACTURA_VENTA",
                "items": items,
                "payment_means_type": "DEBITO" if base["forma_pago"] == 1 else "CREDITO",
                "operation": "SS_CUFE",
                "number": base["nro_factura"],
                "numbering": {
                    "resolution_number": base["numero_resolucion"],
                    "prefix": base["prefijo"],
                    "flexible": True
                },
                "dataico_account_id": base["account_id"],
                "env": "PRODUCCION",
                "customer": {
                    "email": base["correo"],
                    "phone": base["telefono"],
                    "party_identification_type": "NIT", #base["tipo_documento"],
                    "party_identification": base["codigo"],
                    "party_type": base["tipo_persona"],
                    "tax_level_code": "SIMPLIFICADO",
                    "regimen": "SIMPLE",
                    "department": base["depto_persona"],
                    "city": base["munic_persona"],
                    "address_line": base["direccion"],
                    "company_name": base["nombre"]
                } if base["tipo_persona"] == "PERSONA_JURIDICA" else {
                    "email": base["correo"],
                    "phone": base["telefono"],
                    "party_identification_type": "NIT", 
                    "party_identification": base["codigo"], 
                    "party_type": base["tipo_persona"],
                    "tax_level_code": "SIMPLIFICADO",
                    "regimen": "SIMPLE",
                    "department": base["depto_persona"],
                    "city": base["munic_persona"],
                    "address_line": base["direccion"],
                    "first_name": base["p_nombre"], 
                    "family_name": base["p_apellido"]
                },
                "payment_means": "BANK_TRANSFER"
                }
            }
        
        return json  
    
    except Exception as ex:
        print(f"Se presentó un error inesperado generando el JSON de la Factura {nro_factura}. \n {ex}")
        return None
    finally:
        conn.close()

#Metodo para actualizar datos de FE en BD post emitida factura Estatus 200
def update_campos_fe(fe_uuid, fe_cufe, fe_issue_date, fe_issue_time, fe_pdf_url, fe_xml_url, nro_factura):
    conn = db.connection()
    query = """ UPDATE facturas SET fe_uuid = %s, fe_cufe = %s, fe_issue_date = %s, fe_issue_time = %s, fe_pdf_url = %s,
                fe_xml_url = %s where nro_factura = %s """
    
    params = (fe_uuid, fe_cufe, fe_issue_date, fe_issue_time, fe_pdf_url, fe_xml_url, nro_factura)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar la factura para generar nota credito
def listar_factura_nc(nro_factura):
    factura = None
    conn = db.connection()
    query = """ SELECT cod_fuente, nro_factura, fe_uuid FROM facturas where nro_factura = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (nro_factura, ))
        result = cursor.fetchone()
        factura = result

    conn.close()
    return factura    