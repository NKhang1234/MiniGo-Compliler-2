from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

class ASTGeneration(MiniGoVisitor):

    # program  : decl+ EOF ;
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.decl()])

    # --------------------------------------- Declare -----------------------------------------------

    # decl: structDecl | interfaceDecl | varDecl | constDecl | funcDecl | methodStructDecl;
    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))

    # typee: (INT | FLOAT | BOOLEAN | STRING | arrType | ID);
    def visitTypee(self,ctx:MiniGoParser.TypeeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.arrType():
            return self.visit(ctx.arrType())
        return Id(ctx.ID().getText())

    # arrType:  dimenList (INT | FLOAT | BOOLEAN | STRING | ID);
    def visitArrType(self,ctx:MiniGoParser.ArrTypeContext):
        eleType = None
        if ctx.INT():
            eleType = IntType()
        elif ctx.FLOAT():
            eleType = FloatType()
        elif ctx.BOOLEAN():
            eleType = BoolType()
        elif ctx.STRING():
            eleType = StringType()
        elif ctx.ID():
            eleType = Id(ctx.ID().getText())
        
        return ArrayType(self.visit(ctx.dimenList()), eleType)
    
    # dimenList: OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE dimenList |  (OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE);
    def visitDimenList(self,ctx:MiniGoParser.DimenListContext):
        if ctx.dimenList():
            if ctx.INT_LIT():
                numText = ctx.INT_LIT().getText()
                num = None
                if numText[:2] == '0b' or numText[:2] == '0B':
                    num = int(numText[2:], 2)
                elif numText[:2] == '0o' or numText[:2] == '0O':
                    num = int(numText[2:], 8)
                elif numText[:2] == '0x' or numText[:2] == '0X':
                    num = int(numText[2:], 16)
                else:
                    num = int(numText)
                return [IntLiteral(num)] + self.visit(ctx.dimenList())
            else:
                return [Id(ctx.ID().getText())] + self.visit(ctx.dimenList())
        else:
            if ctx.INT_LIT():
                numText = ctx.INT_LIT().getText()
                num = None
                if numText[:2] == '0b' or numText[:2] == '0B':
                    num = int(numText[2:], 2)
                elif numText[:2] == '0o' or numText[:2] == '0O':
                    num = int(numText[2:], 8)
                elif numText[:2] == '0x' or numText[:2] == '0X':
                    num = int(numText[2:], 16)   
                else:
                    num = int(numText)    
                return [IntLiteral(num)]
            else:
                return [Id(ctx.ID().getText())]

    # structDecl: TYPE ID STRUCT OPEN_CURVE bodyList CLOSE_CURVE SEMICOLON;
    def visitStructDecl(self,ctx:MiniGoParser.StructDeclContext):
        # fieldList = []
        # methodList = []
        # elementList = self.visit(ctx.bodyList())
        
        # for structEL in elementList:
        #     if isinstance(structEL, tuple):  # If the element is a Field, add it to the fields list
        #         fieldList.append(structEL)
        #     elif isinstance(structEL, MethodDecl):  # If the element is a Method, add it to the methods list
        #         methodList.append(structEL)

        return StructType(ctx.ID().getText(),self.visit(ctx.bodyList()), [])
    
    # bodyList: structEl bodyList | structEl;
    def visitBodyList(self,ctx:MiniGoParser.BodyListContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.structEl())] + self.visit(ctx.bodyList())
        else:
            return [self.visit(ctx.structEl())]

    # structEl: field
    def visitStructEl(self,ctx:MiniGoParser.StructElContext):
        return self.visit(ctx.field())

    # field: ID typee SEMICOLON;
    def visitField(self,ctx:MiniGoParser.FieldContext):
        return (ctx.ID().getText(),self.visit(ctx.typee())) # Tuple

    # interfaceDecl: TYPE ID INTERFACE OPEN_CURVE interfaceBody CLOSE_CURVE SEMICOLON;
    def visitInterfaceDecl(self,ctx:MiniGoParser.InterfaceDeclContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.interfaceBody()))
    
    # interfaceBody: listMethod;
    def visitInterfaceBody(self,ctx:MiniGoParser.InterfaceBodyContext):
        return self.visit(ctx.listMethod())

    # listMethod: method listMethod | method;
    def visitListMethod(self,ctx:MiniGoParser.ListMethodContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.method())] + self.visit(ctx.listMethod())
        else:
            return [self.visit(ctx.method())]

    # method: ID OPEN_ROUND paramList CLOSE_ROUND typee? SEMICOLON;
    def visitMethod(self,ctx:MiniGoParser.MethodContext):
        retType = self.visit(ctx.typee()) if ctx.typee() else VoidType()
        paramList = reduce(lambda prev, curr: prev + curr, self.visit(ctx.paramList()), [])
        return Prototype(ctx.ID().getText(), paramList, retType)

    # paramList: paramPrime | ;
    def visitParamList(self,ctx:MiniGoParser.ParamListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.paramPrime())
        return []
    
    # paramPrime: param COMMA paramPrime | param;
    def visitParamPrime(self,ctx:MiniGoParser.ParamPrimeContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.param())] + self.visit(ctx.paramPrime())
        return [self.visit(ctx.param())]
    
    # param: nameList typee;
    def visitParam(self,ctx:MiniGoParser.ParamContext):
        return [self.visit(ctx.typee()) for x in self.visit(ctx.nameList())]

    # nameList: ID COMMA nameList | ID;
    def visitNameList(self,ctx:MiniGoParser.NameListContext): 
        if ctx.getChildCount() == 3:
            return [ctx.ID().getText()] + self.visit(ctx.nameList())
        return [ctx.ID().getText()]
    
    # varDecl: VAR ID typee ASSIGN expr SEMICOLON
    #         | VAR ID ASSIGN expr SEMICOLON
    #         | VAR ID typee SEMICOLON;
    def visitVarDecl(self,ctx:MiniGoParser.VarDeclContext):
        if ctx.getChildCount() == 6:
            return VarDecl(ctx.ID().getText(), self.visit(ctx.typee()), self.visit(ctx.expr()))
        elif ctx.getChildCount() == 5:
            return VarDecl(ctx.ID().getText(), None, self.visit(ctx.expr()))
        return VarDecl(ctx.ID().getText(), self.visit(ctx.typee()), None)

    # constDecl: CONST ID ASSIGN expr SEMICOLON;
    def visitConstDecl(self,ctx:MiniGoParser.ConstDeclContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expr()))

    # literalConst: (INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL);
    def visitLiteralConst(self,ctx:MiniGoParser.LiteralConstContext):
        if ctx.INT_LIT():
            numText = ctx.INT_LIT().getText()
            num = None
            if numText[:2] == '0b' or numText[:2] == '0B':
                num = int(numText[2:], 2)
            elif numText[:2] == '0o' or numText[:2] == '0O':
                num = int(numText[2:], 8)
            elif numText[:2] == '0x' or numText[:2] == '0X':
                num = int(numText[2:], 16) 
            else:
                num = int(numText)      
            return IntLiteral(num)
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        return NilLiteral()

    # funcDecl: 'func' ID OPEN_ROUND funcParamList CLOSE_ROUND typee? OPEN_CURVE funcBody CLOSE_CURVE SEMICOLON;
    def visitFuncDecl(self,ctx:MiniGoParser.FuncDeclContext):
        retType = self.visit(ctx.typee()) if ctx.typee() else VoidType()
        paramList = reduce(lambda prev, curr : prev + curr, self.visit(ctx.funcParamList()), []) # Flatten [[Param1, Param2],[Param3, Param4]]
        return FuncDecl(ctx.ID().getText(), paramList, retType, self.visit(ctx.funcBody()))

    # funcParamList: funcParamPrime | ;
    def visitFuncParamList(self,ctx:MiniGoParser.FuncParamListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.funcParamPrime())
        return []
    
    # funcParamPrime: funcParam COMMA funcParamPrime | funcParam;
    def visitFuncParamPrime(self,ctx:MiniGoParser.FuncParamPrimeContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.funcParam())] + self.visit(ctx.funcParamPrime())
        return [self.visit(ctx.funcParam())]

    # funcParam: nameList typee;
    def visitFuncParam(self,ctx:MiniGoParser.FuncParamContext):
        name_list = self.visit(ctx.nameList())
        paramType = self.visit(ctx.typee())
        return [ParamDecl(x, paramType) for x in name_list] # Distribute

    # funcBody: statementList;
    def visitFuncBody(self,ctx:MiniGoParser.FuncBodyContext):
        return Block(self.visit(ctx.statementList()))
    	
    # methodStructDecl: 'func' OPEN_ROUND ID ID CLOSE_ROUND ID OPEN_ROUND funcParamList CLOSE_ROUND typee? OPEN_CURVE funcBody CLOSE_CURVE SEMICOLON; // The second 'ID' is 'struct' and 'interface'
    def visitMethodStructDecl(self,ctx:MiniGoParser.MethodStructDeclContext):
        retType = self.visit(ctx.typee()) if ctx.typee() else VoidType()
        paramList = reduce(lambda prev, curr : prev + curr, self.visit(ctx.funcParamList()), []) # Flatten [[Param1, Param2],[Param3, Param4]]
        func = FuncDecl(ctx.ID(2).getText(), paramList, retType, self.visit(ctx.funcBody()))
         
        return MethodDecl(ctx.ID(0).getText(), Id(ctx.ID(1).getText()), func)

    # --------------------------------------- Expression -----------------------------------------------

    # arrLit: arrLitDimenList (INT | FLOAT | BOOLEAN | STRING | ID) arrBody;
    def visitArrLit(self,ctx:MiniGoParser.ArrLitContext):
        eleType = None
        if ctx.INT():
            eleType = IntType()
        elif ctx.FLOAT():
            eleType = FloatType()
        elif ctx.BOOLEAN():
            eleType = BoolType()
        elif ctx.STRING():
            eleType = StringType()
        else:
            eleType = Id(ctx.ID().getText())
        return ArrayLiteral(self.visit(ctx.arrLitDimenList()), eleType, self.visit(ctx.arrBody()))

    # arrLitDimenList: OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE arrLitDimenList |  OPEN_SQUARE (INT_LIT | ID) CLOSE_SQUARE;
    def visitArrLitDimenList(self,ctx:MiniGoParser.ArrLitDimenListContext): 
        if ctx.getChildCount() == 4:
            if ctx.INT_LIT():
                numText = ctx.INT_LIT().getText()
                num = None
                if numText[:2] == '0b' or numText[:2] == '0B':
                    num = int(numText[2:], 2)
                elif numText[:2] == '0o' or numText[:2] == '0O':
                    num = int(numText[2:], 8)
                elif numText[:2] == '0x' or numText[:2] == '0X':
                    num = int(numText[2:], 16) 
                else:
                    num = int(numText) 
                return [IntLiteral(num)] + self.visit(ctx.arrLitDimenList())
            else:
                return [Id(ctx.ID().getText())] + self.visit(ctx.arrLitDimenList())
        else: 
            if ctx.INT_LIT():
                numText = ctx.INT_LIT().getText()
                num = None
                if numText[:2] == '0b' or numText[:2] == '0B':
                    num = int(numText[2:], 2)
                elif numText[:2] == '0o' or numText[:2] == '0O':
                    num = int(numText[2:], 8)
                elif numText[:2] == '0x' or numText[:2] == '0X':
                    num = int(numText[2:], 16) 
                else:
                    num = int(numText)
                return [IntLiteral(num)]
            else:
                return [Id(ctx.ID().getText())]
            
    
    # arrBody: OPEN_CURVE elementList CLOSE_CURVE;
    def visitArrBody(self,ctx:MiniGoParser.ArrBodyContext): 
        return self.visit(ctx.elementList())

    # elementList: element COMMA elementList | element;
    def visitElementList(self,ctx:MiniGoParser.ElementListContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.element())] + self.visit(ctx.elementList())
        return [self.visit(ctx.element())]

    # element: literalConst | structLit | arrBody | ID;
    def visitElement(self,ctx:MiniGoParser.ElementContext):
        return self.visit(ctx.getChild(0))

    # structLit: ID OPEN_CURVE structElList CLOSE_CURVE;
    def visitStructLit(self,ctx:MiniGoParser.StructLitContext):
        return StructLiteral(ctx.ID().getText(), self.visit(ctx.structElList()))

    # structElList: structELPrime | ;
    def visitStructElList(self,ctx:MiniGoParser.StructElListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.structELPrime())
        return []

    # structELPrime: structEL COMMA structELPrime | structEL;
    def visitStructELPrime(self,ctx:MiniGoParser.StructELPrimeContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.structEL())] + self.visit(ctx.structELPrime())
        return [self.visit(ctx.structEL())]

    # structEL:ID COLON expr;
    def visitStructEL(self,ctx:MiniGoParser.StructELContext): 
        return (ctx.ID().getText(), self.visit(ctx.expr()))

    # funcCall: ID OPEN_ROUND argumentList CLOSE_ROUND;
    def visitFuncCall(self,ctx:MiniGoParser.FuncCallContext): 
        return FuncCall(ctx.ID().getText(), self.visit(ctx.argumentList()))

    # argumentList: argumentListPrime | ;
    def visitArgumentList(self,ctx:MiniGoParser.ArgumentListContext): 
        if ctx.getChildCount() == 1:
            return self.visit(ctx.argumentListPrime())
        return []
    
    # argumentListPrime: argument COMMA argumentListPrime | argument;
    def visitArgumentListPrime(self,ctx:MiniGoParser.ArgumentListPrimeContext): 
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.argument())] + self.visit(ctx.argumentListPrime())
        return [self.visit(ctx.argument())]

    # argument: expr;
    def visitArgument(self,ctx:MiniGoParser.ArgumentContext): 
        return self.visit(ctx.expr())
    
    # expr: expr OR expr1 | expr1;
    def visitExpr(self,ctx:MiniGoParser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr()), self.visit(ctx.expr1()))
        return self.visit(ctx.expr1())

    # expr1: expr1 AND expr2 | expr2;
    def visitExpr1(self,ctx:MiniGoParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr1()), self.visit(ctx.expr2()))
        return self.visit(ctx.expr2())

    # expr2: expr2 (EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL) expr3 | expr3;
    def visitExpr2(self,ctx:MiniGoParser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())

    # expr3: expr3 (PLUS | MINUS) expr4 | expr4;
    def visitExpr3(self,ctx:MiniGoParser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())

    # expr4: expr4 (MULTI | DIV | MODULO) expr5 | expr5;
    def visitExpr4(self,ctx:MiniGoParser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())

    # expr5: (NOT | MINUS) expr5 | expr6;
    def visitExpr5(self,ctx:MiniGoParser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())

    # expr6: expr6 indexList | expr6 DOT ID | expr6 DOT ID OPEN_ROUND argumentList CLOSE_ROUND | expr7;
    def visitExpr6(self,ctx:MiniGoParser.Expr6Context):
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.expr6()), self.visit(ctx.indexList()))
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.expr6()), ctx.ID().getText())
        elif ctx.getChildCount() == 6:
            return MethCall(self.visit(ctx.expr6()), ctx.ID().getText(), self.visit(ctx.argumentList()))
        return self.visit(ctx.expr7())

    # expr7: OPEN_ROUND expr CLOSE_ROUND | operand;
    def visitExpr7(self,ctx:MiniGoParser.Expr7Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        return self.visit(ctx.operand())
        
    # operand: literal | funcCall | ID;
    def visitOperand(self,ctx:MiniGoParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))

    # literal: literalConst | arrLit | structLit;
    def visitLiteral(self,ctx:MiniGoParser.LiteralContext): 
        return self.visit(ctx.getChild(0))

    # indexList: OPEN_SQUARE expr CLOSE_SQUARE indexList | OPEN_SQUARE expr CLOSE_SQUARE;
    def visitIndexList(self,ctx:MiniGoParser.IndexListContext): 
        if ctx.getChildCount() == 4:
            return [self.visit(ctx.expr())] + self.visit(ctx.indexList())
        return [self.visit(ctx.expr())]

    # --------------------------------------- Statement -----------------------------------------------

    # statementList: statementListPrime | ;
    def visitStatementList(self,ctx:MiniGoParser.StatementListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.statementListPrime())
        return []

    # statementListPrime: statement statementListPrime | statement;
    def visitStatementListPrime(self,ctx:MiniGoParser.StatementListPrimeContext): 
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.statement())] + self.visit(ctx.statementListPrime())
        return [self.visit(ctx.statement())]

    # statement: varDecl | constDecl | assignment | ifStatement | forStatement | breakStatement | continueStatement | callStatement | returnStatement;
    def visitStatement(self,ctx:MiniGoParser.StatementContext): 
        return self.visit(ctx.getChild(0))

    # assignment: lhs (ASSIGN1 | PLUS_EQUAL| MINUS_EQUAL | MULTI_EQUAL | DIV_EQUAL | MODULO_EQUAL) rhs SEMICOLON;
    def visitAssignment(self,ctx:MiniGoParser.AssignmentContext): 
        if ctx.ASSIGN1():
            return Assign(self.visit(ctx.lhs()), self.visit(ctx.rhs()))
        elif ctx.PLUS_EQUAL():
            return Assign(self.visit(ctx.lhs()), BinaryOp('+', self.visit(ctx.lhs()), self.visit(ctx.rhs())))
        elif ctx.MINUS_EQUAL():
            return Assign(self.visit(ctx.lhs()), BinaryOp('-', self.visit(ctx.lhs()), self.visit(ctx.rhs())))
        elif ctx.MULTI_EQUAL():
            return Assign(self.visit(ctx.lhs()), BinaryOp('*', self.visit(ctx.lhs()), self.visit(ctx.rhs())))
        elif ctx.DIV_EQUAL():
            return Assign(self.visit(ctx.lhs()), BinaryOp('/', self.visit(ctx.lhs()), self.visit(ctx.rhs())))
        elif ctx.MODULO_EQUAL():
            return Assign(self.visit(ctx.lhs()), BinaryOp('%', self.visit(ctx.lhs()), self.visit(ctx.rhs())))

    # lhs: lhs indexList | lhs DOT ID | ID | exprLhs;
    def visitLhs(self,ctx:MiniGoParser.LhsContext): 
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.lhs()), self.visit(ctx.indexList()))
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.lhs()), ctx.ID().getText())
        elif ctx.exprLhs():
            return self.visit(ctx.exprLhs())
        return Id(ctx.ID().getText())

    # exprLhs: OPEN_ROUND expr CLOSE_ROUND | operand;
    def visitExprLhs(self,ctx:MiniGoParser.ExprLhsContext): 
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        return self.visit(ctx.operand())

    # rhs: expr;
    def visitRhs(self,ctx:MiniGoParser.RhsContext): 
        return self.visit(ctx.expr())

    # ifStatement: iff SEMICOLON;
    def visitIfStatement(self,ctx:MiniGoParser.IfStatementContext): 
        return self.visit(ctx.iff())

    # iff: IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE elseIf;
    def visitIff(self,ctx:MiniGoParser.IffContext): 
        return If(self.visit(ctx.expr()), Block(self.visit(ctx.statementList())), self.visit(ctx.elseIf()))

    # elseIf: ELSE IF OPEN_ROUND expr CLOSE_ROUND OPEN_CURVE statementList CLOSE_CURVE elseIf 
    #     | ELSE OPEN_CURVE statementList CLOSE_CURVE 
    #     | ;
    def visitElseIf(self,ctx:MiniGoParser.ElseIfContext): 
        if ctx.expr():
            return If(self.visit(ctx.expr()), Block(self.visit(ctx.statementList())), self.visit(ctx.elseIf()))
        elif ctx.getChildCount() == 4:
            return Block(self.visit(ctx.statementList()))
        return None

    # forStatement: forBasic | forInitial | forRange;
    def visitForStatement(self,ctx:MiniGoParser.ForStatementContext): 
        return self.visit(ctx.getChild(0))

    # forBasic: FOR expr OPEN_CURVE statementList CLOSE_CURVE SEMICOLON;
    def visitForBasic(self,ctx:MiniGoParser.ForBasicContext): 
        return ForBasic(self.visit(ctx.expr()), Block(self.visit(ctx.statementList())))

# class ForStep(Stmt):
#     init:Stmt -> Warning in using VarDecl class as it not inherited from Stmt
#     cond:Expr
#     upda:Assign
#     loop:Block


    # forInitial: FOR initialization SEMICOLON condition SEMICOLON update OPEN_CURVE statementList CLOSE_CURVE SEMICOLON;
    def visitForInitial(self,ctx:MiniGoParser.ForInitialContext):
        return ForStep(self.visit(ctx.initialization()), self.visit(ctx.condition()), self.visit(ctx.update()), Block(self.visit(ctx.statementList())))

    # initialization: assignScalar | varDeclInitial;
    def visitInitialization(self,ctx:MiniGoParser.InitializationContext):
        return self.visit(ctx.getChild(0))

    # varDeclInitial: VAR ID typee? ASSIGN expr;  Warning
    def visitVarDeclInitial(self,ctx:MiniGoParser.VarDeclInitialContext):
        varType = self.visit(ctx.typee()) if ctx.typee() else None
        return VarDecl(ctx.ID().getText(), varType, self.visit(ctx.expr()))

    # condition: expr;
    def visitCondition(self,ctx:MiniGoParser.ConditionContext):
        return self.visit(ctx.expr())

    # update: assignScalar;
    def visitUpdate(self,ctx:MiniGoParser.UpdateContext):
        return self.visit(ctx.assignScalar())

    # assignScalar: ID (ASSIGN1 | PLUS_EQUAL| MINUS_EQUAL | MULTI_EQUAL | DIV_EQUAL | MODULO_EQUAL) expr;
    def visitAssignScalar(self,ctx:MiniGoParser.AssignScalarContext):
        lhs = Id(ctx.ID().getText())
        if ctx.ASSIGN1():
            return Assign(lhs, self.visit(ctx.expr()))
        elif ctx.PLUS_EQUAL():
            return Assign(lhs, BinaryOp('+', lhs, self.visit(ctx.expr())))
        elif ctx.MINUS_EQUAL():
            return Assign(lhs, BinaryOp('-', lhs, self.visit(ctx.expr())))
        elif ctx.MULTI_EQUAL():
            return Assign(lhs, BinaryOp('*', lhs, self.visit(ctx.expr())))
        elif ctx.DIV_EQUAL():
            return Assign(lhs, BinaryOp('/', lhs, self.visit(ctx.expr())))
        elif ctx.MODULO_EQUAL():
            return Assign(lhs, BinaryOp('%', lhs, self.visit(ctx.expr())))

    # forRange: FOR (ID | UNDERSCORE) COMMA ID ASSIGN1 RANGE expr OPEN_CURVE statementList CLOSE_CURVE SEMICOLON;
    def visitForRange(self,ctx:MiniGoParser.ForRangeContext):
        idx = Id(ctx.getChild(1).getText())
        value = Id(ctx.getChild(3).getText())
        arr = self.visit(ctx.expr())
        loop = Block(self.visit(ctx.statementList()))
        return ForEach(idx, value, arr, loop)

    # breakStatement: BREAK SEMICOLON;
    def visitBreakStatement(self,ctx:MiniGoParser.BreakStatementContext):
        return Break()

    # continueStatement: CONTINUE SEMICOLON;
    def visitContinueStatement(self,ctx:MiniGoParser.ContinueStatementContext):
        return Continue()

    # callStatement: (funcCall | expr6 DOT ID OPEN_ROUND argumentList CLOSE_ROUND) SEMICOLON;
    def visitCallStatement(self,ctx:MiniGoParser.CallStatementContext):
        if ctx.funcCall():
            return self.visit(ctx.funcCall())
        return MethCall(self.visit(ctx.expr6()), ctx.ID().getText(), self.visit(ctx.argumentList()))

    # returnStatement: RETURN expr? SEMICOLON;
    def visitReturnStatement(self,ctx:MiniGoParser.ReturnStatementContext):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)