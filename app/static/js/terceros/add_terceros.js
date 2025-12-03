/* Constantes */
const $tipo_idf = document.getElementById("tipo_idf");
const $digito_verf = document.getElementById("digito_verf");
const $nom_tercero = document.getElementById("nom_tercero");
const $dir_tercero = document.getElementById("dir_tercero");
const $cod_depto_tercero = document.getElementById("cod_depto_tercero");
const $nom_depto_tercero = document.getElementById("nom_depto_tercero");
const $cod_munic_tercero = document.getElementById("cod_munic_tercero");
const $nom_munic_tercero = document.getElementById("nom_munic_tercero");
const $form_addtercero = document.getElementById("form_addtercero");

/* Activar Campo de Digito de verificación */
$tipo_idf.addEventListener("change", () => {
    if($tipo_idf.value === "NIT"){
        $digito_verf.style.display = "block";
        $digito_verf.required = "true";
    }else{
        $digito_verf.style.display = "none";
        $digito_verf.required = "false";
    }
})

/* Uppercase */
$nom_tercero.addEventListener("keyup", () => {
    $nom_tercero.value = $nom_tercero.value.toUpperCase();
});

$dir_tercero.addEventListener("keyup", () => {
    $dir_tercero.value = $dir_tercero.value.toUpperCase();
});

/* JSON Departamentos y Municipios en Terceros */
const getDeptosTerceros = () => {
    $cod_depto_tercero.innerHTML = `<option value=""></option>`;
    fetch("/get_deptos", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(depto => {
            $cod_depto_tercero.innerHTML += `<option value="${depto.id_depto}">${depto.nom_depto}</option>`
        });
    })
    .catch(error => console.error("error: ", error))
}

const getMunicTerceros = () => {
    let codDepto = $cod_depto_tercero.value;
    $cod_munic_tercero.innerHTML = `<option value=""></option>`;
    fetch("/get_municipios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "codDepto": codDepto
        })
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(municipio => {
            $cod_munic_tercero.innerHTML += `<option value="${municipio.id_municipio}">${municipio.nom_municipio}</option>`
        })
    })
    .catch(error => console.error("error: ", error))
}

/* Obtener Nombre de Departamento y Municipio */
$cod_depto_tercero.addEventListener("change", (e) => {
    e.preventDefault();
    $nom_depto_tercero.value = $cod_depto_tercero.options[$cod_depto_tercero.selectedIndex].text;
    getMunicTerceros();
});

$cod_munic_tercero.addEventListener("change", (e) => {
    e.preventDefault();
    $nom_munic_tercero.value = $cod_munic_tercero.options[$cod_munic_tercero.selectedIndex].text;
});

/* Validar Formulario */
$form_addtercero.addEventListener("submit", (e) => {
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