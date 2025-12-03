/* Fecha y Hora Actual */
const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");

window.onload = () => {
    let fecha = new Date();
    /* Fecha Actual */
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
    /* Hora Actual */
    let hora = fecha.getHours().toString().padStart(2, '0')
    let minutos = fecha.getMinutes().toString().padStart(2, '0')
    $hora.value = `${hora}:${minutos}`
}

/* Traer los datos de especialidad del modal */
const $cod_especialidad = document.getElementById("cod_especialidad");
const $nom_especialidad = document.getElementById("nom_especialidad");
const $tablaBusquedaEspecialidadesInter = document.getElementById("tablaBusquedaEspecialidadesInter");

$tablaBusquedaEspecialidadesInter.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataEspecialidad(data);
    closeAllModals();
})

const fillDataEspecialidad = (data) => {
    $cod_especialidad.value = data[0].innerText;
    $nom_especialidad.value = data[1].innerText;
}

/* Validar Formulario */
const $form_addinterconsulta = document.getElementById("form_addinterconsulta");
$form_addinterconsulta.addEventListener("submit", (e) => {
    /* Especialidad */
    let codEspecialidad = $cod_especialidad.value;
    let nomEspecialidad = $nom_especialidad.value;
    if (!codEspecialidad || !nomEspecialidad) {
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
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
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