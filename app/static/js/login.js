/* Constantes */
const $userId = document.getElementById("userId");
const $userPass = document.getElementById("userPass");
const $form_login = document.getElementById("form_login");

/* Validación de Formulario */
$form_login.addEventListener("submit", (e) => {
    let usuario = $userId.value;
    let contrasena = $userPass.value;
    if(!usuario || !contrasena){
        e.preventDefault();
        Swal.fire({
            title: "Notificación!",
            text: "Debe diligenciar su usuario y/o constraseña.",
            icon: "info"
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
    })
})