from deep_translator import GoogleTranslator

class Translator:
    @staticmethod
    def translate(content: str, source: str, target: str) -> str:
        return GoogleTranslator(
            source=source,
            target=target
        ).translate(content)