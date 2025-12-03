from app.database import db

#Metodo para insertar nueva hc de nutrición a la bd
def insert_hcnutricion(codigo, medico, fecha, hora, motivo_consulta, enf_actual, antper_diarrea, antper_estrenimiento, antper_gastritis,
    antper_ulcera, antper_nausea, antper_pirosis, antper_vomito, antper_colitis, antper_otro, antper_otro_cual, antper_dentadura, antper_protesis,
    antper_observaciones, padece_enf, padece_enf_cual, enf_importante, enf_importante_cual, toma_medicamento, toma_medicamento_cual, toma_medicamento_dosis,
    toma_laxantes, toma_diureticos, toma_antiacidos, toma_analgesicos, practica_cirugia, practica_cirugia_cual, antfam_obesidad, antfam_obesidad_parent,
    antfam_diabetes, antfam_diabetes_parent, antfam_cancer, antfam_cancer_parent, antfam_hta, antfam_hta_parent, antfam_hipercolesterolemia,
    antfam_hipercolesterolemia_parent, antfam_hipertrigliceridemia, antfam_hipertrigliceridemia_parent, desayuno_alimentos, desayuno_tiempo,
    mediamanana_alimentos, mediamanana_tiempo, almuerzo_alimentos, almuerzo_tiempo, mediatarde_alimentos, mediatarde_tiempo, cena_alimentos,
    cena_tiempo, aerobicos, aerobicos_frecuencia, aerobicos_duracion, anaerobicos, anaerobicos_frecuencia, anaerobicos_duracion,
    musculatura, musculatura_frecuencia, musculatura_duracion, alcohol, alcohol_frecuencia, alcohol_cantidad, tabaco, tabaco_frecuencia,
    tabaco_cantidad, cafe, cafe_frecuencia, cafe_cantidad, signo_cabello, signo_ojos, signo_piel, signo_unas, signo_labios, signo_encias,
    alimentos_preferidos, alimentos_noagradan, alimentos_malestar, alergico, alergico_cual, peso_habitual, peso_actual, estatura, imc,
    circunferencia_brazo, circunferencia_cintura, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, cod_diag4, nom_diag4,
    plan_trata, id_atencion):

    conn = db.connection()
    query = """ INSERT INTO hc_nutricion (codigo, medico, fecha, hora, motivo_consulta, enf_actual, antper_diarrea, antper_estrenimiento, antper_gastritis,
    antper_ulcera, antper_nausea, antper_pirosis, antper_vomito, antper_colitis, antper_otro, antper_otro_cual, antper_dentadura, antper_protesis,
    antper_observaciones, padece_enf, padece_enf_cual, enf_importante, enf_importante_cual, toma_medicamento, toma_medicamento_cual, toma_medicamento_dosis,
    toma_laxantes, toma_diureticos, toma_antiacidos, toma_analgesicos, practica_cirugia, practica_cirugia_cual, antfam_obesidad, antfam_obesidad_parent,
    antfam_diabetes, antfam_diabetes_parent, antfam_cancer, antfam_cancer_parent, antfam_hta, antfam_hta_parent, antfam_hipercolesterolemia,
    antfam_hipercolesterolemia_parent, antfam_hipertrigliceridemia, antfam_hipertrigliceridemia_parent, desayuno_alimentos, desayuno_tiempo,
    mediamanana_alimentos, mediamanana_tiempo, almuerzo_alimentos, almuerzo_tiempo, mediatarde_alimentos, mediatarde_tiempo, cena_alimentos,
    cena_tiempo, aerobicos, aerobicos_frecuencia, aerobicos_duracion, anaerobicos, anaerobicos_frecuencia, anaerobicos_duracion,
    musculatura, musculatura_frecuencia, musculatura_duracion, alcohol, alcohol_frecuencia, alcohol_cantidad, tabaco, tabaco_frecuencia,
    tabaco_cantidad, cafe, cafe_frecuencia, cafe_cantidad, signo_cabello, signo_ojos, signo_piel, signo_unas, signo_labios, signo_encias,
    alimentos_preferidos, alimentos_noagradan, alimentos_malestar, alergico, alergico_cual, peso_habitual, peso_actual, estatura, imc,
    circunferencia_brazo, circunferencia_cintura, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, cod_diag4, nom_diag4,
    plan_trata, id_atencion) 
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s)"""
        
    params = (codigo, medico, fecha, hora, motivo_consulta, enf_actual, antper_diarrea, antper_estrenimiento, antper_gastritis,
    antper_ulcera, antper_nausea, antper_pirosis, antper_vomito, antper_colitis, antper_otro, antper_otro_cual, antper_dentadura, antper_protesis,
    antper_observaciones, padece_enf, padece_enf_cual, enf_importante, enf_importante_cual, toma_medicamento, toma_medicamento_cual, toma_medicamento_dosis,
    toma_laxantes, toma_diureticos, toma_antiacidos, toma_analgesicos, practica_cirugia, practica_cirugia_cual, antfam_obesidad, antfam_obesidad_parent,
    antfam_diabetes, antfam_diabetes_parent, antfam_cancer, antfam_cancer_parent, antfam_hta, antfam_hta_parent, antfam_hipercolesterolemia,
    antfam_hipercolesterolemia_parent, antfam_hipertrigliceridemia, antfam_hipertrigliceridemia_parent, desayuno_alimentos, desayuno_tiempo,
    mediamanana_alimentos, mediamanana_tiempo, almuerzo_alimentos, almuerzo_tiempo, mediatarde_alimentos, mediatarde_tiempo, cena_alimentos,
    cena_tiempo, aerobicos, aerobicos_frecuencia, aerobicos_duracion, anaerobicos, anaerobicos_frecuencia, anaerobicos_duracion,
    musculatura, musculatura_frecuencia, musculatura_duracion, alcohol, alcohol_frecuencia, alcohol_cantidad, tabaco, tabaco_frecuencia,
    tabaco_cantidad, cafe, cafe_frecuencia, cafe_cantidad, signo_cabello, signo_ojos, signo_piel, signo_unas, signo_labios, signo_encias,
    alimentos_preferidos, alimentos_noagradan, alimentos_malestar, alergico, alergico_cual, peso_habitual, peso_actual, estatura, imc,
    circunferencia_brazo, circunferencia_cintura, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, cod_diag4, nom_diag4,
    plan_trata, id_atencion)

    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Metodo para listar todos los registros de hc de nutrición por medico y paciente
def listar_hc_nutricion(paciente, medico):
    regs_nutricion = []
    conn = db.connection()
    query = """ SELECT hcn.id_hcnutricion, hcn.fecha, hcn.hora, hcn.codigo, CONCAT(p.p_apellido,' ',p.s_apellido,' ',p.p_nombre,' ',p.s_nombre), hcn.id_atencion
                FROM hc_nutricion hcn INNER JOIN pacientes p ON p.num_doc = hcn.codigo WHERE hcn.codigo = %s AND hcn.medico = %s """ 

    params = (paciente, medico)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
        for row in result:
            regs_nutricion.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'codigo': row[3] ,'paciente': row[4], 'atencion': row[5]})

    conn.close()
    return regs_nutricion

#Metodo para listar el contenido de la hc de nutrición por id
def listar_hc_nutricion_id(id_hcnutricion):
    reg_nutricion = None
    conn = db.connection()
    query = "SELECT * FROM hc_nutricion WHERE id_hcnutricion = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id_hcnutricion, ))
        result = cursor.fetchone()
        reg_nutricion = result

    conn.close()
    return reg_nutricion              