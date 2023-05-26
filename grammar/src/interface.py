import PySimpleGUI as sg
import antlr4
from generated import TextLexer
import os

def getTokenNameById(id: int):
  # Get the directory where this script is located
  scriptDir = os.path.dirname(os.path.abspath(__file__))

  # Construct the path to the Text.tokens file relative to the script directory
  path = os.path.join(scriptDir, 'generated', 'Text.tokens')

  with open(path, 'r') as file:
    for line in file:
      name, identifier = line.split('=')
      if int(identifier.strip()) == id:
        return name

if __name__ == '__main__':
  layout = [
    [sg.Text('Select a file to analyze:')],
    [sg.Input(), sg.FileBrowse()],
    [sg.OK(), sg.Cancel()],
    [sg.Text('File content:')],
    [sg.Output(size=(50, 8), key='_FILE_CONTENT_')],
    [sg.Text('Token output:')],
    [sg.Output(size=(50, 8), key='_TOKEN_OUTPUT_')]
]

  window = sg.Window('Token recognizer', layout, size=(400,450), resizable=True)

  while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
      break
    elif event == 'OK':
      selectedFile = values[0]
      if selectedFile:
        try:
          with open(selectedFile, 'r', encoding='utf-8') as file:
             with open(selectedFile, 'r', encoding='utf-8') as file:
              content = file.read()
              window['_FILE_CONTENT_'].print(content)

          dados = antlr4.FileStream(selectedFile, encoding='utf-8')
          lexer = TextLexer.TextLexer(dados)
          for tok in lexer.getAllTokens():
            window['_TOKEN_OUTPUT_'].print(f'{tok.text} -> {getTokenNameById(tok.type)}')
        except Exception as e:
          print(e)
          print('Error reading file')