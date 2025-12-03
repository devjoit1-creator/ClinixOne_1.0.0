/* Constantes */
const $profile = document.getElementById("profile");
const $menu1 = document.getElementById("toogle-list-1");
const $menu2 = document.getElementById("toogle-list-2");
const $menu3 = document.getElementById("toogle-list-3");
const $menu4 = document.getElementById("toogle-list-4");

const activarPerfil = () => {
    let perfil = $profile.value;
    if(perfil === "1"){
        $menu1.classList.remove('is-hidden');
        $menu2.classList.remove('is-hidden');
        $menu3.classList.remove('is-hidden');
        $menu4.classList.remove('is-hidden');
    }else if (perfil === "2"){
        $menu3.classList.remove('is-hidden');
    }else if (perfil === "3"){
        $menu2.classList.remove('is-hidden');
    }
}

document.addEventListener("DOMContentLoaded", () => {
     activarPerfil();
});