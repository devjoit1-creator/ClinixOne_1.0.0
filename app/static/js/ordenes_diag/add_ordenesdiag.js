const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");

window.onload = () => {
    /* Fecha Actual */
    let fecha = new Date()
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(mes < 10){
        mes = "0" + mes
    }
    
    if(dia < 10){
        dia = "0" + dia
    }
    $fecha.value = anio +"-"+ mes +"-"+ dia
    /* Hora actual */
    let hora = fecha.getHours().toString().padStart(2, '0')
    let minutos = fecha.getMinutes().toString().padStart(2, '0')
    $hora.value = `${hora}:${minutos}`
}

/* Cargar cups al formalurio */
const $cod_servicio = document.getElementById("cod_servicio");
const $nom_servicio = document.getElementById("nom_servicio");
const $tablaBusquedaProcedimientosCups = document.getElementById("tablaBusquedaProcedimientosCups");

$tablaBusquedaProcedimientosCups.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataCups(data);
    closeAllModals();
});

const fillDataCups = (data) => {
    $cod_servicio.value = data[0].innerText;
    $nom_servicio.value = data[1].innerText;
}
/* Funciones para cerrar Modal */
function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}