import speech_recognition as sr


r = sr.Recognizer()
m = sr.Microphone()



with m as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='pt-BR'))
except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))