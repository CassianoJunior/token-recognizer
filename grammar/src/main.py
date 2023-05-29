from antlr4 import InputStream, FileStream
from generated.TextLexer import TextLexer
from generated.TextParser import TextParser
import PySimpleGUI as sg

if __name__ == '__main__':
  # dados = FileStream('../scraper/news.txt', encoding='utf-8')
  dados = InputStream('Jose Cassiano De Melo Junior é do FBI')
  lexer = TextLexer(dados)
  for tok in lexer.getAllTokens():
    if(tok.text == '\n'):
      print("breakLine ", tok.type)
    else: 
      print(tok.text, tok.type)
    
  #lexer.reset()
  #stream = CommonTokenStream(lexer)
  #parser = TextParser(stream)
  #tree = parser.text()
  #print(tree.toStringTree())