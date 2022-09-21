import speech_recognition as sr

class Listen:

    def __init__(self, language: str) -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language

    def listen(self) -> sr.AudioData:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print('Escutando...')
            audio = self.recognizer.listen(source)
            return audio

    def audio_to_text_google(self, audio: sr.AudioData) -> str:
        try:
            return self.recognizer.recognize_google(audio, language=self.language)
        except sr.UnknownValueError:
            # print("Google Speech Recognition could not understand audio")
            return 'Não foi possivel entender o audio.'
        except sr.RequestError as e:
            # print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return 'Erro ao processar o audio.'

if __name__ == '__main__':

    listen = Listen('pt-BR')
    audio = listen.listen()
    text = listen.audio_to_text_google(audio)
    print(text)