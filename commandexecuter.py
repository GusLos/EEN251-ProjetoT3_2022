from browseryt import BrowserYT
from mqqtPublish import MqqtPublish

class CommandExecutor():

    def __init__(self) -> None:
        self.you_tube = BrowserYT()
        self.publish = MqqtPublish()
        pass

    def execute_command(self, command: dict) -> None:
        if command['tag'] == 'play music':
            self.execute_autoyt(command['arguments'])
        if command['tag'] == 'stop music':
            self.you_tube.close_youtube()
        if command['tag'] == 'light on':
            # self.publish.publishValue('cozinha', 1)
            self.publish.publishValue(command['arguments'], 1)
        if command['tag'] == 'light off':
            self.publish.publishValue('cozinha', 0)
        else:
            print('Erro: Nada pode ser feito.')

    def execute_autoyt(self, arguments: str) -> None:
        self.you_tube.run_yt_auto(arguments)
        pass

    pass

if __name__ == '__main__':
    
    e = CommandExecutor().execute_command
    e({'tag':'light on', 'arguments':'cozinha'})
    pass