/* Constantes */
const $atencion = document.getElementById("atencion");
const $btn_buscar = document.getElementById("btn_buscar");
const $modal_opcionesHospitalizacion = document.getElementById("modal-opcionesHospitalizacion");
const $tablaHospitalizacion = document.getElementById("tablaHospitalizacion");

/* Validar Formulario de Busqueda de Atención Hosp */
const validar = () => {
    let atencion = $atencion.value;
    if(!atencion){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe Diligenciar el numero de atención a buscar.",
            icon: "warning"
        })
        .then((result) => {
            if(result.isConfirmed){
                $atencion.focus();
            }
        })
        return;
    } else {
        getAtencionHosp();
    }
}

/* Ejecutar Validación */
$btn_buscar.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
})

/* Obtener Atenciones por Hospitalización */
const getAtencionHosp = () => {
    let atencion = $atencion.value;
    while($tablaHospitalizacion.rows.length > 1){
        $tablaHospitalizacion.deleteRow(1);
    }
    fetch("/getAtencionHosp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ atencion })
    })
    .then(response => response.json())
    .then(data => {
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron registros.",
                icon: "warning"
            })
            return;
        }

        data.forEach(hospitalizacion => {
            $tablaHospitalizacion.insertRow().innerHTML = `
                <td style="width: 3%; font-size: small;" scope="col">${hospitalizacion.atencion}</td>
                <td style="width: 10%; font-size: small;" scope="col">${hospitalizacion.fecha_ingreso}</td>
                <td style="width: 8%; font-size: small;" scope="col">${hospitalizacion.hora_ingreso}</td>
                <td style="width: 10%; font-size: small;" scope="col">${hospitalizacion.codigo}</td>
                <td style="width: 30%; font-size: small;" scope="col">${hospitalizacion.paciente}</td>
                <td style="width: 10%; font-size: small;" scope="col">${hospitalizacion.fecha_salida}</td>
                <td style="width: 8%; font-size: small;" scope="col">${hospitalizacion.hora_salida}</td>
                <td style="width: 8%; font-size: small;" scope="col">${hospitalizacion.aut}</td>
                <td style="width: 5%; font-size: small;" scope="col">${hospitalizacion.numero_fact}</td>
                <td style="width: 15%;">
                    <a onclick="anularHospitalizacion(${hospitalizacion.atencion})" class="enlace_anular_hosp button is-small is-danger has-tooltip-bottom" data-tooltip="Anular Atención" style="padding: 0em 1.0em;">
                        <span class="icon is-normal"><i aria-hidden="true"><img src="./static/img/icons/basura.png" alt="icon"></i></span>
                    </a>
                    <a onclick="activarModal(${hospitalizacion.atencion}, '${hospitalizacion.codigo}', '${hospitalizacion.paciente}', '${hospitalizacion.fecha_salida}', '${hospitalizacion.aut}', '${hospitalizacion.numero_fact}')" class="enlace_opciones button is-small is-primary has-tooltip-bottom js-modal-trigger" data-tooltip="Opciones" data-target="modal-opcionesHospitalizacion" style="padding: 0em 1.0em;">
                        <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/menu.png" alt="icon"></i></span>
                    </a>
                </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Swal para anular/eliminar atención por consulta externa */
const anularHospitalizacion = (atencion) => {
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
            window.location.href = `/drop_hospitalizacion/${atencion}`
        }
    })
};

/* Activar Modal de Opciones */
const $atencion_modal = document.getElementById("atencion_modal");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $fecha_egreso = document.getElementById("fecha_egreso");
const $nro_autorizacion = document.getElementById("nro_autorizacion");
const $nro_factura = document.getElementById("nro_factura");
const activarModal = (atencion, codigo, paciente, fecha_egreso, nro_autorizacion, nro_factura) => {
    $modal_opcionesHospitalizacion.classList.remove("is-hidden");
    $modal_opcionesHospitalizacion.classList.add("is-active");

    $atencion_modal.value = atencion;
    $codigo.value = codigo;
    $paciente.value = paciente;
    $fecha_egreso.value = fecha_egreso;
    $nro_autorizacion.value = nro_autorizacion;
    $nro_factura.value = nro_factura;

    toogle_botones_egreso($fecha_egreso.value);
    toogle_botones_servicios($nro_autorizacion.value);
}

/* Verificar estado egreso */
const toogle_botones_egreso = (valor) => {
    let generar_salida_link = document.getElementById("generar_salida_link");
    let anular_salida_link = document.getElementById("anular_salida_link");
    if(valor !== "null"){
        generar_salida_link.classList.add("enlace-desactivado");
        anular_salida_link.classList.remove("enlace-desactivado");
    } else {
        generar_salida_link.classList.remove("enlace-desactivado");
        anular_salida_link.classList.add("enlace-desactivado");
    }
};

/* Verificar estado servicios y factura */
const toogle_botones_servicios = (valor) => {
    let cargar_servicios_link = document.getElementById("cargar_servicios_link");
    let generar_factura_link = document.getElementById("generar_factura_link");
    if(valor !== "null"){
        cargar_servicios_link.classList.add("enlace-desactivado");
        generar_factura_link.classList.remove("enlace-desactivado");
    } else {
        cargar_servicios_link.classList.remove("enlace-desactivado");
        generar_factura_link.classList.add("enlace-desactivado");
    }
}

//Función Egresar Paciente 
const generar_salida_link = document.getElementById("generar_salida_link");
const generar_salida = () => {
    window.location.href = `/add_egreso_hosp/${$atencion.value}`;
};
generar_salida_link.addEventListener("click", (event) => {
    event.preventDefault();
    generar_salida();
});

//Función Anular Egreso Paciente
const anular_salida_link = document.getElementById("anular_salida_link");
const confirmacion_anular_egreso = () => {
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Esta acción no se puede deshacer!",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Si, Eliminar!",
        confirmButtonColor: "#48c78e",
        cancelButtonText: "No, Cancelar",
        cancelButtonColor: "#f14668",
        showCancelButton: true,
        allowOutsideClick: false
    }).then((result) => {
        if(result.isConfirmed){
            window.location.href = `/anular_egreso_hosp/${$atencion.value}`
        }
    })
};
anular_salida_link.addEventListener("click", (event) => {
    event.preventDefault();
    confirmacion_anular_egreso();
});

//Función Cargue Servicios
const cargar_servicios_link = document.getElementById("cargar_servicios_link");
const cargar_servicios = () => {
    window.location.href = `/cargue_servicios_hosp/${$atencion.value}`;
};
cargar_servicios_link.addEventListener("click", (event) => {
    event.preventDefault();
    cargar_servicios();
});

//Función Facturar Hospitalización
const generar_factura_link = document.getElementById("generar_factura_link");
const generar_factura = () => {
    window.location.href = `/generar_factura_hosp/${$atencion.value}`;
};
generar_factura_link.addEventListener("click", (event) => {
    event.preventDefault();
    generar_factura();
});