const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");

// Calcular Fecha y Hora del Sistema
window.onload = function (){
    /* Fecha */
    let fecha = new Date();
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();

    if(mes < 10){
        mes = "0" + mes;
    }

    if(dia < 10){
        dia = "0" + dia;
    }
    $fecha.value = anio +"-"+ mes + "-" + dia;

    /* Hora */
    let hora = fecha.getHours().toString().padStart(2, '0')
    let minutos = fecha.getMinutes().toString().padStart(2, '0')
    $hora.value = `${hora}:${minutos}`
}