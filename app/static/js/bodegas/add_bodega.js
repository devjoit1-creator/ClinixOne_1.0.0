/* Constantes */
const $id_bodega = document.getElementById("id_bodega");
const $nom_bodega = document.getElementById("nom_bodega");
const $ubicacion = document.getElementById("ubicacion");
const $form_addbodega = document.getElementById("form_addbodega");
const $btn_cancelar  = document.getElementById("btn_cancelar");

/* UpperCase */
$nom_bodega.addEventListener("keyup", () => {
    $nom_bodega.value = $nom_bodega.value.toUpperCase();
});

$ubicacion.addEventListener("keyup", () => {
    $ubicacion.value = $ubicacion.value.toUpperCase();
})
/* Modo Cancelar */
$btn_cancelar.addEventListener("click", (e) => {
    e.preventDefault();
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
            window.location.href = "/bodegas"
        }
    });
});

/* Validar Formulario */
$form_addbodega.addEventListener("submit", (e) => {
    let id = $id_bodega.value;
    let nombre = $nom_bodega.value;
    let ubicacion = $ubicacion.value;

    if(!id || !nombre || !ubicacion){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar todos los campos del formulario.",
            icon: "warning"
        })
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