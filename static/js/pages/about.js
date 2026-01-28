// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

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

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});