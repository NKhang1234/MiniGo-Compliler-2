grammar MiniGo;

// 2211460
@lexer::header { 
from lexererr import *
}

@lexer::members {
_prev_token_type = 0
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        token = super().emit();
        self._prev_token_type = token.type;
        return token;
}

options{
	language=Python3;
}

program  : decl+ EOF ;

// -------------------------------------- Parser -----------------------------------------------------------------------

// ---------------------------- Declare ---------------------------------------- //
decl: structDecl | interfaceDecl | varDecl | constDecl | funcDecl | methodStructDecl;

// Type
typee: (INT | FLOAT | BOOLEAN | STRING | arrType | ID); // ID is notified for 'struct' or 'interface'
arrType:  dimenList (INT | FLOAT | BOOLEAN | STRING | ID); // ID is notified for 'struct' or 'interface'
dimenList: OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE dimenList |  (OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE); // ID is notified for 'constant'

// Struct Declare
structDecl: TYPE ID STRUCT OPEN_CURVE structBody CLOSE_CURVE SEMICOLON;
structBody: listField;
listField: field listField | field;
field: ID typee SEMICOLON;

// Interface Declare
interfaceDecl: TYPE ID INTERFACE OPEN_CURVE interfaceBody CLOSE_CURVE SEMICOLON;
interfaceBody: listMethod;

listMethod: method listMethod | method;
method: ID OPEN_ROUND paramList CLOSE_ROUND typee? SEMICOLON;

paramList: paramPrime | ;
paramPrime: param COMMA paramPrime | param;
param: nameList typee;

nameList: ID COMMA nameList | ID;

// Variable Declare
varDecl: VAR ID (typee ASSIGN expr | ASSIGN expr | typee) SEMICOLON;

// Constant Declare
constDecl: CONST ID ASSIGN (literalConst | expr) SEMICOLON;
literalConst: (INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL);

// Function Declare
funcDecl: 'func' ID OPEN_ROUND paramList CLOSE_ROUND typee? OPEN_CURVE funcBody CLOSE_CURVE SEMICOLON;
funcBody: statementList;

// Method for Struct Declare
methodStructDecl: 'func' OPEN_ROUND ID ID CLOSE_ROUND ID OPEN_ROUND paramList CLOSE_ROUND typee? OPEN_CURVE funcBody CLOSE_CURVE SEMICOLON; // The second 'ID' is 'struct' and 'interface'

// ---------------------------- Expression ---------------------------------------- //

/* // Array Accessing Element
arrAccess: exprA positionList;
positionList: OPEN_SQUARE expr CLOSE_SQUARE positionList | OPEN_SQUARE expr CLOSE_SQUARE; // Array Accessing Element can be described at expr6

exprA: exprA OR exprA1 | exprA1;
exprA1: exprA1 AND exprA2 | exprA2;
exprA2: exprA2 (EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL) exprA3 | exprA3;
exprA3: exprA3 (PLUS | MINUS) exprA4 | exprA4;
exprA4: exprA4 (MULTI | DIV | MODULO) exprA5 | exprA5;
exprA5: ('!' | '-') exprA5 | exprA6;
exprA6: OPEN_ROUND exprA CLOSE_ROUND | operandA;
operandA: ID (OPEN_CURVE structElList CLOSE_CURVE | ) | literal | funcCall | ID; */

/* // Struct Field Accessing
structAccess: refList DOT ID; // Struct Field Accessing can be described at expr6 
refList: refList DOT exprS | exprS;

exprS: exprS OR exprS1 | exprS1;
exprS1: exprS1 AND exprS2 | exprS2;
exprS2: exprS2 (EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL) exprS3 | exprS3;
exprS3: exprS3 (PLUS | MINUS) exprS4 | exprS4;
exprS4: exprS4 (MULTI | DIV | MODULO) exprS5 | exprS5;
exprS5: ('!' | '-') exprS5 | exprS6;
exprS6: OPEN_ROUND exprS CLOSE_ROUND | operandS;
operandS: literal | arrAccess | funcCall | ID (OPEN_CURVE structElList CLOSE_CURVE | ) | ID; */


/* // Array and Struct Access Composite
arrStructAccess: arrStructAccess accessList | accessList | arrAccess;
accessList: positionList | structAccess; */

// Array Literal
arrLit: arrType arrBody;
arrBody: OPEN_CURVE elementList CLOSE_CURVE;
elementList: element COMMA elementList | element;
element: literalConst | structLit | arrBody;
// Struct Literal
structLit: ID OPEN_CURVE structElList CLOSE_CURVE;
structElList: structELPrime | ;
structELPrime: structEL COMMA structELPrime | structEL;
structEL:ID COLON expr;

// Function call
funcCall: ID OPEN_ROUND argumentList CLOSE_ROUND;
argumentList: argumentListPrime | ;
argumentListPrime: argument COMMA argumentListPrime | argument;
argument: expr | arrBody;

/* // Method Call
methodCall: exprM DOT ID OPEN_ROUND argumentList CLOSE_ROUND; // Method Call is a func call with DOT => Can be described in expr6
exprM: exprM OR exprM1 | exprM1;
exprM1: exprM1 AND exprM2 | exprM2;
exprM2: exprM2 (EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL) exprM3 | exprM3;
exprM3: exprM3 (PLUS | MINUS) exprM4 | exprM4;
exprM4: exprM4 (MULTI | DIV | MODULO) exprM5 | exprM5;
exprM5: ('!' | '-') exprM5 | exprM6;
exprM6: OPEN_ROUND exprM CLOSE_ROUND | operandM;
operandM: literal | arrStructAccess | ID; */

// Expression
expr: expr OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2;
expr2: expr2 (EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MULTI | DIV | MODULO) expr5 | expr5;
expr5: ('!' | '-') expr5 | expr6;
expr6: expr6 OPEN_SQUARE expr CLOSE_SQUARE| expr6 DOT ID | expr6 DOT funcCall| expr7;// access array | struct access | method call
expr7: OPEN_ROUND expr CLOSE_ROUND | operand;
operand: literal | funcCall | ID;

literal: literalConst | arrLit | structLit;

// ---------------------------- Statement ---------------------------------------- //
statement: (varDeclStatement | constDeclStatement | assignment | ifStatement | forStatement | breakStatement | continueStatement | callStatement | returnStatement) SEMICOLON;
statementList: statement statementList | statement;

// Variable and Constant Declaration
varDeclStatement: VAR ID (typee ASSIGN expr | ASSIGN expr | typee);
constDeclStatement: CONST ID ASSIGN (literalConst | expr);

// Assignemt Statement
assignment: lhs assignOperator rhs;
lhs: lhs OPEN_SQUARE expr CLOSE_SQUARE| lhs DOT ID | ID;
assignOperator: ASSIGN1 | PLUS_EQUAL| MINUS_EQUAL | MULTI_EQUAL | DIV_EQUAL | MODULO_EQUAL;
rhs: expr;

// If Statement
ifStatement: IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE elifList (ELSE OPEN_CURVE statementList CLOSE_CURVE)?;

elifList: eliff elifList | ;
eliff: ELSE IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE;

// For Statememt
forStatement: forBasic | forInitial | forRange;

forBasic: FOR expr OPEN_CURVE statementList CLOSE_CURVE;

forInitial: FOR initialization SEMICOLON condition SEMICOLON update OPEN_CURVE statementList CLOSE_CURVE;
initialization: assignScalar | varDeclInitial;
varDeclInitial: VAR ID typee? ASSIGN expr;
condition: expr;
update: assignScalar;
assignScalar: ID assignOperator expr;

forRange: FOR (ID | '_') COMMA ID ASSIGN1 RANGE expr OPEN_CURVE statementList CLOSE_CURVE;

// Break Statememt
breakStatement: BREAK;

// Continue Statement
continueStatement: CONTINUE;

// Function and Method Call Statement
callStatement: funcCall | expr DOT funcCall;

// Return Statement
returnStatement: RETURN expr?;

// -------------------------------------- End Parser -----------------------------------------------------------------------

// -------------------------------------- Lexical ---------------------------------------------
// Keyword
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// Operator
PLUS: '+';
MINUS: '-';
MULTI: '*';
DIV: '/';
MODULO: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
LESS_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ASSIGN1: ':=';
PLUS_EQUAL: '+=';
MINUS_EQUAL: '-=';
MULTI_EQUAL: '*=';
DIV_EQUAL: '/=';
MODULO_EQUAL: '%=';
DOT: '.';
COLON: ':';

// Separator
OPEN_ROUND: '(';
CLOSE_ROUND: ')';
OPEN_CURVE: '{';
CLOSE_CURVE: '}';
OPEN_SQUARE: '[';
CLOSE_SQUARE: ']';
COMMA: ',';
SEMICOLON: ';';

// Identifier
fragment Letter: [a-zA-Z];
fragment Digit: [0-9];

ID: (Letter | '_') (Letter | Digit | '_')*;

// Literal
//-------- Integer Literals
INT_LIT: (Decimal | Binary | Octal | Hex) 
// {
//     if self.text[:2] == '0b' or self.text[:2] == '0B':
//         self.text = str(int(self.text[2:], 2))
//     elif self.text[:2] == '0o' or self.text[:2] == '0O':
//         self.text = str(int(self.text[2:], 8))
//     elif self.text[:2] == '0x' or self.text[:2] == '0X':
//         self.text = str(int(self.text[2:], 16))
// }
;
fragment Decimal: '0' | ([1-9] Digit*);
fragment Binary: '0' [bB] [0-1]+;
fragment Octal: '0' [oO] [0-7]+;
fragment Hex: '0' [xX] [0-9a-fA-F]+;

//-------- Floating-point Literals
FLOAT_LIT: No_exponent | Exponent;
fragment No_exponent: Digit+ '.' Digit*;
fragment Exponent: Digit+ '.' Digit* [eE] ('+'|'-')? Digit+;

//-------- String Literals
STRING_LIT: '"' (String_Character|String_Escape)* '"'
// {
//     self.text = self.text[1:-1]
//     # print(f"string lit: {self.text}")
// }
;
fragment String_Character: ~["\\\n];
fragment String_Escape:  '\\n' | '\\t' | '\\r' | '\\"'| '\\\\';

//-------- Boolean and NIL Literals
// Boolean Literal and NIL Literals have have value true/false and nil as keyword defined previously

//-------- Comment
COMMENT_INLINE: '//' (~[\n])* ('\n' | EOF) -> skip;
COMMENT_BLOCK: '/*' (~[*/] | COMMENT_BLOCK)* '*/' -> skip;
// COMMENT_BLOCK: '/*' (COMMENT_BLOCK | .)*? '*/' -> skip;

NL: '\n'
{
    # print(f"prev_token: {self._prev_token_type}")
    if(self._prev_token_type in {self.ID,self.INT_LIT, self.FLOAT_LIT, self.TRUE, self.FALSE, self.STRING_LIT, self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.RETURN, self.CONTINUE, self.BREAK, self.CLOSE_ROUND, self.CLOSE_CURVE, self.CLOSE_SQUARE}):
        # print(f"Im in, before me: {self._prev_token_type}")
        # self.emitToken(self.commonToken(self.SEMICOLON, ';'))
        self.text = ';'  
        self.type = self.SEMICOLON
    else:
        self.skip()
}
;

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs 

fragment ILL_ESC: '\\' ~[ntr"\\];

ILLEGAL_ESCAPE: '"' (String_Character|String_Escape)* ILL_ESC;
UNCLOSE_STRING: '"' (String_Character|String_Escape)* ('\n' | '\r\n'| EOF) 
{
    if(len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
        self.text = self.text[:-2]
    elif(self.text[-1] == '\n'):
        self.text = self.text[:-1]
    else:
        self.text = self.text
}
;
ERROR_CHAR: .;

// -------------------------------------- End Lexical ---------------------------------------------