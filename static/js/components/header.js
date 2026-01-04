// ? GETTING DOC ELEMENTS
const openNav = document.querySelector('.menu.open');
const closeNav = document.querySelector('.menu.close');
const nav = document.querySelector('.nav');
const navLinks = document.querySelectorAll('.nav li');

// | ADDING TRANSITION DELAY TO NAV LINKS
navLinks.forEach((link, index) => {
    link.style.transitionDelay = `${index * 0.1 + 0.3}s`;
});

// & EVENT LISTENER TO OPEN NAV
openNav.addEventListener('click', () => {
    nav.style.display = "flex";

    setTimeout(() => {
        nav.classList.add('show');
    }, 100);
});

// & EVENT LISTENER TO CLOSE NAV
closeNav.addEventListener('click', () => {
    nav.classList.remove('show');

    setTimeout(() => {
        nav.style.display = "none";
    }, 500);
});

// & EVENT LISTENERS TO CLOSE NAV WHEN BODY IS CLICKED
document.body.addEventListener('click', (e) => {
    if (nav.classList.contains('show') && !e.target.closest('.nav') && !e.target.closest('.menu.open')) {
        nav.classList.remove('show');

        setTimeout(() => {
            nav.style.display = "none";
        }, 500);
    }
});