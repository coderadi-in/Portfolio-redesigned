// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

// ? GETTING DOCUMENT ELEMENTS
const heroSection = document.querySelector('.hero');

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection];

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});