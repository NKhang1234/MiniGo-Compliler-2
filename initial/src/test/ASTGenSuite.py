import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() {};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """func main () {}; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    ## -------------------------------- Failed Vo Tien Tc -----------------------------------

    #  -------------------------------- Format IntLit and StringLit -----------------------------------

    def test_001(self):
        input = """const VoTien = 1; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 1))

    def test_002(self):
        """ chuyển đổi sang kiểu int hết """
        input = """const VoTien = 0b11; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 2))

    def test_003(self):
        input = """const VoTien = 0o70; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(56))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 3))

    def test_004(self):
        input = """const VoTien = 0Xa1; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(161))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 4))

    def test_005(self):
        input = """const VoTien = 01.e-1; """
        expect = Program([ConstDecl("VoTien", None, FloatLiteral(0.1))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 5))

    def test_006(self):
        """ đầu vào là giá trị True False chứ không phải string """
        input = """const VoTien = true; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 6))

    def test_007(self):
        input = """const VoTien = false; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 7))

    def test_008(self):
        """ loại bỏ "" ở trước và sau string """
        input = """const VoTien = "votien"; """
        expect = Program([ConstDecl("VoTien", None, StringLiteral("votien"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 8))

    def test_009(self):
        input = """const VoTien = nil; """
        expect = Program([ConstDecl("VoTien", None, NilLiteral())])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 9))
    
    def test_010(self):
        input = """const VoTien = STRUCT {}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 10))

    def test_011(self):
        input = """const VoTien = STRUCT {
            a : 1,
            b : false}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 11))

    def test_012(self):
        input = """const VoTien = [ID] int {1}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 12))

    def test_013(self):
        input = """const VoTien = [1][2] int {1., STRUCT{}, nil}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral(1.0),StructLiteral("STRUCT",[]),NilLiteral()]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 13))

    def test_014(self):
        input = """const VoTien = [1][2] STRUCT {{1, {3}}, {2}}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1), [IntLiteral(3)]],[IntLiteral(2)]]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 14))

    def test_015(self):
        input = """const VoTien = 1 || 2 || 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 15))

    def test_016(self):
        input = """const VoTien = 1 && 2 && 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 16))

    def test_017(self):
        input = """const VoTien = 1 >= 2 <= 3 > 4 < 5 == 6 != 7; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 17))
    
    def test_018(self):
        input = """const VoTien = 1 + 2 - 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 18))

    def test_019(self):
        input = """const VoTien = 1 * 2 / 3 % 4; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 19))

    def test_020(self):
        input = """const VoTien = ! - 1; """
        expect = Program([ConstDecl("VoTien", None, UnaryOp("!",UnaryOp("-",IntLiteral(1))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 20))

    def test_021(self):
        input = """const VoTien = a; """
        expect = Program([ConstDecl("VoTien", None, Id("a"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 21))

    def test_022(self):
        input = """const VoTien = (1+2)*3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 22))

    def test_023(self):
        input = """const VoTien = foo(); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 23))

    def test_024(self):
        input = """const VoTien = foo(1, 2); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 24))

    def test_025(self):
        input = """const VoTien = a[2][3]; """
        expect = Program([ConstDecl("VoTien",None,ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 25))

    def test_026(self):
        input = """const VoTien = a.b.c; """
        expect = Program([ConstDecl("VoTien", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 26))

    def test_027(self):
        input = """const VoTien = a.b().c(1, 2); """
        expect = Program([ConstDecl("VoTien", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 27))

    def test_028(self):
        input = """const VoTien = a.b[2].c.d(); """
        expect = Program([ConstDecl("VoTien", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 28))

    def test_029(self):
        input = """
    var a int = 1;
    var a float = 1;
    var a boolean;
    var a string = 1;
    var a = 1;
    var a ID = 1;
    var a [ID][1] int = 1;
"""
        expect = Program([VarDecl("a",IntType(),IntLiteral(1)),
			VarDecl("a",FloatType(),IntLiteral(1)),
			VarDecl("a",BoolType(), None),
			VarDecl("a",StringType(),IntLiteral(1)),
			VarDecl("a", None,IntLiteral(1)),
			VarDecl("a",Id("ID"),IntLiteral(1)),
			VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 29))


    def test_030(self):
        input = """
    const a = 1;
"""
        expect = Program([ConstDecl("a",None,IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 30))

    def test_031(self):
        input = """
    type ID struct {
        a int;
        b ID;
        c [2]int;
    }
"""
        expect = Program([StructType("ID",[("a",IntType()),("b",Id("ID")),("c",ArrayType([IntLiteral(2)],IntType()))],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 31))

    def test_032(self):
        input = """
    func foo () {var a = 1;}
    func foo () int {var a = 1;}
    func foo () [2] ID {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 32))

    def test_033(self):
        input = """
    func foo (a int) {var a = 1;}
    func foo (a int, b ID) {var a = 1;}
    func foo (a, b int) {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 33))


    def test_034(self):
        input = """
    func (ID ID) foo () {var a = 1;}
    func (ID ID) foo () int {var a = 1;}
    func (ID ID) foo () [2] ID {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 34))

    def test_035(self):
        input = """
    func (ID ID) foo (a int) {var a = 1;}
    func (ID ID) foo (a int, b ID) {var a = 1;}
    func (ID ID) foo (a, b int) {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 35))

    def test_036(self):
        input = """
        type INTERFACE interface {
            foo();
            foo() int;
            foo() [2]ID;
            foo(a int);
            foo(a int, b int);
            foo(a, b int);
        }
"""
        expect = Program([InterfaceType("INTERFACE",[
            Prototype("foo",[],VoidType()),Prototype("foo",[],IntType()),
            Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
            Prototype("foo",[IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 36))

    def test_037(self):
        input = """
    func foo () {
        continue;
        break;
        return;
        return 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 37))


    def test_038(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 38))

    def test_039(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 39))


    def test_040(self):
        input = """
    func foo () {
        a := 1;
        a += 1;
        a -= 1;
        a *= 1;
        a /= 1;
        a %= 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 40))

    def test_041(self):
        input = """
    func foo () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 41))

    def test_042(self):
        input = """
    func foo () {
        a();
        a(1, 2);
        a(1);
        b.a.a();
        b.a.a(1, 2);
        b.a.a(1);
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            FuncCall("a",[]),
            FuncCall("a",[IntLiteral(1),IntLiteral(2)]),
            FuncCall("a",[IntLiteral(1)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1),IntLiteral(2)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 42))
    
    def test_043(self):
        input = """
        func foo () {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 43))

    def test_044(self):
        input = """
        func foo () {
            for(1) {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 44))

    def test_045(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 45))

    def test_046(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 46))

    def test_047(self):
        input = """
        func foo () {
            for var a = 1; a < 10; a := 1 {return;}
            for a += 1; a < 10; a -= 1 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)])),
            ForStep(Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 47))


    def test_048(self):
        input = """
        func foo () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), None)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 48))

    def test_049(self):
        input = """
        func foo () {
            return a[2][3][4];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 49))

    def test_050(self):
        input = """
        func foo () {
            a.b[2][3][4] := 1;
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 50))

    def test_051(self):
        input = """
        func foo () {
            a[1*2][1+2] := a[1*2][1+2];
            a[1+2] := a[1+2];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 51))

    def test_052(self):
        input = """const VoTien = foo( 1 ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[IntLiteral(1)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 52))

    def test_053(self):
        input = """const VoTien = foo( 1.0,true,false,nil,\"votien\" ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[FloatLiteral(1.0),BooleanLiteral(True),BooleanLiteral(False),NilLiteral(),StringLiteral("votien")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 53))

    def test_054(self):
        input = """const VoTien = foo( id ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[Id("id")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 54))

    def test_055(self):
        input = """const VoTien = foo( 1+2-3&&5--1 ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-",IntLiteral(1))))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 55))

    def test_056(self):
        input = """const VoTien = foo( a > b <= c ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[BinaryOp("<=", BinaryOp(">", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 56))

    def test_057(self):
        input = """const VoTien = foo( a[2][3] ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 57))

    def test_058(self):
        input = """const VoTien = foo( a.b.c ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[FieldAccess(FieldAccess(Id("a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 58))

    def test_059(self):
        input = """const VoTien = foo( a(),b.a(2, 3) ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 59))

    def test_060(self):
        input = """const VoTien = foo( a * (1+2) ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 60))

    def test_061(self):
        input = """const VoTien = foo( Votien {}, Votien {a: 1} ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[StructLiteral("Votien",[]),StructLiteral("Votien",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 61))

    def test_062(self):
        input = """const VoTien = foo( [1]int{1}, [1][1]int{2} ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(1)],IntType(),[IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 62))

    def test_063(self):
        input = """
            var Votien = 1;
            var Votien int;
            var Votine int = 1;
"""
        expect = Program([VarDecl("Votien", None,IntLiteral(1)),
			VarDecl("Votien",IntType(), None),
			VarDecl("Votine",IntType(),IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 63))

    def test_064(self):
        input = """
            func foo() int {return;}
            func foo(a int, b int) {return;}
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 64))

    def test_065(self):
        input = """
            func (Votien v) foo(Votien int) {return;}
"""
        expect = Program([MethodDecl("Votien",Id("v"),FuncDecl("foo",[ParamDecl("Votien",IntType())],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 65))


    def test_066(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 66))


    def test_067(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 67))

    def test_069(self):
        input = """
            func votien() {
                var a int;
                const a = nil;
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 69))

    def test_070(self):
        input = """
            func votien() {
                a += 1;
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 70))

    def test_071(self):
        input = """
            func votien() {
                break;
                continue;
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 71))

    def test_072(self):
        input = """
            func votien() {
                foo(1, 2);
                a[2].foo(1,3);
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 72))

    def test_073(self):
        input = """
            func votien() {
                if(1) {return;}
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([If(IntLiteral(1), Block([Return(None)]), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 73))

    def test_074(self):
        input = """
            func votien() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), Block([Assign(Id("a"),IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 74))

    def test_075(self):
        input = """
            func votien() {
                if(1) { return;
                }else if(1) {
                    a := 1;
                }else if(2) {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), 
                    If(IntLiteral(2), Block([Assign(Id("a"),IntLiteral(1))]), None)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 75))


    def test_076(self):
        input = """
            func votien() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([Return(None)])),ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 76))

    def test_077(self):
        input = """
            func votien() {
                for index, value := range array[2] {return;}
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 77))

    def test_078(self):
        input = """
            const a = true + false - true;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 78))

    def test_079(self):
        input = """
            const a = 1 && 2 || 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 79))

    def test_080(self):
        input = """
            const a = 1 + 2 && 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 80))

    def test_081(self):
        input = """
            const a = 1 - 2 % 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", IntLiteral(1), BinaryOp("%", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 81))

    def test_082(self):
        input = """
            const a = 1 + -2 - 1;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(1), UnaryOp("-",IntLiteral(2))), IntLiteral(1)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 82))

    def test_083(self):
        input = """
            const a = [1]ID{Votien{}};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1)],Id("ID"),[StructLiteral("Votien",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 83))

    def test_084(self):
        input = """
            const a = [1][3]float{1.};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1),IntLiteral(3)],FloatType(),[FloatLiteral(1.0)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 84))

    def test_085(self):
        input = """
            const a = ID{a: 1, b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",IntLiteral(1)),("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 85))
    
    def test_086(self):
        input = """
            const a = ID{a: [1]int{1}};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 86))


    def test_087(self):
        input = """
            const a = ID{b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 87))

    def test_088(self):
        input = """
            const a = 0 && 1 && 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("&&", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 88))

    def test_089(self):
        input = """
            const a = 0 || 1 || 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("||", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 89))

    def test_090(self):
        input = """
            const a = 0 >= 1 <= 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("<=", BinaryOp(">=", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 90))

    def test_091(self):
        input = """
            const a = 0 + 1 - 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 91))

    def test_092(self):
        input = """
            const a = 0 * 1 / 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("/", BinaryOp("*", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 92))

    def test_093(self):
        input = """
            const a = !-!2;
"""
        expect = Program([ConstDecl("a",None,UnaryOp("!",UnaryOp("-",UnaryOp("!",IntLiteral(2)))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 93))

    def test_094(self):
        input = """
            const a = 1 && 2 || 3 >= 4 + 5 * -6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6)))))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 94))

    def test_095(self):
        input = """
            const a = 1 > 2 < 3 >= 4 <=5 == 6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("==", BinaryOp("<=", BinaryOp(">=", BinaryOp("<", BinaryOp(">", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 95))

    def test_096(self):
        input = """
            const a = 1 >= 2 + 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp(">=", IntLiteral(1), BinaryOp("+", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 96))

    def test_097(self):
        input = """
            const a = a[1][2][3][4];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 97))

    def test_098(self):
        input = """
            const a = a[1 + 2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 98))

    def test_099(self):
        input = """
            const a = a.b.c.d.e;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 99))

    def test_100(self):
        input = """
            const a = ID {}.a;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(StructLiteral("ID",[]),"a"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 100))

    def test_101(self):
        input = """
            const a = ID {}.a[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FieldAccess(StructLiteral("ID",[]),"a"),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 101))

    def test_102(self):
        input = """
            const a = a.b().c().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(MethCall(MethCall(Id("a"),"b",[]),"c",[]),"d",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 102))

    def test_103(self):
        input = """
            const a = a().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(FuncCall("a",[]),"d",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 103))

    def test_104(self):
        input = """
            const a = a[1].b.c()[2].d.e();
"""
        expect = Program([ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 104))
    
    def test_105(self):
        input = """
            const a = a * (nil - "a");
"""
        expect = Program([ConstDecl("a",None,BinaryOp("*", Id("a"), BinaryOp("-", NilLiteral(), StringLiteral("a"))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 105))

    def test_106(self):
        input = """
            const a = f() + f(1 + 2, 3.);
"""
        expect = Program([ConstDecl("a",None,BinaryOp("+", FuncCall("f",[]), FuncCall("f",[BinaryOp("+", IntLiteral(1), IntLiteral(2)),FloatLiteral(3.0)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 106))

    def test_107(self):
        input = """
            const a = foo()[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FuncCall("foo",[]),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 107))

    def test_108(self):
        input = """
            const a = a;
"""
        expect = Program([ConstDecl("a",None,Id("a"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 108))

    def test_109(self):
        input = """
            var a Votien = 1.;
"""
        expect = Program([VarDecl("a",Id("Votien"),FloatLiteral(1.0))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 109))

    def test_110(self):
        "thêm type array vào AST anh có thông bao trong nhóm task 3"
        input = """
            var a [2][3]int;
"""
        expect = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None)
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 110))
    
    def test_111(self):
        input = """
            var a = 1;
"""
        expect = Program([VarDecl("a", None,IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 111))

    def test_112(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 112))
    
    def test_113(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 113))

    def test_114(self):
        input = """
            type Votien struct {
                a  int;
                b  boolean;
                
            }
"""
        expect = Program([StructType("Votien",[("a",IntType()),("b",BoolType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 114))

    def test_115(self):
        input = """
            type Votien struct {
                a  int;
                b  boolean;
                c  [2]Votien;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType()),("b",BoolType()),("c",ArrayType([IntLiteral(2)],Id("Votien")))],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 115))

    def test_116(self):
        input = """
            type Votien interface {
                Add() ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 116))

    def test_117(self):
        input = """
            type Votien interface {
                Add(a int) ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 117))

    def test_118(self):
        input = """
            type Votien interface {
                Add(a int, b int) ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 118))

    def test_119(self):
        input = """
            type Votien interface {
                Add(a, c int, b int) ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType(),IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 119))

    def test_120(self):
        input = """
            type Votien interface {
                Add(a, c int, b int) [2]string;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType()))])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 120))

    def test_121(self):
        input = """
            type Votien interface {
                Add() [2]string;
                Add() ID;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[],ArrayType([IntLiteral(2)],StringType())),Prototype("Add",[],Id("ID"))])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 121))

    def test_122(self):
        input = """
            type Votien interface {
                Add();
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 122))


    def test_123(self):
        input = """
            func foo() {return;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 123))

    def test_124(self):
        input = """
            func foo(a [2]ID) {return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 124))


    def test_125(self):
        input = """
            func foo(a int, b [1]int) {return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 125))

    def test_126(self):
        input = """
            func foo() [2]int {return;}
"""
        expect = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 126))

    def test_127(self):
        input = """
            func (Cat c) foo() {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 127))

    def test_128(self):
        input = """
            func  (Cat c) foo(a [2]ID) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 128))


    def test_129(self):
        input = """
            func  (Cat c) foo(a int, b [1]int) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 129))

    def test_130(self):
        input = """
            func  (Cat c) foo() [2]int {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 130))

    def test_131(self):
        input = """
            var a = 1;
            const b = 2;
            type a struct{a float;}
            type b interface {foo();} 
            func foo(){return;}
            func  (Cat c) foo() [2]int {return;}
"""
        expect = Program([VarDecl("a", None,IntLiteral(1)),
			ConstDecl("b",None,IntLiteral(2)),
			StructType("a",[("a",FloatType())],[]),
			InterfaceType("b",[Prototype("foo",[],VoidType())]),
			FuncDecl("foo",[],VoidType(),Block([Return(None)])),
			MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 131))

    def test_132(self):
        input = """
            func foo(a,b,c,d [ID][2][c] ID ){return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("b",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("c",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("d",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 132))

    def test_133(self):
        input = """
            func foo(){
                const a = 1.;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 133))


    def test_134(self):
        input = """
            func foo(){
                var a = 1.;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 134))

    def test_135(self):
        input = """
            func foo(){
                var a [1]int = 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(1)],IntType()),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 135))

    def test_136(self):
        input = """
            func foo(){
                var a int;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 136))

    def test_137(self):
        input = """
            func foo(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 137))

    def test_138(self):
        input = """
            func foo(){
                a[1 + 1] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 138))

    def test_139(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 139))

    def test_140(self):
        input = """
            func foo(){
                a["s"][foo()] := a[2][2][3];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[StringLiteral("s"),FuncCall("foo",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),
            Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 140))

    def test_141(self):
        input = """
            func foo(){
                a.b := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 141))

    def test_142(self):
        input = """
            func foo(){
                a.b[2].c := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 142))

    def test_143(self):
        input = """
            func foo(){
                break;
                continue;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 143))

    def test_144(self):
        input = """
            func foo(){
                return;
                return foo() + 2;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None),Return(BinaryOp("+", FuncCall("foo",[]), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 144))

    def test_145(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("foo",[]),FuncCall("foo",[FuncCall("foo",[]),IntLiteral(2)]),MethCall(Id("a"),"foo",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",[FuncCall("foo",[]),IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 145))

    def test_146(self):
        input = """
            func foo(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 146))

    def test_147(self):
        input = """
            func foo(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 147))

    def test_148(self):
        input = """
            func foo(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                If(IntLiteral(2), Block([Return(IntLiteral(2))]), 
                    If(IntLiteral(3), Block([Return(IntLiteral(3))]), 
                        If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 148))

    def test_149(self):
        input = """
            func votien() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 149))

    def test_150(self):
        input = """
            func votien() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 150))

    def test_151(self):
        input = """
            func votien() {
                a.b.c[2].d()
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)]),"d",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 151))

    def test_152(self):
        input = """
            func votien() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return "THANKS YOU, PPL1 ";
            };
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("2")],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral("THANKS YOU, PPL1 "))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 152))

                # Program([FuncDecl(votien,[],VoidType,Block([Return(ArrayLiteral([IntLiteral(None)],Id(ID),[[IntLiteral(None)],[StringLiteral(2)],[Nil],[StructLiteral(struc,[])]])),Return(StringLiteral(THANKS YOU, PPL1 ))]))])













