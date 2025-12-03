/* Cargar Fecha y Hora actuales */
const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");

window.onload = () => {
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(dia < 10){
        dia = "0" + dia;
    }

    if(mes < 10){
        mes = "0" + mes;
    }

    $fecha.value = anio + '-' + mes + '-' + dia;

    let hora = fecha.getHours().toString().padStart(2, '0');
    let minutos = fecha.getMinutes().toString().padStart(2, '0');
    $hora.value = `${hora}:${minutos}`

    calcularTotalServicios();
}

/* Scripts Calculos Valor Bruto, Desc, Coopg, Subtotal, Iva, Valor Neto */
/* Calcular el Valor Bruto de la Factura */
const $tablaServiciosHospFact = document.getElementById("tablaServiciosHospFact");
const $valor_bruto = document.getElementById("valor_bruto");
const $percent_desc = document.getElementById("percent_desc");
const $descuento = document.getElementById("descuento");
const $copago = document.getElementById("copago");
const $subtotal_factura = document.getElementById("subtotal_factura");
const $percent_iva = document.getElementById("percent_iva");
const $iva = document.getElementById("iva");
const $valor_neto = document.getElementById("valor_neto");

const calcularTotalServicios = () => {
    let total = 0;
    for (let i = 1; i < $tablaServiciosHospFact.rows.length; i++){
        /* console.log($tablaServiciosConsulta.rows[i].cells[5].innerHTML); */
        let rowValue = $tablaServiciosHospFact.rows[i].cells[5].innerHTML;
        total = total + Number(rowValue);
    }
    $valor_bruto.value = total;
    $subtotal_factura.value = $valor_bruto.value;
    $valor_neto.value = $valor_bruto.value;
};

/* Calcular Descuento con Base en Porcentaje */
const calcularDescuentoPorcentaje = () => {
    let porcentaje = $percent_desc.value * 1 / 100;
    $descuento.value = $valor_bruto.value * porcentaje;
    $subtotal_factura.value = $valor_bruto.value - $descuento.value;
    $valor_neto.value = $subtotal_factura.value;
}

$percent_desc.addEventListener('change', (e) => {
    e.preventDefault();
    calcularDescuentoPorcentaje();
})

/* Calcular Subtotal con Descuentos */
const calcularDescuentos = () => {
    let valcopago = $copago.value
    $subtotal_factura.value = $subtotal_factura.value - valcopago
    $valor_neto.value = $subtotal_factura.value;
}

$copago.addEventListener('change', (e) => {
    e.preventDefault();
    calcularDescuentos();
})

/* Calcular Iva con Base en Porcentaje */
$percent_iva.addEventListener('change', (e) => {
    e.preventDefault();
    let porcentaje = $percent_iva.value * 1 / 100;
    $iva.value = $subtotal_factura.value * porcentaje;
    $valor_neto.value = Number($subtotal_factura.value) + Number($iva.value);
})

/* Retornar a 0 campos de Descuento y Copago */
const $limpiarDescuentos = document.getElementById("limpiarDescuentos");
$limpiarDescuentos.addEventListener('click', (e) => {
    e.preventDefault();
    $percent_desc.value = 0
    $descuento.value = 0
    $copago.value = 0

    calcularDescuentoPorcentaje();
    calcularDescuentos();
})