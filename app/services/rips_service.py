from app.database import db

#Metodo para listar las facturas por administradora para generar RIPS
def listar_facturas_rips(fecha_inicio, fecha_fin, administradora):
    facturas = []
    conn = db.connection()
    query = """ SELECT DATE_FORMAT(f.fecha, '%d/%m/%Y'), f.nro_factura, a.nom_administradora 
                from facturas f 
                LEFT JOIN administradoras a on f.cod_admin = a.cod_administradora 
                WHERE f.fecha BETWEEN CAST(%s AS DATE) AND CAST(%s AS DATE) AND f.cod_admin = %s """
    
    params = (fecha_inicio, fecha_fin, administradora)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result: 
            facturas.append({'fecha': row[0], 'factura': row[1], 'admin': row[2]})

    conn.close()
    return facturas

#Metodo Para Crear Diccionario Generador JSON RIPS
def json_rips(nro_factura):
    conn = db.connection()
    query = """ select 
            /* Datos Encabezado RIPS */
            f.ambito_factura, e.nit_entidad as numDocumentoIdObligado, concat(fc.prefijo,f.nro_factura) as numFactura, coalesce(nc.prefijo_notacredito, null) as tipoNota, coalesce(nc.nro_notacredito, null) as numNota,
            /* Datos Arreglo Usuario RIPS */
            p.tipo_doc as usuario_tipoDocumentoIdentificacion, p.num_doc as usuario_numDocumentoIdentificacion, 
            p.regimen as usuario_tipoUsuario, p.fecha_nac as usuario_fechaNacimiento,
            case when p.sexo = 1 then 'M' when p.sexo = 2 then 'F' end as usuario_codSexo, p.pais_res as usuario_codPaisResidencia, p.munic as usuario_codMunicipioResidencia,
            case when p.zona = 1 then '01' when p.zona = 2 then '02' end as usuario_codZonaTerritorialResidencia, p.pais as usuario_codPaisOrigen,
            /* Datos Arreglo Servicio Consulta */
            e.cod_habilitacion as consulta_codPrestador, concat(c.fecha_atencion,' ',c.hora_atencion) as consulta_fechaInicioAtencion, c.nro_autorizacion as consulta_numAutorizacion,
            df.cod_serv as consulta_codConsulta, c.modalidad as consulta_modalidadGrupoServicioTecSal, spc.grupo as consulta_grupoServicios, c.servicio_consulta as consulta_codServicio, c.finalidad_consulta as consulta_finalidadTecnologiaSalud,
            c.causa_externa as consulta_causaMotivoAtencion, c.cod_diag1 as consulta_codDiagnosticoPrincipal, c.cod_diag2 as consulta_codDiagnosticoRelacionado1, c.cod_diag3 as consulta_codDiagnosticoRelacionado2, c.cod_diag4 as consulta_codDiagnosticoRelacionado3,
            c.tipo_diag as consulta_tipoDiagnosticoPrincipal, p.tipo_doc as consulta_tipoDocumentoldentificacion, p.num_doc as consulta_numDocumentoldentificacion, f.valor_neto as consulta_vrServicio,
            c.concepto_recaudo as consulta_conceptoRecaudo, f.copago as consulta_valorPagoModerador,
            /* Datos Arreglo Servicio Hospitalizacion */
            e.cod_habilitacion as hosp_codPrestador, h.via_ingreso as hosp_viaIngresoServicioSalud, concat(h.fecha_ingreso,' ',h.hora_ingreso) as hosp_fechaInicioAtencion, h.nro_autorizacion as hosp_numAutorizacion,
            h.causa_externa as hosp_causaMotivoAtencion, h.cod_diag1 as hosp_codDiagnosticoPrincipal, h.cod_diag_salida as hosp_codDiagnosticoPrincipalE, h.estado_salida as hosp_condicionDestinoUsuarioEgreso, 
            h.cod_diag_muerte as hosp_codDiagnosticoCausaMuerte, concat(h.fecha_salida,' ',h.hora_salida) as hosp_fechaEgreso,
            /* Datos Arreglo Otros Servicios Fact */
            e.cod_habilitacion as otr_codPrestador, coalesce(c.nro_autorizacion, h.nro_autorizacion) as otr_numAutorizacion, concat(f.fe_issue_date,' ',f.fe_issue_time) as otr_fechaSuministroTecnologia ,'03' as otr_tipoOS, df.cod_serv as otr_codTecnologiaSalud,
            df.nom_serv as otr_nomTecnologiaSalud, df.cantidad as otr_cantidadOS, m.tipo_documento as otr_tipoDocumentoIdentificacion, m.num_documento as otr_numDocumentoIdentificacion,
            df.valor_serv as otr_vrUnitOS, f.valor_neto as otr_vrServicio
            from entidad e, facturas f
            left join fuentes_contables fc on fc.cod_fuente = f.cod_fuente
            left join notas_credito nc on nc.factura = f.nro_factura
            left join hospitalizacion h on h.numero_fact = f.nro_factura
            left join consultas c on c.numero_fact = f.nro_factura
            left join detalle_facturas df on df.numero_fact = f.nro_factura
            left join pacientes p on p.num_doc = COALESCE(c.codigo, h.codigo)
            left join medicos m on m.num_documento = COALESCE(c.medico, h.medico)
            left join servicios_proceds_cups spc on spc.cod_servicio = df.cod_serv
            where f.nro_factura = %s
            order by numFactura asc """
    try:

        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query, (nro_factura, ))
            rows = cursor.fetchall()

        if not rows:
            return None

        base = rows[0]
        usuarios = []
        consultas = []
        hospitalizacion = []
        otrosServicios = []
        for row in rows:
            consultas.append({
                "codPrestador": row["consulta_codPrestador"],
                "fechaInicioAtencion": row["consulta_fechaInicioAtencion"],
                "numAutorizacion": row["consulta_numAutorizacion"],
                "codConsulta": row["consulta_codConsulta"],
                "modalidadGrupoServicioTecSal": row["consulta_modalidadGrupoServicioTecSal"],
                "grupoServicios": row["consulta_grupoServicios"],
                "codServicio": row["consulta_codServicio"],
                "finalidadTecnologiaSalud": row["consulta_finalidadTecnologiaSalud"],
                "causaMotivoAtencion": str(row["consulta_causaMotivoAtencion"]),
                "codDiagnosticoPrincipal": row["consulta_codDiagnosticoPrincipal"],
                "codDiagnosticoRelacionado1": None if row["consulta_codDiagnosticoRelacionado1"] == "" else row["consulta_codDiagnosticoRelacionado1"],
                "codDiagnosticoRelacionado2": None if row["consulta_codDiagnosticoRelacionado2"] == "" else row["consulta_codDiagnosticoRelacionado2"],
                "codDiagnosticoRelacionado3": None if row["consulta_codDiagnosticoRelacionado3"] == "" else row["consulta_codDiagnosticoRelacionado3"],
                "tipoDiagnosticoPrincipal": row["consulta_tipoDiagnosticoPrincipal"],
                "tipoDocumentoldentificacion": row["consulta_tipoDocumentoldentificacion"],
                "numDocumentoldentificacion": row["consulta_numDocumentoldentificacion"],
                "vrServicio": int(row["consulta_vrServicio"]),
                "conceptoRecaudo": row["consulta_conceptoRecaudo"],
                "valorPagoModerador": int(row["consulta_valorPagoModerador"]),
                "numFEVPagoModerador": None,
                "consecutivo": 1
            })

            hospitalizacion.append({
                "codPrestador": row["hosp_codPrestador"],
                "viaIngresoServicioSalud": row["hosp_viaIngresoServicioSalud"],
                "fechaInicioAtencion": row["hosp_fechaInicioAtencion"],
                "numAutorizacion": row["hosp_numAutorizacion"],
                "causaMotivoAtencion": str(row["hosp_causaMotivoAtencion"]),
                "codDiagnosticoPrincipal": row["hosp_codDiagnosticoPrincipal"],
                "codDiagnosticoPrincipalE": row["hosp_codDiagnosticoPrincipalE"],
                "codDiagnosticoRelacionadoE1": None,
                "codDiagnosticoRelacionadoE2": None,
                "codDiagnosticoRelacionadoE3": None,
                "codComplicacion": None,
                "condicionDestinoUsuarioEgreso": row["hosp_condicionDestinoUsuarioEgreso"],
                "codDiagnosticoCausaMuerte": None if row["hosp_codDiagnosticoCausaMuerte"] == "" else row["hosp_codDiagnosticoCausaMuerte"],
                "fechaEgreso": row["hosp_fechaEgreso"],
                "consecutivo": 1
            })

            otrosServicios.append({
                "codPrestador": row["otr_codPrestador"],
                "numAutorizacion": row["otr_numAutorizacion"],
                "idMIPRES": None,
                "fechaSuministroTecnologia": row["otr_fechaSuministroTecnologia"],
                "tipoOS": row["otr_tipoOS"],
                "codTecnologiaSalud": row["otr_codTecnologiaSalud"],
                "nomTecnologiaSalud": row["otr_nomTecnologiaSalud"],
                "cantidadOS": row["otr_cantidadOS"],
                "tipoDocumentoIdentificacion": row["otr_tipoDocumentoIdentificacion"],
                "numDocumentoIdentificacion": row["otr_numDocumentoIdentificacion"],
                "vrUnitOS": int(row["otr_vrUnitOS"]),
                "vrServicio": int(row["otr_vrServicio"]),
                "conceptoRecaudo": "05",
                "valorPagoModerador": 0,
                "numFEVPagoModerador": None,
                "consecutivo": 1
            })

            if row["ambito_factura"] == "CONSULTA":
                usuarios.append({
                    "tipoDocumentoIdentificacion": row["usuario_tipoDocumentoIdentificacion"],
                    "numDocumentoIdentificacion": row["usuario_numDocumentoIdentificacion"],
                    "tipoUsuario": row["usuario_tipoUsuario"],
                    "fechaNacimiento": row["usuario_fechaNacimiento"].strftime("%Y-%m-%d"),
                    "codSexo": row["usuario_codSexo"],
                    "codPaisResidencia": str(row["usuario_codPaisResidencia"]),
                    "codMunicipioResidencia": row["usuario_codMunicipioResidencia"],
                    "codZonaTerritorialResidencia": row["usuario_codZonaTerritorialResidencia"],
                    "incapacidad": "NO",
                    "consecutivo": 1,
                    "codPaisOrigen": str(row["usuario_codPaisOrigen"]),
                    "servicios": {
                        "consultas": consultas,
                    }
                })

            elif row["ambito_factura"] == "HOSPITALIZACION":
                usuarios.append({
                    "tipoDocumentoIdentificacion": row["usuario_tipoDocumentoIdentificacion"],
                    "numDocumentoIdentificacion": row["usuario_numDocumentoIdentificacion"],
                    "tipoUsuario": row["usuario_tipoUsuario"],
                    "fechaNacimiento": row["usuario_fechaNacimiento"].strftime("%Y-%m-%d"),
                    "codSexo": row["usuario_codSexo"],
                    "codPaisResidencia": str(row["usuario_codPaisResidencia"]),
                    "codMunicipioResidencia": row["usuario_codMunicipioResidencia"],
                    "codZonaTerritorialResidencia": row["usuario_codZonaTerritorialResidencia"],
                    "incapacidad": "NO",
                    "consecutivo": 1,
                    "codPaisOrigen": str(row["usuario_codPaisOrigen"]),
                    "servicios": {
                        "hospitalizacion": hospitalizacion,
                        "otrosServicios": otrosServicios
                    }
                })

        json = {
            "numDocumentoIdObligado": base["numDocumentoIdObligado"],
            "numFactura": base["numFactura"],
            "tipoNota": base["tipoNota"] ,
            "numNota": base["numNota"],
            "usuarios": usuarios
        }

        return json

    except Exception as ex:
        print(f"Se presentó un error inesperado generando el JSON del RIPS de la factura {nro_factura}. \n {ex}")
        return None

    finally:
        conn.close()