# Generated from c:\Users\cassi\Documents\dev\uni\compilers\token-recognition\grammar\Text.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\30\4\2\t\2\4\3\t\3\3\2\3\2\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\3\6\3\17\n\3\r\3\16\3\20\3\3\6\3\24\n\3\r\3\16\3\25")
        buf.write("\3\3\2\2\4\2\4\2\3\4\2\3\3\5\5\2\31\2\t\3\2\2\2\4\23\3")
        buf.write("\2\2\2\6\7\5\4\3\2\7\b\7\13\2\2\b\n\3\2\2\2\t\6\3\2\2")
        buf.write("\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2")
        buf.write("\r\17\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2\2")
        buf.write("\20\21\3\2\2\2\21\24\3\2\2\2\22\24\7\b\2\2\23\16\3\2\2")
        buf.write("\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2")
        buf.write("\2\2\26\5\3\2\2\2\6\13\20\23\25")
        return buf.getvalue()


class TextParser ( Parser ):

    grammarFileName = "Text.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PONTUATION", "OWN_NAME", "WORD", "MONEY", 
                      "NUM", "DIGIT", "CITATION", "DESCRIPTION", "NEWLINE", 
                      "WS" ]

    RULE_text = 0
    RULE_paragraph = 1

    ruleNames =  [ "text", "paragraph" ]

    EOF = Token.EOF
    PONTUATION=1
    OWN_NAME=2
    WORD=3
    MONEY=4
    NUM=5
    DIGIT=6
    CITATION=7
    DESCRIPTION=8
    NEWLINE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextParser.ParagraphContext)
            else:
                return self.getTypedRuleContext(TextParser.ParagraphContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.NEWLINE)
            else:
                return self.getToken(TextParser.NEWLINE, i)

        def getRuleIndex(self):
            return TextParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = TextParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.paragraph()
                self.state = 5
                self.match(TextParser.NEWLINE)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TextParser.PONTUATION) | (1 << TextParser.WORD) | (1 << TextParser.DIGIT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.DIGIT)
            else:
                return self.getToken(TextParser.DIGIT, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.WORD)
            else:
                return self.getToken(TextParser.WORD, i)

        def PONTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.PONTUATION)
            else:
                return self.getToken(TextParser.PONTUATION, i)

        def getRuleIndex(self):
            return TextParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraph" ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraph" ):
                listener.exitParagraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParagraph" ):
                return visitor.visitParagraph(self)
            else:
                return visitor.visitChildren(self)




    def paragraph(self):

        localctx = TextParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_paragraph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TextParser.PONTUATION, TextParser.WORD]:
                    self.state = 12 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 11
                            _la = self._input.LA(1)
                            if not(_la==TextParser.PONTUATION or _la==TextParser.WORD):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()

                        else:
                            raise NoViableAltException(self)
                        self.state = 14 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass
                elif token in [TextParser.DIGIT]:
                    self.state = 16
                    self.match(TextParser.DIGIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TextParser.PONTUATION) | (1 << TextParser.WORD) | (1 << TextParser.DIGIT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





