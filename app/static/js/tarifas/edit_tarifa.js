/* Constantes */
const $nom_tarifa = document.querySelector('#nom_tarifa');
const $form_updatetarifa = document.querySelector('#form_updatetarifa');

/* Uppercase */
$nom_tarifa.addEventListener("keyup", () => {
    $nom_tarifa.value = $nom_tarifa.value.toUpperCase();
});

/* Validar Formulario */
$form_updatetarifa.addEventListener("submit", (e) => {
    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
        }
    })
});