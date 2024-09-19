import speech_recognition as audio

class SpeechToText:
    def __init__(self, language='zu-ZA'):
        self.recogn = audio.Recognizer()
        self.language = language

    def listen_and_recognize(self):
        with audio.Microphone() as source:
            print("Talk")
            audio_text = self.recogn.listen(source)
            print("/--------Analyzing ----------/")
            try:
                print("Your words")
                return self.recogn.recognize_google(audio_text, language=self.language)
            except audio.UnknownValueError:
                print("Please try again I could not recognise anything you've said")
            except audio.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
