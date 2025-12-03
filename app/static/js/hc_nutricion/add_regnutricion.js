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
const $padece_enf = document.getElementById("padece_enf");
const $padece_enf_cual = document.getElementById("padece_enf_cual");
const $enf_importante = document.getElementById("enf_importante");
const $enf_importante_cual = document.getElementById("enf_importante_cual");

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

$enf_importante.addEventListener("change", () => {
    if($enf_importante.value === "NO"){
        $enf_importante_cual.style.display = "none";
        $enf_importante_cual.required = false
        $enf_importante_cual.value = "";
    }else if($enf_importante.value === "SÍ"){
        $enf_importante_cual.style.display = "block";
        $enf_importante_cual.required = true
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

/* Activar campos preguntas de antecedentes familiares parentesco */
const $antfam_obesidad = document.getElementById("antfam_obesidad");
const $antfam_obesidad_parent = document.getElementById("antfam_obesidad_parent");

$antfam_obesidad.addEventListener("change", () => {
    if($antfam_obesidad.value === "NO"){
        $antfam_obesidad_parent.style.display = "none";
        $antfam_obesidad_parent.required = false
        $antfam_obesidad_parent.value = "";
    }else if($antfam_obesidad.value === "SÍ"){
        $antfam_obesidad_parent.style.display = "block";
        $antfam_obesidad_parent.required = true
    }
})

const $antfam_diabetes = document.getElementById("antfam_diabetes");
const $antfam_diabetes_parent = document.getElementById("antfam_diabetes_parent")

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

const $antfam_hipercolesterolemia = document.getElementById("antfam_hipercolesterolemia");
const $antfam_hipercolesterolemia_parent = document.getElementById("antfam_hipercolesterolemia_parent")

$antfam_hipercolesterolemia.addEventListener("change", () => {
    if($antfam_hipercolesterolemia.value === "NO"){
        $antfam_hipercolesterolemia_parent.style.display = "none";
        $antfam_hipercolesterolemia_parent.required = false
        $antfam_hipercolesterolemia_parent.value = "";
    }else if($antfam_hipercolesterolemia.value === "SÍ"){
        $antfam_hipercolesterolemia_parent.style.display = "block";
        $antfam_hipercolesterolemia_parent.required = true
    }
})

const $antfam_hipertrigliceridemia = document.getElementById("antfam_hipertrigliceridemia");
const $antfam_hipertrigliceridemia_parent = document.getElementById("antfam_hipertrigliceridemia_parent")

$antfam_hipertrigliceridemia.addEventListener("change", () => {
    if($antfam_hipertrigliceridemia.value === "NO"){
        $antfam_hipertrigliceridemia_parent.style.display = "none";
        $antfam_hipertrigliceridemia_parent.required = false
        $antfam_hipertrigliceridemia_parent.value = "";
    }else if($antfam_hipertrigliceridemia.value === "SÍ"){
        $antfam_hipertrigliceridemia_parent.style.display = "block";
        $antfam_hipertrigliceridemia_parent.required = true
    }
})

/* Activar campos frecuencia y duración Ejercicios - Habitos */
const $aerobicos = document.getElementById("aerobicos");
const $aerobicos_frecuencia = document.getElementById("aerobicos_frecuencia");
const $aerobicos_duracion = document.getElementById("aerobicos_duracion");

$aerobicos.addEventListener("change", () => {
    if($aerobicos.value === "NO"){
        $aerobicos_frecuencia.style.display = "none";
        $aerobicos_duracion.style.display = "none";
        $aerobicos_frecuencia.required = false
        $aerobicos_duracion.required = false
        $aerobicos_frecuencia.value = "";
        $aerobicos_duracion.value = "";
    }else if($aerobicos.value === "SÍ"){
        $aerobicos_frecuencia.style.display = "block";
        $aerobicos_duracion.style.display = "block";
        $aerobicos_frecuencia.required = true
        $aerobicos_duracion.required = true
    }
})

const $anaerobicos = document.getElementById("anaerobicos");
const $anaerobicos_frecuencia = document.getElementById("anaerobicos_frecuencia");
const $anaerobicos_duracion = document.getElementById("anaerobicos_duracion");

$anaerobicos.addEventListener("change", () => {
    if($anaerobicos.value === "NO"){
        $anaerobicos_frecuencia.style.display = "none";
        $anaerobicos_duracion.style.display = "none";
        $anaerobicos_frecuencia.required = false
        $anaerobicos_duracion.required = false
        $anaerobicos_frecuencia.value = "";
        $anaerobicos_duracion.value = "";
    }else if($anaerobicos.value === "SÍ"){
        $anaerobicos_frecuencia.style.display = "block";
        $anaerobicos_duracion.style.display = "block";
        $anaerobicos_frecuencia.required = true
        $anaerobicos_duracion.required = true
    }
})

const $musculatura = document.getElementById("musculatura");
const $musculatura_frecuencia = document.getElementById("musculatura_frecuencia");
const $musculatura_duracion = document.getElementById("musculatura_duracion");

$musculatura.addEventListener("change", () => {
    if($musculatura.value === "NO"){
        $musculatura_frecuencia.style.display = "none";
        $musculatura_duracion.style.display = "none";
        $musculatura_frecuencia.required = false
        $musculatura_duracion.required = false
        $musculatura_frecuencia.value = "";
        $musculatura_duracion.value = "";
    }else if($musculatura.value === "SÍ"){
        $musculatura_frecuencia.style.display = "block";
        $musculatura_duracion.style.display = "block";
        $musculatura_frecuencia.required = true
        $musculatura_duracion.required = true
    }
})

/* Activar campos frecuencia y cantidad Consumo - Habitos */
const $alcohol = document.getElementById("alcohol");
const $alcohol_frecuencia = document.getElementById("alcohol_frecuencia");
const $alcohol_cantidad = document.getElementById("alcohol_cantidad");

$alcohol.addEventListener("change", () => {
    if($alcohol.value === "NO"){
        $alcohol_frecuencia.style.display = "none";
        $alcohol_cantidad.style.display = "none";
        $alcohol_frecuencia.required = false
        $alcohol_cantidad.required = false
        $alcohol_frecuencia.value = "";
        $alcohol_cantidad.value = "";
    }else if($alcohol.value === "SÍ"){
        $alcohol_frecuencia.style.display = "block";
        $alcohol_cantidad.style.display = "block";
        $alcohol_frecuencia.required = true
        $alcohol_cantidad.required = true
    }
})

const $tabaco = document.getElementById("tabaco");
const $tabaco_frecuencia = document.getElementById("tabaco_frecuencia");
const $tabaco_cantidad = document.getElementById("tabaco_cantidad");

$tabaco.addEventListener("change", () => {
    if($tabaco.value === "NO"){
        $tabaco_frecuencia.style.display = "none";
        $tabaco_cantidad.style.display = "none";
        $tabaco_frecuencia.required = false
        $tabaco_cantidad.required = false
        $tabaco_frecuencia.value = "";
        $tabaco_cantidad.value = "";
    }else if($tabaco.value === "SÍ"){
        $tabaco_frecuencia.style.display = "block";
        $tabaco_cantidad.style.display = "block";
        $tabaco_frecuencia.required = true
        $tabaco_cantidad.required = true
    }
})

const $cafe = document.getElementById("cafe");
const $cafe_frecuencia = document.getElementById("cafe_frecuencia");
const $cafe_cantidad = document.getElementById("cafe_cantidad");

$cafe.addEventListener("change", () => {
    if($cafe.value === "NO"){
        $cafe_frecuencia.style.display = "none";
        $cafe_cantidad.style.display = "none";
        $cafe_frecuencia.required = false
        $cafe_cantidad.required = false
        $cafe_frecuencia.value = "";
        $cafe_cantidad.value = "";
    }else if($cafe.value === "SÍ"){
        $cafe_frecuencia.style.display = "block";
        $cafe_cantidad.style.display = "block";
        $cafe_frecuencia.required = true
        $cafe_cantidad.required = true
    }
})

/* Activar campo Alergico - Alimentación complementaria */
const $alergico = document.getElementById("alergico");
const $alergico_cual = document.getElementById("alergico_cual");

$alergico.addEventListener("change", () => {
    if($alergico.value === "NO"){
        $alergico_cual.style.display = "none";
        $alergico_cual.required = false
        $alergico_cual.value = "";
    }else if($alergico.value === "SÍ"){
        $alergico_cual.style.display = "block";
        $alergico_cual.required = true
    }
})

/* Calculo de IMC. Indice de Masa Corporal */
const $peso_actual = document.getElementById("peso_actual");
const $estatura = document.getElementById("estatura");
const $imc = document.getElementById("imc");
const $estado_imc = document.getElementById("estado_imc");

$peso_actual.addEventListener("change", () => {
    let calculo = $peso_actual.value / Math.pow($estatura.value, 2)
    $imc.value = Math.round(calculo);

    if($imc.value < 18.5 ){
        $estado_imc.innerHTML = "Nivel de Peso: Bajo Peso"
    }else if($imc.value > 18.5 && $imc.value < 24.9 ){
        $estado_imc.innerHTML = "Nivel de Peso: Peso Saludable"
    }else if($imc.value > 25.0 && $imc.value < 29.9 ){
        $estado_imc.innerHTML= "Nivel de Peso es: Sobrepeso"
    }else{
        $estado_imc.innerHTML = "Nivel de Peso es: Obesidad"
    }
})

$estatura.addEventListener("change", () => {
    let calculo = $peso_actual.value / Math.pow($estatura.value, 2)
    $imc.value = Math.round(calculo);

    if($imc.value < 18.5 ){
        $estado_imc.innerHTML = "Nivel de Peso: Bajo Peso"
    }else if($imc.value > 18.5 && $imc.value < 24.9 ){
        $estado_imc.innerHTML = "Nivel de Peso: Peso Saludable"
    }else if($imc.value > 25.0 && $imc.value < 29.9 ){
        $estado_imc.innerHTML= "Nivel de Peso es: Sobrepeso"
    }else{
        $estado_imc.innerHTML = "Nivel de Peso es: Obesidad"
    }
})

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
const $tablaBusquedaDiagnosticosNutricion = document.getElementById("tablaBusquedaDiagnosticosNutricion");
$tablaBusquedaDiagnosticosNutricion.addEventListener("click", (e) => {
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
const $form_addregnutricion = document.getElementById("form_addregnutricion");
$form_addregnutricion.addEventListener("submit", (e) => {
    /* Diagnostico Principal */
    let codDiag1 = $cod_diag1.value;
    let nomDiag1 = $nom_diag1.value;
    if(!codDiag1 || !nomDiag1){
        e.preventDefault();
        Swal.fire({
           title: "Notificación!",
           text: "Debe diligenciar el formulario con los campos obligatorios.",
           icon: "warning"
        });
        return;
    };

    /* Loading */
    Swal.fire({
        showConfirmButton: false,
        allowEscapeKey: false,
        allowOutsideClick: false,
        didOpen:  () => {
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
