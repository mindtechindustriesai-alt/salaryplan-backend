class KnowledgeBase:
    def __init__(self):
        self.data = {}
    def get(self, key):
        return self.data.get(key, "Information not found")

knowledge_base = KnowledgeBase()
