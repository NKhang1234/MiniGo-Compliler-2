# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0292\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\6\2\u0096\n")
        buf.write("\2\r\2\16\2\u0097\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\u00a2\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00aa\n\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00b6\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u00c4\n")
        buf.write("\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00da\n\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\5\16\u00e1\n\16\3\16\3\16\3\17")
        buf.write("\3\17\5\17\u00e7\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00ee")
        buf.write("\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00f7\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u010b\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u011b\n\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\27\3\27\5\27\u0124\n\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u012b\n\30\3\31\3\31\3\31\3\32\3\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u013c")
        buf.write("\n\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u014e\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0159\n\37")
        buf.write("\3 \3 \3 \3 \5 \u015f\n \3!\3!\3!\3!\3!\3\"\3\"\5\"\u0168")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u016f\n#\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\5&\u017c\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0183\n")
        buf.write("\'\3(\3(\3)\3)\3)\3)\3)\3)\7)\u018d\n)\f)\16)\u0190\13")
        buf.write(")\3*\3*\3*\3*\3*\3*\7*\u0198\n*\f*\16*\u019b\13*\3+\3")
        buf.write("+\3+\3+\3+\3+\7+\u01a3\n+\f+\16+\u01a6\13+\3,\3,\3,\3")
        buf.write(",\3,\3,\7,\u01ae\n,\f,\16,\u01b1\13,\3-\3-\3-\3-\3-\3")
        buf.write("-\7-\u01b9\n-\f-\16-\u01bc\13-\3.\3.\3.\5.\u01c1\n.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u01d2\n")
        buf.write("/\f/\16/\u01d5\13/\3\60\3\60\3\60\3\60\3\60\5\60\u01dc")
        buf.write("\n\60\3\61\3\61\3\61\5\61\u01e1\n\61\3\62\3\62\3\62\5")
        buf.write("\62\u01e6\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01f1\n\63\3\64\3\64\5\64\u01f5\n\64\3\65\3")
        buf.write("\65\3\65\3\65\5\65\u01fb\n\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u0206\n\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\38\38\38\58\u0210\n8\38\38\38\38\38\78\u0217")
        buf.write("\n8\f8\168\u021a\138\39\39\39\39\39\59\u0221\n9\3:\3:")
        buf.write("\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0241\n=\3>\3>\3>\5")
        buf.write(">\u0246\n>\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3A\3A\5A\u025c\nA\3B\3B\3B\5B\u0261\nB\3B\3")
        buf.write("B\3B\3C\3C\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\5")
        buf.write("I\u0288\nI\3I\3I\3J\3J\5J\u028e\nJ\3J\3J\3J\2\tPRTVX\\")
        buf.write("nK\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\2\13")
        buf.write("\4\2\13\16\67\67\3\2\678\4\2\24\268:\3\2\34!\3\2\27\30")
        buf.write("\3\2\31\33\4\2\30\30$$\3\2&+\3\2\66\67\2\u028e\2\u0095")
        buf.write("\3\2\2\2\4\u00a1\3\2\2\2\6\u00a9\3\2\2\2\b\u00ab\3\2\2")
        buf.write("\2\n\u00b5\3\2\2\2\f\u00b7\3\2\2\2\16\u00c3\3\2\2\2\20")
        buf.write("\u00c5\3\2\2\2\22\u00c7\3\2\2\2\24\u00cb\3\2\2\2\26\u00d3")
        buf.write("\3\2\2\2\30\u00d9\3\2\2\2\32\u00db\3\2\2\2\34\u00e6\3")
        buf.write("\2\2\2\36\u00ed\3\2\2\2 \u00ef\3\2\2\2\"\u00f6\3\2\2\2")
        buf.write("$\u010a\3\2\2\2&\u010c\3\2\2\2(\u0112\3\2\2\2*\u0114\3")
        buf.write("\2\2\2,\u0123\3\2\2\2.\u012a\3\2\2\2\60\u012c\3\2\2\2")
        buf.write("\62\u012f\3\2\2\2\64\u0131\3\2\2\2\66\u0142\3\2\2\28\u014d")
        buf.write("\3\2\2\2:\u014f\3\2\2\2<\u0158\3\2\2\2>\u015e\3\2\2\2")
        buf.write("@\u0160\3\2\2\2B\u0167\3\2\2\2D\u016e\3\2\2\2F\u0170\3")
        buf.write("\2\2\2H\u0174\3\2\2\2J\u017b\3\2\2\2L\u0182\3\2\2\2N\u0184")
        buf.write("\3\2\2\2P\u0186\3\2\2\2R\u0191\3\2\2\2T\u019c\3\2\2\2")
        buf.write("V\u01a7\3\2\2\2X\u01b2\3\2\2\2Z\u01c0\3\2\2\2\\\u01c2")
        buf.write("\3\2\2\2^\u01db\3\2\2\2`\u01e0\3\2\2\2b\u01e5\3\2\2\2")
        buf.write("d\u01f0\3\2\2\2f\u01f4\3\2\2\2h\u01fa\3\2\2\2j\u0205\3")
        buf.write("\2\2\2l\u0207\3\2\2\2n\u020f\3\2\2\2p\u0220\3\2\2\2r\u0222")
        buf.write("\3\2\2\2t\u0224\3\2\2\2v\u0227\3\2\2\2x\u0240\3\2\2\2")
        buf.write("z\u0245\3\2\2\2|\u0247\3\2\2\2~\u024e\3\2\2\2\u0080\u025b")
        buf.write("\3\2\2\2\u0082\u025d\3\2\2\2\u0084\u0265\3\2\2\2\u0086")
        buf.write("\u0267\3\2\2\2\u0088\u0269\3\2\2\2\u008a\u026d\3\2\2\2")
        buf.write("\u008c\u0279\3\2\2\2\u008e\u027c\3\2\2\2\u0090\u0287\3")
        buf.write("\2\2\2\u0092\u028b\3\2\2\2\u0094\u0096\5\4\3\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\7\2\2\3")
        buf.write("\u009a\3\3\2\2\2\u009b\u00a2\5\f\7\2\u009c\u00a2\5\24")
        buf.write("\13\2\u009d\u00a2\5$\23\2\u009e\u00a2\5&\24\2\u009f\u00a2")
        buf.write("\5*\26\2\u00a0\u00a2\5\64\33\2\u00a1\u009b\3\2\2\2\u00a1")
        buf.write("\u009c\3\2\2\2\u00a1\u009d\3\2\2\2\u00a1\u009e\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\5\3\2\2")
        buf.write("\2\u00a3\u00aa\7\f\2\2\u00a4\u00aa\7\r\2\2\u00a5\u00aa")
        buf.write("\7\16\2\2\u00a6\u00aa\7\13\2\2\u00a7\u00aa\5\b\5\2\u00a8")
        buf.write("\u00aa\7\67\2\2\u00a9\u00a3\3\2\2\2\u00a9\u00a4\3\2\2")
        buf.write("\2\u00a9\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7")
        buf.write("\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\7\3\2\2\2\u00ab\u00ac")
        buf.write("\5\n\6\2\u00ac\u00ad\t\2\2\2\u00ad\t\3\2\2\2\u00ae\u00af")
        buf.write("\7\62\2\2\u00af\u00b0\t\3\2\2\u00b0\u00b1\7\63\2\2\u00b1")
        buf.write("\u00b6\5\n\6\2\u00b2\u00b3\7\62\2\2\u00b3\u00b4\t\3\2")
        buf.write("\2\u00b4\u00b6\7\63\2\2\u00b5\u00ae\3\2\2\2\u00b5\u00b2")
        buf.write("\3\2\2\2\u00b6\13\3\2\2\2\u00b7\u00b8\7\b\2\2\u00b8\u00b9")
        buf.write("\7\67\2\2\u00b9\u00ba\7\t\2\2\u00ba\u00bb\7\60\2\2\u00bb")
        buf.write("\u00bc\5\16\b\2\u00bc\u00bd\7\61\2\2\u00bd\u00be\7\65")
        buf.write("\2\2\u00be\r\3\2\2\2\u00bf\u00c0\5\20\t\2\u00c0\u00c1")
        buf.write("\5\16\b\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4\5\20\t\2\u00c3")
        buf.write("\u00bf\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\17\3\2\2\2\u00c5")
        buf.write("\u00c6\5\22\n\2\u00c6\21\3\2\2\2\u00c7\u00c8\7\67\2\2")
        buf.write("\u00c8\u00c9\5\6\4\2\u00c9\u00ca\7\65\2\2\u00ca\23\3\2")
        buf.write("\2\2\u00cb\u00cc\7\b\2\2\u00cc\u00cd\7\67\2\2\u00cd\u00ce")
        buf.write("\7\n\2\2\u00ce\u00cf\7\60\2\2\u00cf\u00d0\5\26\f\2\u00d0")
        buf.write("\u00d1\7\61\2\2\u00d1\u00d2\7\65\2\2\u00d2\25\3\2\2\2")
        buf.write("\u00d3\u00d4\5\30\r\2\u00d4\27\3\2\2\2\u00d5\u00d6\5\32")
        buf.write("\16\2\u00d6\u00d7\5\30\r\2\u00d7\u00da\3\2\2\2\u00d8\u00da")
        buf.write("\5\32\16\2\u00d9\u00d5\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da")
        buf.write("\31\3\2\2\2\u00db\u00dc\7\67\2\2\u00dc\u00dd\7.\2\2\u00dd")
        buf.write("\u00de\5\34\17\2\u00de\u00e0\7/\2\2\u00df\u00e1\5\6\4")
        buf.write("\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e3\7\65\2\2\u00e3\33\3\2\2\2\u00e4\u00e7")
        buf.write("\5\36\20\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\35\3\2\2\2\u00e8\u00e9\5 \21\2\u00e9")
        buf.write("\u00ea\7\64\2\2\u00ea\u00eb\5\36\20\2\u00eb\u00ee\3\2")
        buf.write("\2\2\u00ec\u00ee\5 \21\2\u00ed\u00e8\3\2\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\37\3\2\2\2\u00ef\u00f0\5\"\22\2\u00f0\u00f1")
        buf.write("\5\6\4\2\u00f1!\3\2\2\2\u00f2\u00f3\7\67\2\2\u00f3\u00f4")
        buf.write("\7\64\2\2\u00f4\u00f7\5\"\22\2\u00f5\u00f7\7\67\2\2\u00f6")
        buf.write("\u00f2\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7#\3\2\2\2\u00f8")
        buf.write("\u00f9\7\20\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fb\5\6\4")
        buf.write("\2\u00fb\u00fc\7%\2\2\u00fc\u00fd\5P)\2\u00fd\u00fe\7")
        buf.write("\65\2\2\u00fe\u010b\3\2\2\2\u00ff\u0100\7\20\2\2\u0100")
        buf.write("\u0101\7\67\2\2\u0101\u0102\7%\2\2\u0102\u0103\5P)\2\u0103")
        buf.write("\u0104\7\65\2\2\u0104\u010b\3\2\2\2\u0105\u0106\7\20\2")
        buf.write("\2\u0106\u0107\7\67\2\2\u0107\u0108\5\6\4\2\u0108\u0109")
        buf.write("\7\65\2\2\u0109\u010b\3\2\2\2\u010a\u00f8\3\2\2\2\u010a")
        buf.write("\u00ff\3\2\2\2\u010a\u0105\3\2\2\2\u010b%\3\2\2\2\u010c")
        buf.write("\u010d\7\17\2\2\u010d\u010e\7\67\2\2\u010e\u010f\7%\2")
        buf.write("\2\u010f\u0110\5P)\2\u0110\u0111\7\65\2\2\u0111\'\3\2")
        buf.write("\2\2\u0112\u0113\t\4\2\2\u0113)\3\2\2\2\u0114\u0115\7")
        buf.write("\7\2\2\u0115\u0116\7\67\2\2\u0116\u0117\7.\2\2\u0117\u0118")
        buf.write("\5,\27\2\u0118\u011a\7/\2\2\u0119\u011b\5\6\4\2\u011a")
        buf.write("\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u011d\7\60\2\2\u011d\u011e\5\62\32\2\u011e\u011f")
        buf.write("\7\61\2\2\u011f\u0120\7\65\2\2\u0120+\3\2\2\2\u0121\u0124")
        buf.write("\5.\30\2\u0122\u0124\3\2\2\2\u0123\u0121\3\2\2\2\u0123")
        buf.write("\u0122\3\2\2\2\u0124-\3\2\2\2\u0125\u0126\5\60\31\2\u0126")
        buf.write("\u0127\7\64\2\2\u0127\u0128\5.\30\2\u0128\u012b\3\2\2")
        buf.write("\2\u0129\u012b\5\60\31\2\u012a\u0125\3\2\2\2\u012a\u0129")
        buf.write("\3\2\2\2\u012b/\3\2\2\2\u012c\u012d\5\"\22\2\u012d\u012e")
        buf.write("\5\6\4\2\u012e\61\3\2\2\2\u012f\u0130\5f\64\2\u0130\63")
        buf.write("\3\2\2\2\u0131\u0132\7\7\2\2\u0132\u0133\7.\2\2\u0133")
        buf.write("\u0134\7\67\2\2\u0134\u0135\7\67\2\2\u0135\u0136\7/\2")
        buf.write("\2\u0136\u0137\7\67\2\2\u0137\u0138\7.\2\2\u0138\u0139")
        buf.write("\5,\27\2\u0139\u013b\7/\2\2\u013a\u013c\5\6\4\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013e\7\60\2\2\u013e\u013f\5\62\32\2\u013f\u0140")
        buf.write("\7\61\2\2\u0140\u0141\7\65\2\2\u0141\65\3\2\2\2\u0142")
        buf.write("\u0143\58\35\2\u0143\u0144\t\2\2\2\u0144\u0145\5:\36\2")
        buf.write("\u0145\67\3\2\2\2\u0146\u0147\7\62\2\2\u0147\u0148\t\3")
        buf.write("\2\2\u0148\u0149\7\63\2\2\u0149\u014e\58\35\2\u014a\u014b")
        buf.write("\7\62\2\2\u014b\u014c\t\3\2\2\u014c\u014e\7\63\2\2\u014d")
        buf.write("\u0146\3\2\2\2\u014d\u014a\3\2\2\2\u014e9\3\2\2\2\u014f")
        buf.write("\u0150\7\60\2\2\u0150\u0151\5<\37\2\u0151\u0152\7\61\2")
        buf.write("\2\u0152;\3\2\2\2\u0153\u0154\5> \2\u0154\u0155\7\64\2")
        buf.write("\2\u0155\u0156\5<\37\2\u0156\u0159\3\2\2\2\u0157\u0159")
        buf.write("\5> \2\u0158\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u0159=")
        buf.write("\3\2\2\2\u015a\u015f\5(\25\2\u015b\u015f\5@!\2\u015c\u015f")
        buf.write("\5:\36\2\u015d\u015f\7\67\2\2\u015e\u015a\3\2\2\2\u015e")
        buf.write("\u015b\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f?\3\2\2\2\u0160\u0161\7\67\2\2\u0161\u0162\7\60")
        buf.write("\2\2\u0162\u0163\5B\"\2\u0163\u0164\7\61\2\2\u0164A\3")
        buf.write("\2\2\2\u0165\u0168\5D#\2\u0166\u0168\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168C\3\2\2\2\u0169\u016a")
        buf.write("\5F$\2\u016a\u016b\7\64\2\2\u016b\u016c\5D#\2\u016c\u016f")
        buf.write("\3\2\2\2\u016d\u016f\5F$\2\u016e\u0169\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016fE\3\2\2\2\u0170\u0171\7\67\2\2\u0171\u0172")
        buf.write("\7-\2\2\u0172\u0173\5P)\2\u0173G\3\2\2\2\u0174\u0175\7")
        buf.write("\67\2\2\u0175\u0176\7.\2\2\u0176\u0177\5J&\2\u0177\u0178")
        buf.write("\7/\2\2\u0178I\3\2\2\2\u0179\u017c\5L\'\2\u017a\u017c")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("K\3\2\2\2\u017d\u017e\5N(\2\u017e\u017f\7\64\2\2\u017f")
        buf.write("\u0180\5L\'\2\u0180\u0183\3\2\2\2\u0181\u0183\5N(\2\u0182")
        buf.write("\u017d\3\2\2\2\u0182\u0181\3\2\2\2\u0183M\3\2\2\2\u0184")
        buf.write("\u0185\5P)\2\u0185O\3\2\2\2\u0186\u0187\b)\1\2\u0187\u0188")
        buf.write("\5R*\2\u0188\u018e\3\2\2\2\u0189\u018a\f\4\2\2\u018a\u018b")
        buf.write("\7#\2\2\u018b\u018d\5R*\2\u018c\u0189\3\2\2\2\u018d\u0190")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("Q\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\b*\1\2\u0192")
        buf.write("\u0193\5T+\2\u0193\u0199\3\2\2\2\u0194\u0195\f\4\2\2\u0195")
        buf.write("\u0196\7\"\2\2\u0196\u0198\5T+\2\u0197\u0194\3\2\2\2\u0198")
        buf.write("\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019aS\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019d\b+\1\2")
        buf.write("\u019d\u019e\5V,\2\u019e\u01a4\3\2\2\2\u019f\u01a0\f\4")
        buf.write("\2\2\u01a0\u01a1\t\5\2\2\u01a1\u01a3\5V,\2\u01a2\u019f")
        buf.write("\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5U\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7")
        buf.write("\u01a8\b,\1\2\u01a8\u01a9\5X-\2\u01a9\u01af\3\2\2\2\u01aa")
        buf.write("\u01ab\f\4\2\2\u01ab\u01ac\t\6\2\2\u01ac\u01ae\5X-\2\u01ad")
        buf.write("\u01aa\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0W\3\2\2\2\u01b1\u01af\3\2\2")
        buf.write("\2\u01b2\u01b3\b-\1\2\u01b3\u01b4\5Z.\2\u01b4\u01ba\3")
        buf.write("\2\2\2\u01b5\u01b6\f\4\2\2\u01b6\u01b7\t\7\2\2\u01b7\u01b9")
        buf.write("\5Z.\2\u01b8\u01b5\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bbY\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bd\u01be\t\b\2\2\u01be\u01c1\5Z.\2\u01bf\u01c1")
        buf.write("\5\\/\2\u01c0\u01bd\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1")
        buf.write("[\3\2\2\2\u01c2\u01c3\b/\1\2\u01c3\u01c4\5^\60\2\u01c4")
        buf.write("\u01d3\3\2\2\2\u01c5\u01c6\f\6\2\2\u01c6\u01d2\5d\63\2")
        buf.write("\u01c7\u01c8\f\5\2\2\u01c8\u01c9\7,\2\2\u01c9\u01d2\7")
        buf.write("\67\2\2\u01ca\u01cb\f\4\2\2\u01cb\u01cc\7,\2\2\u01cc\u01cd")
        buf.write("\7\67\2\2\u01cd\u01ce\7.\2\2\u01ce\u01cf\5J&\2\u01cf\u01d0")
        buf.write("\7/\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01c5\3\2\2\2\u01d1")
        buf.write("\u01c7\3\2\2\2\u01d1\u01ca\3\2\2\2\u01d2\u01d5\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4]\3\2\2")
        buf.write("\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\7.\2\2\u01d7\u01d8")
        buf.write("\5P)\2\u01d8\u01d9\7/\2\2\u01d9\u01dc\3\2\2\2\u01da\u01dc")
        buf.write("\5`\61\2\u01db\u01d6\3\2\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("_\3\2\2\2\u01dd\u01e1\5b\62\2\u01de\u01e1\5H%\2\u01df")
        buf.write("\u01e1\7\67\2\2\u01e0\u01dd\3\2\2\2\u01e0\u01de\3\2\2")
        buf.write("\2\u01e0\u01df\3\2\2\2\u01e1a\3\2\2\2\u01e2\u01e6\5(\25")
        buf.write("\2\u01e3\u01e6\5\66\34\2\u01e4\u01e6\5@!\2\u01e5\u01e2")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6")
        buf.write("c\3\2\2\2\u01e7\u01e8\7\62\2\2\u01e8\u01e9\5P)\2\u01e9")
        buf.write("\u01ea\7\63\2\2\u01ea\u01eb\5d\63\2\u01eb\u01f1\3\2\2")
        buf.write("\2\u01ec\u01ed\7\62\2\2\u01ed\u01ee\5P)\2\u01ee\u01ef")
        buf.write("\7\63\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01e7\3\2\2\2\u01f0")
        buf.write("\u01ec\3\2\2\2\u01f1e\3\2\2\2\u01f2\u01f5\5h\65\2\u01f3")
        buf.write("\u01f5\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2")
        buf.write("\u01f5g\3\2\2\2\u01f6\u01f7\5j\66\2\u01f7\u01f8\5h\65")
        buf.write("\2\u01f8\u01fb\3\2\2\2\u01f9\u01fb\5j\66\2\u01fa\u01f6")
        buf.write("\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fbi\3\2\2\2\u01fc\u0206")
        buf.write("\5$\23\2\u01fd\u0206\5&\24\2\u01fe\u0206\5l\67\2\u01ff")
        buf.write("\u0206\5t;\2\u0200\u0206\5z>\2\u0201\u0206\5\u008cG\2")
        buf.write("\u0202\u0206\5\u008eH\2\u0203\u0206\5\u0090I\2\u0204\u0206")
        buf.write("\5\u0092J\2\u0205\u01fc\3\2\2\2\u0205\u01fd\3\2\2\2\u0205")
        buf.write("\u01fe\3\2\2\2\u0205\u01ff\3\2\2\2\u0205\u0200\3\2\2\2")
        buf.write("\u0205\u0201\3\2\2\2\u0205\u0202\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0205\u0204\3\2\2\2\u0206k\3\2\2\2\u0207\u0208")
        buf.write("\5n8\2\u0208\u0209\t\t\2\2\u0209\u020a\5r:\2\u020a\u020b")
        buf.write("\7\65\2\2\u020bm\3\2\2\2\u020c\u020d\b8\1\2\u020d\u0210")
        buf.write("\7\67\2\2\u020e\u0210\5p9\2\u020f\u020c\3\2\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u0210\u0218\3\2\2\2\u0211\u0212\f\6\2\2")
        buf.write("\u0212\u0217\5d\63\2\u0213\u0214\f\5\2\2\u0214\u0215\7")
        buf.write(",\2\2\u0215\u0217\7\67\2\2\u0216\u0211\3\2\2\2\u0216\u0213")
        buf.write("\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219o\3\2\2\2\u021a\u0218\3\2\2\2\u021b")
        buf.write("\u021c\7.\2\2\u021c\u021d\5P)\2\u021d\u021e\7/\2\2\u021e")
        buf.write("\u0221\3\2\2\2\u021f\u0221\5`\61\2\u0220\u021b\3\2\2\2")
        buf.write("\u0220\u021f\3\2\2\2\u0221q\3\2\2\2\u0222\u0223\5P)\2")
        buf.write("\u0223s\3\2\2\2\u0224\u0225\5v<\2\u0225\u0226\7\65\2\2")
        buf.write("\u0226u\3\2\2\2\u0227\u0228\7\3\2\2\u0228\u0229\7.\2\2")
        buf.write("\u0229\u022a\5P)\2\u022a\u022b\7/\2\2\u022b\u022c\7\60")
        buf.write("\2\2\u022c\u022d\5f\64\2\u022d\u022e\7\61\2\2\u022e\u022f")
        buf.write("\5x=\2\u022fw\3\2\2\2\u0230\u0231\7\4\2\2\u0231\u0232")
        buf.write("\7\3\2\2\u0232\u0233\7.\2\2\u0233\u0234\5P)\2\u0234\u0235")
        buf.write("\7/\2\2\u0235\u0236\7\60\2\2\u0236\u0237\5f\64\2\u0237")
        buf.write("\u0238\7\61\2\2\u0238\u0239\5x=\2\u0239\u0241\3\2\2\2")
        buf.write("\u023a\u023b\7\4\2\2\u023b\u023c\7\60\2\2\u023c\u023d")
        buf.write("\5f\64\2\u023d\u023e\7\61\2\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u0241\3\2\2\2\u0240\u0230\3\2\2\2\u0240\u023a\3\2\2\2")
        buf.write("\u0240\u023f\3\2\2\2\u0241y\3\2\2\2\u0242\u0246\5|?\2")
        buf.write("\u0243\u0246\5~@\2\u0244\u0246\5\u008aF\2\u0245\u0242")
        buf.write("\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0244\3\2\2\2\u0246")
        buf.write("{\3\2\2\2\u0247\u0248\7\5\2\2\u0248\u0249\5P)\2\u0249")
        buf.write("\u024a\7\60\2\2\u024a\u024b\5f\64\2\u024b\u024c\7\61\2")
        buf.write("\2\u024c\u024d\7\65\2\2\u024d}\3\2\2\2\u024e\u024f\7\5")
        buf.write("\2\2\u024f\u0250\5\u0080A\2\u0250\u0251\7\65\2\2\u0251")
        buf.write("\u0252\5\u0084C\2\u0252\u0253\7\65\2\2\u0253\u0254\5\u0086")
        buf.write("D\2\u0254\u0255\7\60\2\2\u0255\u0256\5f\64\2\u0256\u0257")
        buf.write("\7\61\2\2\u0257\u0258\7\65\2\2\u0258\177\3\2\2\2\u0259")
        buf.write("\u025c\5\u0088E\2\u025a\u025c\5\u0082B\2\u025b\u0259\3")
        buf.write("\2\2\2\u025b\u025a\3\2\2\2\u025c\u0081\3\2\2\2\u025d\u025e")
        buf.write("\7\20\2\2\u025e\u0260\7\67\2\2\u025f\u0261\5\6\4\2\u0260")
        buf.write("\u025f\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0262\3\2\2\2")
        buf.write("\u0262\u0263\7%\2\2\u0263\u0264\5P)\2\u0264\u0083\3\2")
        buf.write("\2\2\u0265\u0266\5P)\2\u0266\u0085\3\2\2\2\u0267\u0268")
        buf.write("\5\u0088E\2\u0268\u0087\3\2\2\2\u0269\u026a\7\67\2\2\u026a")
        buf.write("\u026b\t\t\2\2\u026b\u026c\5P)\2\u026c\u0089\3\2\2\2\u026d")
        buf.write("\u026e\7\5\2\2\u026e\u026f\t\n\2\2\u026f\u0270\7\64\2")
        buf.write("\2\u0270\u0271\7\67\2\2\u0271\u0272\7&\2\2\u0272\u0273")
        buf.write("\7\23\2\2\u0273\u0274\5P)\2\u0274\u0275\7\60\2\2\u0275")
        buf.write("\u0276\5f\64\2\u0276\u0277\7\61\2\2\u0277\u0278\7\65\2")
        buf.write("\2\u0278\u008b\3\2\2\2\u0279\u027a\7\22\2\2\u027a\u027b")
        buf.write("\7\65\2\2\u027b\u008d\3\2\2\2\u027c\u027d\7\21\2\2\u027d")
        buf.write("\u027e\7\65\2\2\u027e\u008f\3\2\2\2\u027f\u0288\5H%\2")
        buf.write("\u0280\u0281\5\\/\2\u0281\u0282\7,\2\2\u0282\u0283\7\67")
        buf.write("\2\2\u0283\u0284\7.\2\2\u0284\u0285\5J&\2\u0285\u0286")
        buf.write("\7/\2\2\u0286\u0288\3\2\2\2\u0287\u027f\3\2\2\2\u0287")
        buf.write("\u0280\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\7\65\2")
        buf.write("\2\u028a\u0091\3\2\2\2\u028b\u028d\7\6\2\2\u028c\u028e")
        buf.write("\5P)\2\u028d\u028c\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028f")
        buf.write("\3\2\2\2\u028f\u0290\7\65\2\2\u0290\u0093\3\2\2\2\61\u0097")
        buf.write("\u00a1\u00a9\u00b5\u00c3\u00d9\u00e0\u00e6\u00ed\u00f6")
        buf.write("\u010a\u011a\u0123\u012a\u013b\u014d\u0158\u015e\u0167")
        buf.write("\u016e\u017b\u0182\u018e\u0199\u01a4\u01af\u01ba\u01c0")
        buf.write("\u01d1\u01d3\u01db\u01e0\u01e5\u01f0\u01f4\u01fa\u0205")
        buf.write("\u020f\u0216\u0218\u0220\u0240\u0245\u025b\u0260\u0287")
        buf.write("\u028d")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "'_'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MULTI", 
                      "DIV", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                      "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "AND", 
                      "OR", "NOT", "ASSIGN", "ASSIGN1", "PLUS_EQUAL", "MINUS_EQUAL", 
                      "MULTI_EQUAL", "DIV_EQUAL", "MODULO_EQUAL", "DOT", 
                      "COLON", "OPEN_ROUND", "CLOSE_ROUND", "OPEN_CURVE", 
                      "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", "COMMA", 
                      "SEMICOLON", "UNDERSCORE", "ID", "INT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "COMMENT_INLINE", "COMMENT_BLOCK", "NL", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_typee = 2
    RULE_arrType = 3
    RULE_dimenList = 4
    RULE_structDecl = 5
    RULE_bodyList = 6
    RULE_structEl = 7
    RULE_field = 8
    RULE_interfaceDecl = 9
    RULE_interfaceBody = 10
    RULE_listMethod = 11
    RULE_method = 12
    RULE_paramList = 13
    RULE_paramPrime = 14
    RULE_param = 15
    RULE_nameList = 16
    RULE_varDecl = 17
    RULE_constDecl = 18
    RULE_literalConst = 19
    RULE_funcDecl = 20
    RULE_funcParamList = 21
    RULE_funcParamPrime = 22
    RULE_funcParam = 23
    RULE_funcBody = 24
    RULE_methodStructDecl = 25
    RULE_arrLit = 26
    RULE_arrLitDimenList = 27
    RULE_arrBody = 28
    RULE_elementList = 29
    RULE_element = 30
    RULE_structLit = 31
    RULE_structElList = 32
    RULE_structELPrime = 33
    RULE_structEL = 34
    RULE_funcCall = 35
    RULE_argumentList = 36
    RULE_argumentListPrime = 37
    RULE_argument = 38
    RULE_expr = 39
    RULE_expr1 = 40
    RULE_expr2 = 41
    RULE_expr3 = 42
    RULE_expr4 = 43
    RULE_expr5 = 44
    RULE_expr6 = 45
    RULE_expr7 = 46
    RULE_operand = 47
    RULE_literal = 48
    RULE_indexList = 49
    RULE_statementList = 50
    RULE_statementListPrime = 51
    RULE_statement = 52
    RULE_assignment = 53
    RULE_lhs = 54
    RULE_exprLhs = 55
    RULE_rhs = 56
    RULE_ifStatement = 57
    RULE_iff = 58
    RULE_elseIf = 59
    RULE_forStatement = 60
    RULE_forBasic = 61
    RULE_forInitial = 62
    RULE_initialization = 63
    RULE_varDeclInitial = 64
    RULE_condition = 65
    RULE_update = 66
    RULE_assignScalar = 67
    RULE_forRange = 68
    RULE_breakStatement = 69
    RULE_continueStatement = 70
    RULE_callStatement = 71
    RULE_returnStatement = 72

    ruleNames =  [ "program", "decl", "typee", "arrType", "dimenList", "structDecl", 
                   "bodyList", "structEl", "field", "interfaceDecl", "interfaceBody", 
                   "listMethod", "method", "paramList", "paramPrime", "param", 
                   "nameList", "varDecl", "constDecl", "literalConst", "funcDecl", 
                   "funcParamList", "funcParamPrime", "funcParam", "funcBody", 
                   "methodStructDecl", "arrLit", "arrLitDimenList", "arrBody", 
                   "elementList", "element", "structLit", "structElList", 
                   "structELPrime", "structEL", "funcCall", "argumentList", 
                   "argumentListPrime", "argument", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "operand", 
                   "literal", "indexList", "statementList", "statementListPrime", 
                   "statement", "assignment", "lhs", "exprLhs", "rhs", "ifStatement", 
                   "iff", "elseIf", "forStatement", "forBasic", "forInitial", 
                   "initialization", "varDeclInitial", "condition", "update", 
                   "assignScalar", "forRange", "breakStatement", "continueStatement", 
                   "callStatement", "returnStatement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    PLUS=21
    MINUS=22
    MULTI=23
    DIV=24
    MODULO=25
    EQUAL=26
    NOT_EQUAL=27
    LESS_THAN=28
    LESS_EQUAL=29
    GREATER_THAN=30
    GREATER_EQUAL=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ASSIGN1=36
    PLUS_EQUAL=37
    MINUS_EQUAL=38
    MULTI_EQUAL=39
    DIV_EQUAL=40
    MODULO_EQUAL=41
    DOT=42
    COLON=43
    OPEN_ROUND=44
    CLOSE_ROUND=45
    OPEN_CURVE=46
    CLOSE_CURVE=47
    OPEN_SQUARE=48
    CLOSE_SQUARE=49
    COMMA=50
    SEMICOLON=51
    UNDERSCORE=52
    ID=53
    INT_LIT=54
    FLOAT_LIT=55
    STRING_LIT=56
    COMMENT_INLINE=57
    COMMENT_BLOCK=58
    NL=59
    WS=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.decl()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 151
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structDecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclContext,0)


        def interfaceDecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,0)


        def methodStructDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodStructDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.structDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.interfaceDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 157
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 158
                self.methodStructDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def arrType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrTypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypee" ):
                return visitor.visitTypee(self)
            else:
                return visitor.visitChildren(self)




    def typee(self):

        localctx = MiniGoParser.TypeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typee)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.state = 161
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.state = 162
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.state = 163
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.state = 164
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.state = 165
                self.arrType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 166
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimenList(self):
            return self.getTypedRuleContext(MiniGoParser.DimenListContext,0)


        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrType" ):
                return visitor.visitArrType(self)
            else:
                return visitor.visitChildren(self)




    def arrType(self):

        localctx = MiniGoParser.ArrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.dimenList()
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimenListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def dimenList(self):
            return self.getTypedRuleContext(MiniGoParser.DimenListContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimenList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimenList" ):
                return visitor.visitDimenList(self)
            else:
                return visitor.visitChildren(self)




    def dimenList(self):

        localctx = MiniGoParser.DimenListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimenList)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 173
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 174
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 175
                self.dimenList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 177
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.match(MiniGoParser.CLOSE_SQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def bodyList(self):
            return self.getTypedRuleContext(MiniGoParser.BodyListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = MiniGoParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_structDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MiniGoParser.TYPE)
            self.state = 182
            self.match(MiniGoParser.ID)
            self.state = 183
            self.match(MiniGoParser.STRUCT)
            self.state = 184
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 185
            self.bodyList()
            self.state = 186
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 187
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structEl(self):
            return self.getTypedRuleContext(MiniGoParser.StructElContext,0)


        def bodyList(self):
            return self.getTypedRuleContext(MiniGoParser.BodyListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_bodyList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyList" ):
                return visitor.visitBodyList(self)
            else:
                return visitor.visitChildren(self)




    def bodyList(self):

        localctx = MiniGoParser.BodyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bodyList)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.structEl()
                self.state = 190
                self.bodyList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.structEl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructElContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structEl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructEl" ):
                return visitor.visitStructEl(self)
            else:
                return visitor.visitChildren(self)




    def structEl(self):

        localctx = MiniGoParser.StructElContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structEl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.field()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MiniGoParser.ID)
            self.state = 198
            self.typee()
            self.state = 199
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDecl" ):
                return visitor.visitInterfaceDecl(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDecl(self):

        localctx = MiniGoParser.InterfaceDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interfaceDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.TYPE)
            self.state = 202
            self.match(MiniGoParser.ID)
            self.state = 203
            self.match(MiniGoParser.INTERFACE)
            self.state = 204
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 205
            self.interfaceBody()
            self.state = 206
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 207
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listMethod(self):
            return self.getTypedRuleContext(MiniGoParser.ListMethodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceBody" ):
                return visitor.visitInterfaceBody(self)
            else:
                return visitor.visitChildren(self)




    def interfaceBody(self):

        localctx = MiniGoParser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_interfaceBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.listMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def listMethod(self):
            return self.getTypedRuleContext(MiniGoParser.ListMethodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListMethod" ):
                return visitor.visitListMethod(self)
            else:
                return visitor.visitChildren(self)




    def listMethod(self):

        localctx = MiniGoParser.ListMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listMethod)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.method()
                self.state = 212
                self.listMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MiniGoParser.ID)
            self.state = 218
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 219
            self.paramList()
            self.state = 220
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 221
                self.typee()


            self.state = 224
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MiniGoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.paramPrime()
                pass
            elif token in [MiniGoParser.CLOSE_ROUND]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamPrime" ):
                return visitor.visitParamPrime(self)
            else:
                return visitor.visitChildren(self)




    def paramPrime(self):

        localctx = MiniGoParser.ParamPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramPrime)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.param()
                self.state = 231
                self.match(MiniGoParser.COMMA)
                self.state = 232
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameList(self):
            return self.getTypedRuleContext(MiniGoParser.NameListContext,0)


        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.nameList()
            self.state = 238
            self.typee()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def nameList(self):
            return self.getTypedRuleContext(MiniGoParser.NameListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nameList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameList" ):
                return visitor.visitNameList(self)
            else:
                return visitor.visitChildren(self)




    def nameList(self):

        localctx = MiniGoParser.NameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nameList)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(MiniGoParser.ID)
                self.state = 241
                self.match(MiniGoParser.COMMA)
                self.state = 242
                self.nameList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_varDecl)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(MiniGoParser.VAR)
                self.state = 247
                self.match(MiniGoParser.ID)
                self.state = 248
                self.typee()
                self.state = 249
                self.match(MiniGoParser.ASSIGN)
                self.state = 250
                self.expr(0)
                self.state = 251
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(MiniGoParser.VAR)
                self.state = 254
                self.match(MiniGoParser.ID)
                self.state = 255
                self.match(MiniGoParser.ASSIGN)
                self.state = 256
                self.expr(0)
                self.state = 257
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.match(MiniGoParser.VAR)
                self.state = 260
                self.match(MiniGoParser.ID)
                self.state = 261
                self.typee()
                self.state = 262
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.CONST)
            self.state = 267
            self.match(MiniGoParser.ID)
            self.state = 268
            self.match(MiniGoParser.ASSIGN)
            self.state = 269
            self.expr(0)
            self.state = 270
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literalConst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralConst" ):
                return visitor.visitLiteralConst(self)
            else:
                return visitor.visitChildren(self)




    def literalConst(self):

        localctx = MiniGoParser.LiteralConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literalConst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def funcParamList(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def funcBody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MiniGoParser.FUNC)
            self.state = 275
            self.match(MiniGoParser.ID)
            self.state = 276
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 277
            self.funcParamList()
            self.state = 278
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 279
                self.typee()


            self.state = 282
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 283
            self.funcBody()
            self.state = 284
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 285
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcParamPrime(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParamList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParamList" ):
                return visitor.visitFuncParamList(self)
            else:
                return visitor.visitChildren(self)




    def funcParamList(self):

        localctx = MiniGoParser.FuncParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_funcParamList)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.funcParamPrime()
                pass
            elif token in [MiniGoParser.CLOSE_ROUND]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def funcParamPrime(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParamPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParamPrime" ):
                return visitor.visitFuncParamPrime(self)
            else:
                return visitor.visitChildren(self)




    def funcParamPrime(self):

        localctx = MiniGoParser.FuncParamPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcParamPrime)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.funcParam()
                self.state = 292
                self.match(MiniGoParser.COMMA)
                self.state = 293
                self.funcParamPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.funcParam()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameList(self):
            return self.getTypedRuleContext(MiniGoParser.NameListContext,0)


        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParam" ):
                return visitor.visitFuncParam(self)
            else:
                return visitor.visitChildren(self)




    def funcParam(self):

        localctx = MiniGoParser.FuncParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.nameList()
            self.state = 299
            self.typee()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncBody" ):
                return visitor.visitFuncBody(self)
            else:
                return visitor.visitChildren(self)




    def funcBody(self):

        localctx = MiniGoParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_funcBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.statementList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodStructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def OPEN_ROUND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_ROUND)
            else:
                return self.getToken(MiniGoParser.OPEN_ROUND, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def CLOSE_ROUND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_ROUND)
            else:
                return self.getToken(MiniGoParser.CLOSE_ROUND, i)

        def funcParamList(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamListContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def funcBody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodStructDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodStructDecl" ):
                return visitor.visitMethodStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodStructDecl(self):

        localctx = MiniGoParser.MethodStructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_methodStructDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MiniGoParser.FUNC)
            self.state = 304
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 305
            self.match(MiniGoParser.ID)
            self.state = 306
            self.match(MiniGoParser.ID)
            self.state = 307
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 308
            self.match(MiniGoParser.ID)
            self.state = 309
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 310
            self.funcParamList()
            self.state = 311
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 312
                self.typee()


            self.state = 315
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 316
            self.funcBody()
            self.state = 317
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 318
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrLitDimenList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrLitDimenListContext,0)


        def arrBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrBodyContext,0)


        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrLit" ):
                return visitor.visitArrLit(self)
            else:
                return visitor.visitChildren(self)




    def arrLit(self):

        localctx = MiniGoParser.ArrLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arrLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.arrLitDimenList()
            self.state = 321
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 322
            self.arrBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrLitDimenListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def arrLitDimenList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrLitDimenListContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrLitDimenList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrLitDimenList" ):
                return visitor.visitArrLitDimenList(self)
            else:
                return visitor.visitChildren(self)




    def arrLitDimenList(self):

        localctx = MiniGoParser.ArrLitDimenListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arrLitDimenList)
        self._la = 0 # Token type
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 325
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 327
                self.arrLitDimenList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 329
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 330
                self.match(MiniGoParser.CLOSE_SQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def elementList(self):
            return self.getTypedRuleContext(MiniGoParser.ElementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrBody" ):
                return visitor.visitArrBody(self)
            else:
                return visitor.visitChildren(self)




    def arrBody(self):

        localctx = MiniGoParser.ArrBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 334
            self.elementList()
            self.state = 335
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def elementList(self):
            return self.getTypedRuleContext(MiniGoParser.ElementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementList" ):
                return visitor.visitElementList(self)
            else:
                return visitor.visitChildren(self)




    def elementList(self):

        localctx = MiniGoParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elementList)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.element()
                self.state = 338
                self.match(MiniGoParser.COMMA)
                self.state = 339
                self.elementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def arrBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrBodyContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_element)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.literalConst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.structLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.arrBody()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def structElList(self):
            return self.getTypedRuleContext(MiniGoParser.StructElListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLit" ):
                return visitor.visitStructLit(self)
            else:
                return visitor.visitChildren(self)




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MiniGoParser.ID)
            self.state = 351
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 352
            self.structElList()
            self.state = 353
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructElListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structELPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StructELPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structElList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructElList" ):
                return visitor.visitStructElList(self)
            else:
                return visitor.visitChildren(self)




    def structElList(self):

        localctx = MiniGoParser.StructElListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_structElList)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.structELPrime()
                pass
            elif token in [MiniGoParser.CLOSE_CURVE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructELPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structEL(self):
            return self.getTypedRuleContext(MiniGoParser.StructELContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structELPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StructELPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structELPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructELPrime" ):
                return visitor.visitStructELPrime(self)
            else:
                return visitor.visitChildren(self)




    def structELPrime(self):

        localctx = MiniGoParser.StructELPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_structELPrime)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.structEL()
                self.state = 360
                self.match(MiniGoParser.COMMA)
                self.state = 361
                self.structELPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.structEL()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructELContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structEL

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructEL" ):
                return visitor.visitStructEL(self)
            else:
                return visitor.visitChildren(self)




    def structEL(self):

        localctx = MiniGoParser.StructELContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_structEL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MiniGoParser.ID)
            self.state = 367
            self.match(MiniGoParser.COLON)
            self.state = 368
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = MiniGoParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MiniGoParser.ID)
            self.state = 371
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 372
            self.argumentList()
            self.state = 373
            self.match(MiniGoParser.CLOSE_ROUND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = MiniGoParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_argumentList)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.argumentListPrime()
                pass
            elif token in [MiniGoParser.CLOSE_ROUND]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def argumentListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentListPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentListPrime" ):
                return visitor.visitArgumentListPrime(self)
            else:
                return visitor.visitChildren(self)




    def argumentListPrime(self):

        localctx = MiniGoParser.ArgumentListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_argumentListPrime)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.argument()
                self.state = 380
                self.match(MiniGoParser.COMMA)
                self.state = 381
                self.argumentListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 391
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 392
                    self.match(MiniGoParser.OR)
                    self.state = 393
                    self.expr1(0) 
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 402
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 403
                    self.match(MiniGoParser.AND)
                    self.state = 404
                    self.expr2(0) 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(MiniGoParser.LESS_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(MiniGoParser.GREATER_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 413
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 414
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 415
                    self.expr3(0) 
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 424
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 425
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 426
                    self.expr4(0) 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MULTI(self):
            return self.getToken(MiniGoParser.MULTI, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 435
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 436
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 437
                    self.expr5() 
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 444
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def indexList(self):
            return self.getTypedRuleContext(MiniGoParser.IndexListContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 463
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 451
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 452
                        self.indexList()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 453
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 454
                        self.match(MiniGoParser.DOT)
                        self.state = 455
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 456
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 457
                        self.match(MiniGoParser.DOT)
                        self.state = 458
                        self.match(MiniGoParser.ID)
                        self.state = 459
                        self.match(MiniGoParser.OPEN_ROUND)
                        self.state = 460
                        self.argumentList()
                        self.state = 461
                        self.match(MiniGoParser.CLOSE_ROUND)
                        pass

             
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr7)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.OPEN_ROUND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 469
                self.expr(0)
                self.state = 470
                self.match(MiniGoParser.CLOSE_ROUND)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_operand)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.funcCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 477
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def arrLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literal)
        try:
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.literalConst()
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.arrLit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 482
                self.structLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def indexList(self):
            return self.getTypedRuleContext(MiniGoParser.IndexListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_indexList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexList" ):
                return visitor.visitIndexList(self)
            else:
                return visitor.visitChildren(self)




    def indexList(self):

        localctx = MiniGoParser.IndexListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_indexList)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 486
                self.expr(0)
                self.state = 487
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 488
                self.indexList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 491
                self.expr(0)
                self.state = 492
                self.match(MiniGoParser.CLOSE_SQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_statementList)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.statementListPrime()
                pass
            elif token in [MiniGoParser.CLOSE_CURVE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementListPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementListPrime" ):
                return visitor.visitStatementListPrime(self)
            else:
                return visitor.visitChildren(self)




    def statementListPrime(self):

        localctx = MiniGoParser.StatementListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_statementListPrime)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.statement()
                self.state = 501
                self.statementListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_statement)
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.constDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 509
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 510
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 511
                self.breakStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 512
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 513
                self.callStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 514
                self.returnStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

        def PLUS_EQUAL(self):
            return self.getToken(MiniGoParser.PLUS_EQUAL, 0)

        def MINUS_EQUAL(self):
            return self.getToken(MiniGoParser.MINUS_EQUAL, 0)

        def MULTI_EQUAL(self):
            return self.getToken(MiniGoParser.MULTI_EQUAL, 0)

        def DIV_EQUAL(self):
            return self.getToken(MiniGoParser.DIV_EQUAL, 0)

        def MODULO_EQUAL(self):
            return self.getToken(MiniGoParser.MODULO_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.lhs(0)
            self.state = 518
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN1) | (1 << MiniGoParser.PLUS_EQUAL) | (1 << MiniGoParser.MINUS_EQUAL) | (1 << MiniGoParser.MULTI_EQUAL) | (1 << MiniGoParser.DIV_EQUAL) | (1 << MiniGoParser.MODULO_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 519
            self.rhs()
            self.state = 520
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def exprLhs(self):
            return self.getTypedRuleContext(MiniGoParser.ExprLhsContext,0)


        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def indexList(self):
            return self.getTypedRuleContext(MiniGoParser.IndexListContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 523
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 524
                self.exprLhs()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 532
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 527
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 528
                        self.indexList()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 529
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 530
                        self.match(MiniGoParser.DOT)
                        self.state = 531
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprLhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprLhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLhs" ):
                return visitor.visitExprLhs(self)
            else:
                return visitor.visitChildren(self)




    def exprLhs(self):

        localctx = MiniGoParser.ExprLhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_exprLhs)
        try:
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.OPEN_ROUND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 538
                self.expr(0)
                self.state = 539
                self.match(MiniGoParser.CLOSE_ROUND)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iff(self):
            return self.getTypedRuleContext(MiniGoParser.IffContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.iff()
            self.state = 547
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def elseIf(self):
            return self.getTypedRuleContext(MiniGoParser.ElseIfContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_iff

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIff" ):
                return visitor.visitIff(self)
            else:
                return visitor.visitChildren(self)




    def iff(self):

        localctx = MiniGoParser.IffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_iff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MiniGoParser.IF)
            self.state = 550
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 551
            self.expr(0)
            self.state = 552
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 553
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 554
            self.statementList()
            self.state = 555
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 556
            self.elseIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def elseIf(self):
            return self.getTypedRuleContext(MiniGoParser.ElseIfContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIf" ):
                return visitor.visitElseIf(self)
            else:
                return visitor.visitChildren(self)




    def elseIf(self):

        localctx = MiniGoParser.ElseIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_elseIf)
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.match(MiniGoParser.ELSE)
                self.state = 559
                self.match(MiniGoParser.IF)
                self.state = 560
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 561
                self.expr(0)
                self.state = 562
                self.match(MiniGoParser.CLOSE_ROUND)
                self.state = 563
                self.match(MiniGoParser.OPEN_CURVE)
                self.state = 564
                self.statementList()
                self.state = 565
                self.match(MiniGoParser.CLOSE_CURVE)
                self.state = 566
                self.elseIf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.match(MiniGoParser.ELSE)
                self.state = 569
                self.match(MiniGoParser.OPEN_CURVE)
                self.state = 570
                self.statementList()
                self.state = 571
                self.match(MiniGoParser.CLOSE_CURVE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forBasic(self):
            return self.getTypedRuleContext(MiniGoParser.ForBasicContext,0)


        def forInitial(self):
            return self.getTypedRuleContext(MiniGoParser.ForInitialContext,0)


        def forRange(self):
            return self.getTypedRuleContext(MiniGoParser.ForRangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_forStatement)
        try:
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.forBasic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
                self.forInitial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 578
                self.forRange()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBasicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forBasic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBasic" ):
                return visitor.visitForBasic(self)
            else:
                return visitor.visitChildren(self)




    def forBasic(self):

        localctx = MiniGoParser.ForBasicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_forBasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.FOR)
            self.state = 582
            self.expr(0)
            self.state = 583
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 584
            self.statementList()
            self.state = 585
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 586
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def initialization(self):
            return self.getTypedRuleContext(MiniGoParser.InitializationContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forInitial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitial" ):
                return visitor.visitForInitial(self)
            else:
                return visitor.visitChildren(self)




    def forInitial(self):

        localctx = MiniGoParser.ForInitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_forInitial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(MiniGoParser.FOR)
            self.state = 589
            self.initialization()
            self.state = 590
            self.match(MiniGoParser.SEMICOLON)
            self.state = 591
            self.condition()
            self.state = 592
            self.match(MiniGoParser.SEMICOLON)
            self.state = 593
            self.update()
            self.state = 594
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 595
            self.statementList()
            self.state = 596
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 597
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignScalar(self):
            return self.getTypedRuleContext(MiniGoParser.AssignScalarContext,0)


        def varDeclInitial(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclInitialContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_initialization)
        try:
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                self.assignScalar()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.varDeclInitial()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclInitialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclInitial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclInitial" ):
                return visitor.visitVarDeclInitial(self)
            else:
                return visitor.visitChildren(self)




    def varDeclInitial(self):

        localctx = MiniGoParser.VarDeclInitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_varDeclInitial)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(MiniGoParser.VAR)
            self.state = 604
            self.match(MiniGoParser.ID)
            self.state = 606
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 605
                self.typee()


            self.state = 608
            self.match(MiniGoParser.ASSIGN)
            self.state = 609
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignScalar(self):
            return self.getTypedRuleContext(MiniGoParser.AssignScalarContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.assignScalar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignScalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

        def PLUS_EQUAL(self):
            return self.getToken(MiniGoParser.PLUS_EQUAL, 0)

        def MINUS_EQUAL(self):
            return self.getToken(MiniGoParser.MINUS_EQUAL, 0)

        def MULTI_EQUAL(self):
            return self.getToken(MiniGoParser.MULTI_EQUAL, 0)

        def DIV_EQUAL(self):
            return self.getToken(MiniGoParser.DIV_EQUAL, 0)

        def MODULO_EQUAL(self):
            return self.getToken(MiniGoParser.MODULO_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignScalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignScalar" ):
                return visitor.visitAssignScalar(self)
            else:
                return visitor.visitChildren(self)




    def assignScalar(self):

        localctx = MiniGoParser.AssignScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_assignScalar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(MiniGoParser.ID)
            self.state = 616
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN1) | (1 << MiniGoParser.PLUS_EQUAL) | (1 << MiniGoParser.MINUS_EQUAL) | (1 << MiniGoParser.MULTI_EQUAL) | (1 << MiniGoParser.DIV_EQUAL) | (1 << MiniGoParser.MODULO_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 617
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def UNDERSCORE(self):
            return self.getToken(MiniGoParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRange" ):
                return visitor.visitForRange(self)
            else:
                return visitor.visitChildren(self)




    def forRange(self):

        localctx = MiniGoParser.ForRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_forRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(MiniGoParser.FOR)
            self.state = 620
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 621
            self.match(MiniGoParser.COMMA)
            self.state = 622
            self.match(MiniGoParser.ID)
            self.state = 623
            self.match(MiniGoParser.ASSIGN1)
            self.state = 624
            self.match(MiniGoParser.RANGE)
            self.state = 625
            self.expr(0)
            self.state = 626
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 627
            self.statementList()
            self.state = 628
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 629
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self.match(MiniGoParser.BREAK)
            self.state = 632
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.match(MiniGoParser.CONTINUE)
            self.state = 635
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 637
                self.funcCall()
                pass

            elif la_ == 2:
                self.state = 638
                self.expr6(0)
                self.state = 639
                self.match(MiniGoParser.DOT)
                self.state = 640
                self.match(MiniGoParser.ID)
                self.state = 641
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 642
                self.argumentList()
                self.state = 643
                self.match(MiniGoParser.CLOSE_ROUND)
                pass


            self.state = 647
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(MiniGoParser.RETURN)
            self.state = 651
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.OPEN_ROUND) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 650
                self.expr(0)


            self.state = 653
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[39] = self.expr_sempred
        self._predicates[40] = self.expr1_sempred
        self._predicates[41] = self.expr2_sempred
        self._predicates[42] = self.expr3_sempred
        self._predicates[43] = self.expr4_sempred
        self._predicates[45] = self.expr6_sempred
        self._predicates[54] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         




