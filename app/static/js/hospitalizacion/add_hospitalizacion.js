/* Cargar Fecha y Hora Actual */
const $fecha_ingreso = document.getElementById("fecha_ingreso");
const $hora_ingreso = document.getElementById("hora_ingreso");

window.onload = () => {
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate()

    if(mes < 10){
        mes = "0" + mes
    }

    if(dia < 10){
        dia = "0" + dia
    }

    $fecha_ingreso.value = anio + "-" + mes + "-" + dia;
    let hora = fecha.getHours().toString().padStart(2, '0');
    let minutos = fecha.getMinutes().toString().padStart(2, '0');
    $hora_ingreso.value = `${hora}:${minutos}`
}

/* Cargar datos del paciente desde Modal */
const $tipo = document.getElementById("tipo");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tablaBusquedaPacientesHospitalizacion = document.getElementById("tablaBusquedaPacientesHospitalizacion");

$tablaBusquedaPacientesHospitalizacion.addEventListener('click', (e) => {
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
}

/* Traer Regimen del Paciente */
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

/* Cargar datos de administradora desde Modal */
const $cod_admin = document.getElementById("cod_admin");
const $nit_admin = document.getElementById("nit_admin");
const $nom_admin = document.getElementById("nom_admin");
const $tablaBusquedaAdminsHospitalizacion = document.getElementById("tablaBusquedaAdminsHospitalizacion");

$tablaBusquedaAdminsHospitalizacion.addEventListener('click', (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataAdmin(data);
    closeAllModals();
    get_cobertura_hosp();
    get_concepto_hosp();
})

const fillDataAdmin = (data) => {
    $cod_admin.value = data[0].innerText;
    $nit_admin.value = data[1].innerText;
    $nom_admin.value = data[2].innerText;
}

/* Cargar datos de Unidad Funcional y Habitación desde Modal */
const $und_funcional = document.getElementById("und_funcional");
const $habitacion = document.getElementById("habitacion");
const $ufuncional_modal = document.getElementById("ufuncional_modal");
const $tablaHabitacionesModal = document.getElementById("tablaHabitacionesModal");

$tablaHabitacionesModal.addEventListener('click', (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    $und_funcional.value = $ufuncional_modal.value;
    fillDataHabitacion(data);
    closeAllModals();
})

const fillDataHabitacion = (data) => {
    $habitacion.value = data[0].innerText;
}

const getHabitaciones = () => {
    let undFuncional = $ufuncional_modal.value;
    while($tablaHabitacionesModal.rows.length > 1){
        $tablaHabitacionesModal.deleteRow(1);
    }
    fetch("/get_habitaciones", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ undFuncional })
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(habitacion => {
            $tablaHabitacionesModal.insertRow().innerHTML = `
                <td style="width: 30%;">${ habitacion.codigo }</td>
                <td style="width: 70%;">${ habitacion.nombre }</td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
}

$ufuncional_modal.addEventListener("change", (e) => {
    e.preventDefault();
    getHabitaciones();
})

/* Cargar datos de Diagnosticos desde Modal */
const $cod_diag1 = document.getElementById("cod_diag1");
const $nom_diag1 = document.getElementById("nom_diag1");
const $cod_diag2 = document.getElementById("cod_diag2");
const $nom_diag2 = document.getElementById("nom_diag2");
const $cod_diag3 = document.getElementById("cod_diag3");
const $nom_diag3 = document.getElementById("nom_diag3");
const $cod_diag4 = document.getElementById("cod_diag4");
const $nom_diag4 = document.getElementById("nom_diag4");
/* Cargar Datos de Modal diagnosticos a sus campos */
const $tablaBusquedaDiagnosticosHospitalizacion = document.getElementById("tablaBusquedaDiagnosticosHospitalizacion");
$tablaBusquedaDiagnosticosHospitalizacion.addEventListener("click", (e) => {
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

/* Funciones para cerrar modal */
function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

function closeModal($el) {
    $el.classList.remove('is-active');
}

/* Función ajax fetch */
function get_cobertura_hosp(){
    let valor = $cod_admin.value;
    fetch("/get_cobertura_administradora", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"cod_admin": valor})
    })
    .then(response => response.json())
    .then(data => {
        let plan_beneficios = document.getElementById("plan_beneficios");
        plan_beneficios.innerHTML = `<option value="${data[0]}" selected>${data[1]}</option>`;
    }).catch(error => console.error("error: ", error))
};

function get_concepto_hosp() {
    let valor = $cod_admin.value;
    fetch("/get_concepto_administradora", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"cod_admin": valor})
    })
    .then(response => response.json())
    .then(data => {
        let concepto_recaudo = document.getElementById("concepto_recaudo");
        concepto_recaudo.innerHTML = `<option value="${data[0]}" selected>${data[1]}</option>`
    })
    .catch(error => console.error("error: ", error))
};

/* Validar Formulario */
const $form_addhospitalizacion = document.getElementById("form_addhospitalizacion");
$form_addhospitalizacion.addEventListener("submit", (e) => {
    /* Datos de Paciente */
    let tipoDoc = $tipo.value;
    let docPac = $codigo.value;
    let nomPac = $paciente.value;
    /* Datos de Administradora */
    let codAdmin = $cod_admin.value;
    let nitAdmin = $nit_admin.value;
    let nomAdmin = $nom_admin.value;
    /* Unidad Funcional y Habitación */
    let undFuncional = $und_funcional.value;
    let habitacion = $habitacion.value;
    /* Diagnostico Principal */
    let codDiagPrincipal = $cod_diag1.value;
    let nomDiagPrincipal = $nom_diag1.value;
    if(!tipoDoc || !docPac || !nomPac || !codAdmin || !nitAdmin || !nomAdmin || !undFuncional || !habitacion || !codDiagPrincipal || !nomDiagPrincipal){
        e.preventDefault();
        Swal.fire({
            title: 'Notificación',
            text: 'Debe diligenciar el formulario con los campos obligatorios.',
            icon: 'warning'
        });
        return;
    }

    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });
})