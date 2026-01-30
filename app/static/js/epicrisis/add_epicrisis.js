/* Constantes Formulario */
const $tipo_doc = document.getElementById("tipo_doc");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $medico = document.getElementById("medico");
const $atencion = document.getElementById("atencion");
const $fecha_ingreso = document.getElementById("fecha_ingreso");
const $hora_ingreso = document.getElementById("hora_ingreso");
const $servicio_ingreso = document.getElementById("servicio_ingreso");
const $fecha_salida = document.getElementById("fecha_salida");
const $hora_salida = document.getElementById("hora_salida");
const $servicio_salida = document.getElementById("servicio_salida");
const $btn_consultar = document.getElementById("btn_consultar");
const $btn_cancelar = document.getElementById("btn_cancelar");

/* Constantes Modal Pacientes */
const $tablaBusquedaPacientesEpicrisis = document.getElementById("tablaBusquedaPacientesEpicrisis");

/* Constantes Modal Atenciones */
const $modal_resultadoAtenciones = document.getElementById("modal_resultadoAtenciones");
const $tab_consultas = document.getElementById("tab_consultas");
const $tabAtencionesConsultas = document.getElementById("tabAtencionesConsultas");
const $tab_hosp = document.getElementById("tab_hosp");
const $tabAtencionesHosp = document.getElementById("tabAtencionesHosp");
const $tablaAtencionesConsultaEpicrisis = document.getElementById("tablaAtencionesConsultaEpicrisis");
const $tablaAtencionesHospEpicrisis = document.getElementById("tablaAtencionesHospEpicrisis");

/* Obtener Datos de paciente desde el modal pacientes */
$tablaBusquedaPacientesEpicrisis.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    $tipo_doc.value = data[0].innerText;
    $codigo.value = data[1].innerText;
    $paciente.value = data[2].innerText;
    closeAllModals();
});

/* Validación */
const validar = () => {
    let codigo = $codigo.value;
    if(!codigo){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe seleccionar al paciente para consultar atenciones.",
            icon: "warning"
        });
    } else {
        activarModalResultados();
        getAtencionesConsultaEpicrisis();
        getAtencionesHospEpicrisis();
    }
};

$btn_consultar.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
});

/* Fetch Atenciones de consulta por paciente y medico */
const getAtencionesConsultaEpicrisis = () => {
    let paciente = $codigo.value;
    let medico = $medico.value;
    /* Limpiar Tabla */
    while($tablaAtencionesConsultaEpicrisis.rows.length > 1){
        $tablaAtencionesConsultaEpicrisis.deleteRow(1);
    };
    /* API Fetch */
    fetch("/getAtencionesConsultaEpicrisis", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ paciente, medico })
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
        }
        /* Resultados en tabla */
        data.forEach(atencion => {
            $tablaAtencionesConsultaEpicrisis.insertRow().innerHTML = `
                <td style="width: 5%; font-size: x-small;">${atencion.atencion}</td>
                <td style="width: 20%; font-size: x-small;">${atencion.ingreso}</td>
                <td style="width: 10%; font-size: x-small;">${atencion.hora_ingreso}</td>
                <td style="width: 20%; font-size: x-small;">${atencion.salida}</td>
                <td style="width: 10%; font-size: x-small;">${atencion.hora_salida}</td>
                <td style="width: 20%; font-size: x-small;">${atencion.servicio}</td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
};

/* Fetch Atenciones de hospitalizacion por paciente y medico */
const getAtencionesHospEpicrisis = () => {
    let paciente = $codigo.value;
    let medico = $medico.value;
    /* Limpiar Tabla */
    while ($tablaAtencionesHospEpicrisis.rows.length > 1) {
        $tablaAtencionesHospEpicrisis.deleteRow(1);
    };
    /* API Fetch */
    fetch("/getAtencionesHospEpicrisis", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ paciente, medico })
    })
    .then(response => response.json())
    .then(data => {
        /* Alerta si no hay resultados */
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron resultados asociados.",
                icon: "warning"
            });
            return;
        }

        /* Resultados en tabla */
        data.forEach(atencion => {
            $tablaAtencionesHospEpicrisis.insertRow().innerHTML = `
                <td style="width: 5%; font-size: x-small;">${atencion.atencion}</td>
                <td style="width: 20%; font-size: x-small;">${atencion.ingreso}</td>
                <td style="width: 10%; font-size: x-small;">${atencion.hora_ingreso}</td>
                <td style="width: 20%; font-size: x-small;">${atencion.salida}</td>
                <td style="width: 10%; font-size: x-small;">${atencion.hora_salida}</td>
                <td style="width: 20%; font-size: x-small;">${atencion.servicio}</td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
};

/* Activar Modal de Resultados de Atenciones */
const activarModalResultados = () => {
    $modal_resultadoAtenciones.classList.remove("is-hidden");
    $modal_resultadoAtenciones.classList.add("is-active");
};

/* Obtener Datos de atención desde el modal consultas */
$tablaAtencionesConsultaEpicrisis.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    $atencion.value = data[0].innerText;
    $fecha_ingreso.value = data[1].innerText;
    $hora_ingreso.value = data[2].innerText;
    $servicio_ingreso.value = data[5].innerText;
    $fecha_salida.value = data[3].innerText;
    $hora_salida.value = data[4].innerText;
    $servicio_salida.value = $servicio_ingreso.value;
    closeAllModals();
});

/* Obtener Datos de atención desde el modal hospitalización */
$tablaAtencionesHospEpicrisis.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    $atencion.value = data[0].innerText;
    $fecha_ingreso.value = data[1].innerText;
    $hora_ingreso.value = data[2].innerText;
    $servicio_ingreso.value = data[5].innerText;
    $fecha_salida.value = data[3].innerText;
    $hora_salida.value = data[4].innerText;
    $servicio_salida.value = $servicio_ingreso.value;
    closeAllModals();
});

/* Activar/Desactivar Pestañas */
$tab_consultas.addEventListener("click", () => {
    ocultarCont();
    $tab_consultas.classList.add("is-active");
    $tabAtencionesConsultas.classList.remove("is-hidden");
    $tab_hosp.classList.remove("is-active")
});

$tab_hosp.addEventListener("click", () => {
    ocultarCont();
    $tab_hosp.classList.add("is-active");
    $tabAtencionesHosp.classList.remove("is-hidden");
    $tab_consultas.classList.remove("is-active");
});

function ocultarCont(){
    $tabAtencionesConsultas.classList.add("is-hidden");
    $tabAtencionesHosp.classList.add("is-hidden");
};

/* Modo Cancelar */
$btn_cancelar.addEventListener("click", (e) => {
    e.preventDefault();
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Los cambios no se guardaran!",
        icon: "question",
        confirmButtonText: "Si, Cancelar!",
        confirmButtonColor: "#48c78e",
        cancelButtonText: "No, Continuar",
        cancelButtonColor: "#f14668",
        showCancelButton: true,
        allowOutsideClick: false
    })
    .then((result) => {
        if(result.isConfirmed){
            window.location.href = `/epicrisis`
        }
    })
});

/* Funciones para cerrar modal */
function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}