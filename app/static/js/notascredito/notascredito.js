/* Constantes */
const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");
const $cod_fte_factura = document.getElementById("cod_fte_factura");
const $fe_uuid = document.getElementById("fe_uuid");

/* Obtener Fecha y Hora del Sistema */
window.onload = () => {
    /* Fecha */
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(mes < 10){
        mes = "0" + mes;
    }

    if(dia < 10){
        dia = "0" + dia;
    }

    $fecha.value = anio + "-" + mes + "-" + dia;

    /* Hora */
    let hora = fecha.getHours().toString().padStart(2, '0');
    let minutos = fecha.getMinutes().toString().padStart(2, '0');
    $hora.value = `${hora}:${minutos}`
}

/* Validar Busqueda de Numero de Factura */
const $nro_factura = document.getElementById("nro_factura");
const $buscar_factura = document.getElementById("buscar_factura");
const $tablaFacturasNotaCredito = document.getElementById("tablaFacturasNotaCredito");

const validar = () => {
    let nroFactura = $nro_factura.value;
    if(!nroFactura){
        $nro_factura.focus();
        Swal.fire({
            title: "Notificación",
            text: "Primero debe buscar la factura.",
            icon: "warning"
        })
    } else {
        get_factura();
    }
}

/* Consumo de API para obtener la factura para generar nota de credito */
const get_factura = () => {
    let nroFactura = $nro_factura.value;
    fetch("/get_factura_nc", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"nro_factura": nroFactura })
    })
    .then(response => response.json())
    .then(data => {
        $cod_fte_factura.value = `${data[0]}`;
        $fe_uuid.value = `${data[2]}`;
    })
    .catch(error => console.error("error: ", error))
}

$buscar_factura.addEventListener("click", () => {
    validar();
})

/* Validar Tabla antes de hacer submit */
const $formulario = document.getElementById("form_addnotacredito")
$formulario.addEventListener("submit", (e) => {
    let codFteFactura = $cod_fte_factura.value;
    let nroFactura = $nro_factura.value;
    let feUuid = $fe_uuid.value;
    if(!codFteFactura || !nroFactura || !feUuid){
        e.preventDefault();
        Swal.fire({
            title: 'Notificación',
            text: 'Debe diligenciar el formulario con los campos obligatorios.',
            icon: 'warning'
        });
        return;
    }

    if(feUuid === "null"){
        e.preventDefault();
        Swal.fire({
            title: 'Notificación',
            text: `La factura ${nroFactura} no ha sido emitida.`,
            icon: 'warning'
        })
        return;
    }

    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => Swal.showLoading()
    })
})