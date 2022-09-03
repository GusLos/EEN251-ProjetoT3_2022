# https://pyttsx3.readthedocs.io/en/latest/engine.html
# https://pyttsx3.readthedocs.io/en/latest/

import pyttsx3

class speak:
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


engine = pyttsx3.init()
def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print ('finishing', name, completed)
   if name == 'raposa':
      engine.say('Que cão preguiçoso', 'cachorro')
   elif name == 'cachorro':
      engine.endLoop()
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('A raposa marrom rápida saltou sobre o cão preguiçoso.', 'raposa')
engine.startLoop()
