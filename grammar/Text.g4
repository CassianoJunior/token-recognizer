grammar Text;

text: (paragraph NEWLINE)+;

paragraph: ((WORD | PONTUATION)+ | DIGIT)+;

PONTUATION: '.' | ',' | '!' | '?' | ':' | ';' | '-' | '(' | ')' | '[' | ']' | '{' | '}' | '"' | '\'';

OWN_NAME: ([A-Z]WORD+)+;

// áóíéúãàêõçÁÓÍÉÚÃÀÊõÇ
WORD: [a-zA-ZáóíéúâÂêãàõôÔçÁÓÍÉÚÃÀÊÕÇ-]+;

MONEY: (('R$' | 'U$' | '€' | '£' | '¥')NUM);

NUM: (DIGIT | DIGIT','DIGIT | DIGIT'.'DIGIT | DIGIT'.'DIGIT','DIGIT | DIGIT','DIGIT'.'DIGIT);

DIGIT: [0-9]+;

CITATION: '"'WORD+'"';

DESCRIPTION: '('WORD+')' | '(' WORD+ ')';

NEWLINE: [\r\n];

WS: (' '|'\t')+ -> skip;