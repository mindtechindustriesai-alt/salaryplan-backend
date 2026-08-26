class KnowledgeBase:
    def __init__(self):
        self.knowledge = {"nca": "National Credit Act protects consumers"}
    
    def get_info(self, topic):
        return self.knowledge.get(topic, "Information not found")

def get_knowledge_base():
    return KnowledgeBase()

knowledge_base = get_knowledge_base()
