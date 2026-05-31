// Constantes
const $fecha_entrada = document.getElementById("fecha_entrada");
const $hora_entrada = document.getElementById("hora_entrada");
const $cod_tercero = document.getElementById("cod_tercero");
const $nom_tercero = document.getElementById("nom_tercero");
const $tablaBusquedaTercerosEntradaFarm = document.getElementById("tablaBusquedaTercerosEntradaFarm");
const $cod_referencia = document.getElementById("cod_referencia");
const $nom_referencia = document.getElementById("nom_referencia");
const $registro_invima = document.getElementById("registro_invima");
const $tablaBusquedaMedicamentosEntradaFarm = document.getElementById("tablaBusquedaMedicamentosEntradaFarm");
const $btn_cancelar = document.getElementById("btn_cancelar");
const $fecha_vencimiento = document.getElementById("fecha_vencimiento");

// Fecha Actual del Sistema
document.addEventListener("DOMContentLoaded", () => {
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(dia < 10){
        dia = "0" + dia;
    };

    if(mes < 10){
        mes= "0" + mes;
    };

    $fecha_entrada.value = anio + "-" + mes + "-" + dia;
    
    let fecha_venc = new Date();
    fecha_venc.setDate(fecha_venc.getDate() + 30);
    let anio_venc = fecha_venc.getFullYear();
    let mes_venc = fecha_venc.getMonth() + 1;
    let dia_venc = fecha_venc.getDate();

     if(dia_venc < 10){
        dia_venc = "0" + dia_venc;
    };

    if(mes_venc < 10){
        mes_venc= "0" + mes_venc;
    };

    $fecha_vencimiento.value = anio_venc + "-" + mes_venc + "-" + dia_venc;


    // Hora actual
    let hora = fecha.getHours().toString().padStart(2, "0");
    let minutos = fecha.getMinutes().toString().padStart(2, "0");
    $hora_entrada.value = `${hora}:${minutos}`;
});

// Modo Cancelar
$btn_cancelar.addEventListener("click", (e) => {
    e.preventDefault();
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Los cambios no se guardaran.",
        icon: "question",
        confirmButtonText: "Si, Cancelar!",
        confirmButtonColor: "#48c78e",
        cancelButtonText: "No, Continuar",
        cancelButtonColor: "#f14668",
        showCancelButton: true,
        allowOutsideClick: false
    })
    .then((result) => {
        if(result.isConfirmed){
            window.location.href = "/entradas_farmacia"
        }
    });
});

/* Seleccionar Datos de tabla terceros */
$tablaBusquedaTercerosEntradaFarm.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    $cod_tercero.value = data[0].innerText;
    $nom_tercero.value = data[1].innerText;
    closeAllModals();
});

/* Seleccionar Datos de tabla Medicamentos */
$tablaBusquedaMedicamentosEntradaFarm.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    $cod_referencia.value = data[0].innerText;
    $nom_referencia.value = data[1].innerText;
    $registro_invima.value = data[2].innerText;
    closeAllModals();
});

/*  Cerrar Modals */
function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
    closeModal($modal);
    });
}