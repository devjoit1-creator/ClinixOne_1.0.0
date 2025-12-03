/* Declaración de Constantes Elementos */
const $fecha_inicio = document.getElementById("fecha_inicio");
const $fecha_fin = document.getElementById("fecha_fin");
const $emp_admin = document.getElementById("emp_admin");
const $consultar_rips = document.getElementById("consultar_rips");
const $generar_rips = document.getElementById("generar_rips");
const $tablaRips = document.getElementById("tablaRips");

/* Validación de Campos requeridos */
const validar = () => {
    let fechaInicio = $fecha_inicio.value;
    let fechaFin = $fecha_fin.value;
    let eapb = $emp_admin.value;
    if (!fechaInicio || !fechaFin || !eapb) {
        Swal.fire({
            title: "Advertencia!",
            text: "Debe Diligenciar las Fechas de Inicio y Fin. Tambien debe seleccionar una EAPB.",
            icon: "warning",
        })
    }else {
        get_rips();
    }
}

/* Consumo Api para obtener las facturas emitidas por rango de fecha y eapb */
const get_rips = () => {
    let fechaInicio = $fecha_inicio.value;
    let fechaFin = $fecha_fin.value;
    let eapb = $emp_admin.value;
    /* Limpiar la tabla */
    while ($tablaRips.rows.length > 1) {
        $tablaRips.deleteRow(1);
    }
    fetch("/get_facturas_rips", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            'fecha_inicio': fechaInicio,
            'fecha_fin': fechaFin,
            'administradora': eapb
        })
    })
    .then(response => response.json())
    .then(data => {
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se han emitido facturas en ese rango de fecha.",
                icon: "warning"
            });
            return;
        }

        data.forEach(factura => {
            /* Insertar los Datos del JSON consulta */
            $tablaRips.insertRow().innerHTML = `
            <td><input type="checkbox" class="fila-checkbox" data-index="${factura.factura}" checked></td>
            <td style="font-size: small;">${factura.fecha}</td>
            <td style="font-size: small;">${factura.factura}</td>
            <td style="font-size: small;">${factura.admin}</td>
            <td>
                <a href="/get_json_rips/${factura.factura}" class="button is-small is-warning">
                    <span class="icon is-small"><i class="fa fa-dollar" aria-hidden="true"></i></span>
                </a>
            </td>
            `
        });
        
    })
    .catch(error => console.error("error: ", error))
}

$consultar_rips.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
})

/* Consumo Api para generar archivo fisico de RIPS Individual */
/* const send_rips = async () => {
    const checkboxes = document.querySelectorAll(".fila-checkbox:checked");
    if(checkboxes.length === 0){
        Swal.fire({
            title: "Acción Requerida",
            text: "Por favor, selecciona al menos una factura para generar su RIPS.",
            icon: "info"
        })
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
            const response = await fetch("/send_json_rips", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({ id })
            })

            if (!response.ok) {
                throw new Error(`RIPS de Factura ${id}: Código ${response.status}`);
            }

            // Obtener el nombre del archivo desde el header
            const contentDisposition = response.headers.get("Content-Disposition");
            const match = contentDisposition?.match(/filename="?(.+)"?/);
            const filename = match ? match[1] : `FE${id}.json`;

            // Convertir la respuesta en blob
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);

            // Crear un enlace y simular clic
            const a = document.createElement("a");
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            a.remove();
            URL.revokeObjectURL(url);
            
            successes.push(id);

        } catch (error) {
            failures.push(`RIPS de Factura ${id}: ${error.message}`);
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
} */

/* Consumo Api para generar archivo fisico de RIPS ZIP */
const send_rips = async () => {
    const checkboxes = document.querySelectorAll(".fila-checkbox:checked");
    if (checkboxes.length === 0) {
        Swal.fire({
            title: "Acción Requerida",
            text: "Por favor, selecciona al menos una factura para generar su RIPS.",
            icon: "info"
        });
        return;
    }

    const ids = Array.from(checkboxes).map(cb => cb.dataset.index);

    Swal.fire({
        title: "Procesando...",
        html: `<p>Generando RIPS de ${ids.length} factura(s). Por favor, espera.</p>`,
        allowOutsideClick: false,
        didOpen: () => Swal.showLoading()
    });

    try {
        const response = await fetch("/send_json_rips", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ ids })
        });

        if (!response.ok) {
            throw new Error(`Error al generar ZIP: Código ${response.status}`);
        }

        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "RIPS_Facturas.zip";
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(url);

        Swal.fire({
            title: "¡Proceso completado!",
            html: `<p><b>${ids.length} factura(s) exportadas en ZIP.</b></p>`,
            icon: "success"
        });

    } catch (error) {
        Swal.fire({
            title: "Error",
            text: error.message,
            icon: "error"
        });
    }
};


$generar_rips.addEventListener("click", (e) => {
    e.preventDefault();
    send_rips();
})