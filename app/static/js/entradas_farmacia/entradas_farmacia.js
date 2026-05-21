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