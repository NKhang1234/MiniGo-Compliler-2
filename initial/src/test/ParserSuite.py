import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

#------------------------------------------PROVIDED TEST -------------------------------------------------------------
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {
                    var a int
                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        var a int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,303))

#------------------------------------------MYSELF TEST -------------------------------------------------------------


    def test_240(self):
        input = """
            func test() {
                if (x > 10) {
                    println("x is greater than 10");
                    if (x>11) {
                        println("x is greater than 10");
                    } else if (x>11) {
                        println("x is greater than 10");
                    } else {
                        println("x is greater than 10");
                    }
                } else {
                    println("x is greater than 10");
                }
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 240))

    def test_241(self):
        input = """
            func test() {
                        if (x > 10) {
                            println("x is greater than 10");
                        }
                    };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 241))

    def test_242(self):
        input = """
            func test() {
                        if (x > 10) {
                            println("x is greater than 10");
                        } else {
                            println("x is greater than 10");
                        }
                    };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 242))






    