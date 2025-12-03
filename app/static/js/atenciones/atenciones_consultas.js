const $atencion = document.getElementById("atencion");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $containerPanelHC = document.getElementById("containerPanelHC");

const $tablaAtenciones = document.getElementById("tablaAtenciones");
$tablaAtenciones.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataAtencion(data);
    $containerPanelHC.style.display = "block";
});

const fillDataAtencion = (data) => {
    $atencion.value = data[0].innerText;
    $codigo.value = data[3].innerText;
    $paciente.value = data[4].innerText;
};

/* Cargar Fecha Actual */
/* window.onload = function () {
    let fecha = new Date()
    let dia = fecha.getDate();
    let mes = fecha.getMonth() + 1;
    let anio = fecha.getFullYear();
    if (dia < 10) {
        dia = "0" + dia;
    }
    if (mes < 10) {
        mes = "0" + mes;
    }
    document.getElementById("fecha_atencion").value = anio + "-" + mes + "-" + dia;
} */