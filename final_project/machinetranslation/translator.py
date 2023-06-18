"""Module deep_translator for translating text languages."""
from deep_translator import GoogleTranslator, MyMemoryTranslator

def english_to_french(english_text):
    """Function translating English text to French."""
    translator = GoogleTranslator(source='english', target='french')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Function translating French text to English."""
    translator = MyMemoryTranslator(source='french', target='english')
    english_text = translator.translate(french_text)
    return english_text
