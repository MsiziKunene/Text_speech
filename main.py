from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech
from speech_translator import Translator

class SpeechTranslator:
    def __init__(self, language='english'):
        self.language = language
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.translator = Translator()

    def translate_speech(self):
        while True:
            text = self.stt.listen_and_recognize()
            print(text)
            if not text:  # Assuming speech_to_text() returns None or an empty string when the speaker is done
                break
            translation = self.translator.speech_translator(text, self.language)
            self.tts.say(translation)
            print(text)

# Usage
# Create an instance of the SpeechTranslator class
translator = SpeechTranslator(language='french')  # replace 'french' with your preferred language

# Use the translate_speech method
translator.translate_speech()
