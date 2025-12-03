/* Constantes */
const $cod_servicio = document.getElementById("cod_servicio");
const $nom_servicio = document.getElementById("nom_servicio");
const $grupo = document.getElementById("grupo");
const $nomGrupo = document.getElementById("nomGrupo");

/* Uppercase */
$cod_servicio.addEventListener("keyup", () => {
    $cod_servicio.value = $cod_servicio.value.toUpperCase();
});

$nom_servicio.addEventListener("keyup", () => {
    $nom_servicio.value = $nom_servicio.value.toUpperCase();
});

/* Traer los datos del modal grupos a los respectivos inputs */
const $tablaBusquedaGrupos = document.getElementById("tablaBusquedaGrupos");
$tablaBusquedaGrupos.addEventListener("click", (event) => {
    event.stopPropagation();
    let data = event.target.parentElement.children;
    fillDataGrupo(data);
    closeAllModals();
})

const fillDataGrupo = (data) => {
    $grupo.value = data[0].innerText;
    $nomGrupo.value = data[1].innerText;
}

/* Validar Formulario */
const $form_addservicios = document.getElementById("form_addservicios");
$form_addservicios.addEventListener('submit', (e) => {
    let grupo = $grupo.value;
    let nomgrupo = $nomGrupo.value;
    if(!grupo || !nomgrupo){
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

/* Funciones para cerrar modal */
function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

function closeModal($el) {
    $el.classList.remove('is-active');
}