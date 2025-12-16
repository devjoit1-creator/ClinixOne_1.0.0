/* Constantes */
const $atencion = document.getElementById("atencion");
const $btn_buscar = document.getElementById("btn_buscar");
const $tablaConsultas = document.getElementById("tablaConsultas");

/* Validar Campo Atención */
const validar = () => {
    let atencion = $atencion.value;
    if(!atencion){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe Diligenciar el numero de atención a buscar.",
            icon: "warning"
        })
        .then(result => {
            if(result.isConfirmed){
                $atencion.focus()
            }
        })
        return;
    } else {
        getAtencionConsulta();
    }
}

/* Obtener Atenciones por Consulta */
const getAtencionConsulta = () => {
    let atencion = $atencion.value;
    while($tablaConsultas.rows.length > 1){
        $tablaConsultas.deleteRow(1)
    };
    fetch("/getAtencionConsulta", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({atencion})
    })
    .then(response => response.json())
    .then(data => {
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron registros.",
                icon: "warning"
            });
            return;
        }

        data.forEach(consulta => {
            $tablaConsultas.insertRow().innerHTML = `
                <td class="valor_atencion" style="width: 3%; font-size: small;">${consulta.id}</td>
                <td style="width: 9%; font-size: small;">${consulta.fecha }</td>
                <td style="width: 3%; font-size: small;">${consulta.hora }</td>
                <td style="width: 25%; font-size: small;">${consulta.paciente}</td>
                <td style="width: 25%; font-size: small;">${consulta.medico}</td>
                <td class="valor_aut" style="width: 10%; font-size: small;">${consulta.aut}</td>
                <td class="valor_factura" style="width: 10%; font-size: small;">${consulta.numero_fact}</td>
                <td style="width: 22%;">
                    <a onclick="anularConsulta(${consulta.id})" class="enlace_anular_consulta button is-small is-danger has-tooltip-bottom" data-tooltip="Anular" style="padding: 0em 1.0em;">
                        <span class="icon is-normal"><i aria-hidden="true"><img src="./static/img/icons/basura.png" alt="icon"></i></span>
                    </a>
                    <a href="/generar_factura_consulta/${consulta.id}" class="enlace_factura button is-small is-primary has-tooltip-bottom" data-tooltip="Generar Factura" style="padding: 0em 1.0em;">
                        <span class="icon is-normal"><i aria-hidden="true"><img src="./static/img/icons/factura.png" alt="icon"></i></span>
                    </a>
                </td>
            `
        });
        desactivarEnlaces();
    })
    .catch(error => console.error("error: ",error))
}

/* Ejecutar Validación */
$btn_buscar.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
})

/* Activar y Desactivar Botones */
const desactivarEnlaces = () => {
    let filas = document.querySelectorAll("#tablaConsultas tr");
    filas.forEach(fila => {
        const valor_aut = fila.cells[5].innerText.trim();
        const valor_fact = fila.cells[6].innerText.trim();
        if(valor_aut !== null){
            const enlace_anular_consulta = fila.querySelector(".enlace_anular_consulta");
            if(enlace_anular_consulta){
                enlace_anular_consulta.classList.add("enlace-desactivado");
                enlace_anular_consulta.removeAttribute("onclick");
            }
        }

        if(valor_fact !== "null"){
            const enlace_factura = fila.querySelector(".enlace_factura");
            if(enlace_factura){
                enlace_factura.classList.add("enlace-desactivado");
                enlace_factura.removeAttribute("href");
            }
        }
    });
}


/* Swal para anular/eliminar atención por consulta externa */
const anularConsulta = (atencion) => {
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Esta acción no se puede revertir!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Si, Eliminar!",
        confirmButtonColor: "#48c78e",
        cancelButtonText: "No, Cancelar",
        cancelButtonColor: "#f14668",
        showCancelButton: true,
        allowOutsideClick: false
    })
    .then((result) => {
        if(result.isConfirmed){
            window.location.href = `/drop_consulta/${atencion}`
        }
    })
};