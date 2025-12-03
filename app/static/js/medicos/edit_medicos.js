/* Constantes */
const $nombre_completo = document.getElementById("nombre_completo");
const $p_nombre = document.getElementById("p_nombre");
const $s_nombre = document.getElementById("s_nombre");
const $p_apellido = document.getElementById("p_apellido");
const $s_apellido = document.getElementById("s_apellido");
const $dir_medico = document.getElementById("dir_medico");
const $consultorio = document.getElementById("consultorio");

/* Uppercase */
$p_nombre.addEventListener("keyup", () => {
    $p_nombre.value = $p_nombre.value.toUpperCase();
});

$s_nombre.addEventListener("keyup", () => {
    $s_nombre.value = $s_nombre.value.toUpperCase();
});

$p_apellido.addEventListener("keyup", () => {
    $p_apellido.value = $p_apellido.value.toUpperCase();
});

$s_apellido.addEventListener("keyup", () => {
    $s_apellido.value = $s_apellido.value.toUpperCase();
});

$nombre_completo.addEventListener("keyup", () => {
    $nombre_completo.value = $nombre_completo.value.toUpperCase();
});

$dir_medico.addEventListener("keyup", () => {
    $dir_medico.value = $dir_medico.value.toUpperCase();
});

$consultorio.addEventListener("keyup", () => {
    $consultorio.value = $consultorio.value.toUpperCase();
});

/* Evento para autorellenar campo "Nombre Completo" */
$p_nombre.addEventListener('input', () => {
    $nombre_completo.value = $p_nombre.value
});

$s_nombre.addEventListener('input', () => {
    $nombre_completo.value = $p_nombre.value +' '+ $s_nombre.value
});

$p_apellido.addEventListener('input', () => {
    $nombre_completo.value = $p_nombre.value +' '+ $s_nombre.value +' '+ $p_apellido.value
});

$s_apellido.addEventListener('input', () => {
    $nombre_completo.value = $p_nombre.value +' '+ $s_nombre.value +' '+ $p_apellido.value +' '+ $s_apellido.value
});

//Evento para subir cargo asistencial a formulario de nuevo medico
const $id_cargo_asis = document.getElementById("id_cargo_asis");
const $cargo_asis = document.getElementById("cargo_asis");

const $tablaCargosAsistenciales = document.getElementById("tablaCargosAsistenciales");
$tablaCargosAsistenciales.addEventListener('click', (event) =>{
    event.stopPropagation();
    let data = event.target.parentElement.children;
    fillDataCargo(data);
    closeAllModals();
});

const fillDataCargo = (data) => {
    $id_cargo_asis.value = data[0].innerText;
    $cargo_asis.value = data[1].innerText;
};

/* Funciones para cerrar modal */
function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

function closeModal($el) {
    $el.classList.remove('is-active');
}

/* Evento para cargar firma desde el equipo */
const $firma_medico = document.getElementById("firma_medico");
$firma_medico.addEventListener('change', (event) => {
    let file = event.target.files[0];
    if (file) {
       let reader = new FileReader();
       reader.onload = (e) => {
        const img = document.getElementById("imgPreview");
        img.src = e.target.result;
        img.style.display = "block"; 
       };
       reader.readAsDataURL(file); 
    } 
});

/* Validar Formulario */
const $form_editmedicos = document.getElementById("form_editmedicos");
$form_editmedicos.addEventListener('submit', (e) => {
    let idCargoAsis = $id_cargo_asis.value;
    let nomCargoAsis = $cargo_asis.value;
    if(!idCargoAsis || !nomCargoAsis){
        e.preventDefault();
        Swal.fire({
            title: 'Notificación',
            text: 'Debe diligenciar el formulario con los campos obligatorios.',
            icon: 'warning'
        });
        return;
    }

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