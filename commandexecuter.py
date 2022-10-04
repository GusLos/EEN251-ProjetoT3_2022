from browseryt import BrowserYT

class CommandExecutor():

    def __init__(self) -> None:
        self.you_tube = BrowserYT()
        pass

    def execute_command(self, command: dict) -> None:
        if command['tag'] == 'play music':
            self.execute_autoyt(command['arguments'])
        if command['tag'] == 'stop music':
            self.you_tube.close_youtube()
        else:
            print('Erro: Nada pode ser feito.')

    def execute_autoyt(self, arguments: str) -> None:
        self.you_tube.run_yt_auto(arguments)
        pass

    pass

if __name__ == '__main__':
    
    # di = CommandExecutor().execute_command
    # di({'tag':'play music', 'arguments':'acas'})
    pass