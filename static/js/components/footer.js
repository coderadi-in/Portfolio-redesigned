// ? GETTING DOC ELEMENTS
const main = document.querySelector("main");
const footer = document.querySelector("footer");

document.addEventListener('DOMContentLoaded', () => {
    // & GETTING FOOTER HEIGHT
    const footerHeight = footer.offsetHeight;

    // & ADDING MARGIN RELATIVE TO THE HEIGHT OF FOOTER
    main.style.marginBottom = `${footerHeight}px`;
})