/* Constantes */
const radioButtons = document.querySelectorAll("input[name='toogle']");
const $containerBusquedaEntradaNumero = document.getElementById("containerBusquedaEntradaNumero");
const $numeroEntrada = document.getElementById("numeroEntrada");
const $btn_buscarEntradaNumero = document.getElementById("btn_buscarEntradaNumero");

const $containerBusquedaEntradaFecha = document.getElementById("containerBusquedaEntradaFecha");
const $fechaInicio = document.getElementById("fechaInicio");
const $fechaFin = document.getElementById("fechaFin");
const $btn_buscarEntradaFecha = document.getElementById("btn_buscarEntradaFecha");

/* Seleccionar container de busqueda */
radioButtons.forEach(radio => {
    radio.addEventListener("change", () => {
        if(radio.id === "busquedaNumero"){
            $containerBusquedaEntradaNumero.classList.add('is-active');
            $containerBusquedaEntradaNumero.classList.remove('is-hidden');

            $containerBusquedaEntradaFecha.classList.add('is-hidden');
            $containerBusquedaEntradaFecha.classList.remove('is-active');
        } else if (radio.id === "busquedaFecha"){
            $containerBusquedaEntradaNumero.classList.add('is-hidden');
            $containerBusquedaEntradaNumero.classList.remove('is-active');

            $containerBusquedaEntradaFecha.classList.remove('is-hidden');
            $containerBusquedaEntradaFecha.classList.add('is-active');
        }
    })
});

/* Fetch entrada de farmacia x numero */
const $tablaEntradasFarmacia = document.getElementById("tablaEntradasFarmacia");
// Validar
const validarNumero = () => {
    let numero = $numeroEntrada.value;
    if(!numero){
        Swal.fire({
            title: "Advertencia",
            text: "Debe Diligenciar el numero para buscar la entrada de farmacia.",
            icon: "warning"
        })
        .then((result) => {
            if(result.isConfirmed){
                $numeroEntrada.focus();
            };
        });

        return;
    } else {
        getEntradaFarmaciaNumero();
    }
};
// Fetch
const getEntradaFarmaciaNumero = () => {
    let numero = $numeroEntrada.value;
    while($tablaEntradasFarmacia.rows.length > 1){
        $tablaEntradasFarmacia.deleteRow(1);
    };
    fetch("/getEntradaFarmaciaNumero", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ numero })
    })
    .then(response => response.json())
    .then(data => {
        //Verificar si hay resultados
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia",
                text: "No se encontraron registros asociados.",
                icon: "warning"
            });

            return;
        };

        data.forEach(entrada => {
            $tablaEntradasFarmacia.insertRow().innerHTML = `
                <td style="width: 5%;">${entrada.fuente}</td>
                <td style="width: 10%;">${entrada.numero}</td>
                <td style="width: 10%;">${entrada.fecha}</td>
                <td style="width: 10%;">${entrada.cod_tercero}</td>
                <td style="width: 15%;">${entrada.nom_tercero}</td>
                <td style="width: 10%;">
                
                </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
};

$btn_buscarEntradaNumero.addEventListener("click", (e) => {
    e.preventDefault();
    validarNumero();
});