/* Cargar datos de paciente y atención desde la tabla */
const $atencion = document.getElementById("atencion");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tablaAtencionesHosp = document.getElementById("tablaAtencionesHosp");
const $containerPanelHC = document.getElementById("containerPanelHC");

$tablaAtencionesHosp.addEventListener('click', (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataAtencionHosp(data);
    $containerPanelHC.style.display = "block";
})

const fillDataAtencionHosp = (data) => {
    $atencion.value = data[0].innerText;
    $codigo.value = data[2].innerText;
    $paciente.value = data[3].innerText;
}