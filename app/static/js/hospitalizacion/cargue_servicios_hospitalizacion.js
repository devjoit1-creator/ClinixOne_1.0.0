/* Cargar datos de servicios medicos desde modal */
const $cod_serv = document.getElementById("cod_serv");
const $nom_serv = document.getElementById("nom_serv");
const $valor_serv = document.getElementById("valor_serv");
const $tablaBusquedaServiciosHosp = document.getElementById("tablaBusquedaServiciosHosp");

$tablaBusquedaServiciosHosp.addEventListener('click', (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataServiciosHosp(data);
    closeAllModals();
})

const fillDataServiciosHosp = (data) => {
    $cod_serv.value = data[0].innerText;
    $nom_serv.value = data[1].innerText;
    $valor_serv.value = data[2].innerText;
}

/* Calcular el subtotal del servicio */
const $cantidad = document.getElementById("cantidad");
const $subtotal = document.getElementById("subtotal");

$cantidad.addEventListener("change", () => {
    $subtotal.value = $valor_serv.value * $cantidad.value
});

function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}