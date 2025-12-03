/* Traer Los datos del paciente del modal */
const $tipo = document.getElementById("tipo");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tablaBusquedaPacientesConsultas = document.getElementById("tablaBusquedaPacientesConsultas");

$tablaBusquedaPacientesConsultas.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataPaciente(data);
    closeAllModals();
    getRegimenPaciente();
});

const fillDataPaciente = (data) => {
    $tipo.value = data[0].innerText;
    $codigo.value = data[1].innerText;
    $paciente.value = data[2].innerText;
};

/* Fetch regimen del paciente */
const $regimen_paciente = document.getElementById("regimen_paciente");
const getRegimenPaciente = () => {
    let numDoc = $codigo.value;
    $regimen_paciente.innerHTML = `<option value=""></option>`
    fetch("/get_regimen_paciente", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ numDoc })
    })
    .then(response => response.json())
    .then(data => {
        $regimen_paciente.innerHTML += `<option value="${data[0]}" selected>${data[1]}</option>`
    })
    .catch(error => console.error("error: ", error))
}

/* Cargar la hora del sistema junto con el template */
const $fecha_atencion = document.getElementById("fecha_atencion");
const $hora_atencion = document.getElementById("hora_atencion");
const $fecha_salida = document.getElementById("fecha_salida");
const $hora_salida = document.getElementById("hora_salida");
const $tiempo_consulta = document.getElementById("tiempo_consulta");

window.onload = () => {
    let fecha = new Date();
    /* Fecha Actual */
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(mes < 10){
        mes = "0" + mes;
    }

    if(dia < 10){
        dia = "0" + dia;
    }

    $fecha_atencion.value = anio + "-" + mes + "-" + dia;
    /* Hora Actual */
    let hora = fecha.getHours().toString().padStart(2, '0')
    let minutos = fecha.getMinutes().toString().padStart(2, '0')
    $hora_atencion.value = `${hora}:${minutos}`
}

/* Sumar Minutos para definir salida de la consulta */
const sumarMinutos12Horas = (horaInicial, minutosASumar) => {
  // Dividir la hora inicial en horas y minutos
  const partes = horaInicial.split(':');
  const fecha = new Date();
  fecha.setHours(parseInt(partes[0], 10));
  fecha.setMinutes(parseInt(partes[1], 10));
  fecha.setSeconds(0);

  // Sumar los minutos
  fecha.setMinutes(fecha.getMinutes() + minutosASumar);

  // Obtener horas y minutos
  let horas = fecha.getHours();
  const minutos = fecha.getMinutes().toString().padStart(2, '0');

  // Determinar AM o PM
  //const periodo = horas >= 12 ? 'PM' : 'AM';

  // Convertir a formato 12 horas
  //horas = horas % 12;
  //horas = horas === 0 ? 12 : horas; // Ajustar medianoche y mediodía
  //const horasFormateadas = horas.toString().padStart(2, '0');

  return `${horas}:${minutos}`; //${periodo}
}

$tiempo_consulta.addEventListener("change", (e) => {
    e.preventDefault();
    let horaInicial = $hora_atencion.value;
    let minutos = parseInt($tiempo_consulta.value, 10)
    let resultado = sumarMinutos12Horas(horaInicial, minutos);

    $fecha_salida.value = $fecha_atencion.value;
    $hora_salida.value = resultado;
})

/* Mostrar Valor de Unidad funcional en tab cargue de servicios */
const $und_funcional = document.getElementById("und_funcional");
const $undf_serv = document.getElementById("undf_serv");

$und_funcional.addEventListener("change", () => {
    $undf_serv.value = $und_funcional.value;
})

document.addEventListener("DOMContentLoaded", () => {
    calcularTotalServicios();
});

/* Traer los datos de la administradora del modal */
const $cod_admin = document.getElementById("cod_admin");
const $nit_admin = document.getElementById("nit_admin");
const $nom_admin = document.getElementById("nom_admin");
const $tablaBusquedaAdminsConsultas = document.getElementById("tablaBusquedaAdminsConsultas")

$tablaBusquedaAdminsConsultas.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataAdministradora(data);
    closeAllModals();
    get_cobertura_admin();
    get_concepto_admin();
});

const fillDataAdministradora = (data) => {
    $cod_admin.value = data[0].innerText;
    $nit_admin.value = data[1].innerText;
    $nom_admin.value = data[2].innerText;
};

/* AJAX para traer cobertura y concepto recaudo administradora */
const $plan_beneficios = document.getElementById("plan_beneficios");
const $concepto_recaudo = document.getElementById("concepto_recaudo");

const get_cobertura_admin = () => {
    let cod_admin = $cod_admin.value
    fetch("/get_cobertura_administradora", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"cod_admin": cod_admin})
    })
    .then(response => response.json())
    .then(data => {
        $plan_beneficios.innerHTML = `<option value="${data[0]}" selected>${data[1]}</option>`
    })
    .catch(error => console.error("error: ", error))
}

const get_concepto_admin = () => {
    let cod_admin = $cod_admin.value;
    fetch("/get_concepto_administradora", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"cod_admin": cod_admin})
    })
    .then(response => response.json())
    .then(data => {
        $concepto_recaudo.innerHTML = `<option value="${data[0]}" selected>${data[1]}</option>`
    })
    .catch(error => console.error("error: ", error))
}

/* Traer los datos de diagnosticos del modal */
const $cod_diag1 = document.getElementById("cod_diag1");
const $nom_diag1 = document.getElementById("nom_diag1");
const $cod_diag2 = document.getElementById("cod_diag2");
const $nom_diag2 = document.getElementById("nom_diag2");
const $cod_diag3 = document.getElementById("cod_diag3");
const $nom_diag3 = document.getElementById("nom_diag3");
const $cod_diag4 = document.getElementById("cod_diag4");
const $nom_diag4 = document.getElementById("nom_diag4");
/* Cargar Datos de Modal diagnosticos a sus campos */
const $tablaBusquedaDiagnosticosConsultas = document.getElementById("tablaBusquedaDiagnosticosConsultas");
$tablaBusquedaDiagnosticosConsultas.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    if($cod_diag1.value === '' && $nom_diag1.value === ''){
        $cod_diag1.value = data[0].innerText;
        $nom_diag1.value = data[1].innerText;
    }else if($cod_diag2.value === '' && $nom_diag2.value === ''){
        $cod_diag2.value = data[0].innerText;
        $nom_diag2.value = data[1].innerText; 
    }else if($cod_diag3.value === '' && $nom_diag3.value === ''){
        $cod_diag3.value = data[0].innerText;
        $nom_diag3.value = data[1].innerText;
    }else if($cod_diag4.value === '' && $nom_diag4.value === ''){
        $cod_diag4.value = data[0].innerText;
        $nom_diag4.value = data[1].innerText;
    }
    closeAllModals();
});

/* Limpiar todos los campos de diagnosticos */
const $btn_corregir = document.getElementById("btn_corregir");
function limpiarDiagnosticos() {
    $cod_diag1.value = "";
    $nom_diag1.value = "";
    $cod_diag2.value = "";
    $nom_diag2.value = "";
    $cod_diag3.value = "";
    $nom_diag3.value = "";
    $cod_diag4.value = "";
    $nom_diag4.value = "";
}; 

$btn_corregir.addEventListener("click", (e) => {
    e.preventDefault();
    limpiarDiagnosticos();
});

/* Traer datos de servicio asociado consulta del modal */
const $servicio_consulta = document.getElementById("servicio_consulta");
const $nom_servicio_consulta = document.getElementById("nom_servicio_consulta");
const $tablaBusquedaServicioAsoConsultas = document.getElementById("tablaBusquedaServicioAsoConsultas");

$tablaBusquedaServicioAsoConsultas.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataServicioAsoc(data);
    closeAllModals();
})

const fillDataServicioAsoc = (data) => {
    $servicio_consulta.value = data[0].innerText;
    $nom_servicio_consulta.value = data[1].innerText;
}

/* Traer los datos de servicios/proceds. del modal */
const $cod_serv = document.getElementById("cod_serv");
const $nom_serv = document.getElementById("nom_serv");
const $valor_serv = document.getElementById("valor_serv");
const $cantidad = document.getElementById("cantidad");
const $subtotal = document.getElementById("subtotal");
const $tablaBusquedaServiciosConsultas = document.getElementById("tablaBusquedaServiciosConsultas")

$tablaBusquedaServiciosConsultas.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataServicios(data);
    closeAllModals();
});

const fillDataServicios = (data) => {
    $cod_serv.value = data[0].innerText;
    $nom_serv.value = data[1].innerText;
    $valor_serv.value = data[2].innerText;
};

/* Calcular el subtotal del servicio */
$cantidad.addEventListener("change", () => {
    $subtotal.value = $valor_serv.value * $cantidad.value
});

/* Funciones para cerrar modal */
function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

function closeModal($el) {
    $el.classList.remove('is-active');
}