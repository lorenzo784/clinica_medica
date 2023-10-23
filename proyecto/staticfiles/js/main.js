const hamMenu = document.querySelector('.ham-menu');
const navbarModalBackground = document.querySelector('.navbar-modal__background');
const navbarModalMenu = document.querySelector('.navbar-modal__menu');

hamMenu.addEventListener('click', () =>{
    hamMenu.classList.toggle("active");
    navbarModalBackground.classList.toggle("show");
    navbarModalMenu.classList.toggle("show-menu");
})

document.addEventListener('click', function (event) {
    const isClickInsideMenu = hamMenu.contains(event.target) || navbarModalMenu.contains(event.target);
    if (!isClickInsideMenu) {
        navbarModalBackground.classList.remove('show');
        navbarModalMenu.classList.remove("show-menu");
    }
});     