// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

// ? GETTING DOCUMENT ELEMENTS
const heroSection = document.querySelector('.hero');
const skillsSection = document.querySelector('.skills');

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection, skillsSection];

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});