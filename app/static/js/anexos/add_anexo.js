/* Constantes */
const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tipo_documento = document.getElementById("tipo_documento");
const $descripcion = document.getElementById("descripcion");
const $documento = document.getElementById("documento");
const $tablaBusquedaPacientesAnexos = document.getElementById("tablaBusquedaPacientesAnexos");
const $form_addDocumentos = document.getElementById("form_addDocumentos");
const $btn_cancelar = document.getElementById("btn_cancelar");

/* Obtener Fecha y Hora */
document.addEventListener("DOMContentLoaded", () => {
    /* Fecha Actual */
    let fecha = new Date();
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
})

/* Cargar Datos de Paciente desde el modal */
$tablaBusquedaPacientesAnexos.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    $codigo.value = data[1].innerText;
    $paciente.value = data[2].innerText;
    closeAllModals();
})


/* Uppercase */
$descripcion.addEventListener("keyup", () => {
    $descripcion.value = $descripcion.value.toUpperCase();
})

/* Obtener Nombre de Archivo Cargado */
const fileAnexo = document.querySelector("#file-anexo input[type=file]");
    fileAnexo.onchange = () => {
    if (fileAnexo.files.length > 0) {
        const fileName = document.querySelector("#file-anexo .file-name");
        fileName.textContent = fileAnexo.files[0].name;
    }

    /* Verificar tamaño del archivo en bytes */
    if(fileAnexo.files[0].size > 1048576){
        Swal.fire({
            title: "Advertencia.",
            text: "El archivo excede el tamaño permitido (1 MB).",
            icon: "warning"
        })
        const fileName = document.querySelector("#file-anexo .file-name");
        fileName.textContent = "No hay documento cargado";
        return;
    }
};

/* Validar Form */
$form_addDocumentos.addEventListener("submit", (e) => {
    let codigo = $codigo.value;
    let paciente = $paciente.value
    if(codigo === "" || paciente === ""){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar todos los campos obligatorios (*).",
            icon: "warning"
        })
        return;
    }

    /* Loading */
    Swal.fire({
        showConfirmButton: false,
        allowEscapeKey: false,
        allowOutsideClick: false,
        didOpen:  () => {
            Swal.showLoading();
        }
    });
})

/* Modo Cancelar */
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
            window.location.href = "/anexos"
        }
    })
})

/* Cerrar Modal */
function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
    closeModal($modal);
    });
}