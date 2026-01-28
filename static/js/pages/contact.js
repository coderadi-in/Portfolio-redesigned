// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

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

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});