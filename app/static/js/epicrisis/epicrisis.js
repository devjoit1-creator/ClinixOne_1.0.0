/* Constantes */
const $num_doc = document.getElementById("num_doc");
const $medico = document.getElementById("medico");
const $btn_buscar = document.getElementById("btn_buscar");
const $tablaEpicrisis = document.getElementById("tablaEpicrisis");
const $modal_vistaPreviaEpicrisis = document.getElementById("modal_vistaPreviaEpicrisis");
const $iframeEpicrisis = document.getElementById("iframeEpicrisis");
const $btn_cerrarModal = document.getElementById("btn_cerrarModal");

/* Validar Busqueda */
const validar = () => {
    let valor = $num_doc.value;
    if(!valor){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar el No. de documento del paciente para realizar la busqueda.",
            icon: "warning"
        })
        .then((result) => {
            if(result.isConfirmed){
                $num_doc.focus();
            }
        });

        return;
    } else{
        getRegistrosEpicrisis();
    }
};
$btn_buscar.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
})

/* Fetch para obtener los registros de epicrisis por paciente y medico */
const getRegistrosEpicrisis = () => {
    let paciente = $num_doc.value;
    let medico = $medico.value;
    /* Limpiar Tabla */
    while ($tablaEpicrisis.rows.length > 1) {
        $tablaEpicrisis.deleteRow(1);
    };
    /* API Fetch */
    fetch("/getRegistrosEpicrisis", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({paciente, medico})
    })
    .then(response => response.json())
    .then(data => {
        /* Alerta si no hay resultados */
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron registros asociados.",
                icon: "warning"
            });
            return;
        };

        /* Resultados */
        data.forEach(registro => {
            $tablaEpicrisis.insertRow().innerHTML = 
            `
            <td style="width: 10%; font-size: small;">${registro.ID}</td>
            <td style="width: 5%; font-size: small;">${registro.atencion}</td>
            <td style="width: 10%; font-size: small;">${registro.documento}</td>
            <td style="width: 35%; font-size: small;">${registro.paciente}</td>
            <td style="width: 10%; font-size: small;">${registro.fecha}</td>
            <td style="width: 10%; font-size: small;">${registro.hora}</td>
            <td style="width: 20%; font-size: small;">
                <a onclick="activarModal(${registro.ID}, '${registro.documento}', '${medico}')" class="button is-small is-primary has-tooltip-bottom" data-tooltip="Ver PDF">
                    <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/pdf.png" alt="icon"></i></span>
                </a>
            </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Activar Modal */
const activarModal = (id, idpac, idmed) => {
    $modal_vistaPreviaEpicrisis.classList.remove("is-hidden");
    $modal_vistaPreviaEpicrisis.classList.add("is-active");
    $iframeEpicrisis.src = `/hc_epicrisis/${id}/${idpac}/${idmed}`;
}

/* Desactivar Modal */
$btn_cerrarModal.addEventListener("click", (e) => {
    e.preventDefault();
    $modal_vistaPreviaEpicrisis.classList.remove("is-active");
    $iframeEpicrisis.src = "";
})