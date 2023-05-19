# Generated from c:\Users\cassi\Documents\dev\uni\compilers\token-recognition\grammar\Text.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TextParser import TextParser
else:
    from TextParser import TextParser

# This class defines a complete listener for a parse tree produced by TextParser.
class TextListener(ParseTreeListener):

    # Enter a parse tree produced by TextParser#text.
    def enterText(self, ctx:TextParser.TextContext):
        pass

    # Exit a parse tree produced by TextParser#text.
    def exitText(self, ctx:TextParser.TextContext):
        pass


    # Enter a parse tree produced by TextParser#paragraph.
    def enterParagraph(self, ctx:TextParser.ParagraphContext):
        pass

    # Exit a parse tree produced by TextParser#paragraph.
    def exitParagraph(self, ctx:TextParser.ParagraphContext):
        pass



del TextParser