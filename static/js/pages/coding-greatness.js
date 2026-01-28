// ? IMPORTING OBSERVER
import { observer } from '../base/observer.js';

// ? GETTING DOC ELEMENTS
const heroSection = document.querySelector('.hero');
const articlesSection = document.querySelector('.articles');

// & PREPARING OBSERVABLE SECTIONS ARRAY
const observables = [heroSection, articlesSection];

// & OBSERVING DOC SECTION ELEMENTS
observables.forEach(element => {
    observer.observe(element);
});