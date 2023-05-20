import PySimpleGUI as sg
from antlr4 import *
from gen.TextLexer import TextLexer

def mainScreen():
    sg.theme("DarkGrey2")
    layout = [
        [sg.Text("Nome do arquivo-texto com notícias:")],
        [sg.Input(key="textArquive")],
        [sg.Button("Visualizar Arquivo"), sg.Button("Extrair Tokens")],
    ]
    return sg.Window("Main", layout=layout, finalize=True)

def showNews():
    sg.theme("DarkGrey2")
    layout = [
        [sg.Text("Notícias:")],
        [sg.Output(size=(80,30))],
        [sg.Button("Voltar")],
    ]
    return sg.Window("showNews", layout=layout, finalize=True)

def showTokens():
    sg.theme("DarkGrey2")
    layout = [
        [sg.Text("Tokens Encontrados:")],
        [sg.Output(size=(50,30))],
        [sg.Button("Voltar")],
    ]
    return sg.Window("showTokens", layout=layout, finalize=True)

def openTxtArquive(nameArquive):
    data = FileStream(f'./scraper/{nameArquive}', encoding='utf-8')
    return data



initialScreen, showNewsScreen, showTokensScreen = mainScreen(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if (window == initialScreen or window == showNewsScreen or window == showTokensScreen) and event == sg.WIN_CLOSED:
        break

    if window == initialScreen and event == "Visualizar Arquivo":
        data = openTxtArquive(values["textArquive"])
        showNewsScreen = showNews()
        print(data)
        initialScreen.hide()

    if window == initialScreen and event == "Extrair Tokens":
        data = openTxtArquive(values["textArquive"])
        lexer = TextLexer(data)
        showTokensScreen = showTokens()
        for tok in lexer.getAllTokens():
            if(tok.text == '\n'):
                print("Token: breakLine\t\t\t\t", f"token type: {tok.type}")
            else: 
                print(f"Token: {tok.text}\t\t\t\t", f"token type: {tok.type}")
        initialScreen.hide()
        
    if window == showNewsScreen and event == "Voltar":
        showNewsScreen.hide()
        initialScreen.un_hide()

    if window == showTokensScreen and event == "Voltar":
        showTokensScreen.hide()
        initialScreen.un_hide()