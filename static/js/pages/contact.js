// ? GETTING DOCUMENT ELEMENTS
const heroSection = document.querySelector('.hero');
const questionSection = document.querySelector('.question');

// & ADDING TRANSITION DELAYS TO QUESTION SECTIONS' ELEMENTS
document.addEventListener('DOMContentLoaded', () => {    
    const elements = questionSection.querySelectorAll('h1, label, .input, .btn');
    
    elements.forEach((element, index) => {
        element.style.transitionDelay = `${index * 100}ms`;
    });
});

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection, questionSection];

// ! INTERSECTION OBSERVER VALUES
const observerOptions = {
    root: null, // Use viewport as root
    rootMargin: '0px', // No margin around root
    threshold: 0.2 // 20% visibility threshold
};

// ! INITIALIZING INTERSECTION OBSERVER
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');

        } else {
            entry.target.classList.remove('visible');
        }
    });
}, observerOptions);

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});