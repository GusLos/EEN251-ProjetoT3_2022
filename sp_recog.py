import tempfile
from playsound import playsound
import winsound
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os

r = sr.Recognizer()
m = sr.Microphone()


texto = "Bem vindo. Como foi seu dia?"

lingua = 'pt-BR'

myobj = gTTS(text=texto, lang=lingua, slow=False)

temp = tempfile.NamedTemporaryFile(suffix='.wav')

# myobj.save("welcome.mp3")
# playsound(f'{temp.name}')
# playsound('{temp.name}')
print(sympy.cancel(temp.name))


# os.system(f'"start {temp.name}"')




# engine = pyttsx3.init()

# engine.say("Bem vindo de volta?")
# engine.runAndWait()





# with m as source:
#     r.adjust_for_ambient_noise(source)
#     print("Say something!")
#     audio = r.listen(source)

# try:
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='pt-BR'))
# except sr.UnknownValueError:
#      print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))