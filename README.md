
# Projeto para disciplina EEN251 (Microcontroladores e Sistemas Embarcados) T2*

Primeiro baixe as dependencias usando o comando pip3 install -r requirements.txt ou apenas execute o arquivo setup.py.

Após baixar as dependencias, é só executar o programa main.py.

O texto sendo passado no construtor da classe IA é o "nome" da ia, ao falar esse texto/nome a ia vai responder pedindo um comando.

Para saber exatamente quando a ia está escutando basta olhar o terminal, onde deve aparecer 'Escutando...' e outros indicadores.

Os comandos estão presentes no arquivo 'commands.json', embora o mais útil e interessante é o comando de tocar música.

Na branch main, ao abrir o youtube, a ia tenta pular automaticamente os anúncios, caso não consiga ela tira o som. Porém ela não responde (fica travada) até o video acabar.

Na branch EEN251, ao abrir o youtube, a ia não pula os anúncios e nem tira o som, porém ela não fica travada e consegue receber comandos ainda com o youtube aberto, com isso, essa branch tem mais comandos disponíveis para interação com o vídeo.

Em ambas as branchs fechar a página web que abre junto com a execução do programa vai quebrar o programa, e ao final do vídeo a página deve continuar aberta.
