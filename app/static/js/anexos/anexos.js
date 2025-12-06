/* Constantes */
const $fecha = document.getElementById("fecha");
const $hora = document.getElementById("hora");
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tipo_documento = document.getElementById("tipo_documento");
const $descripcion = document.getElementById("descripcion");
const $documento = document.getElementById("documento");

/* Uppercase */
$descripcion.addEventListener("keyup", () => {
    $descripcion.value = $descripcion.value.toUpperCase();
})

/* Obtener Nombre de Archivo Cargado */
const fileAnexo = document.querySelector("#file-anexo input[type=file]");
    fileAnexo.onchange = () => {
    if (fileAnexo.files.length > 0) {
        const fileName = document.querySelector("#file-anexo .file-name");
        fileName.textContent = fileAnexo.files[0].name;
    }

    if(fileAnexo.files[0].size > 1048576){
        Swal.fire({
            title: "Advertencia.",
            text: "El archivo excede el tamaño permitido (1 MB).",
            icon: "warning"
        })
        const fileName = document.querySelector("#file-anexo .file-name");
        fileName.textContent = "No hay documento cargado";
        return;
    }
};