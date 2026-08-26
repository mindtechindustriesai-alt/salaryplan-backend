/**
 * SalaryPlan Quantum Badge
 * CHSH S=2.76 · SA 2026/05142
 */

class QuantumBadge {
    constructor() {
        this.chshValue = 2.76;
        this.patentNumber = 'SA 2026/05142';
        this.lastUpdate = new Date();
        this.initialized = false;
    }
    
    init() {
        if (this.initialized) return;
        
        this.badgeElement = document.querySelector('.quantum-badge');
        if (!this.badgeElement) {
            // Create badge if not found in footer
            this.badgeElement = document.createElement('div');
            this.badgeElement.className = 'quantum-badge';
            const footer = document.querySelector('.quantum-footer');
            if (footer) {
                footer.prepend(this.badgeElement);
            }
        }
        
        this.updateBadge();
        this.startQuantumFluctuations();
        this.initialized = true;
        console.log(`⚛️ Quantum Badge initialized: CHSH S=${this.chshValue} · ${this.patentNumber}`);
    }
    
    updateBadge() {
        if (!this.badgeElement) return;
        
        const entanglement = this.getEntanglementLevel();
        this.badgeElement.innerHTML = `
            ⚛️ CHSH S=${this.chshValue.toFixed(2)} · 
            <span class="chsh">${this.patentNumber}</span>
            <span style="margin-left: 10px; font-size: 0.8rem; color: #8892b0;">
                🔗 ${entanglement}% entangled
            </span>
            <span style="margin-left: 10px; font-size: 0.7rem; color: #8892b0;">
                ${this.lastUpdate.toLocaleTimeString()}
            </span>
        `;
    }
    
    getEntanglementLevel() {
        const baseLevel = 91;
        const fluctuation = Math.sin(Date.now() / 3000) * 5;
        return Math.round(Math.min(100, Math.max(75, baseLevel + fluctuation)));
    }
    
    startQuantumFluctuations() {
        if (this.intervalId) clearInterval(this.intervalId);
        
        this.intervalId = setInterval(() => {
            const fluctuation = (Math.random() - 0.5) * 0.01;
            this.chshValue = Math.min(2.80, Math.max(2.70, this.chshValue + fluctuation));
            this.lastUpdate = new Date();
            this.updateBadge();
        }, 3000);
    }
    
    observe(amount = 0.1) {
        // Observer effect - slight change on user interaction
        this.chshValue = Math.min(2.80, Math.max(2.70, this.chshValue + amount * 0.01));
        this.updateBadge();
    }
}
