// ! INTERSECTION OBSERVER VALUES
const observerOptions = {
    root: null, // Use viewport as root
    rootMargin: '0px', // No margin around root
    threshold: 0.4 // 40% visibility threshold
};

// ! INITIALIZING INTERSECTION OBSERVER
export const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');

        } else {
            entry.target.classList.remove('visible');
        }
    });
}, observerOptions);