/* Obtener Fecha y Hora actual */
const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");

window.onload = () => {
    /* Fecha Actual */
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if (mes < 10) {
        mes = "0" + mes;
    }
    
    if (dia < 10) {
        dia = "0" + dia;
    }
    $fecha.value = anio + "-" + mes + "-" + dia;

    /* Hora Actual */
    let hora = fecha.getHours().toString().padStart(2, '0')
    let minutos = fecha.getMinutes().toString().padStart(2, '0')
    $hora.value = `${hora}:${minutos}`
}

/* Cargar Diagnosticos al formulario */
const $cod_diag = document.getElementById("cod_diag");
const $nom_diag = document.getElementById("nom_diag");
const $cod_diag2 = document.getElementById("cod_diag2");
const $nom_diag2 = document.getElementById("nom_diag2");
const $tablaBusquedaDiagnosticosIncap = document.getElementById("tablaBusquedaDiagnosticosIncap");

$tablaBusquedaDiagnosticosIncap.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    if($cod_diag.value === '' && $nom_diag.value === ''){
        $cod_diag.value = data[0].innerText;
        $nom_diag.value = data[1].innerText;
    }else if($cod_diag2.value === '' && $nom_diag2.value === ''){
        $cod_diag2.value = data[0].innerText;
        $nom_diag2.value = data[1].innerText;
    }
    closeAllModals();
});

/* Limpiar todos los campos de diagnosticos */
const $btn_corregir = document.getElementById("btn_corregir");
function limpiarDiagnosticos() {
    $cod_diag.value = "";
    $nom_diag.value = "";
    $cod_diag2.value = "";
    $nom_diag2.value = "";
}; 

$btn_corregir.addEventListener("click", (e) => {
    e.preventDefault();
    limpiarDiagnosticos();
});

/* Calcular los días de incapacidad entre fechas */
const $fecha_inicio = document.getElementById("fecha_inicio")
const $fecha_fin = document.getElementById("fecha_fin")
const $dias = document.getElementById("dias")

$fecha_fin.addEventListener("change", () => {
    let inicio = new Date($fecha_inicio.value)
    let fin = new Date($fecha_fin.value)
    /* Diferencia en Milisegundos */
    let milisegundos = Math.abs(fin - inicio)
    /* Milisegundos a Dias */
    let milisegundosPorDia = 1000 * 60 * 60 * 24
    let dias = Math.ceil(milisegundos / milisegundosPorDia)
    $dias.value = dias;
})

/* Validar Formulario */
const $form_addincapacidad = document.getElementById("form_addincapacidad");
$form_addincapacidad.addEventListener("submit", (e) => {
    /* Diagnosticos */
    let codDiag = $cod_diag.value;
    let nomDiag = $nom_diag.value;
    let codDiag2 = $cod_diag2.value;
    let nomDiag2 = $nom_diag2.value;
    if(!codDiag || !nomDiag || !codDiag2 || !nomDiag2){
        e.preventDefault();
        Swal.fire({
            title: "Notificación",
            text: "Debe diligenciar el formulario con los campos obligatorios.",
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