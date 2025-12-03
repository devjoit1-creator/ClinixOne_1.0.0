/* Constantes */
const $cod_ufuncional = document.querySelector('#cod_ufuncional');
const $nom_ufuncional = document.querySelector('#nom_ufuncional');

/* UpperCase */
$cod_ufuncional.addEventListener("keyup", () => {
    $cod_ufuncional.value = $cod_ufuncional.value.toUpperCase();
});

$nom_ufuncional.addEventListener("keyup", () => {
    $nom_ufuncional.value = $nom_ufuncional.value.toUpperCase();
});

/* Validar Formulario */
const $form_addufuncional = document.querySelector('#form_addufuncional');
$form_addufuncional.addEventListener("submit", (e) => {
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