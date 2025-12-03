/* Activar busqueda de medicos activando perfil */
const $perfil = document.getElementById('perfil');
const $select_medico = document.getElementById('select_medico');

$select_medico.addEventListener('click', (event) => {
    event.preventDefault();
});
$perfil.addEventListener('change', () => {
    if ($perfil.value === '2') {
        $select_medico.disabled = false;
    }
    else {
        $select_medico.disabled = true;
    }
});

/* Traer datos de medico a Formulario Usuario */
const $doc_usuario = document.getElementById('doc_usuario');
const $nombre_completo = document.getElementById('nombre_completo');
const $tablaDatosMedico = document.getElementById('tablaDatosMedico');

$tablaDatosMedico.addEventListener('click', (event) => {
    event.stopPropagation();
    let data = event.target.parentElement.children;
    fillDataMedico(data);
    closeAllModals();
});

const fillDataMedico = (data) => {
    $doc_usuario.value = data[0].innerText;
    $nombre_completo.value = data[1].innerText;
};

/* Uppercase */
$nombre_completo.addEventListener("keyup", () => {
    $nombre_completo.value = $nombre_completo.value.toUpperCase();
});

/* Validar Formulario */
const $form_addusuario = document.getElementById('form_addusuario');
$form_addusuario.addEventListener("submit", (e) => {
    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading()
        }
    });
})

/* Funciones para cerrar modal */
function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

function closeModal($el) {
    $el.classList.remove('is-active');
}