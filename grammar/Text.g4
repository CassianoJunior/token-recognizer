grammar Text;

text: (paragraph NEWLINE)+;

paragraph: ((WORD | PONTUATION)+ | NUM | ACRONYM | OWN_NAME | MONEY | CITATION | DESCRIPTION | PERCENT | TWITTER_ACCOUNT
            | ORDINARY_NUMER)+;

PONTUATION: '.' | ',' | '!' | '?' | ':' | ';' | '-' | '[' | ']' | '{' | '}' | '"' | '\'';

ACRONYM: [a-zA-Z][A-Z]+;

OWN_NAME: ([A-Z]WORD+)+;

// áóíéúãàêõçÁÓÍÉÚÃÀÊõÇ
WORD: [a-zA-ZáóíéúâÂêãàõôÔçÁÓÍÉÚÃÀÊÕÇ-]+;

MONEY: (('R$' | 'US$' | '€' | '£' | '¥') ' ' NUM);

NUM: (DIGIT(DIGIT)* | DIGIT','DIGIT | DIGIT'.'DIGIT | DIGIT'.'DIGIT','DIGIT | DIGIT','DIGIT'.'DIGIT);

DIGIT: [0-9]+;

CITATION: '"'(WORD+)'"';

DESCRIPTION: '('(WORD+)')';

PERCENT: NUM '%';

TWITTER_ACCOUNT: '@'WORD (NUM)*;

ORDINARY_NUMER: NUM 'º';

NEWLINE: [\r\n];

WS: (' '|'\t')+ -> skip;