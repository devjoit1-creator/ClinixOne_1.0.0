/* Constantes */
const $fecha_inicio = document.getElementById("fecha_inicio");
const $fecha_fin = document.getElementById("fecha_fin");
const $consultar_facturas = document.getElementById("consultar_facturas");
const $tablaEmisionFactElectronica = document.getElementById("tablaEmisionFactElectronica");
const $enviar_facturas = document.getElementById("enviar_facturas");

/* Validación de Campos Fecha */
const validar = () => {
    let fechaInicio = $fecha_inicio.value;
    let fechaFin = $fecha_fin.value;
    if(!fechaInicio){
        Swal.fire({
            title: "Notificación",
            text: "Debe diligenciar Rango de Fecha",
            icon: "warning"
        })
    }else if(!fechaFin){
        Swal.fire({
            title: "Notificación",
            text: "Debe diligenciar Rango de Fecha",
            icon: "warning"
        })
    }else{
        /* Llamado de función para obtener las facturas */
         get_facturas();
    }
}

/* Función para obtener las facturas para emitir */
const get_facturas = () => {
    let fechaInicio = $fecha_inicio.value;
    let fechaFin = $fecha_fin.value;
    /* Limpiar la tabla */
    while ($tablaEmisionFactElectronica.rows.length > 1) {
        $tablaEmisionFactElectronica.deleteRow(1);
    }
    fetch("/get_facturas", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "fecha_inicio": fechaInicio,
            "fecha_fin": fechaFin
        })
    })
    .then(response => response.json())
    .then(data => {
        if (!Array.isArray(data) || data.length === 0) {
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron facturas en el rango de fechas seleccionado.",
                icon: "warning"
            });
            return;
        }

        data.forEach(factura => {
            $tablaEmisionFactElectronica.insertRow().innerHTML = `
            <td><input type="checkbox" class="fila-checkbox" data-index="${factura.numero}" checked></td>
            <td style="font-size: small;">${factura.fuente}</<td>
            <td style="font-size: small;">${factura.numero}</<td>
            <td style="font-size: small;">${factura.codigo}</<td>
            <td style="font-size: small;">${factura.nombre}</<td>
            <td style="font-size: small;">${factura.fecha}</<td>
            <td style="font-size: small;">${factura.valor}</<td>
        `
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Evento para validación */
$consultar_facturas.addEventListener('click', (e) => {
    e.preventDefault();
    validar();
})

/* Función para enviar las facturas al endpoint de PT. */
const send_facturas = async () => {
    const checkboxes = document.querySelectorAll(".fila-checkbox:checked");
    if (checkboxes.length === 0) {
        Swal.fire({
            title: "Acción requerida",
            text: "Por favor, selecciona al menos una factura para enviar.",
            icon: "info"
        });
        return;
    }

    Swal.fire({
        title: "Procesando...",
        html: `<p>Enviando ${checkboxes.length} factura(s). Por favor, espera.</p>`,
        allowOutsideClick: false,
        didOpen: () => Swal.showLoading()
    });

    const successes = [];
    const failures = [];

    for (let i = 0; i < checkboxes.length; i++) {
        const checkbox = checkboxes[i];
        const id = checkbox.dataset.index;

        try {
            const response = await fetch("/send_facturas", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({ id })
            });

            if (!response.ok) {
                throw new Error(`Factura ${id}: Código ${response.status}`);
            }

            const data = await response.json();
            successes.push(id); // Puedes registrar también data si lo necesitas

        } catch (error) {
            failures.push(`Factura ${id}: ${error.message}`);
        }
    }

    let finalTitle = "";
    let finalIcon = "";
    let finalText = `<p><b>${successes.length} factura(s) enviada(s) con éxito.</b></p>`;

    if (failures.length > 0) {
        finalTitle = "Proceso completado con errores";
        finalIcon = "warning";
        finalText += `<p><b>${failures.length} factura(s) fallaron:</b></p><ul>${failures.map(f => `<li>${f}</li>`).join('')}</ul>`;
    } else {
        finalTitle = "¡Proceso completado!";
        finalIcon = "success";
    }

    Swal.fire({
        title: finalTitle,
        html: finalText,
        icon: finalIcon
    });
}

/* Evento para envio de facturas */
$enviar_facturas.addEventListener('click', (e) => {
    e.preventDefault();
    send_facturas();
})