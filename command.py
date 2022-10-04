import json

class Command():

    def __init__(self, commands_json_file: str) -> None:
        self.commands = self.load_commands(commands_json_file)

    def load_commands(self, commands_json_file: str) -> list[dict]:
        with open(commands_json_file, 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            read_file.close()
        return data['commands']

    def process_command(self, text: str) -> dict:
        for command in self.commands:
            for pattern in command['patterns']:
                if pattern in text:
                    clean_text = self.remove_command_pattern_from_text(pattern, text)
                    return {'tag':command['tag'], 'arguments':clean_text, 'responses':command['responses']}
        return {'tag':'unknown' , 'arguments':text, 'responses':command['responses']}

    def remove_command_pattern_from_text(self, pattern: str, text: str) -> str:
        clean_text = text.replace(pattern, '')
        return clean_text

    
    pass

if __name__ == '__main__':

    texto = 'apagar musica do batman'

    command = Command('commands.json')

    dict = command.process_command(text=texto)
    print(dict)