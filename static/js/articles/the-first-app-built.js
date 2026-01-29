// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

// ? GETTING DOC ELEMENTS
const heroSection = document.querySelector('.hero');
const stageSections = document.querySelectorAll('.stage');
const moreSection = document.querySelector('.more');

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection, ...stageSections, moreSection];

// & ADDING TRANSITION DELAYS TO ABOUT SECTIONS' ELEMENTS
document.addEventListener('DOMContentLoaded', () => {    
    stageSections.forEach(section => {
        const sectionContent = section.querySelector('.section');
        
        if (sectionContent) {
            const elements = sectionContent.querySelectorAll('h1, p, .t-normal, .img');
            
            elements.forEach((element, index) => {
                element.style.transitionDelay = `${index * 100}ms`;
            });
        }
    });
});

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});