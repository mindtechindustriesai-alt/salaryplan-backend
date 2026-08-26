/**
 * SalaryPlan Main Application
 * MindTech Financial Intelligence Platform
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('⚛️ SalaryPlan initialized');
    console.log('📊 CHSH S=2.76 · SA 2026/05142');
    
    // Check if running in standalone mode (PWA)
    if (window.matchMedia('(display-mode: standalone)').matches) {
        console.log('📱 Running as standalone PWA');
        document.body.classList.add('pwa-mode');
    }
    
    // Initialize app
    initializeApp();
});

function initializeApp() {
    // Load financial data from localStorage
    loadFinancialData();
    
    // Set up event listeners
    setupEventListeners();
    
    // Check for updates
    checkForUpdates();
}

function loadFinancialData() {
    try {
        const data = localStorage.getItem('salaryplan_data');
        if (data) {
            const parsed = JSON.parse(data);
            console.log('💰 Financial data loaded:', parsed);
            updateUI(parsed);
        }
    } catch (error) {
