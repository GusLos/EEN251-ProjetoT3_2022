# https://pyttsx3.readthedocs.io/en/latest/engine.html
# https://pyttsx3.readthedocs.io/en/latest/

import pyttsx3
from gtts import gTTS
from playsound import playsound

class Speak:

   def __init__(self) -> None:
      self.engine = pyttsx3.init()
      pass

   def say_pyttsx3(self, *phrases: list[str]) -> None:
      for phrase in phrases:
         self.engine.say(phrase)
      self.engine.runAndWait()
      pass

   # def say_gtts(self, phrases: str, language:str = 'pt-br') -> None:
   #    for phrase in phrases:
   #       text = phrase
   #       speech = gTTS(text=text, lang=language, slow=False)
   #       speech.save("phrase.mp3")
   #       playsound("phrase.mp3")
   #       pass
   #    pass

   pass




# engine = pyttsx3.init()

# rate = engine.getProperty('rate') 
# print (rate)            
# engine.setProperty('rate', 225) 

# engine.say("Bem vindo. Como foi seu DIA?")
# engine.runAndWait()


# def onStart(name):
#    print('starting', name)
# def onWord(name, location, length):
#    print('word', name , location , length)
# def onEnd(name, completed):
#    print('finishing', name, completed)
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart('M'))
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


# def onWord(name, location, length):
#    print ('word', name, location, length)
#    if location > 1:
#       engine.stop()
# engine = pyttsx3.init()
# engine.connect('started-word', onWord)
# engine.say('A raposa marrom rápida saltou sobre o cão preguiçoso.')
# engine.runAndWait()


# engine = pyttsx3.init()
# def onStart(name):
#    print('starting', name)
# def onWord(name, location, length):
#    print ('word', name, location, length)
# def onEnd(name, completed):
#    print ('finishing', name, completed)
#    if name == 'raposa':
#       engine.say('Que cão preguiçoso', 'cachorro')
#    elif name == 'cachorro':
#       engine.endLoop()
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('A raposa marrom rápida saltou sobre o cão preguiçoso.', 'raposa')
# engine.startLoop()


if __name__ == '__main__':
   talk = Speak()
   talk.say_pyttsx3(['Olá'])
   # talk.say_gtts('olá')
   # input('teste')
   # talk.say_gtts('e até mais')


   # frases = ['Ola', 'vou te ajudar', 'até']
   # for frase in frases:
   #    speech = gTTS(text=frase, lang='pt-br', slow=False)
   #    speech.save("phrase.mp3")
   #    playsound("phrase.mp3")

   # speech = gTTS(text='olá', lang='pt-br', slow=False)
   # speech.save("phrase.mp3")
   # playsound("phrase.mp3")
   # speech = gTTS(text='vou te ajudar', lang='pt-br', slow=False)
   # speech.save("phrase.mp3")
   # playsound("phrase.mp3")
   # speech = gTTS(text='até mais', lang='pt-br', slow=False)
   # speech.save("phrase.mp3")
   # playsound("phrase.mp3")