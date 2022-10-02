from yt_auto import AutoYT

class CommandExecutor():

    def __init__(self) -> None:
        self.you_tube = AutoYT()
        pass

    def execute_command(self, command: dict) -> None:
        if command['tag'] == 'play music':
            self.execute_autoyt(command['arguments'])
            pass
        else:
            print('Erro: Nada pode ser feito.')
        pass

    def execute_autoyt(self, arguments: str) -> None:
        self.you_tube.open_youtube()
        pass

    pass

if __name__ == '__main__':
    di = [1, 2, 4]
    print(type(di))
    pass