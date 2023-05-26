grammar Text;

text: (paragraph NEWLINE)+;

paragraph: ((WORD | PONTUATION)+ | NUM | ACRONYM | OWN_NAME | MONEY | CITATION | DESCRIPTION | PERCENT | TWITTER_ACCOUNT
            | ORDINARY_NUMER)+;

LINK: ('http' | 'https')'://'WORD+('.'WORD+)+('/'(WORD | WORD'/')+)*;

PONTUATION: '.' | ',' | '!' | '?' | ':' | ';' | '-' | '[' | ']' | '{' | '}' | '(' | ')';

// FIXME: this not has expected behavior, Articles are recognized as acronyms
ACRONYM: [A-Z]{2,};


// FIXME: this not has expected behavior, Start of phrase is recognized as own name
OWN_NAME: ([A-Z]WORD* (' '[A-Z]WORD)*)+;

WEEKDAY: 'segunda-feira' | 'terça-feira' | 'quarta-feira' | 'quinta-feira' | 'sexta-feira' | 'sábado' | 'domingo';

WEEKDAY_WITH_NUMBER: WEEKDAY ' ' (NUM | '('NUM')');

// áóíéúãàêõçÁÓÍÉÚÃÀÊõÇ
WORD: [a-záóíéúâÂêãàõôÔçÁÓÍÉÚÃÀÊÕÇ-]+;

MONEY: (('R$' | 'US$' | '€' | '£' | '¥') ' ' NUM);

NUM: (DIGIT(DIGIT)* | DIGIT','DIGIT | DIGIT'.'DIGIT | DIGIT'.'DIGIT','DIGIT | DIGIT','DIGIT'.'DIGIT);

DIGIT: [0-9]+;

CITATION: ('“'|'‘'|'"'|'”'|'\''|'’')(((WORD | PONTUATION)+ | NUM | ACRONYM | OWN_NAME | MONEY | DESCRIPTION | PERCENT | TWITTER_ACCOUNT
            | ORDINARY_NUMER)+ (' ' | NEWLINE)*)+ ('”'|'\''|'’'|'"'|'“'|'‘');

DESCRIPTION: '('(((WORD | PONTUATION)+ | NUM | ACRONYM | OWN_NAME | MONEY | CITATION | PERCENT | TWITTER_ACCOUNT
            | ORDINARY_NUMER)+ (' ' | NEWLINE)*)+ ')';

PERCENT: NUM '%';

TWITTER_ACCOUNT: '@'WORD (NUM)*;

ORDINARY_NUMER: NUM 'º';

SYMBOL: [&%$#*+@/\\];

NEWLINE: [\r\n];

WS: (' '|'\t')+ -> skip;