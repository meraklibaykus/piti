grammar Math;

// define the parser rules for mathematical expressions
expression
    : expression ('+'|'-') term
    | term
    ;

term
    : term ('*'|'/') factor
    | factor
    ;

factor
    : power
    | '-' factor
    ;

power
    : atom ('^' factor)?
    ;

atom
    : NUMBER
    | '(' expression ')'
    ;

// define the lexer rules for the math language
NUMBER : ('0'..'9')+('.'('0'..'9')+)?;
WS : [ \t\r\n]+ -> skip;
