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
const $registro_invima = document.getElementById("registro_invima");
const $serie_referencia = document.getElementById("serie_referencia");
const $expediente_sanitario = document.getElementById("expediente_sanitario");
const $consecutivo_exp = document.getElementById("consecutivo_exp");
const $codigo_cum = document.getElementById("codigo_cum");
const $codigo_rips = document.getElementById("codigo_rips");
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
});

$registro_invima.addEventListener("keyup", () => {
    $registro_invima.value = $registro_invima.value.toUpperCase();
});

$serie_referencia.addEventListener("keyup", () => {
    $serie_referencia.value = $serie_referencia.value.toUpperCase();
});

/* Diligenciamento COD CUM Y COD RIPS */
$expediente_sanitario.addEventListener("input", () => {
    $codigo_cum.value = $expediente_sanitario.value;
    $codigo_rips.value = $expediente_sanitario.value;
});

$consecutivo_exp.addEventListener("input", () => {
    $codigo_cum.value = $expediente_sanitario.value + "-" + $consecutivo_exp.value;
    $codigo_rips.value = $expediente_sanitario.value + "-" + $consecutivo_exp.value;
});

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

/* Validar Formulario */
$form_addreferencia.addEventListener("submit", () => {
    
    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => { Swal.showLoading() }
    });
});