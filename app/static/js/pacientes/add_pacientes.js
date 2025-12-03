/* Constantes Datos */
const $papellido = document.getElementById("papellido");
const $sapellido = document.getElementById("sapellido");
const $pnombre = document.getElementById("pnombre");
const $snombre = document.getElementById("snombre");
const $direccion = document.getElementById("direccion");
const $barrio = document.getElementById("barrio");
const $nacionalidad = document.getElementById("nacionalidad");

/* UpperCase */
$papellido.addEventListener("keyup", () => {
    $papellido.value = $papellido.value.toUpperCase();
});

$sapellido.addEventListener("keyup", () => {
    $sapellido.value = $sapellido.value.toUpperCase();
});

$pnombre.addEventListener("keyup", () => {
    $pnombre.value = $pnombre.value.toUpperCase();
});

$snombre.addEventListener("keyup", () => {
    $snombre.value = $snombre.value.toUpperCase();
});

$direccion.addEventListener("keyup", () => {
    $direccion.value = $direccion.value.toUpperCase();
});

$barrio.addEventListener("keyup", () => {
    $barrio.value = $barrio.value.toUpperCase();
});

$nacionalidad.addEventListener("keyup", () => {
    $nacionalidad.value = $nacionalidad.value.toUpperCase();
});

/* Calcular edad paciente */
const $fechaNac = document.getElementById("fechaNac");
const $edad = document.getElementById("edad");
const calcularEdad = (fecha) => {
    let hoy = new Date();
    let cumpleanos = new Date(fecha);
    let edad = hoy.getFullYear() - cumpleanos.getFullYear();
    let meses = hoy.getMonth() - cumpleanos.getMonth();

    if (meses < 0 || (meses === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edad--; // Ajuste si aún no ha cumplido años este año
    }

    return edad;
}
const edadCalculada = () => {
    $edad.value = calcularEdad($fechaNac.value)
}
$fechaNac.addEventListener('input', edadCalculada)

/* Fetch de Departamentos y Municipios */
const $depto = document.getElementById("depto");
const $munic = document.getElementById("munic");
const $nom_depto = document.getElementById("nom_depto");
const $nom_munic = document.getElementById("nom_munic");

const getDeptosPacientes = () => {
    $depto.innerHTML = `<option value=""></option>`;
    fetch("/get_deptos", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(depto => {
            $depto.innerHTML += `<option value="${depto.id_depto}">${depto.nom_depto}</option>`;
        })
    })
    .catch(error => console.error("error: ", error))
}

const getMunicPacientes = () => {
    let codDepto = $depto.value;
    $munic.innerHTML = `<option value=""></option>`
    fetch("/get_municipios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"codDepto": codDepto})
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(municipio => {
            $munic.innerHTML += `<option value="${municipio.id_municipio}">${municipio.nom_municipio}</option>`
        })
    })
    .catch(error => console.error("error: ", error))
}

window.onload = () => {
    getDeptosPacientes();
}

/* Obtener los indices de los selects de departamentos y municipios y pasarlos al input */
$depto.addEventListener("change", (e) => {
    e.preventDefault();
    getMunicPacientes();
    $nom_depto.value = $depto.options[$depto.selectedIndex].text;
});

$munic.addEventListener("change", (e) => {
    e.stopPropagation();
    $nom_munic.value = $munic.options[$munic.selectedIndex].text;
});

/* Copiar datos acompañante en responsable */
const $acompanante = document.getElementById("acompanante")
const $responsable = document.getElementById("responsable")
const copiarDatosAcompanante = () => {
    $responsable.value = $acompanante.value
}
$acompanante.addEventListener('input', copiarDatosAcompanante);

const $telAcompanante = document.getElementById("telAcompanante")
const $telResponsable = document.getElementById("telResponsable")
const copiarDatosTelAcompanante = () => {
    $telResponsable.value = $telAcompanante.value
}
$telAcompanante.addEventListener('input', copiarDatosTelAcompanante);

const $parentAcompanante = document.getElementById("parentAcompanante")
const $parentResponsable = document.getElementById("parentResponsable")
const copiarDatosParentAcompanante = () => {
    $parentResponsable.value = $parentAcompanante.value
}
$parentAcompanante.addEventListener('input', copiarDatosParentAcompanante)

/* UpperCase */
$parentAcompanante.addEventListener("keyup", () => {
    $parentAcompanante.value = $parentAcompanante.value.toUpperCase();
});

$acompanante.addEventListener("keyup", () => {
    $acompanante.value = $acompanante.value.toUpperCase();
});

/* Llenar campos "NO TIENE" */
const $sinAcompanante = document.getElementById("noTiene")
const actionNoTiene = () => {
    if ($acompanante.value === "" && $telAcompanante.value === "") {
        $acompanante.value = "No Tiene"
        $telAcompanante.value = "No Tiene"
        $parentAcompanante.value = "No Tiene"
        $responsable.value = $acompanante.value 
        $telResponsable.value = $telAcompanante.value
        $parentResponsable.value = $parentAcompanante.value
    }else if($acompanante.value === "No Tiene" && $telAcompanante.value === "No Tiene"){
        $acompanante.value = ""
        $telAcompanante.value = ""
        $parentAcompanante.value = ""
        $responsable.value = $acompanante.value
        $telResponsable.value = $telAcompanante.value
        $parentResponsable.value = $parentAcompanante.value
    }
}
$sinAcompanante.addEventListener('click', actionNoTiene)