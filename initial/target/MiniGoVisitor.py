# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typee.
    def visitTypee(self, ctx:MiniGoParser.TypeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrType.
    def visitArrType(self, ctx:MiniGoParser.ArrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimenList.
    def visitDimenList(self, ctx:MiniGoParser.DimenListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDecl.
    def visitStructDecl(self, ctx:MiniGoParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#bodyList.
    def visitBodyList(self, ctx:MiniGoParser.BodyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structEl.
    def visitStructEl(self, ctx:MiniGoParser.StructElContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDecl.
    def visitInterfaceDecl(self, ctx:MiniGoParser.InterfaceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceBody.
    def visitInterfaceBody(self, ctx:MiniGoParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#listMethod.
    def visitListMethod(self, ctx:MiniGoParser.ListMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramList.
    def visitParamList(self, ctx:MiniGoParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramPrime.
    def visitParamPrime(self, ctx:MiniGoParser.ParamPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nameList.
    def visitNameList(self, ctx:MiniGoParser.NameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDecl.
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDecl.
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literalConst.
    def visitLiteralConst(self, ctx:MiniGoParser.LiteralConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParamList.
    def visitFuncParamList(self, ctx:MiniGoParser.FuncParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParamPrime.
    def visitFuncParamPrime(self, ctx:MiniGoParser.FuncParamPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParam.
    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcBody.
    def visitFuncBody(self, ctx:MiniGoParser.FuncBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodStructDecl.
    def visitMethodStructDecl(self, ctx:MiniGoParser.MethodStructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrLit.
    def visitArrLit(self, ctx:MiniGoParser.ArrLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrLitDimenList.
    def visitArrLitDimenList(self, ctx:MiniGoParser.ArrLitDimenListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrBody.
    def visitArrBody(self, ctx:MiniGoParser.ArrBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elementList.
    def visitElementList(self, ctx:MiniGoParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structElList.
    def visitStructElList(self, ctx:MiniGoParser.StructElListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structELPrime.
    def visitStructELPrime(self, ctx:MiniGoParser.StructELPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structEL.
    def visitStructEL(self, ctx:MiniGoParser.StructELContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcCall.
    def visitFuncCall(self, ctx:MiniGoParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argumentList.
    def visitArgumentList(self, ctx:MiniGoParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argumentListPrime.
    def visitArgumentListPrime(self, ctx:MiniGoParser.ArgumentListPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argument.
    def visitArgument(self, ctx:MiniGoParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#indexList.
    def visitIndexList(self, ctx:MiniGoParser.IndexListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementList.
    def visitStatementList(self, ctx:MiniGoParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementListPrime.
    def visitStatementListPrime(self, ctx:MiniGoParser.StatementListPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprLhs.
    def visitExprLhs(self, ctx:MiniGoParser.ExprLhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rhs.
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#iff.
    def visitIff(self, ctx:MiniGoParser.IffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseIf.
    def visitElseIf(self, ctx:MiniGoParser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forBasic.
    def visitForBasic(self, ctx:MiniGoParser.ForBasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forInitial.
    def visitForInitial(self, ctx:MiniGoParser.ForInitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialization.
    def visitInitialization(self, ctx:MiniGoParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclInitial.
    def visitVarDeclInitial(self, ctx:MiniGoParser.VarDeclInitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update.
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignScalar.
    def visitAssignScalar(self, ctx:MiniGoParser.AssignScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forRange.
    def visitForRange(self, ctx:MiniGoParser.ForRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatement.
    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return self.visitChildren(ctx)



del MiniGoParser