// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

// ? GETTING DOC ELEMENTS
const heroSection = document.querySelector('.hero');
const overviewSection = document.querySelector('.overview');
const lookSection = document.querySelector('.look');

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection, overviewSection, lookSection];

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});