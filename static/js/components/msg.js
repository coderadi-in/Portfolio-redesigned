// ? GETTING DOC ELEMENTS
const alerts = document.querySelectorAll(".alert");

// * FUNCTION TO SHOW ALERTS
function showAlerts() {
    alerts.forEach((alert, index) => {
        alert.style.transitionDelay = `${index * 100}ms`;
        alert.classList.add("visible");
    });
}

// * FUNCTION TO HIDE ALERTS
function hideAlerts() {
    alerts.forEach((alert_) => {
        alert_.classList.remove('visible');
    })
}

document.addEventListener("DOMContentLoaded", () => {
    // & CALLING THE FUNCTION TO SHOW ALERTS
    showAlerts();

    // & CALLING THE FUNCTION TO HIDE ALERTS AFTER 5 SECONDS
    setTimeout(() => {
        hideAlerts();
    }, 5000);
})