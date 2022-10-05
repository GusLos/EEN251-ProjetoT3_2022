from browseryt import BrowserYT

class CommandExecutor():

    def __init__(self) -> None:
        self.you_tube = BrowserYT()
        pass

    def execute_command(self, command: dict) -> None:
        if command['tag'] == 'play music':
            self.you_tube.open_yt_video(command['arguments'])
            return
        if command['tag'] == 'stop music':
            self.you_tube.close_youtube()
            return
        if command['tag'] == 'pause/play music':
            self.you_tube.yt_play_video()
            return
        if command['tag'] == 'skip yt ad':
            self.you_tube.skip_yt_ad()
        if command['tag'] == 'mute video':
            self.you_tube.yt_mute_video()
        else:
            print('Erro: Nada pode ser feito.')

    # def execute_autoyt(self, arguments: str) -> None:
    #     self.you_tube.run_yt_auto(arguments)
    #     pass

    pass

if __name__ == '__main__':
    
    # di = CommandExecutor().execute_command
    # di({'tag':'play music', 'arguments':'acas'})
    pass