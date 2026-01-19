/* Constantes */
const $tipo_doc = document.getElementById("tipo_doc");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tablaBusquedaPacientesEpicrisis = document.getElementById("tablaBusquedaPacientesEpicrisis");
const $btn_cancelar = document.getElementById("btn_cancelar");

/* Obtener Datos de paciente desde el modal */
$tablaBusquedaPacientesEpicrisis.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    $tipo_doc.value = data[0].innerText;
    $codigo.value = data[1].innerText;
    $paciente.value = data[2].innerText;
    closeAllModals();
})

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