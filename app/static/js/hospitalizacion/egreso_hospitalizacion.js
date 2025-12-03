/* Calcular Días Estancia */
const $fecha_ingreso = document.getElementById("fecha_ingreso");
const $fecha_salida = document.getElementById("fecha_salida");
const $dias_estancia = document.getElementById("dias_estancia");

$fecha_salida.addEventListener('change', () => {
    let ingreso = new Date($fecha_ingreso.value);
    let salida = new Date($fecha_salida.value);
    let diferenciaMilisegundos = salida - ingreso;

    // Convierte la diferencia a días
    let milisegundosPorDía = 1000 * 60 * 60 * 24;
    $dias_estancia.value = diferenciaMilisegundos / milisegundosPorDía;
})

/* Cargar datos de diagnistico salida desde el modal */
const $cod_diag_salida = document.getElementById("cod_diag_salida");
const $nom_diag_salida = document.getElementById("nom_diag_salida");
const $cod_diag_muerte = document.getElementById("cod_diag_muerte");
const $nom_diag_muerte = document.getElementById("nom_diag_muerte");
const $tablaBusquedaDiagnosticosEgresoHosp = document.getElementById("tablaBusquedaDiagnosticosEgresoHosp");

$tablaBusquedaDiagnosticosEgresoHosp.addEventListener('click', (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    if($cod_diag_salida.value === '' && $nom_diag_salida.value === ''){
        $cod_diag_salida.value = data[0].innerText;
        $nom_diag_salida.value = data[1].innerText;
    }else if($cod_diag_muerte.value === '' && $nom_diag_muerte.value === ''){
        $cod_diag_muerte.value = data[0].innerText;
        $nom_diag_muerte.value = data[1].innerText; 
    }
    closeAllModals();
})

const $btn_corregir = document.getElementById("btn_corregir");
function limpiarDiagnosticos() {
    $cod_diag_salida.value = "";
    $nom_diag_salida.value = "";
    $cod_diag_muerte.value = "";
    $nom_diag_muerte.value = "";
}; 

$btn_corregir.addEventListener("click", (e) => {
    e.preventDefault();
    limpiarDiagnosticos();
});


/* Activar campos de diagnostico de muerte y/o remitido salida */
const $estado_salida = document.getElementById("estado_salida");
const $diag_muerte = document.getElementById("diag_muerte");
const $remite_a = document.getElementById("remite_a");
const $remitido_salida = document.getElementById("remitido_salida");
$estado_salida.addEventListener("change", () => {
    /* ($estado_salida.value !== "02") ? $diag_muerte.style.display = "none" : $diag_muerte.style.display = "block";
    ($estado_salida.value !== "04") ? $remite_a.style.display = "none" : $remite_a.style.display = "block"; */
    if($estado_salida.value === "01"){
        /* Diagnostico Muerte */
        $diag_muerte.style.display = "none";
        $cod_diag_muerte.required = false;
        $nom_diag_muerte.required = false;
        $cod_diag_muerte.value = "";
        $nom_diag_muerte.value = "";
        /* Remitido a */
        $remite_a.style.display = "none";
        $remitido_salida.required = false;
        $remitido_salida.value = "";
    }else if($estado_salida.value === "02"){
        /* Diagnostico Muerte */
        $diag_muerte.style.display = "block";
        $cod_diag_muerte.required = true;
        $nom_diag_muerte.required = true;
        /* Remitido a */
        $remite_a.style.display = "none";
        $remitido_salida.required = false;
        $remitido_salida.value = "";
    }else if ($estado_salida.value === "04"){
        $diag_muerte.style.display = "none";
        $cod_diag_muerte.required = false;
        $nom_diag_muerte.required = false;
        $cod_diag_muerte.value = "";
        $nom_diag_muerte.value = "";
        /* Remitido a */
        $remite_a.style.display = "block";
        $remitido_salida.required = true;
    }
})

/* Validar Formulario */
const $form_addegresohosp = document.getElementById("form_addegresohosp");
$form_addegresohosp.addEventListener("submit", (e) => {
    /* Diagnostico salida */
    let codDiagSalida = $cod_diag_salida.value;
    let nomDiagSalida = $nom_diag_salida.value;
    if(!codDiagSalida || !nomDiagSalida){
        e.preventDefault();
        Swal.fire({
            title: 'Notificación',
            text: 'Debe diligenciar el formulario con los campos obligatorios.',
            icon: 'warning'
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
})

/* Funciones para cerrar modal */
function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

function closeModal($el) {
    $el.classList.remove('is-active');
}

