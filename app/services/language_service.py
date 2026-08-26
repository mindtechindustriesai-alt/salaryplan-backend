class LanguageService:
    def __init__(self):
        self.supported = ["en", "zu", "xh", "sn"]
    def translate(self, text, lang):
        return text

language_service = LanguageService()
