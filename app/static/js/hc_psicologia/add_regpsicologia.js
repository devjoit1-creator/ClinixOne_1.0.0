/* Fecha y Hora Actual */
const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");

window.onload = () => {
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(mes < 10){
        mes = "0" + mes;
    }

    if(dia < 10){
        dia = "0" + dia;
    }

    $fecha.value = anio + "-" + mes + "-" + dia;
    let hora = fecha.getHours().toString().padStart(2, '0')
    let minutos = fecha.getMinutes().toString().padStart(2, '0')
    $hora.value = `${hora}:${minutos}`
};

/* Activar campo otro antecedente - cual ?  */
const $antper_otro = document.getElementById("antper_otro");
const $antper_otro_cual = document.getElementById("antper_otro_cual");
$antper_otro.addEventListener("change", () => {
    if ($antper_otro.value === "NO"){
        $antper_otro_cual.style.display = "none";
        $antper_otro_cual.required = false
        $antper_otro_cual.value = "";
    }else if($antper_otro.value === "SÍ") {
        $antper_otro_cual.style.display = "block";
        $antper_otro_cual.required = true
    }
})

/* Activar campos preguntas de antecedentes personales */
const $practica_cirugia = document.getElementById("practica_cirugia");
const $practica_cirugia_cual = document.getElementById("practica_cirugia_cual");

$practica_cirugia.addEventListener("change", () => {
    if($practica_cirugia.value === "NO"){
        $practica_cirugia_cual.style.display = "none";
        $practica_cirugia_cual.required = false
        $practica_cirugia_cual.value = "";
    }else if($practica_cirugia.value === "SÍ"){
        $practica_cirugia_cual.style.display = "block";
        $practica_cirugia_cual.required = true
    }
})

const $padece_enf = document.getElementById("padece_enf");
const $padece_enf_cual = document.getElementById("padece_enf_cual");

$padece_enf.addEventListener("change", () => {
    if($padece_enf.value === "NO"){
        $padece_enf_cual.style.display = "none";
        $padece_enf_cual.required = false
        $padece_enf_cual.value = "";
    }else if($padece_enf.value === "SÍ"){
        $padece_enf_cual.style.display = "block";
        $padece_enf_cual.required = true
    }
})

const $practica_tratamiento = document.getElementById("practica_tratamiento");
const $practica_tratamiento_cual = document.getElementById("practica_tratamiento_cual");

$practica_tratamiento.addEventListener("change", () => {
    if ($practica_tratamiento.value === "NO") {
        $practica_tratamiento_cual.style.display = "none";
        $practica_tratamiento_cual.required = false;
        $practica_tratamiento_cual.value = "";
    } else if($practica_tratamiento.value === "SÍ"){
        $practica_tratamiento_cual.style.display = "block";
        $practica_tratamiento_cual.required = true;
    }
})

const $toma_medicamento = document.getElementById("toma_medicamento");
const $toma_medicamento_cual = document.getElementById("toma_medicamento_cual");
const $toma_medicamento_dosis = document.getElementById("toma_medicamento_dosis");

$toma_medicamento.addEventListener("change", () => {
    if($toma_medicamento.value === "NO"){
        $toma_medicamento_cual.style.display = "none";
        $toma_medicamento_dosis.style.display = "none";
        $toma_medicamento_cual.required = false
        $toma_medicamento_dosis.required = false
        $toma_medicamento_cual.value = "";
        $toma_medicamento_dosis.value = "";
    }else if($toma_medicamento.value == "SÍ"){
        $toma_medicamento_cual.style.display = "block";
        $toma_medicamento_dosis.style.display = "block";
        $toma_medicamento_cual.required = true
        $toma_medicamento_dosis.required = true
    }
})

/* Activar campos preguntas de antecedentes familiares parentesco */
const $antfam_alergia = document.getElementById("antfam_alergia");
const $antfam_alergia_parent = document.getElementById("antfam_alergia_parent");

$antfam_alergia.addEventListener("change", () => {
    if($antfam_alergia.value === "NO"){
        $antfam_alergia_parent.style.display = "none";
        $antfam_alergia_parent.required = false
        $antfam_alergia_parent.value = "";
    }else if($antfam_alergia.value === "SÍ"){
        $antfam_alergia_parent.style.display = "block";
        $antfam_alergia_parent.required = true
    }
})

const $antfam_diabetes = document.getElementById("antfam_diabetes");
const $antfam_diabetes_parent = document.getElementById("antfam_diabetes_parent");

$antfam_diabetes.addEventListener("change", () => {
    if($antfam_diabetes.value === "NO"){
        $antfam_diabetes_parent.style.display = "none";
        $antfam_diabetes_parent.required = false
        $antfam_diabetes_parent.value = "";
    }else if($antfam_diabetes.value === "SÍ"){
        $antfam_diabetes_parent.style.display = "block";
        $antfam_diabetes_parent.required = true
    }
})

const $antfam_cancer = document.getElementById("antfam_cancer");
const $antfam_cancer_parent = document.getElementById("antfam_cancer_parent");

$antfam_cancer.addEventListener("change", () => {
    if($antfam_cancer.value === "NO"){
        $antfam_cancer_parent.style.display = "none";
        $antfam_cancer_parent.required = false
        $antfam_cancer_parent.value = "";
    }else if($antfam_cancer.value === "SÍ"){
        $antfam_cancer_parent.style.display = "block";
        $antfam_cancer_parent.required = true
    }
})

const $antfam_hta = document.getElementById("antfam_hta");
const $antfam_hta_parent = document.getElementById("antfam_hta_parent");

$antfam_hta.addEventListener("change", () => {
    if($antfam_hta.value === "NO"){
        $antfam_hta_parent.style.display = "none";
        $antfam_hta_parent.required = false
        $antfam_hta_parent.value = "";
    }else if($antfam_hta.value === "SÍ"){
        $antfam_hta_parent.style.display = "block";
        $antfam_hta_parent.required = true
    }
})

const $antfam_respiratoria = document.getElementById("antfam_respiratoria");
const $antfam_respiratoria_parent = document.getElementById("antfam_respiratoria_parent");

$antfam_respiratoria.addEventListener("change", () => {
    if($antfam_respiratoria.value === "NO"){
        $antfam_respiratoria_parent.style.display = "none";
        $antfam_respiratoria_parent.required = false
        $antfam_respiratoria_parent.value = "";
    }else if($antfam_respiratoria.value === "SÍ"){
        $antfam_respiratoria_parent.style.display = "block";
        $antfam_respiratoria_parent.required = true
    }
})

const $antfam_asma = document.getElementById("antfam_asma");
const $antfam_asma_parent = document.getElementById("antfam_asma_parent");

$antfam_asma.addEventListener("change", () => {
    if($antfam_asma.value === "NO"){
        $antfam_asma_parent.style.display = "none";
        $antfam_asma_parent.required = false
        $antfam_asma_parent.value = "";
    }else if($antfam_asma.value === "SÍ"){
        $antfam_asma_parent.style.display = "block";
        $antfam_asma_parent.required = true
    }
})

const $antfam_epilepsia = document.getElementById("antfam_epilepsia");
const $antfam_epilepsia_parent = document.getElementById("antfam_epilepsia_parent");

$antfam_epilepsia.addEventListener("change", () => {
    if($antfam_epilepsia.value === "NO"){
        $antfam_epilepsia_parent.style.display = "none";
        $antfam_epilepsia_parent.required = false
        $antfam_epilepsia_parent.value = "";
    }else if($antfam_epilepsia.value === "SÍ"){
        $antfam_epilepsia_parent.style.display = "block";
        $antfam_epilepsia_parent.required = true
    }
})

const $antfam_ceguera = document.getElementById("antfam_ceguera");
const $antfam_ceguera_parent = document.getElementById("antfam_ceguera_parent");

$antfam_ceguera.addEventListener("change", () => {
    if($antfam_ceguera.value === "NO"){
        $antfam_ceguera_parent.style.display = "none";
        $antfam_ceguera_parent.required = false
        $antfam_ceguera_parent.value = "";
    }else if($antfam_ceguera.value === "SÍ"){
        $antfam_ceguera_parent.style.display = "block";
        $antfam_ceguera_parent.required = true
    }
})

const $antfam_dislipidemia = document.getElementById("antfam_dislipidemia");
const $antfam_dislipidemia_parent = document.getElementById("antfam_dislipidemia_parent");

$antfam_dislipidemia.addEventListener("change", () => {
    if($antfam_dislipidemia.value === "NO"){
        $antfam_dislipidemia_parent.style.display = "none";
        $antfam_dislipidemia_parent.required = false
        $antfam_dislipidemia_parent.value = "";
    }else if($antfam_dislipidemia.value === "SÍ"){
        $antfam_dislipidemia_parent.style.display = "block";
        $antfam_dislipidemia_parent.required = true
    }
})

const $antfam_alcoholismo = document.getElementById("antfam_alcoholismo");
const $antfam_alcoholismo_parent = document.getElementById("antfam_alcoholismo_parent");

$antfam_alcoholismo.addEventListener("change", () => {
    if($antfam_alcoholismo.value === "NO"){
        $antfam_alcoholismo_parent.style.display = "none";
        $antfam_alcoholismo_parent.required = false
        $antfam_alcoholismo_parent.value = "";
    }else if($antfam_alcoholismo.value === "SÍ"){
        $antfam_alcoholismo_parent.style.display = "block";
        $antfam_alcoholismo_parent.required = true
    }
})

const $antfam_tabaquismo = document.getElementById("antfam_tabaquismo");
const $antfam_tabaquismo_parent = document.getElementById("antfam_tabaquismo_parent");

$antfam_tabaquismo.addEventListener("change", () => {
    if($antfam_tabaquismo.value === "NO"){
        $antfam_tabaquismo_parent.style.display = "none";
        $antfam_tabaquismo_parent.required = false
        $antfam_tabaquismo_parent.value = "";
    }else if($antfam_tabaquismo.value === "SÍ"){
        $antfam_tabaquismo_parent.style.display = "block";
        $antfam_tabaquismo_parent.required = true
    }
})

const $antfam_drogadiccion = document.getElementById("antfam_drogadiccion");
const $antfam_drogadiccion_parent = document.getElementById("antfam_drogadiccion_parent");

$antfam_drogadiccion.addEventListener("change", () => {
    if($antfam_drogadiccion.value === "NO"){
        $antfam_drogadiccion_parent.style.display = "none";
        $antfam_drogadiccion_parent.required = false
        $antfam_drogadiccion_parent.value = "";
    }else if($antfam_drogadiccion.value === "SÍ"){
        $antfam_drogadiccion_parent.style.display = "block";
        $antfam_drogadiccion_parent.required = true
    }
})

const $antfam_tuberculosis = document.getElementById("antfam_tuberculosis");
const $antfam_tuberculosis_parent = document.getElementById("antfam_tuberculosis_parent");

$antfam_tuberculosis.addEventListener("change", () => {
    if($antfam_tuberculosis.value === "NO"){
        $antfam_tuberculosis_parent.style.display = "none";
        $antfam_tuberculosis_parent.required = false
        $antfam_tuberculosis_parent.value = "";
    }else if($antfam_tuberculosis.value === "SÍ"){
        $antfam_tuberculosis_parent.style.display = "block";
        $antfam_tuberculosis_parent.required = true
    }
})

const $antfam_violencia = document.getElementById("antfam_violencia");
const $antfam_violencia_parent = document.getElementById("antfam_violencia_parent");

$antfam_violencia.addEventListener("change", () => {
    if($antfam_violencia.value === "NO"){
        $antfam_violencia_parent.style.display = "none";
        $antfam_violencia_parent.required = false
        $antfam_violencia_parent.value = "";
    }else if($antfam_violencia.value === "SÍ"){
        $antfam_violencia_parent.style.display = "block";
        $antfam_violencia_parent.required = true
    }
})

/* Diligenciar campos de examen mental y fisico con la palabra "Normal" */
const $check_sueno = document.getElementById("check_sueno");
const $estado_sueno = document.getElementById("estado_sueno");

const cambiarEstadoSueno = () => {
    if($estado_sueno.value === ""){
        $estado_sueno.value = "Normal";
        $estado_sueno.readonly = true;
    }else{
        $estado_sueno.value = "";
        $estado_sueno.readonly = false;
    }
}
$check_sueno.addEventListener('click', cambiarEstadoSueno)

const $check_concentracion = document.getElementById("check_concentracion");
const $estado_concentracion = document.getElementById("estado_concentracion");

const cambiarEstadoConcentracion = () => {
    if($estado_concentracion.value === ""){
        $estado_concentracion.value = "Normal";
        $estado_concentracion.readonly = true; 
    }else{
        $estado_concentracion.value = "";
        $estado_concentracion.readonly = false;
    }
}
$check_concentracion.addEventListener('click', cambiarEstadoConcentracion)

const $check_juicio = document.getElementById("check_juicio");
const $estado_juicio = document.getElementById("estado_juicio");

const cambiarEstadoJuicio = () => {
    if($estado_juicio.value === ""){
        $estado_juicio.value = "Normal";
        $estado_juicio.readonly = true;
    }else{
        $estado_juicio.value = "";
        $estado_juicio.readonly = false;
    }
}
$check_juicio.addEventListener('click', cambiarEstadoJuicio)

const $check_intelectual = document.getElementById("check_intelectual");
const $estado_intelectual = document.getElementById("estado_intelectual");

const cambiarEstadoIntelectual = () => {
    if($estado_intelectual.value === ""){
        $estado_intelectual.value = "Normal";
        $estado_intelectual.readonly = true;
    }else{
        $estado_intelectual.value = "";
        $estado_intelectual.readonly = false;
    }
}
$check_intelectual.addEventListener('click', cambiarEstadoIntelectual)

const $check_orientacion = document.getElementById("check_orientacion");
const $estado_orientacion = document.getElementById("estado_orientacion");

const cambiarEstadoOrientacion = () => {
    if($estado_orientacion.value === ""){
        $estado_orientacion.value = "Normal";
        $estado_orientacion.readonly = true;
    }else{
        $estado_orientacion.value = "";
        $estado_orientacion.readonly = false;
    }
}
$check_orientacion.addEventListener('click', cambiarEstadoOrientacion)

const $check_sensopercepcion = document.getElementById("check_sensopercepcion");
const $estado_sensopercepcion = document.getElementById("estado_sensopercepcion");

const cambiarEstadoSensopercepcion = () => {
    if($estado_sensopercepcion.value === ""){
        $estado_sensopercepcion.value = "Normal";
        $estado_sensopercepcion.readonly = true;
    }else{
        $estado_sensopercepcion.value = "";
        $estado_sensopercepcion.readonly = false;
    }
}
$check_sensopercepcion.addEventListener('click', cambiarEstadoSensopercepcion)

const $check_conciencia = document.getElementById("check_conciencia");
const $estado_conciencia = document.getElementById("estado_conciencia");

const cambiarEstadoConciencia = () => {
    if($estado_conciencia.value === ""){
        $estado_conciencia.value = "Normal";
        $estado_conciencia.readonly = true;
    }else{
        $estado_conciencia.value = "";
        $estado_conciencia.readonly = false;
    }
}
$check_conciencia.addEventListener('click', cambiarEstadoConciencia)

const $check_memoria = document.getElementById("check_memoria");
const $estado_memoria = document.getElementById("estado_memoria");

const cambiarEstadoMemoria = () => {
    if($estado_memoria.value === ""){
        $estado_memoria.value = "Normal";
        $estado_memoria.readonly = true;
    }else{
        $estado_memoria.value = "";
        $estado_memoria.readonly = false;
    }
}
$check_memoria.addEventListener('click', cambiarEstadoMemoria)

const $check_pensamiento = document.getElementById("check_pensamiento");
const $estado_pensamiento = document.getElementById("estado_pensamiento");

const cambiarEstadoPensamiento = () => {
    if($estado_pensamiento.value === ""){
        $estado_pensamiento.value = "Normal";
        $estado_pensamiento.readonly = true;
    }else{
        $estado_pensamiento.value = "";
        $estado_pensamiento.readonly = false;
    }
}
$check_pensamiento.addEventListener('click', cambiarEstadoPensamiento)

const $check_afecto = document.getElementById("check_afecto");
const $estado_afecto = document.getElementById("estado_afecto");

const cambiarEstadoAfecto = () => {
    if($estado_afecto.value === ""){
        $estado_afecto.value = "Normal";
        $estado_afecto.readonly = true;
    }else{
        $estado_afecto.value = "";
        $estado_afecto.readonly = false;
    }
}
$check_afecto.addEventListener('click', cambiarEstadoAfecto)

const $check_higiene = document.getElementById("check_higiene");
const $estado_higiene = document.getElementById("estado_higiene");

const cambiarEstadoHigiene = () => {
    if($estado_higiene.value === ""){
        $estado_higiene.value = "Normal";
        $estado_higiene.readonly = true;
    }else{
        $estado_higiene.value = "";
        $estado_higiene.readonly = false;
    }
}
$check_higiene.addEventListener('click', cambiarEstadoHigiene)

const $check_postura = document.getElementById("check_postura");
const $estado_postura = document.getElementById("estado_postura");

const cambiarEstadoPostura = () => {
    if($estado_postura.value === ""){
        $estado_postura.value = "Normal";
        $estado_postura.readonly = true;
    }else{
        $estado_postura.value = "";
        $estado_postura.readonly = false;
    }
}
$check_postura.addEventListener('click', cambiarEstadoPostura)

const $check_expresion = document.getElementById("check_expresion");
const $estado_expresion = document.getElementById("estado_expresion");

const cambiarEstadoExpresion = () => {
    if($estado_expresion.value === ""){
        $estado_expresion.value = "Normal";
        $estado_expresion.readonly = true;
    }else{
        $estado_expresion.value = "";
        $estado_expresion.readonly = false;
    }
}
$check_expresion.addEventListener('click', cambiarEstadoExpresion)

const $check_alimentacion = document.getElementById("check_alimentacion");
const $estado_alimentacion = document.getElementById("estado_alimentacion");

const cambiarEstadoAlimentacion = () => {
    if($estado_alimentacion.value === ""){
        $estado_alimentacion.value = "Normal";
        $estado_alimentacion.readonly = true;
    }else{
        $estado_alimentacion.value = "";
        $estado_alimentacion.readonly = false;
    }
}
$check_alimentacion.addEventListener('click', cambiarEstadoAlimentacion)

/* Selección de Diagnostico Principal y Relacionados */
const $cod_diag1 = document.getElementById("cod_diag1");
const $nom_diag1 = document.getElementById("nom_diag1");
const $cod_diag2 = document.getElementById("cod_diag2");
const $nom_diag2 = document.getElementById("nom_diag2");
const $cod_diag3 = document.getElementById("cod_diag3");
const $nom_diag3 = document.getElementById("nom_diag3");
const $cod_diag4 = document.getElementById("cod_diag4");
const $nom_diag4 = document.getElementById("nom_diag4");
/* Cargar Datos de Modal diagnosticos a sus campos */
const $tablaBusquedaDiagnosticosPsicologia = document.getElementById("tablaBusquedaDiagnosticosPsicologia");
$tablaBusquedaDiagnosticosPsicologia.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    if($cod_diag1.value === '' && $nom_diag1.value === ''){
        $cod_diag1.value = data[0].innerText;
        $nom_diag1.value = data[1].innerText;
    }else if($cod_diag2.value === '' && $nom_diag2.value === ''){
        $cod_diag2.value = data[0].innerText;
        $nom_diag2.value = data[1].innerText; 
    }else if($cod_diag3.value === '' && $nom_diag3.value === ''){
        $cod_diag3.value = data[0].innerText;
        $nom_diag3.value = data[1].innerText;
    }else if($cod_diag4.value === '' && $nom_diag4.value === ''){
        $cod_diag4.value = data[0].innerText;
        $nom_diag4.value = data[1].innerText;
    }
    closeAllModals();
});

/* Limpiar los diagnosticos */
const $btn_corregir = document.getElementById("btn_corregir");
function limpiarDiagnosticos() {
    $cod_diag1.value = "";
    $nom_diag1.value = "";
    $cod_diag2.value = "";
    $nom_diag2.value = "";
    $cod_diag3.value = "";
    $nom_diag3.value = "";
    $cod_diag4.value = "";
    $nom_diag4.value = "";
}; 

$btn_corregir.addEventListener("click", (e) => {
    e.preventDefault();
    limpiarDiagnosticos();
});

/* Validar Formulario */
const $form_addregpsicologia = document.getElementById("form_addregpsicologia");
$form_addregpsicologia.addEventListener("submit", (e) => {
    /* Diagnostico principal */
    let codDiag1 = $cod_diag1.value;
    let nomDiag1 = $nom_diag1.value;
    if (!codDiag1 || !nomDiag1) {
        e.preventDefault();
        Swal.fire({
            title: "Notificación!",
            text: "Debe diligenciar el formulario con sus campos obligatorios.",
            icon: "warning"
        });
        return;
    };

    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });
});

/* Funciones para cerrar modal */
function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

function closeModal($el) {
    $el.classList.remove('is-active');
}
