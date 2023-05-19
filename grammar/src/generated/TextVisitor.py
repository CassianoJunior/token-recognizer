# Generated from c:\Users\cassi\Documents\dev\uni\compilers\token-recognition\grammar\Text.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TextParser import TextParser
else:
    from TextParser import TextParser

# This class defines a complete generic visitor for a parse tree produced by TextParser.

class TextVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TextParser#text.
    def visitText(self, ctx:TextParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TextParser#paragraph.
    def visitParagraph(self, ctx:TextParser.ParagraphContext):
        return self.visitChildren(ctx)



del TextParser