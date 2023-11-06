const hamMenu = document.querySelector('.ham-menu');
const navbarModalBackground = document.querySelector('.navbar-modal__background');

const navbarModalMenu = document.querySelector('.navbar-modal__menu');
const dropdownToggle = document.querySelector('#dropdown-toggle');
const dropdownMenu = document.querySelector('#dropdown-menu');

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle("active");
    navbarModalBackground.classList.toggle("show");
    navbarModalMenu.classList.toggle("show-menu");
    dropdownMenu.classList.remove('show-toggle');
})

navbarModalBackground.addEventListener('click', () => {
    hamMenu.classList.toggle("active");
    navbarModalBackground.classList.remove('show');
    navbarModalMenu.classList.remove("show-menu");
    dropdownMenu.classList.remove('show-toggle');
});




// ---------- Dropdown ----------


dropdownToggle.addEventListener('click', () => {
    dropdownMenu.classList.toggle('show-toggle');
});

const username = document.querySelector('.navbar__user-name');


document.addEventListener('click', function (event) {
    if (event.target !== dropdownMenu && !dropdownMenu.contains(event.target) &&
        event.target !== username && !username.contains(event.target)) {
        dropdownMenu.classList.remove('show-toggle');
    }
});