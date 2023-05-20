from antlr4 import *
from gen.TextLexer import TextLexer
from gen.TextParser import TextParser
import PySimpleGUI as sg

if __name__ == '__main__':
  #dados = FileStream('./scraper/news.txt', encoding='utf-8')
  dados = InputStream("Gerando uma nova frase (estou fazendo um teste), US$ 20,00.\n")
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