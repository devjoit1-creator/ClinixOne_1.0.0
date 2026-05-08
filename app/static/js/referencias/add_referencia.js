/* Constantes */
const $btn_cancelar = document.getElementById("btn_cancelar");

/* Modo Cancelar */
$btn_cancelar.addEventListener("click", (e) => {
    e.preventDefault()
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
            window.location.href = "/referencias"
        }
    });
});