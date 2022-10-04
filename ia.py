from listen import Listen
from speak import Speak
from command import Command
from commandexecuter import CommandExecutor
import random

class IA():
    
    def __init__(self, name: str, language: str = 'pt-BR') -> None:
        self.name = name 
        self.listen = Listen(language).run_listen
        self.speak = Speak().say_pyttsx3
        self.understand = Command('commands.json').process_command
        self.execute = CommandExecutor().execute_command
        self.presentation()
        self.run_IA()

    def run_IA(self) -> None:
        while True:
            user_phrase = self.listen(5)
            if self.name in user_phrase:
                self.request_command()
                user_phrase = self.listen(10)
                user_command = self.understand(user_phrase)
                responses = user_command['responses']
                self.speak(random.choice(responses))
                self.execute(user_command)
                pass
        pass

    def presentation(self) -> None:
        ia_phrase = ['Olá, eu sou', str(self.name),'um assistente virtual.']
        self.speak(ia_phrase)

    def request_command(self) -> None:
        self.speak(['Me chamou?', 'Já pode dizer o comando.'])
        pass

    pass

if __name__ == '__main__':

    ia = IA('Python')
    # ia.run_IA()


    pass