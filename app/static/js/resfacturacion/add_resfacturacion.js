const $prefijo = document.getElementById("prefijo");
const $fecha_inicio = document.getElementById("fecha_inicio");
const $fecha_fin = document.getElementById("fecha_fin");
const $numero_resolucion = document.getElementById("numero_resolucion");
const $numero_inicio = document.getElementById("numero_inicio");
const $numero_fin = document.getElementById("numero_fin");
const $texto_encabezado = document.getElementById("texto_encabezado");
const $encabezado = document.getElementById("encabezado");

$texto_encabezado.addEventListener('input', () => {
    /* $encabezado.innerText = $texto_encabezado.value */
    llenarEncabezado();
});

const llenarEncabezado = () => {
    $encabezado.value = `${$texto_encabezado.value} ${$numero_resolucion.value} con vigencia desde ${$fecha_inicio.value} hasta ${$fecha_fin.value}. Desde ${$prefijo.value}${$numero_inicio.value} hasta ${$prefijo.value}${$numero_fin.value}`
}