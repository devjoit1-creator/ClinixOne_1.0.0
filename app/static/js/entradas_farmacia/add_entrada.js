// Constantes
const $fecha_entrada = document.getElementById("fecha_entrada");
const $hora_entrada = document.getElementById("hora_entrada");
const $fecha_vencimiento = document.getElementById("fecha_vencimiento");
const $cod_tercero = document.getElementById("cod_tercero");
const $nom_tercero = document.getElementById("nom_tercero");
const $tablaBusquedaTercerosEntradaFarm = document.getElementById("tablaBusquedaTercerosEntradaFarm");
const $bodega = document.getElementById("bodega");
const $cod_referencia = document.getElementById("cod_referencia");
const $nom_referencia = document.getElementById("nom_referencia");
const $registro_invima = document.getElementById("registro_invima");
const $tablaBusquedaMedicamentosEntradaFarm = document.getElementById("tablaBusquedaMedicamentosEntradaFarm");
const $prefijo_remision = document.getElementById("prefijo_remision");
const $lote = document.getElementById("lote");
const $cantidad = document.getElementById("cantidad");
const $vlr_unitario = document.getElementById("vlr_unitario");
const $vlr_subtotal = document.getElementById("vlr_subtotal");
const $ref_vencimiento = document.getElementById("ref_vencimiento");
const $temperatura = document.getElementById("temperatura");
const $riesgo = document.getElementById("riesgo");
const $condicion = document.getElementById("condicion");
const $btn_agregar = document.getElementById("btn_agregar");
const $btn_remover = document.getElementById("btn_remover");
const $tablaEntradasFarm = document.getElementById("tablaEntradasFarm");
const $total = document.getElementById("total");
const $btn_cancelar = document.getElementById("btn_cancelar");
const $form_addEntradaFarm = document.getElementById("form_addEntradaFarm");


// Fecha Actual del Sistema
document.addEventListener("DOMContentLoaded", () => {
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(dia < 10){
        dia = "0" + dia;
    };

    if(mes < 10){
        mes= "0" + mes;
    };

    $fecha_entrada.value = anio + "-" + mes + "-" + dia;
    
    let fecha_venc = new Date();
    fecha_venc.setDate(fecha_venc.getDate() + 30);
    let anio_venc = fecha_venc.getFullYear();
    let mes_venc = fecha_venc.getMonth() + 1;
    let dia_venc = fecha_venc.getDate();

     if(dia_venc < 10){
        dia_venc = "0" + dia_venc;
    };

    if(mes_venc < 10){
        mes_venc= "0" + mes_venc;
    };

    $fecha_vencimiento.value = anio_venc + "-" + mes_venc + "-" + dia_venc;


    // Hora actual
    let hora = fecha.getHours().toString().padStart(2, "0");
    let minutos = fecha.getMinutes().toString().padStart(2, "0");
    $hora_entrada.value = `${hora}:${minutos}`;
});

// Uppercase
$prefijo_remision.addEventListener("keyup", () => {
    $prefijo_remision.value = $prefijo_remision.value.toUpperCase();
});

$lote.addEventListener("keyup", () => {
    $lote.value = $lote.value.toUpperCase();
});

// Modo Cancelar
$btn_cancelar.addEventListener("click", (e) => {
    e.preventDefault();
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Los cambios no se guardaran.",
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
            window.location.href = "/entradas_farmacia"
        }
    });
});

/* Seleccionar Datos de tabla terceros */
$tablaBusquedaTercerosEntradaFarm.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    $cod_tercero.value = data[0].innerText;
    $nom_tercero.value = data[1].innerText;
    closeAllModals();
});

/* Seleccionar Datos de tabla Medicamentos */
$tablaBusquedaMedicamentosEntradaFarm.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    $cod_referencia.value = data[0].innerText;
    $nom_referencia.value = data[1].innerText;
    $registro_invima.value = data[2].innerText;
    closeAllModals();
});

// Calcular subtotal por cantidad del medicamento a entrar
$cantidad.addEventListener("input", () => {
    $vlr_subtotal.value = Number($cantidad.value) * Number($vlr_unitario.value);
});

$vlr_unitario.addEventListener("input", () => {
    $vlr_subtotal.value = Number($cantidad.value) * Number($vlr_unitario.value);
});

// Agregar medicamentos a tabla orden entrada
$btn_agregar.addEventListener("click", (e) => {
    let bodega = $bodega.value;
    let cod_ref = $cod_referencia.value;
    let nom_ref = $nom_referencia.value;
    let invima = $registro_invima.value;
    let lote = $lote.value;
    let cant = $cantidad.value;
    let unitario = $vlr_unitario.value;
    let subtunit = $vlr_subtotal.value;
    let vence = $ref_vencimiento.value;
    let temp = $temperatura.value;
    let riesgo = $riesgo.value;
    let condicion = $condicion.value;
    if(cod_ref === "" && nom_ref === "" && invima === ""){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Debe seleccionar un medicamento",
            icon: "warning"
        });
        return;
    } else {
        // Insertar la fila
        $tablaEntradasFarm.insertRow(-1).innerHTML = `
            <td style="width: 2%; font-size: x-small;">${bodega}</td>
            <td style="width: 8%; font-size: x-small;">${cod_ref}</td>
            <td style="width: 20%; font-size: x-small;">${nom_ref}</td>
            <td style="width: 10%; font-size: x-small;">${invima}</td>
            <td style="width: 5%; font-size: x-small;">${lote}</td>
            <td style="width: 2%; font-size: x-small;">${cant}.</td>
            <td style="width: 5%; font-size: x-small;">${unitario}</td>
            <td style="width: 3%; font-size: x-small;">${subtunit}</td>
            <td style="width: 5%; font-size: x-small;">${vence}</td>
            <td style="width: 2%; font-size: x-small;">${temp}</td>
            <td style="width: 5%; font-size: x-small;">${riesgo}</td>
            <td style="width: 5%; font-size: x-small;">${condicion}</td>
        `;
        // Limpiar campos
        $bodega.value = "";
        $cod_referencia.value = "";
        $nom_referencia.value = "";
        $registro_invima.value = "";
        $lote.value = "";
        $cantidad.value = "";
        $vlr_unitario.value = "";
        $vlr_subtotal.value = "";
        $ref_vencimiento.value = "";
        $temperatura.value = "";
        $riesgo.value = "";
        $condicion.value = "";
        calcularTotal();
    };
});

$btn_remover.addEventListener("click", (e) => {
    let rowCount = $tablaEntradasFarm.rows.length;
    if(rowCount <= 1){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "No hay medicamentos cargados",
            icon: "warning"
        });
        return;
    } else {
        $tablaEntradasFarm.deleteRow(rowCount - 1)
        calcularTotal();
    };
});

// Calcular Subtotal y Total de la entrada
const calcularTotal = () => {
    let total = 0;
    for (let i = 1; i < $tablaEntradasFarm.rows.length; i++){
        /* console.log($tablaServiciosConsulta.rows[i].cells[5].innerHTML); */
        let rowValue = $tablaEntradasFarm.rows[i].cells[7].innerHTML;
        total = total + Number(rowValue);       
    }
    $total.value = total;
};

// Validar Formulario
$form_addEntradaFarm.addEventListener("submit", (e) => {
    let rowCount = $tablaEntradasFarm.rows.length;
    if(rowCount <= 1){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar los campos obligatorios y cargar al menos un medicamento.",
            icon: "warning"
        });
        return;
    };

    let data = '';
    for (let i = 1; i < $tablaEntradasFarm.rows.length; i++) {
        const celdas = $tablaEntradasFarm.rows[i].cells;
        if(celdas.length >= 12){
            data += celdas[0].textContent + '|' + celdas[1].textContent + '|' + celdas[2].textContent + '|' + celdas[3].textContent + '|' + celdas[4].textContent + '|' + celdas[5].textContent + '|' + celdas[6].textContent + '|' + celdas[7].textContent + '|' + celdas[8].textContent + '|' + celdas[9].textContent + '|' + celdas[10].textContent + '|' + celdas[11].textContent +';'; 
        };
    };
    document.getElementById('data').value = data;

    //Loading
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => { Swal.showLoading() }
    });
})

/*  Cerrar Modals */
function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}