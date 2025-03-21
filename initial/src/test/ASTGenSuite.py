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
        """Test a simple integer constant declaration"""
        input = """const Num = 42;"""
        expect = Program([ConstDecl("Num", None, IntLiteral(42))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 1))

    def test_002(self):
        """Test a binary integer literal converted to decimal"""
        input = """const BinNum = 0b1010;"""
        expect = Program([ConstDecl("BinNum", None, IntLiteral('0b1010'))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 2))

    def test_003(self):
        """Test an octal integer literal converted to decimal"""
        input = """const OctNum = 0o12;"""
        expect = Program([ConstDecl("OctNum", None, IntLiteral('0o12'))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 3))

    def test_004(self):
        """Test a hexadecimal integer literal converted to decimal"""
        input = """const HexNum = 0x1F;"""
        expect = Program([ConstDecl("HexNum", None, IntLiteral('0x1F'))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 4))

    def test_005(self):
        """Test a floating-point literal with exponent"""
        input = """const FloatNum = 1.23e-2;"""
        expect = Program([ConstDecl("FloatNum", None, FloatLiteral(0.0123))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 5))

    def test_006(self):
        """Test a boolean true literal"""
        input = """const IsTrue = true;"""
        expect = Program([ConstDecl("IsTrue", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 6))

    def test_007(self):
        """Test a boolean false literal"""
        input = """const IsFalse = false;"""
        expect = Program([ConstDecl("IsFalse", None, BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 7))

    def test_008(self):
        """Test a string literal with escape sequence"""
        input = """const Message = "Hello World";"""
        expect = Program([ConstDecl("Message", None, StringLiteral("\"Hello World\""))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 8))

    def test_009(self):
        """Test a nil literal"""
        input = """const NullPtr = nil;"""
        expect = Program([ConstDecl("NullPtr", None, NilLiteral())])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 9))

    def test_010(self):
        """Test an empty struct literal"""
        input = """const EmptyObj = Data{};"""
        expect = Program([ConstDecl("EmptyObj", None, StructLiteral("Data", []))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 10))

    def test_011(self):
        """Test variable declaration with inferred type"""
        input = """var x = 100;"""
        expect = Program([VarDecl("x", None, IntLiteral(100))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 11))

    def test_012(self):
        """Test variable declaration with explicit type and hex literal"""
        input = """var val int = 0xFF;"""
        expect = Program([VarDecl("val", IntType(), IntLiteral('0xFF'))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 12))

    def test_013(self):
        """Test constant with octal integer"""
        input = """const OctVal = 0o777;"""
        expect = Program([ConstDecl("OctVal", None, IntLiteral('0o777'))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 13))

    def test_014(self):
        """Test constant with floating-point literal and exponent"""
        input = """const SciNum = 2.5e2;"""
        expect = Program([ConstDecl("SciNum", None, FloatLiteral(250.0))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 14))

    def test_015(self):
        """Test variable declaration with string concatenation"""
        input = """var greeting = "Hello" + "World";"""
        expect = Program([VarDecl("greeting", None, BinaryOp("+", StringLiteral("\"Hello\""), StringLiteral("\"World\"")))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 15))

    def test_016(self):
        """Test constant with array literal"""
        input = """const Arr = [2]int{10, 20};"""
        expect = Program([ConstDecl("Arr", None, ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(10), IntLiteral(20)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 16))

    def test_017(self):
        """Test constant with nested array literal"""
        input = """const Matrix = [2][2]int{{1, 2}, {3, 4}};"""
        expect = Program([ConstDecl("Matrix", None, ArrayLiteral([IntLiteral(2), IntLiteral(2)], IntType(), 
                             [[IntLiteral(1), IntLiteral(2)], [IntLiteral(3), IntLiteral(4)]]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 17))

    def test_018(self):
        """Test constant with struct literal and fields"""
        input = """const Person = Person{name: "John", age: 25};"""
        expect = Program([ConstDecl("Person", None, StructLiteral("Person", [("name", StringLiteral("\"John\"")), ("age", IntLiteral(25))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 18))

    def test_019(self):
        """Test constant with binary operation and parentheses"""
        input = """const Result = (5 + 3) * 2;"""
        expect = Program([ConstDecl("Result", None, BinaryOp("*", BinaryOp("+", IntLiteral(5), IntLiteral(3)), IntLiteral(2)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 19))

    def test_020(self):
        """Test constant with function call"""
        input = """const Value = getInt();"""
        expect = Program([ConstDecl("Value", None, FuncCall("getInt", []))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 20))

    def test_021(self):
        """Test constant with unary operation"""
        input = """const NegVal = -42;"""
        expect = Program([ConstDecl("NegVal", None, UnaryOp("-", IntLiteral(42)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 21))

    def test_022(self):
        """Test constant with boolean operation"""
        input = """const Flag = true && false;"""
        expect = Program([ConstDecl("Flag", None, BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 22))

    def test_023(self):
        """Test constant with relational operation"""
        input = """const Compare = 10 > 5;"""
        expect = Program([ConstDecl("Compare", None, BinaryOp(">", IntLiteral(10), IntLiteral(5)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 23))

    def test_024(self):
        """Test variable declaration with nil"""
        input = """var ptr = nil;"""
        expect = Program([VarDecl("ptr", None, NilLiteral())])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 24))

    def test_025(self):
        """Test constant with mixed-type array literal"""
        input = """const Mixed = [3]ID{1, "text", nil};"""
        expect = Program([ConstDecl("Mixed", None, ArrayLiteral([IntLiteral(3)], Id("ID"), 
                             [IntLiteral(1), StringLiteral("\"text\""), NilLiteral()]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 25))

    def test_026(self):
        """Test a for-each loop over an array literal"""
        input = """
        func foo() {
            for i, v := range [3]int{1, 2, 3} { return v; }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([ForEach(Id("i"), Id("v"), 
                                         ArrayLiteral([IntLiteral(3)], IntType(), 
                                                      [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), 
                                         Block([Return(Id("v"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 26))

    def test_027(self):
        """Test a for-step loop with initialization and update"""
        input = """
        func foo() {
            for var i = 0; i <= 5; i += 1 { continue; }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([ForStep(VarDecl("i", None, IntLiteral(0)), 
                                         BinaryOp("<=", Id("i"), IntLiteral(5)), 
                                         Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), 
                                         Block([Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 27))

    def test_028(self):
        """Test an if statement with a return inside a function"""
        input = """
        func foo() {
            if (a == b) { return 42; }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([If(BinaryOp("==", Id("a"), Id("b")), 
                                    Block([Return(IntLiteral(42))]), 
                                    None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 28))

    def test_029(self):
        """Test a function with an assignment statement"""
        input = """
        func foo() {
            x := 10 + 20;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(Id("x"), BinaryOp("+", IntLiteral(10), IntLiteral(20)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 29))

    def test_030(self):
        """Test a for loop with multiple statements"""
        input = """
        func foo() {
            for (true) { x += 1; return; }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([ForBasic(BooleanLiteral(True), 
                                          Block([Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))), 
                                                 Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 30))

    def test_031(self):
        """Test a for-each loop with a function call"""
        input = """
        func foo() {
            for _, val := range arr { putIntLn(val); }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([ForEach(Id("_"), Id("val"), Id("arr"), 
                                         Block([FuncCall("putIntLn", [Id("val")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 31))

    def test_032(self):
        """Test a constant with a struct literal with one field"""
        input = """const Coord = Point{x: 10};"""
        expect = Program([ConstDecl("Coord", None, StructLiteral("Point", [("x", IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 32))

    def test_033(self):
        """Test a function with array element assignment"""
        input = """
        func foo() {
            arr[0] := 5;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 33))

    def test_034(self):
        """Test a function with a struct field access and assignment"""
        input = """
        func foo() {
            p.x := 100;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(FieldAccess(Id("p"), "x"), IntLiteral(100))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 34))

    def test_035(self):
        """Test a for loop with a method call"""
        input = """
        func foo() {
            for (i < n) { obj.method(); }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([ForBasic(BinaryOp("<", Id("i"), Id("n")), 
                                          Block([MethCall(Id("obj"), "method", [])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 35))

    def test_036(self):
        """Test a function with a compound assignment"""
        input = """
        func foo() {
            x *= 2;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(Id("x"), BinaryOp("*", Id("x"), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 36))

    def test_037(self):
        """Test a constant with a float literal without exponent"""
        input = """const PiApprox = 3.14;"""
        expect = Program([ConstDecl("PiApprox", None, FloatLiteral(3.14))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 37))

    def test_038(self):
        """Test a constant with a string literal containing a tab escape"""
        input = """const Tabbed = "Data Value";"""
        expect = Program([ConstDecl("Tabbed", None, StringLiteral("\"Data Value\""))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 38))
    

    def test_039(self):
        """Test a for-step loop with a complex condition"""
        input = """
        func foo() {
            for var k = 0; k + 1 < 10; k += 2 { return k; }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([ForStep(VarDecl("k", None, IntLiteral(0)), 
                                         BinaryOp("<", BinaryOp("+", Id("k"), IntLiteral(1)), IntLiteral(10)), 
                                         Assign(Id("k"), BinaryOp("+", Id("k"), IntLiteral(2))), 
                                         Block([Return(Id("k"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 39))

    def test_040(self):
        """Test a function with a function call and return"""
        input = """
        func foo() {
            return bar(1, 2);
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(FuncCall("bar", [IntLiteral(1), IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 40))

    def test_041(self):
        """Test a function returning a binary operation result"""
        input = """
        func foo() {
            return x + y;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(BinaryOp("+", Id("x"), Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 41))

    def test_042(self):
        """Test a function with an assignment to a variable"""
        input = """
        func foo() {
            result := a * 3;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(Id("result"), BinaryOp("*", Id("a"), IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 42))

    def test_043(self):
        """Test a function returning a method call"""
        input = """
        func foo() {
            return obj.getValue();
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(MethCall(Id("obj"), "getValue", []))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 43))

    def test_044(self):
        """Test a function with an array assignment using an expression"""
        input = """
        func foo() {
            arr[1 + 2] := 5;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(ArrayCell(Id("arr"), [BinaryOp("+", IntLiteral(1), IntLiteral(2))]), 
                                        IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 44))

    def test_045(self):
        """Test a function returning a struct field access"""
        input = """
        func foo() {
            return p.x;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(FieldAccess(Id("p"), "x"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 45))

    def test_046(self):
        """Test a function with a compound assignment to a field"""
        input = """
        func foo() {
            s.value += 10;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(FieldAccess(Id("s"), "value"), 
                                        BinaryOp("+", FieldAccess(Id("s"), "value"), IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 46))

    def test_047(self):
        """Test a function returning an array element with a complex index"""
        input = """
        func foo() {
            return data[x * 2][y];
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(ArrayCell(Id("data"), [BinaryOp("*", Id("x"), IntLiteral(2)), Id("y")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 47))

    def test_048(self):
        """Test a function with a method call assignment"""
        input = """
        func foo() {
            result := obj.compute(1, 2);
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(Id("result"), 
                                        MethCall(Id("obj"), "compute", [IntLiteral(1), IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 48))

    def test_049(self):
        """Test a function returning a multi-dimensional array access"""
        input = """
        func foo() {
            return a[2][3][4];
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3), IntLiteral(4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 49))

    def test_050(self):
        """Test a function with an assignment to a nested array within a struct"""
        input = """
        func foo() {
            a.b[2][3][4] := 1;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(ArrayCell(FieldAccess(Id("a"), "b"), 
                                                  [IntLiteral(2), IntLiteral(3), IntLiteral(4)]), 
                                        IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 50))

    def test_051(self):
        """Test a function with a nested field access assignment"""
        input = """
        func foo() {
            a.b.c := "nested";
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(FieldAccess(FieldAccess(Id("a"), "b"), "c"), 
                                        StringLiteral("\"nested\""))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 51))

    def test_052(self):
        """Test a function returning a unary operation on an array element"""
        input = """
        func foo() {
            return -arr[0];
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(UnaryOp("-", ArrayCell(Id("arr"), [IntLiteral(0)])))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 52))

    def test_053(self):
        """Test a function with a compound assignment to an array element"""
        input = """
        func foo() {
            data[1] -= 5;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(ArrayCell(Id("data"), [IntLiteral(1)]), 
                                        BinaryOp("-", ArrayCell(Id("data"), [IntLiteral(1)]), 
                                                 IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 53))

    def test_054(self):
        """Test a function with an assignment from a function call"""
        input = """
        func foo() {
            x := compute(y, 3);
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(Id("x"), FuncCall("compute", [Id("y"), IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 54))

    def test_055(self):
        """Test a function returning a boolean operation"""
        input = """
        func foo() {
            return x > 0 && y < 10;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(BinaryOp("&&", BinaryOp(">", Id("x"), IntLiteral(0)), 
                                                 BinaryOp("<", Id("y"), IntLiteral(10))))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 55))

    def test_056(self):
        """Test a function with an array assignment from a struct literal"""
        input = """
        func foo() {
            arr[0] := Point{x: 1, y: 2};
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), 
                                        StructLiteral("Point", [("x", IntLiteral(1)), 
                                                                ("y", IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 56))

    def test_057(self):
        """Test a function returning a mixed operation with array and field access"""
        input = """
        func foo() {
            return arr[1] + p.value;
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(BinaryOp("+", ArrayCell(Id("arr"), [IntLiteral(1)]), 
                                                 FieldAccess(Id("p"), "value")))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 57))

    def test_058(self):
        """Test a function with an if statement and array assignment"""
        input = """
        func foo() {
            if (x == 0) { arr[2] := nil; }
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([If(BinaryOp("==", Id("x"), IntLiteral(0)), 
                                    Block([Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), 
                                                  NilLiteral())]), 
                                    None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 58))

    def test_059(self):
        """Test a function returning a nested array literal"""
        input = """
        func foo() {
            return [2][2]int{{1, 2}, {3, 4}};
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(ArrayLiteral([IntLiteral(2), IntLiteral(2)], IntType(), 
                                                     [[IntLiteral(1), IntLiteral(2)], 
                                                      [IntLiteral(3), IntLiteral(4)]]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 59))

    def test_060(self):
        """Test a function with a complex assignment involving method and array"""
        input = """
        func foo() {
            obj.data[1] := obj.getValue()[0];
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Assign(ArrayCell(FieldAccess(Id("obj"), "data"), [IntLiteral(1)]), 
                                        ArrayCell(MethCall(Id("obj"), "getValue", []), 
                                                  [IntLiteral(0)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 60))
    
    def test_061(self):
        """Test a function returning a nested method call"""
        input = """
        func foo() {
            return obj.getInner().value();
        }
"""
        expect = Program([FuncDecl("foo", [], VoidType(), 
                          Block([Return(MethCall(MethCall(Id("obj"), "getInner", []), 
                                                 "value", []))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 61))

    def test_062(self):
        """Test a constant with a function call with a boolean and integer"""
        input = """const nhatKhang = foo(true, 42);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BooleanLiteral(True), IntLiteral(42)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 62))

    def test_063(self):
        """Test a constant with a function call with a float and nil"""
        input = """const nhatKhang = foo(3.14, nil);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [FloatLiteral(3.14), NilLiteral()]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 63))

    def test_064(self):
        """Test a constant with a function call with an array literal"""
        input = """const nhatKhang = foo([2]int{1, 2});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [ArrayLiteral([IntLiteral(2)], IntType(), 
                                                                                  [IntLiteral(1), IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 64))

    def test_065(self):
        """Test a constant with a function call with a struct literal"""
        input = """const nhatKhang = foo(Point{x: 5});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [StructLiteral("Point", [("x", IntLiteral(5))])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 65))

    def test_066(self):
        """Test a constant with a function call with a binary addition"""
        input = """const nhatKhang = foo(x + y);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("+", Id("x"), Id("y"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 66))

    def test_067(self):
        """Test a constant with a function call with a unary negation"""
        input = """const nhatKhang = foo(-10);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [UnaryOp("-", IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 67))

    def test_068(self):
        """Test a constant with a function call with multiple identifiers"""
        input = """const nhatKhang = foo(a, b, c);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [Id("a"), Id("b"), Id("c")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 68))

    def test_069(self):
        """Test a constant with a function call with a complex binary expression"""
        input = """const nhatKhang = foo(1 * x + 2 / y);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("+", 
                                                                              BinaryOp("*", IntLiteral(1), Id("x")), 
                                                                              BinaryOp("/", IntLiteral(2), Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 69))

    def test_070(self):
        """Test a constant with a function call with a relational operation"""
        input = """const nhatKhang = foo(x >= 5);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp(">=", Id("x"), IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 70))

    def test_071(self):
        """Test a constant with a function call with mixed literals and operations"""
        input = """const nhatKhang = foo(1.5 + 2, "text" == "test");"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("+", FloatLiteral(1.5), IntLiteral(2)), 
                                                                     BinaryOp("==", StringLiteral("\"text\""), 
                                                                              StringLiteral("\"test\""))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 71))

    def test_072(self):
        """Test a constant with a function call with an array access"""
        input = """const nhatKhang = foo(arr[0]);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [ArrayCell(Id("arr"), [IntLiteral(0)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 72))

    def test_073(self):
        """Test a constant with a function call with a field access"""
        input = """const nhatKhang = foo(p.x);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [FieldAccess(Id("p"), "x")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 73))

    def test_074(self):
        """Test a constant with a function call with a nested function call"""
        input = """const nhatKhang = foo(bar(3));"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [FuncCall("bar", [IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 74))

    def test_075(self):
        """Test a constant with a function call with a method call"""
        input = """const nhatKhang = foo(obj.get());"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [MethCall(Id("obj"), "get", [])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 75))

    def test_076(self):
        """Test a constant with a function call with multiple mixed arguments"""
        input = """const nhatKhang = foo(1, x.y, true || false);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [IntLiteral(1), 
                                                                     FieldAccess(Id("x"), "y"), 
                                                                     BinaryOp("||", BooleanLiteral(True), 
                                                                              BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 76))

    def test_077(self):
        """Test a constant with a function call with a nested array literal"""
        input = """const nhatKhang = foo([1][2]int{{1, 2}});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [ArrayLiteral([IntLiteral(1), IntLiteral(2)], 
                                                                                  IntType(), 
                                                                                  [[IntLiteral(1), IntLiteral(2)]])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 77))

    def test_078(self):
        """Test a constant with a function call with a nested array access and operation"""
        input = """const nhatKhang = foo(arr[x + 1][2] * 3);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("*", 
                                                                              ArrayCell(Id("arr"), 
                                                                                        [BinaryOp("+", Id("x"), IntLiteral(1)), 
                                                                                         IntLiteral(2)]), 
                                                                              IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 78))

    def test_079(self):
        """Test a constant with a function call with a complex nested expression"""
        input = """const nhatKhang = foo(!(x < y) || z);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("||", 
                                                                              UnaryOp("!", BinaryOp("<", Id("x"), Id("y"))), 
                                                                              Id("z"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 79))

    def test_080(self):
        """Test a constant with a function call with array and field access combination"""
        input = """const nhatKhang = foo(arr[1].field);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [FieldAccess(ArrayCell(Id("arr"), [IntLiteral(1)]), 
                                                                                 "field")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 80))

    def test_081(self):
        """Test a constant with a function call with a simple float literal"""
        input = """const nhatKhang = foo(2.718);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [FloatLiteral(2.718)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 81))

    def test_082(self):
        """Test a constant with a function call with a binary subtraction"""
        input = """const nhatKhang = foo(10 - 5);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("-", IntLiteral(10), IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 82))

    def test_083(self):
        """Test a constant with a function call with a string concatenation"""
        input = """const nhatKhang = foo("hello" + "world");"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("+", StringLiteral("\"hello\""), StringLiteral("\"world\""))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 83))

    def test_084(self):
        """Test a constant with a function call with a boolean negation"""
        input = """const nhatKhang = foo(!true);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [UnaryOp("!", BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 84))

    def test_085(self):
        """Test a constant with a function call with a binary operation on field accesses"""
        input = """const nhatKhang = foo(p.x + q.y);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("+", 
                                                                              FieldAccess(Id("p"), "x"), 
                                                                              FieldAccess(Id("q"), "y"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 85))

    def test_086(self):
        """Test a constant with a function call with a struct literal with multiple fields"""
        input = """const nhatKhang = foo(Point{x: 1, y: "test"});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [StructLiteral("Point", 
                                                                                  [("x", IntLiteral(1)), 
                                                                                   ("y", StringLiteral("\"test\""))])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 86))

    def test_087(self):
        """Test a constant with a function call with a nested binary operation"""
        input = """const nhatKhang = foo(2 * (3 + 4));"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("*", IntLiteral(2), 
                                                                              BinaryOp("+", IntLiteral(3), IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 87))

    def test_088(self):
        """Test a constant with a function call with a multi-level field access"""
        input = """const nhatKhang = foo(a.b.c.d);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [FieldAccess(FieldAccess(FieldAccess(Id("a"), "b"), "c"), "d")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 88))

    def test_089(self):
        """Test a constant with a function call with a nested struct literal"""
        input = """const nhatKhang = foo(Struct{x: Point{y: 2}});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [StructLiteral("Struct", 
                                                                                  [("x", StructLiteral("Point", 
                                                                                                       [("y", IntLiteral(2))]))])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 89))

    def test_090(self):
        """Test a constant with a function call with a complex relational chain"""
        input = """const nhatKhang = foo(x < y <= z);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("<=", BinaryOp("<", Id("x"), Id("y")), Id("z"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 90))

    def test_091(self):
        """Test a constant with a function call with an array access with computed index"""
        input = """const nhatKhang = foo(arr[2 + x]);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [ArrayCell(Id("arr"), [BinaryOp("+", IntLiteral(2), Id("x"))])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 91))

    def test_092(self):
        """Test a constant with a function call with a nested function call with operation"""
        input = """const nhatKhang = foo(bar(x * 2));"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [FuncCall("bar", [BinaryOp("*", Id("x"), IntLiteral(2))])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 92))

    def test_093(self):
        """Test a constant with a function call with mixed types and operations"""
        input = """const nhatKhang = foo(1 + 2.5, "a" != "b");"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("+", IntLiteral(1), FloatLiteral(2.5)), 
                                                                     BinaryOp("!=", StringLiteral("\"a\""), StringLiteral("\"b\""))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 93))

    def test_094(self):
        """Test a constant with a function call with a nested array literal and nil"""
        input = """const nhatKhang = foo([2]int{0, nil});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [ArrayLiteral([IntLiteral(2)], IntType(), 
                                                                                  [IntLiteral(0), NilLiteral()])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 94))

    def test_095(self):
        """Test a constant with a function call with a struct literal and field access"""
        input = """const nhatKhang = foo(Point{x: p.y});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [StructLiteral("Point", 
                                                                                  [("x", FieldAccess(Id("p"), "y"))])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 95))

    def test_096(self):
        """Test a constant with a function call with a complex unary and binary operation"""
        input = """const nhatKhang = foo(-x * y);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("*", UnaryOp("-", Id("x")), Id("y"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 96))

    def test_097(self):
        """Test a constant with a function call with a nested method call and array access"""
        input = """const nhatKhang = foo(obj.get()[1]);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [ArrayCell(MethCall(Id("obj"), "get", []), 
                                                                               [IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 97))

    def test_098(self):
        """Test a constant with a function call with a multi-dimensional array access"""
        input = """const nhatKhang = foo(arr[0][1][2]);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [ArrayCell(Id("arr"), [IntLiteral(0), IntLiteral(1), IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 98))

    def test_099(self):
        """Test a constant with a function call with a combination of operations and literals"""
        input = """const nhatKhang = foo(1 + x * 2, true && false);"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [BinaryOp("+", IntLiteral(1), BinaryOp("*", Id("x"), IntLiteral(2))), 
                                                                     BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 99))

    def test_100(self):
        """Test a constant with a function call with a nested struct and array operation"""
        input = """const nhatKhang = foo(Point{x: arr[0] + 1});"""
        expect = Program([ConstDecl("nhatKhang", None, FuncCall("foo", [StructLiteral("Point", 
                                                                                  [("x", BinaryOp("+", ArrayCell(Id("arr"), [IntLiteral(0)]), 
                                                                                                  IntLiteral(1)))])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 100))

    

