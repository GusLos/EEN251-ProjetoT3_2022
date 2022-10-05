import speech_recognition as sr

class Listen:

    def __init__(self, language: str) -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        # self.recognizer.dynamic_energy_threshold = False
        

    def audio_input(self, time_limit: int = None) -> sr.AudioData:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print('Escutando...')
            try:
                audio = self.recognizer.listen(source=source, phrase_time_limit=time_limit, timeout=time_limit)
            except:
                audio = None
            return audio

    def audio_to_text_google(self, audio: sr.AudioData) -> str:
        if audio == None:
            return ''
        try:
            return self.recognizer.recognize_google(audio, language=self.language)
        except sr.UnknownValueError:
            # print("Google Speech Recognition could not understand audio")
            return 'Não foi possivel entender o audio.'
        except sr.RequestError as e:
            # print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return 'Erro ao processar o audio.'

    def run_listen(self, time_limit: int = None) -> str:
        audio = self.audio_input(time_limit=time_limit)
        text = self.audio_to_text_google(audio)
        return text

if __name__ == '__main__':

    listen = Listen('pt-BR')
    while True:
        try:
            audio = listen.audio_input(5)
            print('interpretando...')
            text = listen.audio_to_text_google(audio)
            print(text)
        except:
            pass
    
    # print(listen.recognizer.dynamic_energy_threshold)

    # with listen.microphone as source:
    #     listen.recognizer.adjust_for_ambient_noise(source)
    #     while True:
    #         print('Escutando...')
    #         try:
    #             audio = listen.recognizer.listen(source=source, phrase_time_limit=5, timeout=5)
    #             print('interpretando...')
    #             text = listen.audio_to_text_google(audio)
    #             print(text)
    #         except:
    #             pass
        