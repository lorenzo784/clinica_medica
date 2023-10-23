const hamMenu = document.querySelector('.ham-menu');
const navbarModalBackground = document.querySelector('.navbar-modal__background');
const navbarModalMenu = document.querySelector('.navbar-modal__menu');

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle("active");
    navbarModalBackground.classList.toggle("show");
    navbarModalMenu.classList.toggle("show-menu");
})

navbarModalBackground.addEventListener('click', () => {
    hamMenu.classList.toggle("active");
    navbarModalBackground.classList.remove('show');
    navbarModalMenu.classList.remove("show-menu");
});
