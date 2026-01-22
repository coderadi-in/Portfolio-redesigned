// ? GETTING DOCUMENT ELEMENTS
const heroSection = document.querySelector('.hero');
const aboutSections = document.querySelectorAll('.about-content');

// & ADDING TRANSITION DELAYS TO ABOUT SECTIONS' ELEMENTS
document.addEventListener('DOMContentLoaded', () => {    
    aboutSections.forEach(section => {
        const sectionContent = section.querySelector('.section');
        
        if (sectionContent) {
            const elements = sectionContent.querySelectorAll('h1, p, .t-normal');
            
            elements.forEach((element, index) => {
                element.style.transitionDelay = `${index * 100}ms`;
            });
        }
    });
});

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection, ...aboutSections];

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