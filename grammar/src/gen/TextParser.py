# Generated from C:/Users/jose1/Documents/UFPI/6º período/Compiladores/antlr4-trab1/token-recognizer/grammar\Text.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,30,2,0,7,0,2,1,7,1,1,0,1,0,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        4,1,13,8,1,11,1,12,1,14,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,
        26,8,1,11,1,12,1,27,1,1,0,0,2,0,2,0,1,2,0,1,1,4,4,39,0,7,1,0,0,0,
        2,25,1,0,0,0,4,5,3,2,1,0,5,6,5,13,0,0,6,8,1,0,0,0,7,4,1,0,0,0,8,
        9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,13,7,0,0,0,12,
        11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,26,1,0,0,
        0,16,26,5,6,0,0,17,26,5,2,0,0,18,26,5,3,0,0,19,26,5,5,0,0,20,26,
        5,8,0,0,21,26,5,9,0,0,22,26,5,10,0,0,23,26,5,11,0,0,24,26,5,12,0,
        0,25,12,1,0,0,0,25,16,1,0,0,0,25,17,1,0,0,0,25,18,1,0,0,0,25,19,
        1,0,0,0,25,20,1,0,0,0,25,21,1,0,0,0,25,22,1,0,0,0,25,23,1,0,0,0,
        25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,3,1,0,
        0,0,4,9,14,25,27
    ]

class TextParser ( Parser ):

    grammarFileName = "Text.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PONTUATION", "ACRONYM", "OWN_NAME", 
                      "WORD", "MONEY", "NUM", "DIGIT", "CITATION", "DESCRIPTION", 
                      "PERCENT", "TWITTER_ACCOUNT", "ORDINARY_NUMER", "NEWLINE", 
                      "WS" ]

    RULE_text = 0
    RULE_paragraph = 1

    ruleNames =  [ "text", "paragraph" ]

    EOF = Token.EOF
    PONTUATION=1
    ACRONYM=2
    OWN_NAME=3
    WORD=4
    MONEY=5
    NUM=6
    DIGIT=7
    CITATION=8
    DESCRIPTION=9
    PERCENT=10
    TWITTER_ACCOUNT=11
    ORDINARY_NUMER=12
    NEWLINE=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8062) != 0)):
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

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.NUM)
            else:
                return self.getToken(TextParser.NUM, i)

        def ACRONYM(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.ACRONYM)
            else:
                return self.getToken(TextParser.ACRONYM, i)

        def OWN_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.OWN_NAME)
            else:
                return self.getToken(TextParser.OWN_NAME, i)

        def MONEY(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.MONEY)
            else:
                return self.getToken(TextParser.MONEY, i)

        def CITATION(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.CITATION)
            else:
                return self.getToken(TextParser.CITATION, i)

        def DESCRIPTION(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.DESCRIPTION)
            else:
                return self.getToken(TextParser.DESCRIPTION, i)

        def PERCENT(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.PERCENT)
            else:
                return self.getToken(TextParser.PERCENT, i)

        def TWITTER_ACCOUNT(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.TWITTER_ACCOUNT)
            else:
                return self.getToken(TextParser.TWITTER_ACCOUNT, i)

        def ORDINARY_NUMER(self, i:int=None):
            if i is None:
                return self.getTokens(TextParser.ORDINARY_NUMER)
            else:
                return self.getToken(TextParser.ORDINARY_NUMER, i)

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




    def paragraph(self):

        localctx = TextParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_paragraph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4]:
                    self.state = 12 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 11
                            _la = self._input.LA(1)
                            if not(_la==1 or _la==4):
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
                elif token in [6]:
                    self.state = 16
                    self.match(TextParser.NUM)
                    pass
                elif token in [2]:
                    self.state = 17
                    self.match(TextParser.ACRONYM)
                    pass
                elif token in [3]:
                    self.state = 18
                    self.match(TextParser.OWN_NAME)
                    pass
                elif token in [5]:
                    self.state = 19
                    self.match(TextParser.MONEY)
                    pass
                elif token in [8]:
                    self.state = 20
                    self.match(TextParser.CITATION)
                    pass
                elif token in [9]:
                    self.state = 21
                    self.match(TextParser.DESCRIPTION)
                    pass
                elif token in [10]:
                    self.state = 22
                    self.match(TextParser.PERCENT)
                    pass
                elif token in [11]:
                    self.state = 23
                    self.match(TextParser.TWITTER_ACCOUNT)
                    pass
                elif token in [12]:
                    self.state = 24
                    self.match(TextParser.ORDINARY_NUMER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8062) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





