const $cod_cuenta = document.getElementById("cod_cuenta");
const $clasificacion = document.getElementById("clasificacion");

/* Clasificación de la cuenta */
$cod_cuenta.addEventListener('change', () => {
    if($cod_cuenta.value.length === 1){
        $clasificacion.value = "CL"
    }else if($cod_cuenta.value.length === 2){
        $clasificacion.value = "G"
    }else if($cod_cuenta.value.length === 3 || $cod_cuenta.value.length === 5){
        $clasificacion.value = ""
        if($clasificacion.value === ""){
            alert("No existen cuentas con 3 y/o 5 digitos")
            $cod_cuenta.value = ""
            $cod_cuenta.focus()
        }
    }else if($cod_cuenta.value.length === 4){
        $clasificacion.value = "C"
    }else if($cod_cuenta.value.length >= 6){
        $clasificacion.value = "SC"
    }
})

/* Validar Formulario */
const $form_addcuenta = document.getElementById("form_addcuenta");
$form_addcuenta.addEventListener("submit", (e) => {
    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });
});