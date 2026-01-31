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

// & PRICE CALCULATION LOGIC
document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const priceDisplay = document.getElementById('price-value');
    const maintenanceDisplay = document.getElementById('maintenance-value');
    
    // State variables
    let oneTimeCost = 0;      // For building costs (pages, animation)
    let monthlyCost = 0;      // For recurring costs (server, database, etc.)
    let hasMaintenance = false; // Tracks if maintenance service is selected
    let integrationsCost = 0;   // Stores monthly integrations cost (server + db + notify)
    let maintenanceServiceCost = 0; // Stores maintenance service cost only
    
    // Initialize with default values
    updatePrice();
    
    // Add event listeners to all radio buttons
    const radioButtons = document.querySelectorAll('.selection .input');
    radioButtons.forEach(radio => {
        radio.addEventListener('change', handleSelectionChange);
    });
    
    // Set default selections
    setDefaultSelections();
    
    /**
     * Handle selection changes
     */
    function handleSelectionChange(event) {
        updatePrice();
    }
    
    /**
     * Set default selections
     */
    function setDefaultSelections() {
        // Set default radio selections
        const defaultSelections = {
            'config-pages': 'lite',
            'config-animation': 'zero',
            'config-server': 'lite',
            'config-db': 'zero',
            'config-notify': 'zero',
            'config-siteMaintenance': 'zero'
        };
        
        Object.entries(defaultSelections).forEach(([name, value]) => {
            const radio = document.querySelector(`input[name="${name}"][value="${value}"]`);
            if (radio) {
                radio.checked = true;
            }
        });
        
        // Calculate initial price
        updatePrice();
    }
    
    /**
     * Calculate total price and breakdown
     */
    function calculatePriceBreakdown() {
        // Reset all cost variables
        oneTimeCost = 0;
        monthlyCost = 0;
        integrationsCost = 0;
        maintenanceServiceCost = 0;
        hasMaintenance = false;
        
        // Get all selected radio buttons
        const selectedRadios = document.querySelectorAll('.selection .input:checked');
        
        selectedRadios.forEach(radio => {
            const selection = radio.closest('.selection');
            const price = parseFloat(selection.getAttribute('data-price'));
            const isRepeating = selection.getAttribute('data-repeating') === 'true';
            
            // Categorize the cost
            if (radio.name === 'config-pages' || radio.name === 'config-animation') {
                // Building costs (one-time)
                if (!isRepeating) {
                    oneTimeCost += price;
                }
            } 
            else if (radio.name === 'config-siteMaintenance') {
                // Maintenance service cost (monthly)
                if (radio.value !== 'zero') {
                    hasMaintenance = true;
                    maintenanceServiceCost = price;
                }
                if (isRepeating) {
                    monthlyCost += price;
                }
            }
            else {
                // Integration costs (monthly) - server, db, notify
                integrationsCost += price;
                if (isRepeating) {
                    monthlyCost += price;
                }
            }
        });
        
        // Calculate maintenance total (service + integrations) if maintenance is selected
        const maintenanceTotal = hasMaintenance ? maintenanceServiceCost + integrationsCost : 0;
        
        return {
            oneTime: oneTimeCost,
            monthly: monthlyCost,
            integrations: integrationsCost,
            maintenanceService: maintenanceServiceCost,
            maintenanceTotal: maintenanceTotal, // Service + integrations
            hasMaintenance: hasMaintenance,
            // First month total: one-time + all monthly costs
            total: oneTimeCost + monthlyCost - maintenanceServiceCost
        };
    }
    
    /**
     * Update price displays
     */
    function updatePrice() {
        const prices = calculatePriceBreakdown();
        
        // Format and display total price
        const formattedTotal = formatCurrency(prices.total);
        priceDisplay.textContent = `INR ${formattedTotal}`;
        
        // Format and display maintenance price (if selected)
        if (prices.hasMaintenance) {
            const formattedMaintenance = formatCurrency(prices.maintenanceTotal);
            maintenanceDisplay.textContent = `INR ${formattedMaintenance}/month`;
        } else {
            maintenanceDisplay.textContent = 'Not selected';
        }
        
        // Log detailed breakdown (useful for debugging)
        console.log('Price Breakdown:', {
            'One-time building cost': formatCurrency(prices.oneTime),
            'Monthly integrations (server + db + notify)': formatCurrency(prices.integrations),
            'Monthly maintenance service': formatCurrency(prices.maintenanceService),
            'Maintenance total (service + integrations)': formatCurrency(prices.maintenanceTotal),
            'Total monthly': formatCurrency(prices.monthly),
            'Total (first month)': formatCurrency(prices.total),
            'Has Maintenance': prices.hasMaintenance
        });
        
        // Store in global scope for other scripts to access
        window.priceCalculation = prices;
    }
    
    /**
     * Format currency with commas
     */
    function formatCurrency(amount) {
        return amount.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    }
    
    // Expose functions to global scope if needed
    window.calculatePriceBreakdown = calculatePriceBreakdown;
    window.updatePrice = updatePrice;
});