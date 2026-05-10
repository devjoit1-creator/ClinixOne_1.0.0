/* Constantes */
const $cod_referencia = document.getElementById("cod_referencia");
const $nom_referencia = document.getElementById("nom_referencia");
const $principio_activo = document.getElementById("principio_activo");
const $nom_comercial_ref = document.getElementById("nom_comercial_ref");
const $unidad_medida = document.getElementById("unidad_medida");
const $concentracion = document.getElementById("concentracion");
const $forma_farm = document.getElementById("forma_farm");
const $laboratorio = document.getElementById("laboratorio");
const $presentacion = document.getElementById("presentacion");
const $btn_cancelar = document.getElementById("btn_cancelar");
const $form_addreferencia = document.getElementById("form_addreferencia");

/* Uppercase */
$nom_referencia.addEventListener("keyup", () => {
    $nom_referencia.value = $nom_referencia.value.toUpperCase();
});

$principio_activo.addEventListener("keyup", () => {
    $principio_activo.value = $principio_activo.value.toUpperCase();
});

$nom_comercial_ref.addEventListener("keyup", () => {
    $nom_comercial_ref.value = $nom_comercial_ref.value.toUpperCase();
});

$unidad_medida.addEventListener("keyup", () => {
    $unidad_medida.value = $unidad_medida.value.toUpperCase();
});

$concentracion.addEventListener("keyup", () => {
    $concentracion.value = $concentracion.value.toUpperCase();
});

$forma_farm.addEventListener("keyup", () => {
    $forma_farm.value = $forma_farm.value.toUpperCase();
});

$laboratorio.addEventListener("keyup", () => {
    $laboratorio.value = $laboratorio.value.toUpperCase();
});

$presentacion.addEventListener("keyup", () => {
    $presentacion.value = $presentacion.value.toUpperCase();
})

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