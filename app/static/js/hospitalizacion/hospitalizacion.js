/* Constantes */
const $atencion = document.getElementById("atencion");
const $btn_buscar = document.getElementById("btn_buscar");
const $modal_opcionesHospitalizacion = document.getElementById("modal-opcionesHospitalizacion");
const $tablaHospitalizacion = document.getElementById("tablaHospitalizacion");

/* Validar Formulario de Busqueda de Atención Hosp */
const validar = () => {
    let atencion = $atencion.value;
    if(!atencion){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe Diligenciar el numero de atención a buscar.",
            icon: "warning"
        })
        .then((result) => {
            if(result.isConfirmed){
                $atencion.focus();
            }
        })
        return;
    } else {
        alert("Prueba Exitosa.")
    }
}

/* Ejecutar Validación */
$btn_buscar.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
})