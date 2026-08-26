class QuantumService:
    def __init__(self):
        self.chsh = 2.76
        self.patent = "SA 2026/05142"
    
    def get_chsh(self):
        return {"chsh": self.chsh, "patent": self.patent}

def get_quantum_service():
    return QuantumService()

quantum_service = get_quantum_service()
