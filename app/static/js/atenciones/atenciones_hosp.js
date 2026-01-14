/* Constantes */
const $un_funcional = document.getElementById("un_funcional");
const $atencion = document.getElementById("atencion");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tablaAtencionesHosp = document.getElementById("tablaAtencionesHosp");
const $modal_historiasHosp = document.getElementById("modal_historiasHosp");
/* const $containerPanelHC = document.getElementById("containerPanelHC"); */

/* Obtener Atenciones de Hospitalizacion por Unidad Funcional */
const getAtencionesHosp = () => {
    let un_funcional = $un_funcional.value;
    /* Limpiar tabla */
    while ($tablaAtencionesHosp.rows.length > 1) {
        $tablaAtencionesHosp.deleteRow(1)
    }
    /* Fetch */
    fetch("/getAtencionesHosp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ un_funcional })
    })
    .then(response => response.json())
    .then(data => {
        /* Alerta si no se encuentran registros */
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia.",
                text: "No se encontraron registros activos en esta und. funcional.",
                icon: "warning"
            });
            return;
        }

        /* Traer datos obtenidos a la tabla de Atenciones de Hosp. */
        data.forEach(atencion => {
            $tablaAtencionesHosp.insertRow().innerHTML = `
                <td style="width: 5%; font-size: small;">${ atencion.id }</td>
                <td style="width: 10%; font-size: small;">${ atencion.fecha }</td>
                <td style="width: 10%; font-size: small;">${ atencion.codigo }</td>
                <td style="width: 30%; font-size: small;">${ atencion.paciente }</td>
                <td style="width: 10%; font-size: small;">${ atencion.habitacion }</td>
                <td style="width: 20%; font-size: small;">${ atencion.administradora }</td>
                <td style="width: 10%;">
                    <a onclick="activarModal(${ atencion.id }, '${ atencion.codigo }', '${ atencion.paciente }')" class="button is-small is-primary has-tooltip-bottom" data-tooltip="Menú de Atención" style="padding: 0em 1.0em">
                        <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/menu.png" alt="icon"></i></span>
                    </a>
                </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Evento para llamar y obtener los registros de atención */
$un_funcional.addEventListener("change", (e) => {
    e.preventDefault();
    getAtencionesHosp();
})

/* Activar Modal con Datos */
const activarModal = (atencion, codigo, paciente) => {
    $modal_historiasHosp.classList.remove("is-hidden");
    $modal_historiasHosp.classList.add("is-active");

    /* Obtener Valores de la tabla */
    $atencion.value = atencion;
    $codigo.value = codigo;
    $paciente.value = paciente;
}

/* Cargar datos de paciente y atención desde la tabla */
/* $tablaAtencionesHosp.addEventListener('click', (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataAtencionHosp(data);
    $containerPanelHC.style.display = "block";
})

const fillDataAtencionHosp = (data) => {
    $atencion.value = data[0].innerText;
    $codigo.value = data[2].innerText;
    $paciente.value = data[3].innerText;
} */