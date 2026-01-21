/* Constantes */
const $tipo_doc = document.getElementById("tipo_doc");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $medico = document.getElementById("medico");
const $tablaBusquedaPacientesEpicrisis = document.getElementById("tablaBusquedaPacientesEpicrisis");
const $modal_resultadoAtenciones = document.getElementById("modal_resultadoAtenciones");
const $btn_consultar = document.getElementById("btn_consultar");
const $btn_cancelar = document.getElementById("btn_cancelar");

/* Obtener Datos de paciente desde el modal pacientes */
$tablaBusquedaPacientesEpicrisis.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    $tipo_doc.value = data[0].innerText;
    $codigo.value = data[1].innerText;
    $paciente.value = data[2].innerText;
    closeAllModals();
})

/* Validación */
const validar = () => {
    let codigo = $codigo.value;
    if(!codigo){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe seleccionar al paciente para consultar atenciones.",
            icon: "warning"
        });
    } else {
       getAtencionesConsultaEpicrisis();
    }
}

$btn_consultar.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
})

/* Fetch Atenciones de consulta por paciente y medico */
const getAtencionesConsultaEpicrisis = () => {
    let paciente = $codigo.value;
    let medico = $medico.value;
    fetch("/getAtencionesConsultaEpicrisis", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ paciente, medico })
    })
    .then(response => response.json())
    .then(data => {
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron registros asociados.",
                icon: "warning"
            });
            return;
        }
        
        data.forEach(atencion => {
            alert(`la atención es: ${atencion.atencion}, ingresó ${atencion.ingreso}, salió ${atencion.salida}, en el servicio ${atencion.servicio}`)
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Modo Cancelar */
$btn_cancelar.addEventListener("click", (e) => {
    e.preventDefault();
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Los cambios no se guardaran!",
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
            window.location.href = `/epicrisis`
        }
    })
})

/* Funciones para cerrar modal */
function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}