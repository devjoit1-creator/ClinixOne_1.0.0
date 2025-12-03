/* Constantes */
const $cod_habitacion = document.getElementById("cod_habitacion");
const $nom_habitacion = document.getElementById("nom_habitacion");
const $form_updatehabitacion = document.getElementById("form_updatehabitacion");

/* Uppercase */
$cod_habitacion.addEventListener("keyup", () => {
    $cod_habitacion.value = $cod_habitacion.value.toUpperCase();
});

$nom_habitacion.addEventListener("keyup", () => {
    $nom_habitacion.value = $nom_habitacion.value.toUpperCase();
});

/* Validar Formulario */
$form_updatehabitacion.addEventListener("submit", (e) => {
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