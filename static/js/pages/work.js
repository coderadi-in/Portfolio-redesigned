// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

// ? GETTING DOCUMENT ELEMENTS
const heroSection = document.querySelector('.hero');
const offersSection = document.querySelector('.offers');

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection, offersSection];

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});