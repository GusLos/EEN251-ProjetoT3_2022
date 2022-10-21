
# Projeto para disciplina EEN251 (Microcontroladores e Sistemas Embarcados) T2*

Primeiro baixe as dependências usando o comando ```pip3 install -r requirements.txt``` ou apenas execute o arquivo ```setup.py```.

Após baixar as dependências, é necessário baixar um driver para o selenium conseguir utilizar o navegador.(O programa foi feito e testado no Chromium/Chrome)

Os drivers podem ser encontrados em: <br>
<sub>Verifique a versão do navegador do seu computador antes de baixar o driver.</sub><br>
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

Com o ambiente preparado basta rodar o programa ```main.py```.

O texto sendo passado no construtor da classe IA é o "nome" da IA, ao falar esse texto/nome a IA vai responder pedindo um comando.<br>
Ao iniciar o programa, a IA vai se apresentar e esperar ser chamada.<br>
<sub>**Nota:** Para saber exatamente quando a IA está escutando basta olhar o terminal, onde deve aparecer ```Escutando...``` e outros indicadores. Vale resaltar que dependendo do computador e do ambiente (barulho), a IA pode acabar demorando para identificar a voz/comado.</sub>

Os comandos estão presentes no arquivo ```commands.json```, embora o mais útil e interessante é o comando de tocar música.

Na *branch main*, ao abrir o YouTube, a IA tenta pular automaticamente os anúncios, caso não consiga ela tira o som. Porém, ela não responde (fica travada) até o vídeo acabar.<br>
**NÃO FECHE O NAVEGADOR**, o programa não consegue abrir e vincular uma nova janela do navegador.

Na *branch EEN251*, ao abrir o YouTube, a IA não pula os anúncios e nem tira o som, porém ela não fica travada e consegue receber comandos ainda com o YouTube aberto, com isso, essa branch tem mais comandos disponíveis para interação com o vídeo.

Em ambas as branch fechar a página web que abre com a execução do programa gera erro no programa.
