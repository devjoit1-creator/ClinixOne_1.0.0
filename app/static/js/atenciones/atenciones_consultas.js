/* Constantes */
const $medico = document.getElementById("medico");
const $fecha_atencion = document.getElementById("fecha_atencion");
const $atencion = document.getElementById("atencion");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tablaAtenciones = document.getElementById("tablaAtenciones");
const $modal_historiasConsulta = document.getElementById("modal_historiasConsulta");
const $containerPanelHC = document.getElementById("containerPanelHC");

/* Cargar Fecha Actual */
document.addEventListener("DOMContentLoaded", () => {
    let fecha = new Date()
    let dia = fecha.getDate();
    let mes = fecha.getMonth() + 1;
    let anio = fecha.getFullYear();

    if (dia < 10) {
        dia = "0" + dia;
    }
    if (mes < 10) {
        mes = "0" + mes;
    }
    $fecha_atencion.value = anio + "-" + mes + "-" + dia;
    getAtencionesConsulta();
})

/* Obtener Atenciones asignadas de consulta por medico y fecha */
const getAtencionesConsulta = () => {
    let medico =  $medico.value;
    let fecha_atencion = $fecha_atencion.value;
    /* Limpiar Tabla */
    while ($tablaAtenciones.rows.length > 1) {
        $tablaAtenciones.deleteRow(1);
    }
    /* API Fetch */
    fetch("/getAtencionesConsulta", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ medico, fecha_atencion })
    })
    .then(response => response.json())
    .then(data => {
        /* Alerta si no existen registros para el medico en la fecha */
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia",
                text: "No se encontraron atenciones en la fecha seleccionada",
                icon: "warning"
            })
            return;
        }

        /* Traer los registros encontrados a la tabla */
        data.forEach(atencion => {
            $tablaAtenciones.insertRow().innerHTML = 
            `
            <td style="width: 10%; font-size: small;">${ atencion.id }</td>
            <td style="width: 10%; font-size: small;">${ atencion.fecha }</td>
            <td style="width: 10%; font-size: small;">${ atencion.hora }</td>
            <td style="width: 20%; font-size: small;">${ atencion.documento }</td>
            <td style="width: 40%; font-size: small;">${ atencion.paciente }</td>
            <td style="width: 10%; font-size: small;">
                <a onclick="activarModal(${atencion.id}, '${atencion.documento}', '${atencion.paciente}')" class="button is-small is-primary has-tooltip-bottom" data-tooltip="Menú de Atención" style="padding: 0em 1.0em">
                    <span class="icon is-small"><i><img src="./static/img/icons/menu.png" alt="icon"></i></span>
                </a>
            </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Obtener registros al cambiar fecha */
$fecha_atencion.addEventListener("change", (e) => {
    e.preventDefault();
    getAtencionesConsulta();
})

/* Activar Modal con Datos */
const activarModal = (atencion, codigo, paciente) => {
    $modal_historiasConsulta.classList.remove("is-hidden");
    $modal_historiasConsulta.classList.add("is-active");

    /* Obtener Valores de la tabla */
    $atencion.value = atencion;
    $codigo.value = codigo;
    $paciente.value = paciente;
}

/* $tablaAtenciones.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataAtencion(data);
    $containerPanelHC.style.display = "block";
}); */

/* const fillDataAtencion = (data) => {
    $atencion.value = data[0].innerText;
    $codigo.value = data[3].innerText;
    $paciente.value = data[4].innerText;
}; */