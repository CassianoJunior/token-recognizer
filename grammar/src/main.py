from antlr4 import *
from src.generated.TextLexer import TextLexer
from src.generated.TextParser import TextParser

if __name__ == '__main__':
  # dados = FileStream('../scraper/news.txt', encoding='utf-8')
  dados = InputStream("U$ 20,00.\n")
  lexer = TextLexer(dados)
  for tok in lexer.getAllTokens():
    print(tok.text, tok.type)
  lexer.reset()
  # stream = CommonTokenStream(lexer)
  # parser = TextParser(stream)
  # tree = parser.text()
  # print(tree.toStringTree())