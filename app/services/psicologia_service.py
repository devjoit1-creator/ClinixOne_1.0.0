from app.database import db

#Metodo para insertar nueva hc de psicología a la bd
def insert_hcpsicologia(codigo, medico, fecha, hora, motivo_consulta, enf_actual, antper_diabetes, antper_hta, antper_dislipidemia, antper_cancer, antper_asma,
                        antper_epilepsia, antper_tuberculosis, antper_violencia, antper_otro, antper_otro_cual, antper_observaciones, practica_cirugia, practica_cirugia_cual,
                        padece_enf, padece_enf_cual, practica_tratamiento, practica_tratamiento_cual, toma_medicamento, toma_medicamento_cual, toma_medicamento_dosis,
                        antfam_alergia, antfam_alergia_parent, antfam_diabetes, antfam_diabetes_parent, antfam_cancer, antfam_cancer_parent, antfam_hta, antfam_hta_parent,
                        antfam_respiratoria, antfam_respiratoria_parent, antfam_asma, antfam_asma_parent, antfam_epilepsia, antfam_epilepsia_parent, antfam_ceguera,
                        antfam_ceguera_parent, antfam_dislipidemia, antfam_dislipidemia_parent, antfam_alcoholismo, antfam_alcoholismo_parent, antfam_tabaquismo,
                        antfam_tabaquismo_parent, antfam_drogadiccion, antfam_drogadiccion_parent, antfam_tuberculosis, antfam_tuberculosis_parent, antfam_violencia,
                        antfam_violencia_parent, aspfam_vive, aspfam_relacion, aspfam_hecho, aspper_estudio, aspper_social, aspper_orientacion, aspper_conducta,
                        estado_sueno, estado_concentracion, estado_juicio, estado_intelectual, estado_orientacion, estado_sensopercepcion, estado_conciencia, estado_memoria,
                        estado_pensamiento, estado_afecto, estado_higiene, estado_postura, estado_expresion, estado_alimentacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2,
                        cod_diag3, nom_diag3, cod_diag4, nom_diag4, tipo_diag,  plan_trata, id_atencion):
    
    conn = db.connection()
    query = """ INSERT INTO hc_psicologia (codigo, medico, fecha, hora, motivo_consulta, enf_actual, antper_diabetes, antper_hta, antper_dislipidemia, antper_cancer, antper_asma,
                        antper_epilepsia, antper_tuberculosis, antper_violencia, antper_otro, antper_otro_cual, antper_observaciones, practica_cirugia, practica_cirugia_cual,
                        padece_enf, padece_enf_cual, practica_tratamiento, practica_tratamiento_cual, toma_medicamento, toma_medicamento_cual, toma_medicamento_dosis,
                        antfam_alergia, antfam_alergia_parent, antfam_diabetes, antfam_diabetes_parent, antfam_cancer, antfam_cancer_parent, antfam_hta, antfam_hta_parent,
                        antfam_respiratoria, antfam_respiratoria_parent, antfam_asma, antfam_asma_parent, antfam_epilepsia, antfam_epilepsia_parent, antfam_ceguera,
                        antfam_ceguera_parent, antfam_dislipidemia, antfam_dislipidemia_parent, antfam_alcoholismo, antfam_alcoholismo_parent, antfam_tabaquismo,
                        antfam_tabaquismo_parent, antfam_drogadiccion, antfam_drogadiccion_parent, antfam_tuberculosis, antfam_tuberculosis_parent, antfam_violencia,
                        antfam_violencia_parent, aspfam_vive, aspfam_relacion, aspfam_hecho, aspper_estudio, aspper_social, aspper_orientacion, aspper_conducta,
                        estado_sueno, estado_concentracion, estado_juicio, estado_intelectual, estado_orientacion, estado_sensopercepcion, estado_conciencia, estado_memoria,
                        estado_pensamiento, estado_afecto, estado_higiene, estado_postura, estado_expresion, estado_alimentacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2,
                        cod_diag3, nom_diag3, cod_diag4, nom_diag4, tipo_diag,  plan_trata, id_atencion) 
                        VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                         %s, %s)"""
    
    params = (codigo, medico, fecha, hora, motivo_consulta, enf_actual, antper_diabetes, antper_hta, antper_dislipidemia, antper_cancer, antper_asma,
              antper_epilepsia, antper_tuberculosis, antper_violencia, antper_otro, antper_otro_cual, antper_observaciones, practica_cirugia, practica_cirugia_cual,
              padece_enf, padece_enf_cual, practica_tratamiento, practica_tratamiento_cual, toma_medicamento, toma_medicamento_cual, toma_medicamento_dosis,
              antfam_alergia, antfam_alergia_parent, antfam_diabetes, antfam_diabetes_parent, antfam_cancer, antfam_cancer_parent, antfam_hta, antfam_hta_parent,
              antfam_respiratoria, antfam_respiratoria_parent, antfam_asma, antfam_asma_parent, antfam_epilepsia, antfam_epilepsia_parent, antfam_ceguera,
              antfam_ceguera_parent, antfam_dislipidemia, antfam_dislipidemia_parent, antfam_alcoholismo, antfam_alcoholismo_parent, antfam_tabaquismo,
              antfam_tabaquismo_parent, antfam_drogadiccion, antfam_drogadiccion_parent, antfam_tuberculosis, antfam_tuberculosis_parent, antfam_violencia,
              antfam_violencia_parent, aspfam_vive, aspfam_relacion, aspfam_hecho, aspper_estudio, aspper_social, aspper_orientacion, aspper_conducta,
              estado_sueno, estado_concentracion, estado_juicio, estado_intelectual, estado_orientacion, estado_sensopercepcion, estado_conciencia, estado_memoria,
              estado_pensamiento, estado_afecto, estado_higiene, estado_postura, estado_expresion, estado_alimentacion, cod_diag1, nom_diag1, cod_diag2, nom_diag2,
              cod_diag3, nom_diag3, cod_diag4, nom_diag4, tipo_diag,  plan_trata, id_atencion)
    
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todos los registros de hc de nutrición por medico y paciente
def listar_hc_psicologia(paciente, medico):
    regs_psicologia = []
    conn = db.connection()
    query = """ SELECT hcp.id_hcpsicologia, hcp.fecha, hcp.hora, hcp.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre), hcp.id_atencion
                FROM hc_psicologia hcp INNER JOIN pacientes p ON p.num_doc = hcp.codigo WHERE hcp.codigo = %s AND hcp.medico = %s """ 

    params = (paciente, medico)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            regs_psicologia.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'codigo': row[3] ,'paciente': row[4], 'atencion': row[5]})

    conn.close()
    return regs_psicologia

#Metodo para listar el contenido de la hc de psicologia por id
def listar_hc_psicologia_id(id_hcpsicologia):
    reg_psicologia = None
    conn = db.connection()
    query = "SELECT * FROM hc_psicologia WHERE id_hcpsicologia = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_hcpsicologia, ))
        result = cursor.fetchone()
        reg_psicologia = result

    conn.close()
    return reg_psicologia           
