/* Evento para cargar logo desde el equipo */
const $logo_entidad = document.getElementById("logo_entidad");
$logo_entidad.addEventListener('change', (event) => {
    let file = event.target.files[0];
    if (file) {
       let reader = new FileReader();
       reader.onload = (e) => {
        const img = document.getElementById("imgPreview");
        img.src = e.target.result;
        img.style.display = "block"; 
       };
       reader.readAsDataURL(file); 
    } 
});