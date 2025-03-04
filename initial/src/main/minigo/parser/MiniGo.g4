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

program  : decl+ EOF ; //DONE

// -------------------------------------- Parser -----------------------------------------------------------------------

// ---------------------------- Declare ---------------------------------------- //
decl: structDecl | interfaceDecl | varDecl | constDecl | funcDecl | methodStructDecl; //DONE

// Type
typee: (INT | FLOAT | BOOLEAN | STRING | arrType | ID); // ID is notified for 'struct' or 'interface' //DONE
arrType:  dimenList (INT | FLOAT | BOOLEAN | STRING | ID); // ID is notified for 'struct' or 'interface' //DONE
dimenList: OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE dimenList |  (OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE); // ID is notified for 'constant' //DONE

// Struct Declare
structDecl: TYPE ID STRUCT OPEN_CURVE bodyList CLOSE_CURVE SEMICOLON; //DONE
bodyList: structEl bodyList | structEl; //DONE
structEl: field; //DONE
field: ID typee SEMICOLON; //DONE

// Interface Declare
interfaceDecl: TYPE ID INTERFACE OPEN_CURVE interfaceBody CLOSE_CURVE SEMICOLON;//DONE
interfaceBody: listMethod;//DONE

listMethod: method listMethod | method;//DONE
method: ID OPEN_ROUND paramList CLOSE_ROUND typee? SEMICOLON;//DONE

paramList: paramPrime | ;//DONE 
paramPrime: param COMMA paramPrime | param; //DONE
param: nameList typee; //DONE

nameList: ID COMMA nameList | ID; //DONE

// Variable Declare
// varDecl: VAR ID (typee ASSIGN expr | ASSIGN expr | typee) SEMICOLON;
varDecl: VAR ID typee ASSIGN expr SEMICOLON //DONE
        | VAR ID ASSIGN expr SEMICOLON
        | VAR ID typee SEMICOLON;

// Constant Declare
constDecl: CONST ID ASSIGN expr SEMICOLON;//DONE
literalConst: (INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL);//DONE

// Function Declare
funcDecl: 'func' ID OPEN_ROUND funcParamList CLOSE_ROUND typee? OPEN_CURVE funcBody CLOSE_CURVE SEMICOLON;
funcParamList: funcParamPrime | ;//DONE 
funcParamPrime: funcParam COMMA funcParamPrime | funcParam; //DONE
funcParam: nameList typee; //DONE

funcBody: statementList; //DONE

// Method for Struct Declare
methodStructDecl: 'func' OPEN_ROUND ID ID CLOSE_ROUND ID OPEN_ROUND funcParamList CLOSE_ROUND typee? OPEN_CURVE funcBody CLOSE_CURVE SEMICOLON; // The second 'ID' is 'struct' and 'interface'
//DONE
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
arrLit: arrLitDimenList (INT | FLOAT | BOOLEAN | STRING | ID) arrBody;//DONE

arrLitDimenList: OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE arrLitDimenList |  OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE;//DONE

arrBody: OPEN_CURVE elementList CLOSE_CURVE;//DONE

elementList: element COMMA elementList | element;//DONE
element: literalConst | structLit | arrBody | ID;//DONE
// Struct Literal
structLit: ID OPEN_CURVE structElList CLOSE_CURVE;//DONE
structElList: structELPrime | ;//DONE
structELPrime: structEL COMMA structELPrime | structEL;//DONE
structEL:ID COLON expr;//DONE

// Function call
funcCall: ID OPEN_ROUND argumentList CLOSE_ROUND;//DONE
argumentList: argumentListPrime | ;//DONE
argumentListPrime: argument COMMA argumentListPrime | argument;//DONE
argument: expr;//DONE

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
expr: expr OR expr1 | expr1;//DONE
expr1: expr1 AND expr2 | expr2;//DONE
expr2: expr2 (EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL) expr3 | expr3;//DONE
expr3: expr3 (PLUS | MINUS) expr4 | expr4;//DONE
expr4: expr4 (MULTI | DIV | MODULO) expr5 | expr5;//DONE
expr5: (NOT | MINUS) expr5 | expr6;//DONE
expr6: expr6 indexList | expr6 DOT ID | expr6 DOT ID OPEN_ROUND argumentList CLOSE_ROUND | expr7;// access array | struct access | method call //DONE
expr7: OPEN_ROUND expr CLOSE_ROUND | operand;//DONE
operand: literal | funcCall | ID;//DONE

literal: literalConst | arrLit | structLit;//DONE
indexList: OPEN_SQUARE expr CLOSE_SQUARE indexList | OPEN_SQUARE expr CLOSE_SQUARE;//DONE

// ---------------------------- Statement ---------------------------------------- //
statementList: statementListPrime | ;
statementListPrime: statement statementListPrime | statement;//DONE
statement: varDecl | constDecl | assignment | ifStatement | forStatement | breakStatement | continueStatement | callStatement | returnStatement;//DONE

/* // Variable and Constant Declaration
varDeclStatement: VAR ID (typee ASSIGN expr | ASSIGN expr | typee);
constDeclStatement: CONST ID ASSIGN (literalConst | expr); */

// Assignemt Statement
assignment: lhs (ASSIGN1 | PLUS_EQUAL| MINUS_EQUAL | MULTI_EQUAL | DIV_EQUAL | MODULO_EQUAL) rhs SEMICOLON;//DONE
lhs: lhs indexList | lhs DOT ID | ID | exprLhs;//DONE
exprLhs: OPEN_ROUND expr CLOSE_ROUND | operand;//DONE
rhs: expr;//DONE

// If Statement

// ifStatement: IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE elifList (ELSE OPEN_CURVE statementList CLOSE_CURVE)? SEMICOLON;

// elifList: eliff elifList | ;
// eliff: ELSE IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE;

ifStatement: iff SEMICOLON;
iff: IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE elseIf;
elseIf: ELSE IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE elseIf 
        | ELSE OPEN_CURVE statementList CLOSE_CURVE 
        | ;

// For Statememt
forStatement: forBasic | forInitial | forRange;//DONE

forBasic: FOR expr OPEN_CURVE statementList CLOSE_CURVE SEMICOLON;//DONE

forInitial: FOR initialization SEMICOLON condition SEMICOLON update OPEN_CURVE statementList CLOSE_CURVE SEMICOLON;//DONE
initialization: assignScalar | varDeclInitial;//DONE
varDeclInitial: VAR ID typee? ASSIGN expr;//DONE
condition: expr;//DONE
update: assignScalar;//DONE
assignScalar: ID (ASSIGN1 | PLUS_EQUAL| MINUS_EQUAL | MULTI_EQUAL | DIV_EQUAL | MODULO_EQUAL) expr;//DONE

forRange: FOR (ID | UNDERSCORE) COMMA ID ASSIGN1 RANGE expr OPEN_CURVE statementList CLOSE_CURVE SEMICOLON;//DONE

// Break Statememt
breakStatement: BREAK SEMICOLON;//DONE

// Continue Statement
continueStatement: CONTINUE SEMICOLON;//DONE

// Function and Method Call Statement
callStatement: (funcCall | expr6 DOT ID OPEN_ROUND argumentList CLOSE_ROUND) SEMICOLON;//DONE

// Return Statement
returnStatement: RETURN expr? SEMICOLON;//DONE

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
UNDERSCORE: '_';

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