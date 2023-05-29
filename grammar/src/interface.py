import PySimpleGUI as sg
import antlr4
import os
import importlib

def getTokenNameById(id: int, folderPath: str):
  # Construct the path to the Text.tokens file relative to the script directory
  path = os.path.join(folderPath, 'Text.tokens')

  with open(path, 'r') as file:
    for line in file:
      name, identifier = line.split('=')
      if int(identifier.strip()) == id:
        return name

if __name__ == '__main__':
  layout = [
    [sg.Text('Select a path to AntLR generated files:')],
    [sg.Input(key=0), sg.FolderBrowse()],
    [sg.Text('Select a file to analyze:')],
    [sg.Input(key=1), sg.FileBrowse()],
    [sg.OK(), sg.Cancel()],
    [sg.Text('File content:')],
    [sg.Output(size=(50, 8), key='_FILE_CONTENT_')],
    [sg.Text('Token output:')],
    [sg.Output(size=(50, 8), key='_TOKEN_OUTPUT_')]
]

  window = sg.Window('Token recognizer', layout, size=(400,480), resizable=True)

  while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
      break
    elif event == 'OK':
      antlrFolderPath, selectedFile = values[0], values[1]
      window['_FILE_CONTENT_'].update('')
      window['_TOKEN_OUTPUT_'].update('')
      if selectedFile and antlrFolderPath:
        try:
          with open(selectedFile, 'r', encoding='utf-8') as file:
             with open(selectedFile, 'r', encoding='utf-8') as file:
              content = file.read()
              window['_FILE_CONTENT_'].print(content)

          dados = antlr4.FileStream(selectedFile, encoding='utf-8')

          pathToLexerModule = os.path.join(antlrFolderPath, 'TextLexer.py').replace('\\', '/')
          spec = importlib.util.spec_from_file_location('TextLexer', pathToLexerModule)
          lexerModule = importlib.util.module_from_spec(spec)
          spec.loader.exec_module(lexerModule)
          lexer = lexerModule.TextLexer(dados)

          for tok in lexer.getAllTokens():
            window['_TOKEN_OUTPUT_'].print(f'{tok.text} -> {getTokenNameById(tok.type, antlrFolderPath)}')
        except Exception as e:
          print(e)
          print('Error reading file')
      
      else: 
        window['_FILE_CONTENT_'].print("Select a file and a folder with AntLR generated files")