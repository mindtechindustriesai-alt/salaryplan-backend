"""
Knowledge Base Service for SalaryPlan
CHSH S=2.76 · SA 2026/05142
"""

class KnowledgeBase:
    def __init__(self):
        self.knowledge = {
            "nca": "The National Credit Act (NCA) protects consumers in South Africa...",
            "debt_counselling": "Debt counselling is a legal process...",
            "loan_shark": "Loan sharks are illegal lenders..."
        }
    
    def get_info(self, topic: str) -> str:
        return self.knowledge.get(topic, "Information not found")

def get_knowledge_base():
    return KnowledgeBase()

knowledge_base = get_knowledge_base()
