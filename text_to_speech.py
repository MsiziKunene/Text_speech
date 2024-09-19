import pyttsx3

class TextToSpeech:
    def __init__(self, rate=110, voice_id=1):
        self.speech = pyttsx3.init()
        self.speech.setProperty('rate', rate)
        self.speech.setProperty('voice', self.speech.getProperty('voices')[voice_id].id)

    def say(self, corpus):
        self.speech.say(corpus)
        self.speech.runAndWait()
