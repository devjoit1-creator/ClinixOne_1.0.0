/* Constantes */
const $cod_administradora = document.getElementById("cod_administradora");
const $nom_administradora = document.getElementById("nom_administradora");
const $dir_administradora = document.getElementById("dir_administradora");
const $cod_rips_adm = document.getElementById("cod_rips_adm");
const $form_updateadministradora = document.getElementById("form_updateadministradora");

/* Uppercase */
$cod_administradora.addEventListener("keyup", () => {
    $cod_administradora.value = $cod_administradora.value.toUpperCase();
});

$nom_administradora.addEventListener("keyup", () => {
    $nom_administradora.value = $nom_administradora.value.toUpperCase();
});

$dir_administradora.addEventListener("keyup", () => {
    $dir_administradora.value = $dir_administradora.value.toUpperCase();
});

$cod_rips_adm.addEventListener("keyup", () => {
    $cod_rips_adm.value = $cod_rips_adm.value.toUpperCase();
});

/* Validar Formulario */
$form_updateadministradora.addEventListener("submit", (e) => {
    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading()
        }
    });
});