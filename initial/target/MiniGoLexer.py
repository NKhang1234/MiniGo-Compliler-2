# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

 
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0210\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\58\u015f\n8\38\3")
        buf.write("8\38\78\u0164\n8\f8\168\u0167\138\39\39\39\39\59\u016d")
        buf.write("\n9\3:\3:\3:\7:\u0172\n:\f:\16:\u0175\13:\5:\u0177\n:")
        buf.write("\3;\3;\3;\6;\u017c\n;\r;\16;\u017d\3<\3<\3<\6<\u0183\n")
        buf.write("<\r<\16<\u0184\3=\3=\3=\6=\u018a\n=\r=\16=\u018b\3>\3")
        buf.write(">\5>\u0190\n>\3?\6?\u0193\n?\r?\16?\u0194\3?\3?\7?\u0199")
        buf.write("\n?\f?\16?\u019c\13?\3@\6@\u019f\n@\r@\16@\u01a0\3@\3")
        buf.write("@\7@\u01a5\n@\f@\16@\u01a8\13@\3@\3@\5@\u01ac\n@\3@\6")
        buf.write("@\u01af\n@\r@\16@\u01b0\3A\3A\3A\7A\u01b6\nA\fA\16A\u01b9")
        buf.write("\13A\3A\3A\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u01c9")
        buf.write("\nC\3D\3D\3D\3D\7D\u01cf\nD\fD\16D\u01d2\13D\3D\5D\u01d5")
        buf.write("\nD\3D\3D\3E\3E\3E\3E\3E\7E\u01de\nE\fE\16E\u01e1\13E")
        buf.write("\3E\3E\3E\3E\3E\3F\3F\3F\3G\6G\u01ec\nG\rG\16G\u01ed\3")
        buf.write("G\3G\3H\3H\3H\3I\3I\3I\7I\u01f8\nI\fI\16I\u01fb\13I\3")
        buf.write("I\3I\3J\3J\3J\7J\u0202\nJ\fJ\16J\u0205\13J\3J\3J\3J\3")
        buf.write("J\5J\u020b\nJ\3J\3J\3K\3K\2\2L\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\2m\2o\67q8s\2u\2w\2y\2{9}\2\177")
        buf.write("\2\u0081:\u0083\2\u0085\2\u0087;\u0089<\u008b=\u008d>")
        buf.write("\u008f\2\u0091?\u0093@\u0095A\3\2\23\4\2C\\c|\3\2\62;")
        buf.write("\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2")
        buf.write("\62;CHch\4\2GGgg\4\2--//\5\2\f\f$$^^\3\2\f\f\3\3\f\f\4")
        buf.write("\2,,\61\61\5\2\13\13\16\17\"\"\7\2$$^^ppttvv\2\u0227\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2{\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u0097\3\2\2\2\5\u009a\3\2\2\2\7\u009f\3\2\2")
        buf.write("\2\t\u00a3\3\2\2\2\13\u00aa\3\2\2\2\r\u00af\3\2\2\2\17")
        buf.write("\u00b4\3\2\2\2\21\u00bb\3\2\2\2\23\u00c5\3\2\2\2\25\u00cc")
        buf.write("\3\2\2\2\27\u00d0\3\2\2\2\31\u00d6\3\2\2\2\33\u00de\3")
        buf.write("\2\2\2\35\u00e4\3\2\2\2\37\u00e8\3\2\2\2!\u00f1\3\2\2")
        buf.write("\2#\u00f7\3\2\2\2%\u00fd\3\2\2\2\'\u0101\3\2\2\2)\u0106")
        buf.write("\3\2\2\2+\u010c\3\2\2\2-\u010e\3\2\2\2/\u0110\3\2\2\2")
        buf.write("\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116\3\2\2\2\67")
        buf.write("\u0119\3\2\2\29\u011c\3\2\2\2;\u011e\3\2\2\2=\u0121\3")
        buf.write("\2\2\2?\u0123\3\2\2\2A\u0126\3\2\2\2C\u0129\3\2\2\2E\u012c")
        buf.write("\3\2\2\2G\u012e\3\2\2\2I\u0130\3\2\2\2K\u0133\3\2\2\2")
        buf.write("M\u0136\3\2\2\2O\u0139\3\2\2\2Q\u013c\3\2\2\2S\u013f\3")
        buf.write("\2\2\2U\u0142\3\2\2\2W\u0144\3\2\2\2Y\u0146\3\2\2\2[\u0148")
        buf.write("\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2a\u014e\3\2\2\2")
        buf.write("c\u0150\3\2\2\2e\u0152\3\2\2\2g\u0154\3\2\2\2i\u0156\3")
        buf.write("\2\2\2k\u0158\3\2\2\2m\u015a\3\2\2\2o\u015e\3\2\2\2q\u016c")
        buf.write("\3\2\2\2s\u0176\3\2\2\2u\u0178\3\2\2\2w\u017f\3\2\2\2")
        buf.write("y\u0186\3\2\2\2{\u018f\3\2\2\2}\u0192\3\2\2\2\177\u019e")
        buf.write("\3\2\2\2\u0081\u01b2\3\2\2\2\u0083\u01bc\3\2\2\2\u0085")
        buf.write("\u01c8\3\2\2\2\u0087\u01ca\3\2\2\2\u0089\u01d8\3\2\2\2")
        buf.write("\u008b\u01e7\3\2\2\2\u008d\u01eb\3\2\2\2\u008f\u01f1\3")
        buf.write("\2\2\2\u0091\u01f4\3\2\2\2\u0093\u01fe\3\2\2\2\u0095\u020e")
        buf.write("\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099\7h\2\2\u0099\4")
        buf.write("\3\2\2\2\u009a\u009b\7g\2\2\u009b\u009c\7n\2\2\u009c\u009d")
        buf.write("\7u\2\2\u009d\u009e\7g\2\2\u009e\6\3\2\2\2\u009f\u00a0")
        buf.write("\7h\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7t\2\2\u00a2\b")
        buf.write("\3\2\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\u00a7\7w\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\n\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac")
        buf.write("\7w\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\f")
        buf.write("\3\2\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7{\2\2\u00b1\u00b2")
        buf.write("\7r\2\2\u00b2\u00b3\7g\2\2\u00b3\16\3\2\2\2\u00b4\u00b5")
        buf.write("\7u\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7w\2\2\u00b8\u00b9\7e\2\2\u00b9\u00ba\7v\2\2\u00ba\20")
        buf.write("\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7h\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\24\3\2\2\2\u00cc\u00cd")
        buf.write("\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\26")
        buf.write("\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7v\2\2\u00d5\30")
        buf.write("\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7c\2\2\u00dc\u00dd\7p\2\2\u00dd\32\3\2\2\2\u00de\u00df")
        buf.write("\7e\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2\u00e3\7v\2\2\u00e3\34\3\2\2\2\u00e4\u00e5")
        buf.write("\7x\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7t\2\2\u00e7\36")
        buf.write("\3\2\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0\7g\2\2\u00f0 \3")
        buf.write("\2\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7m\2\2\u00f6\"")
        buf.write("\3\2\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7i\2\2\u00fb\u00fc\7g\2\2\u00fc$\3")
        buf.write("\2\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7n\2\2\u0100&\3\2\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7w\2\2\u0104\u0105\7g\2\2\u0105(\3")
        buf.write("\2\2\2\u0106\u0107\7h\2\2\u0107\u0108\7c\2\2\u0108\u0109")
        buf.write("\7n\2\2\u0109\u010a\7u\2\2\u010a\u010b\7g\2\2\u010b*\3")
        buf.write("\2\2\2\u010c\u010d\7-\2\2\u010d,\3\2\2\2\u010e\u010f\7")
        buf.write("/\2\2\u010f.\3\2\2\2\u0110\u0111\7,\2\2\u0111\60\3\2\2")
        buf.write("\2\u0112\u0113\7\61\2\2\u0113\62\3\2\2\2\u0114\u0115\7")
        buf.write("\'\2\2\u0115\64\3\2\2\2\u0116\u0117\7?\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118\66\3\2\2\2\u0119\u011a\7#\2\2\u011a\u011b")
        buf.write("\7?\2\2\u011b8\3\2\2\2\u011c\u011d\7>\2\2\u011d:\3\2\2")
        buf.write("\2\u011e\u011f\7>\2\2\u011f\u0120\7?\2\2\u0120<\3\2\2")
        buf.write("\2\u0121\u0122\7@\2\2\u0122>\3\2\2\2\u0123\u0124\7@\2")
        buf.write("\2\u0124\u0125\7?\2\2\u0125@\3\2\2\2\u0126\u0127\7(\2")
        buf.write("\2\u0127\u0128\7(\2\2\u0128B\3\2\2\2\u0129\u012a\7~\2")
        buf.write("\2\u012a\u012b\7~\2\2\u012bD\3\2\2\2\u012c\u012d\7#\2")
        buf.write("\2\u012dF\3\2\2\2\u012e\u012f\7?\2\2\u012fH\3\2\2\2\u0130")
        buf.write("\u0131\7<\2\2\u0131\u0132\7?\2\2\u0132J\3\2\2\2\u0133")
        buf.write("\u0134\7-\2\2\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136")
        buf.write("\u0137\7/\2\2\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139")
        buf.write("\u013a\7,\2\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c")
        buf.write("\u013d\7\61\2\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f")
        buf.write("\u0140\7\'\2\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7\60\2\2\u0143V\3\2\2\2\u0144\u0145\7<\2\2\u0145")
        buf.write("X\3\2\2\2\u0146\u0147\7*\2\2\u0147Z\3\2\2\2\u0148\u0149")
        buf.write("\7+\2\2\u0149\\\3\2\2\2\u014a\u014b\7}\2\2\u014b^\3\2")
        buf.write("\2\2\u014c\u014d\7\177\2\2\u014d`\3\2\2\2\u014e\u014f")
        buf.write("\7]\2\2\u014fb\3\2\2\2\u0150\u0151\7_\2\2\u0151d\3\2\2")
        buf.write("\2\u0152\u0153\7.\2\2\u0153f\3\2\2\2\u0154\u0155\7=\2")
        buf.write("\2\u0155h\3\2\2\2\u0156\u0157\7a\2\2\u0157j\3\2\2\2\u0158")
        buf.write("\u0159\t\2\2\2\u0159l\3\2\2\2\u015a\u015b\t\3\2\2\u015b")
        buf.write("n\3\2\2\2\u015c\u015f\5k\66\2\u015d\u015f\7a\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015f\u0165\3\2\2\2")
        buf.write("\u0160\u0164\5k\66\2\u0161\u0164\5m\67\2\u0162\u0164\7")
        buf.write("a\2\2\u0163\u0160\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166p\3\2\2\2\u0167\u0165\3\2\2\2\u0168")
        buf.write("\u016d\5s:\2\u0169\u016d\5u;\2\u016a\u016d\5w<\2\u016b")
        buf.write("\u016d\5y=\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016dr\3\2\2\2\u016e")
        buf.write("\u0177\7\62\2\2\u016f\u0173\t\4\2\2\u0170\u0172\5m\67")
        buf.write("\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0177\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0176\u016e\3\2\2\2\u0176\u016f\3\2\2\2")
        buf.write("\u0177t\3\2\2\2\u0178\u0179\7\62\2\2\u0179\u017b\t\5\2")
        buf.write("\2\u017a\u017c\t\6\2\2\u017b\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("v\3\2\2\2\u017f\u0180\7\62\2\2\u0180\u0182\t\7\2\2\u0181")
        buf.write("\u0183\t\b\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185x\3\2\2")
        buf.write("\2\u0186\u0187\7\62\2\2\u0187\u0189\t\t\2\2\u0188\u018a")
        buf.write("\t\n\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cz\3\2\2\2\u018d")
        buf.write("\u0190\5}?\2\u018e\u0190\5\177@\2\u018f\u018d\3\2\2\2")
        buf.write("\u018f\u018e\3\2\2\2\u0190|\3\2\2\2\u0191\u0193\5m\67")
        buf.write("\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u019a\7\60\2\2\u0197\u0199\5m\67\2\u0198\u0197\3\2\2")
        buf.write("\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b~\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019f")
        buf.write("\5m\67\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a6\7\60\2\2\u01a3\u01a5\5m\67\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a9\u01ab\t\13\2\2\u01aa\u01ac\t\f\2\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad")
        buf.write("\u01af\5m\67\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u0080\3")
        buf.write("\2\2\2\u01b2\u01b7\7$\2\2\u01b3\u01b6\5\u0083B\2\u01b4")
        buf.write("\u01b6\5\u0085C\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2")
        buf.write("\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u01bb\7$\2\2\u01bb\u0082\3\2\2\2\u01bc\u01bd\n\r\2\2")
        buf.write("\u01bd\u0084\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c9\7")
        buf.write("p\2\2\u01c0\u01c1\7^\2\2\u01c1\u01c9\7v\2\2\u01c2\u01c3")
        buf.write("\7^\2\2\u01c3\u01c9\7t\2\2\u01c4\u01c5\7^\2\2\u01c5\u01c9")
        buf.write("\7$\2\2\u01c6\u01c7\7^\2\2\u01c7\u01c9\7^\2\2\u01c8\u01be")
        buf.write("\3\2\2\2\u01c8\u01c0\3\2\2\2\u01c8\u01c2\3\2\2\2\u01c8")
        buf.write("\u01c4\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u0086\3\2\2\2")
        buf.write("\u01ca\u01cb\7\61\2\2\u01cb\u01cc\7\61\2\2\u01cc\u01d0")
        buf.write("\3\2\2\2\u01cd\u01cf\n\16\2\2\u01ce\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d5\t")
        buf.write("\17\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d7\bD\2\2\u01d7\u0088\3\2\2\2\u01d8\u01d9\7\61\2\2")
        buf.write("\u01d9\u01da\7,\2\2\u01da\u01df\3\2\2\2\u01db\u01de\n")
        buf.write("\20\2\2\u01dc\u01de\5\u0089E\2\u01dd\u01db\3\2\2\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2")
        buf.write("\u01df\u01e0\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01df\3")
        buf.write("\2\2\2\u01e2\u01e3\7,\2\2\u01e3\u01e4\7\61\2\2\u01e4\u01e5")
        buf.write("\3\2\2\2\u01e5\u01e6\bE\2\2\u01e6\u008a\3\2\2\2\u01e7")
        buf.write("\u01e8\7\f\2\2\u01e8\u01e9\bF\3\2\u01e9\u008c\3\2\2\2")
        buf.write("\u01ea\u01ec\t\21\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f0\bG\2\2\u01f0\u008e\3\2\2\2")
        buf.write("\u01f1\u01f2\7^\2\2\u01f2\u01f3\n\22\2\2\u01f3\u0090\3")
        buf.write("\2\2\2\u01f4\u01f9\7$\2\2\u01f5\u01f8\5\u0083B\2\u01f6")
        buf.write("\u01f8\5\u0085C\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2")
        buf.write("\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa")
        buf.write("\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc")
        buf.write("\u01fd\5\u008fH\2\u01fd\u0092\3\2\2\2\u01fe\u0203\7$\2")
        buf.write("\2\u01ff\u0202\5\u0083B\2\u0200\u0202\5\u0085C\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u020a\3")
        buf.write("\2\2\2\u0205\u0203\3\2\2\2\u0206\u020b\7\f\2\2\u0207\u0208")
        buf.write("\7\17\2\2\u0208\u020b\7\f\2\2\u0209\u020b\7\2\2\3\u020a")
        buf.write("\u0206\3\2\2\2\u020a\u0207\3\2\2\2\u020a\u0209\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u020d\bJ\4\2\u020d\u0094\3")
        buf.write("\2\2\2\u020e\u020f\13\2\2\2\u020f\u0096\3\2\2\2 \2\u015e")
        buf.write("\u0163\u0165\u016c\u0173\u0176\u017d\u0184\u018b\u018f")
        buf.write("\u0194\u019a\u01a0\u01a6\u01ab\u01b0\u01b5\u01b7\u01c8")
        buf.write("\u01d0\u01d4\u01dd\u01df\u01ed\u01f7\u01f9\u0201\u0203")
        buf.write("\u020a\5\b\2\2\3F\2\3J\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    PLUS = 21
    MINUS = 22
    MULTI = 23
    DIV = 24
    MODULO = 25
    EQUAL = 26
    NOT_EQUAL = 27
    LESS_THAN = 28
    LESS_EQUAL = 29
    GREATER_THAN = 30
    GREATER_EQUAL = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGN = 35
    ASSIGN1 = 36
    PLUS_EQUAL = 37
    MINUS_EQUAL = 38
    MULTI_EQUAL = 39
    DIV_EQUAL = 40
    MODULO_EQUAL = 41
    DOT = 42
    COLON = 43
    OPEN_ROUND = 44
    CLOSE_ROUND = 45
    OPEN_CURVE = 46
    CLOSE_CURVE = 47
    OPEN_SQUARE = 48
    CLOSE_SQUARE = 49
    COMMA = 50
    SEMICOLON = 51
    UNDERSCORE = 52
    ID = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    STRING_LIT = 56
    COMMENT_INLINE = 57
    COMMENT_BLOCK = 58
    NL = 59
    WS = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", 
            "'_'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MULTI", 
            "DIV", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", 
            "GREATER_THAN", "GREATER_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ASSIGN1", "PLUS_EQUAL", "MINUS_EQUAL", "MULTI_EQUAL", "DIV_EQUAL", 
            "MODULO_EQUAL", "DOT", "COLON", "OPEN_ROUND", "CLOSE_ROUND", 
            "OPEN_CURVE", "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", 
            "COMMA", "SEMICOLON", "UNDERSCORE", "ID", "INT_LIT", "FLOAT_LIT", 
            "STRING_LIT", "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "PLUS", "MINUS", "MULTI", "DIV", "MODULO", "EQUAL", "NOT_EQUAL", 
                  "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ASSIGN1", "PLUS_EQUAL", 
                  "MINUS_EQUAL", "MULTI_EQUAL", "DIV_EQUAL", "MODULO_EQUAL", 
                  "DOT", "COLON", "OPEN_ROUND", "CLOSE_ROUND", "OPEN_CURVE", 
                  "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", "COMMA", 
                  "SEMICOLON", "UNDERSCORE", "Letter", "Digit", "ID", "INT_LIT", 
                  "Decimal", "Binary", "Octal", "Hex", "FLOAT_LIT", "No_exponent", 
                  "Exponent", "STRING_LIT", "String_Character", "String_Escape", 
                  "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", "ILL_ESC", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[68] = self.NL_action 
            actions[72] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                # print(f"prev_token: {self._prev_token_type}")
                if(self._prev_token_type in {self.ID,self.INT_LIT, self.FLOAT_LIT, self.TRUE, self.FALSE, self.STRING_LIT, self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.RETURN, self.CONTINUE, self.BREAK, self.CLOSE_ROUND, self.CLOSE_CURVE, self.CLOSE_SQUARE}):
                    # print(f"Im in, before me: {self._prev_token_type}")
                    # self.emitToken(self.commonToken(self.SEMICOLON, ';'))
                    self.text = ';'  
                    self.type = self.SEMICOLON
                else:
                    self.skip()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                if(len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
                    self.text = self.text[:-2]
                elif(self.text[-1] == '\n'):
                    self.text = self.text[:-1]
                else:
                    self.text = self.text

     


