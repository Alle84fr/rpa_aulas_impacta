### AP1 - RPA - Projeto de automação com Python

Desenvolvel asssitente virtual automatizado que deverá:
1. Leitura de Tarefas a partir de um Arquivo
• As tarefas estarão organizadas em um arquivo (Excel ou CSV) que você
deverá criar.
• Cada linha do arquivo representará uma ação a ser executada pelo
assistente.
• Exemplo:
o Tarefa, Tipo, Dado
o Abrir navegador, click, navegador_icone
o Digitar site, texto, www.exemplo.com
o Pressionar Enter, tecla, enter
o Esperar, espera, 5
(Este é apenas um exemplo você deve criar seu csv)
2. Execução das Ações com Base em Condições
• O programa deve interpretar o tipo de ação (clicar, digitar, pressionar tecla,
esperar etc.).
• Com base nisso, deverá tomar decisões e executar as ações de forma
automática.

3. Automação com Teclado e Mouse
• O bot deverá utilizar comandos que simulam o clique do mouse e a
digitação no teclado.
4. Uso de Funções e Organização do Código
• O código deverá ser modularizado, com o uso de funções para separar
as tarefas em blocos reutilizáveis e bem-organizados.
5. Manipulação de Arquivos
• Ao final da execução, o programa deverá gerar um relatório em Excel
contendo um resumo de todas as tarefas executadas, informando:
o Qual tarefa foi realizada
o O status (executada com sucesso ou não)
o O tempo estimado de execução

🛠 Requisitos Técnicos
Seu projeto deve obrigatoriamente envolver:
• Uso de estruturas condicionais (if, elif, else) e laços de repetição (for,
while)
• Criação e uso de funções personalizadas
• Leitura de arquivos CSV ou Excel com a biblioteca pandas
• Geração e formatação de relatórios em Excel com openpyxl
• Uso da biblioteca PyAutoGUI para automação de ações com teclado e
mouse
• Captura de posições de elementos na tela para uso nos cliques
automatizados