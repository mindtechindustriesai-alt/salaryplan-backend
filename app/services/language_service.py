class LanguageService:
    def __init__(self):
        self.supported = ["en", "zu", "xh", "sn"]
    
    def translate(self, text, lang):
        return text

def get_language_service():
    return LanguageService()

language_service = get_language_service()
