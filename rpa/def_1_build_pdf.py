#                     _______________________________________________________________
#                     |                                                             |
#                     |                      FUNÇÃO PDF 1/                         |
#                     |_____________________________________________________________|


from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Image, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from datetime import datetime


def build_pdf(data):
    
    ''' Função para criar relatório final em pdf 
        imposts obrigatórios para o funcionamento:
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle,
        from reportlab.platypus import Paragraph, SimpleDocTemplate,
        from reportlab.lib.pagesizes import A4,
        pip install reportlab.'''
        
        
    #___________ FORMATAÇÃO TEXTO
   
    formatacao = getSampleStyleSheet()

    formatacao_esquerda = ParagraphStyle(name="Esquerda", parent=formatacao["Normal"], alignment=0, fontSize=12)
    formatacao_direita = ParagraphStyle(name="Direita", parent=formatacao["Normal"], alignment=2, fontSize=12)
    formatacao_centro = ParagraphStyle(name="Centro", parent=formatacao["Normal"], alignment=1, fontSize=12)
    formatacao_titulo1 = ParagraphStyle(name="Titulo1", parent=formatacao["Heading1"], alignment=1)
    formatacao_titulo2 = ParagraphStyle(name="Titulo2", parent=formatacao["Heading2"], alignment=1, spaceAfter= 180)
    formatacao_titulo3 = ParagraphStyle(name="Titulo3", parent=formatacao["Heading3"], alignment=1, spaceAfter= 40)
    formatacao_paragafo1 = ParagraphStyle(name="Paragrafi1", parent=formatacao["Heading2"], alignment=1, spaceAfter= 10)
    formatacao_centrodata = ParagraphStyle(name="Centro", parent=formatacao["Normal"], alignment=1, fontSize=8, spaceBefore=400)

    #___________ IMAGENS
    
    img_1 = "Print_tela_09-Jun-2025__20-49-46.png"
    img_1_a = Image(img_1, width=300, height=200)
    img_2 = "Print_tela_09-Jun-2025__20-49-56.png"
    img_2_a = Image(img_2, width=300, height=200)
    img_3 = "Print_tela_09-Jun-2025__20-50-09.png"
    img_3_a = Image(img_3, width=300, height=200)
    img_4 = "Print_tela_09-Jun-2025__20-50-21.png"
    img_4_a = Image(img_4, width=300, height=200)
    img_5 = "Print_tela_09-Jun-2025__20-51-05.png"
    img_5_a = Image(img_5, width=300, height=200)
    img_6 = "Print_tela_09-Jun-2025__20-51-16.png"
    img_6_a = Image(img_6, width=300, height=200)
    img_7 = "Print_tela_09-Jun-2025__20-51-46.png"
    img_7_a = Image(img_7, width=300, height=200)
    img_8 = "Print_tela_09-Jun-2025__21-43-28.png"
    img_8_a = Image(img_8, width=300, height=200)
    img_9 = "tecnotoxpintrest.png"
    img_9_a = Image(img_9, width=300, height=200)
    img_10 = "Print_tela_09-Jun-2025__23-13-25.png"
    img_10_a = Image(img_10, width=300, height=200)
    
    #___________ TEXTO

    paragafos = [
        Paragraph("Faculdade Impacta", formatacao_titulo1),
        Paragraph("Automação Robótica de Processo", formatacao_titulo2),
        Paragraph(f"Alessandra F Rigonatti", formatacao_centro),
        Paragraph(f"RA: 2401151", formatacao_centro),
        Paragraph(f" ", formatacao_titulo2),
        Paragraph(f"São Paulo {data}", formatacao_centrodata),
        Paragraph(f"📼 Requisição de dados a uma API pública 📽️ ", formatacao_titulo3),
        Paragraph(f"Para este projeto de RPA, escolhi a API dos Studios Ghibli - https://ghibliapi.vercel.app/films-", formatacao_centro),
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"Após analisar as apis listadas no pdf de regras do trabalho, escolhi pegar um aplicativo que dispertasse meu interesse e ideias de divisões.\nCheguei nesta api por meio da DeepSeek, queria um que fossem desenhos que gosto com imagens.\nO trabalho será dividido entre desenhos já assistidos e desenhos que estão na lista para assistir.\n Ao todo serão listados 15 desenhos no total, o que tiverem fora de alguma lista é porque não irei assistir ou não prendeu minha atenção.\nInformações que serão mostradas:\nTitulo, Título original, ano, url imagem.", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph("Fases do projeto", formatacao_titulo3),
        Paragraph(f"1° - Função def char_espc -> função que irá analisar o fluxo padrão (std) na saída (Output).\nO io.TextIOWrapper irá garantir que não dará mensagem de erro no programa por causa de caracteres especiais.\nResumindo, nesta função o .py pegar a saída padrão stdout e troca para a que permite caracteres especias.\nQuase todas funções possuem esta função, então separei, agora cada função que percisar dela é só chamar-la\n\nImagem 1", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_1_a,
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"2° - Função build_pdf -> função que irá gerar o relatório em pdf.\nFoi usado a biblioteca reportlab, conseidei mais fácil de organizar os texto, espaço e tamanho de folha.\nA formatação é feita por parágrafos (ParagraphStyle), usando id para cada formatação (name), parent, estilo 'Normal', 'Heading1', fonte maior, equivalente ao h1 do html, 'Heading2' e 'Heading3.\nAlinhamento usado foi Centralizado (1), à esquedar (0) e tem opação de ser à direita (2).\nO spaceAfter é para pular linhas, os Headers já possuem um.\n\nImagem 2", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_2_a,
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"3° - Não é uma função -> O processo desta automação é interno, não envolvendo troca de telas, a não ser que o próprio usuário a faça. Tendo esta característica, a função possui um tempo de espera para que, manualmente, o usuário ache (run), mude para tela que deseja, arrume e espere a capatura.\nPara não haver problemas com o nome, foi inserido data (característica em praticamente todos nomes) com horas, minutos e segundo.\n\nImagem 3", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_3_a,
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"4° - Função desenhos_base -> função que irá acessar (método GET) a api escolhida ( Studio Ghibli), percorrer os 15 primeiros ids para que futuramente possa ser dividido em bancos de dados.\nOs dados que serão usados serão Título, título original, ano e a url da imagem, todos em Inglês\n\nImagem 4", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_4_a,
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"5° - Função bd_geral -> função que irá receber as informações recebidas pela def desenhos_base.\nUsando o SQLite (obrigatório no projeto) executei, sepradamente três tabelas:\nA 1° é tabela quinze_desenhos, recebe todos os desenhos.A forma de texto/string titulo, titulo oficial e url da imagem, o ano é n° inteiro/integrer e o id é criado automaticamente (sendo obrigatório existir).\nA 2° tabela é a de desenhos que amo.A forma de criar é a mesma da 1°, porém esta possui uma condição chumbada no código.\nA 3° é tabela de desenhos que verei, segue mesmo modelo da 2° tabela.\nA 3° tabela é ade desenhos que não verei, ela possui mesmo molde que a 2°, porém a sua condição não é chumbada, ela receberá os dados dos que não entraram nem na 2° nem na 3°.\nNão foi pedido para transfomar os dados emm tabelas ou texto world.\nHá algumas fomas de se ver os dados:\nTerminal - Bash - sqlite3 projeto_rpa.db - .table - .schema quinze_desenhos\nMesmo sendo no terminal deve ser feito dowload do sqlite-tools-win... .\nCriando um função.\nUsando o DB Browser for SQLite\n\nImagem 5", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_5_a,
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"6° - Função emails -> função que irá traduzir o caminho de verificação, com comando do with irá abrir, manipular e fechar o arquivo, codificar os dados, receber anexo e enviar o email\n\nImagem 6", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_6_a,
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"7° - Função main -> Esta é o último arquivo e última função que irá reunir os import de todos files e seus def e roar todos juntos de uam única vez\n\nImagem 7", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_7_a,
        Paragraph(f" ", formatacao_paragafo1),
        img_10_a,
        Paragraph("Conclusão", formatacao_titulo3),
        Paragraph(f"Uma das matérias que mais gostei de fazer.\nPor mais que eu tenha que pedir ajuda a Ai, principalemnete quando há erros que ainda não sei distrinchar, ou quando quero adiconar mais detalhes, eu sinto que ver as aulas, fazer exercícios durante a explicação e rever os códigos corrigidos após, deixa mais fácil a mágica de automatizar algo.\nPerdi tempo considerável no  print, não poser ser difícil, mas porque fiz ele de 3 formas diferentes e não consegui fazer ficar em ponto específico.\nA primeira com comando de 'input', o usuário deveria teclar p+enter. Depois esqueci que as telas não mudam, e por fim, ajustar o time para mudança de tela.\nOutro ponto que tive de investir mais tempo foi em achar api e cometi o erro de querer fazer for no bd, não deu certo.\nUm erro que complicou foi o 'ValueError: I/O operation on closed file', sim anotei, fiz uma breve lista de como achar este erro no cód, no final, era identação, duas letras trocadas.\nAinda no Banco de dados com api, me perdi na forma de fazer o return do desenhos_base, estava pondo nome do dict, não as chaves.\nContinuando no bd, dei um errada ao por o VALUES, 1° escrevi o valor, depois troquei para ? e no final era porque não coloquei S.\nO arquivo que envio tentei tirar todos os somentários, mas se precisar ver posso enviar o original, porém há files que deletei o comentário, não percebi e só vi agora.\nCerteza que houveram mais dificuldes, mas estas foram a que me marcaram.\n\nImagem 8", formatacao_esquerda),
        Paragraph(f" ", formatacao_paragafo1),
        img_8_a,
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f" ", formatacao_paragafo1),
        Paragraph(f"Obrigada por tudo, espero poder manter contato. ", formatacao_centro),
        Paragraph(f" ", formatacao_paragafo1),
        img_9_a,]

    #___________ CRIAR PDF
    
    nome_pdf = f"relatorio_2401151_{datetime.now().strftime("%d-%b-%Y")}.pdf"
    pdf_doc = SimpleDocTemplate(nome_pdf, pag_size = A4)
    pdf_doc.build(paragafos)
    print(f" {nome_pdf} gerado com sucesso")
    
    return paragafos