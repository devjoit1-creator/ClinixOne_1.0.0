/* Constantes */
const $ambiente = document.getElementById("ambiente");
const $tenantid = document.getElementById("tenantid");
const $scope = document.getElementById("scope");
const $subskey = document.getElementById("subskey");
const $form_addparametrorda = document.getElementById("form_addparametrorda");

/* Validar Formulario */
$form_addparametrorda.addEventListener("submit", (e) => {
    let ambiente = $ambiente.value;
    let tenantid = $tenantid.value;
    let scope = $scope.value;
    let subskey = $subskey.value;
    if(!ambiente || !tenantid || !scope || !subskey){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar todos los campos obligatorios.",
            icon: "warning"
        });

        return;
    }

    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => { Swal.showLoading() }
    });
})