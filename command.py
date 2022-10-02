import json
from typing import Dict, List

class Command():

    def __init__(self, commands_json_file: str) -> None:
        self.commands = self.load_commands(commands_json_file)

    def load_commands(self, commands_json_file: str) -> List[Dict]:
        with open(commands_json_file, 'r') as read_file:
            data = json.load(read_file)
            read_file.close()
        return data['commands']

    def process_command(self, text: str) -> Dict:
        for command in self.commands:
            for pattern in command['patterns']:
                if pattern in text:
                    clean_text = self.remove_command_pattern_from_text(pattern, text)
                    return {'tag':command['tag'], 'arguments':clean_text}

    def remove_command_pattern_from_text(self, pattern: str, text: str) -> str:
        clean_text = text.replace(pattern, '')
        return clean_text

    
    pass

if __name__ == '__main__':

    texto = 'toca marvel spider man theme song'

    command = Command('commands.json')

    dict = command.process_command(text=texto)
    print(dict)


    # com = ProcessOrder('commands.json')
    # commands = com.load_commands()

    # tag = com.process_comand(commands, texto)
    # print(tag)

    # for command in commands:
    #     print(command)
    #     for pattern in command['patterns']:
    #         if pattern in text:
    #             print(command['tag'])
    #             break
        



    # com = ['ligar luz', 'acender luz', 'ligar led', 'acender led']
    # for pat in com:
    #     if pat in text:
    #         print('Consigo identificar o comando')
    #         break
    #     else:
    #         print('Não consigo identificar o comando')

    pass