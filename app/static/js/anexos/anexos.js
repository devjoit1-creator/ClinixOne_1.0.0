/* Constantes */
const $codigo = document.getElementById("codigo");
const $btn_buscar = document.getElementById("btn_buscar");
const $tablaAnexos = document.getElementById("tablaAnexos");

/* Validación de Campos requeridos */
const validar = () => {
    let codigo = $codigo.value;
    if (!codigo) {
        Swal.fire({
            title: "Advertencia!",
            text: "Debe Diligenciar el nro. de documento del paciente.",
            icon: "warning",
        })
    }else {
        getAnexos();
    }
}

/* API Fetch para Obtener los registros de anexos */
const getAnexos = () => {
    let codigo = $codigo.value;
    while($tablaAnexos.rows.length > 1){
        $tablaAnexos.deleteRow(1)
    }
    fetch("/getAnexos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ codigo })
    })
    .then(response => response.json())
    .then(data => {
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron registros.",
                icon: "warning"
            });
            return;
        }

        data.forEach(anexo => {
            $tablaAnexos.insertRow().innerHTML = `
                <td style="font-size: small; width: 5%;">${anexo.ID}</td>
                <td style="font-size: small; width: 10%;">${anexo.codigo}</td>
                <td style="font-size: small; width: 20%;">${anexo.nombre}</td>
                <td style="font-size: small; width: 10%;">${anexo.fecha}</td>
                <td style="font-size: small; width: 20%;">${anexo.tipo}</td>
                <td style="font-size: small; width: 5%;">
                    <a onclick="verDocumento('${anexo.base64}')" class="button is-small is-primary has-tooltip-bottom" data-tooltip="Ver Documento" style="padding: 0em 1.0em">
                        <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/vista.png" alt="icon"></i></span>
                    </a>
                </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
}

$btn_buscar.addEventListener("click", (e) => {
    e.preventDefault();
    validar();
})

/* Ver documento Guardado BLOB */
const verDocumento = (documento) => {
    //const dataUrl = `data:application/pdf;base64,${documento}`;

    // 1. Decodificar la cadena Base64
    const byteCharacters = atob(documento);
    
    // 2. Crear un array de bytes
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    
    // 3. Convertir a Uint8Array
    const byteArray = new Uint8Array(byteNumbers);
    
    // 4. Crear el objeto Blob (Binary Large Object)
    const blob = new Blob([byteArray], { type: 'application/pdf' });
    
    // 5. Crear una URL interna temporal que apunta a ese Blob
    const blobUrl = URL.createObjectURL(blob);
    window.open(blobUrl, 'mywin', 'left=500,top=60,position=fixed,width=600,height=600,toolbar=1,resizable=0, centerscreen=yes'); // Usa '_blank' como string para abrir en una nueva pestaña
    return false;
}