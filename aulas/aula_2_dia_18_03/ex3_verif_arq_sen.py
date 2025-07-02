import os
import pyautogui

def verificaArquivo(nomeArquivo):
    if os.path.exists(nomeArquivo):
        pyautogui.alert("Arquivo encontrado!")
    else:
        pyautogui.alert("Arquivo não encontrado")


def verficaUsuario(senha):
    if senha == "admin":
        verificaArquivo("dados.csv")
        local="C:/Users/vande/OneDrive/Documentos"
        listarArquivos(local)
    else:
        pyautogui.alert("Senha inválida! Finalizando processo....")
        
def listarArquivos(diretorio):
    for arquivo in os.listdir(diretorio):
        print(f"Processando: {arquivo}")
    print("Processo finalizado....")

usuario=pyautogui.password("Informe a senha:")
verficaUsuario(usuario)