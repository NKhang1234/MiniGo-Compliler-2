# Generated from c:/Code/PPL_Assignment_2/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,608,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,1,0,4,0,140,8,0,11,0,12,0,141,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,152,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,160,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,172,8,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,188,
        8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        11,1,11,1,11,1,11,3,11,208,8,11,1,12,1,12,1,12,1,12,1,12,3,12,215,
        8,12,1,12,1,12,1,13,1,13,3,13,221,8,13,1,14,1,14,1,14,1,14,1,14,
        3,14,228,8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,237,8,16,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,248,8,17,1,17,1,
        17,1,18,1,18,1,18,1,18,1,18,3,18,257,8,18,1,18,1,18,1,19,1,19,1,
        20,1,20,1,20,1,20,1,20,1,20,3,20,269,8,20,1,20,1,20,1,20,1,20,1,
        20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,288,8,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,
        24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,307,8,25,1,26,1,26,1,26,3,
        26,312,8,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,3,28,321,8,28,1,29,
        1,29,1,29,1,29,1,29,3,29,328,8,29,1,30,1,30,1,30,1,30,1,31,1,31,
        1,31,1,31,1,31,1,32,1,32,3,32,341,8,32,1,33,1,33,1,33,1,33,1,33,
        3,33,348,8,33,1,34,1,34,3,34,352,8,34,1,35,1,35,1,35,1,35,1,35,1,
        35,5,35,360,8,35,10,35,12,35,363,9,35,1,36,1,36,1,36,1,36,1,36,1,
        36,5,36,371,8,36,10,36,12,36,374,9,36,1,37,1,37,1,37,1,37,1,37,1,
        37,5,37,382,8,37,10,37,12,37,385,9,37,1,38,1,38,1,38,1,38,1,38,1,
        38,5,38,393,8,38,10,38,12,38,396,9,38,1,39,1,39,1,39,1,39,1,39,1,
        39,5,39,404,8,39,10,39,12,39,407,9,39,1,40,1,40,1,40,3,40,412,8,
        40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,
        41,1,41,5,41,428,8,41,10,41,12,41,431,9,41,1,42,1,42,1,42,1,42,1,
        42,3,42,438,8,42,1,43,1,43,1,43,3,43,443,8,43,1,44,1,44,1,44,3,44,
        448,8,44,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,459,8,
        45,1,45,1,45,1,46,1,46,1,46,1,46,3,46,467,8,46,1,47,1,47,1,47,1,
        47,1,47,1,47,1,47,1,47,1,47,3,47,478,8,47,1,48,1,48,1,48,1,48,1,
        48,3,48,485,8,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,
        50,1,50,1,50,1,50,1,50,1,50,5,50,502,8,50,10,50,12,50,505,9,50,1,
        51,1,51,1,52,1,52,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,
        53,1,53,1,53,1,53,3,53,524,8,53,1,54,1,54,1,54,1,54,3,54,530,8,54,
        1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,3,56,
        544,8,56,1,57,1,57,1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,58,1,58,
        1,58,1,58,1,58,1,58,1,58,1,59,1,59,3,59,564,8,59,1,60,1,60,1,60,
        3,60,569,8,60,1,60,1,60,1,60,1,61,1,61,1,62,1,62,1,63,1,63,1,63,
        1,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,65,
        1,65,1,66,1,66,1,67,1,67,1,67,1,67,1,67,3,67,602,8,67,1,68,1,68,
        3,68,606,8,68,1,68,0,7,70,72,74,76,78,82,100,69,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,0,9,2,0,10,13,53,53,1,0,53,54,2,0,19,21,54,56,1,0,27,32,
        1,0,22,23,1,0,24,26,2,0,23,23,35,35,1,0,37,42,2,0,1,1,53,53,605,
        0,139,1,0,0,0,2,151,1,0,0,0,4,159,1,0,0,0,6,161,1,0,0,0,8,171,1,
        0,0,0,10,173,1,0,0,0,12,181,1,0,0,0,14,187,1,0,0,0,16,189,1,0,0,
        0,18,193,1,0,0,0,20,201,1,0,0,0,22,207,1,0,0,0,24,209,1,0,0,0,26,
        220,1,0,0,0,28,227,1,0,0,0,30,229,1,0,0,0,32,236,1,0,0,0,34,238,
        1,0,0,0,36,251,1,0,0,0,38,260,1,0,0,0,40,262,1,0,0,0,42,275,1,0,
        0,0,44,277,1,0,0,0,46,294,1,0,0,0,48,297,1,0,0,0,50,306,1,0,0,0,
        52,311,1,0,0,0,54,313,1,0,0,0,56,320,1,0,0,0,58,327,1,0,0,0,60,329,
        1,0,0,0,62,333,1,0,0,0,64,340,1,0,0,0,66,347,1,0,0,0,68,351,1,0,
        0,0,70,353,1,0,0,0,72,364,1,0,0,0,74,375,1,0,0,0,76,386,1,0,0,0,
        78,397,1,0,0,0,80,411,1,0,0,0,82,413,1,0,0,0,84,437,1,0,0,0,86,442,
        1,0,0,0,88,447,1,0,0,0,90,458,1,0,0,0,92,466,1,0,0,0,94,468,1,0,
        0,0,96,479,1,0,0,0,98,486,1,0,0,0,100,490,1,0,0,0,102,506,1,0,0,
        0,104,508,1,0,0,0,106,510,1,0,0,0,108,529,1,0,0,0,110,531,1,0,0,
        0,112,543,1,0,0,0,114,545,1,0,0,0,116,551,1,0,0,0,118,563,1,0,0,
        0,120,565,1,0,0,0,122,573,1,0,0,0,124,575,1,0,0,0,126,577,1,0,0,
        0,128,581,1,0,0,0,130,592,1,0,0,0,132,594,1,0,0,0,134,601,1,0,0,
        0,136,603,1,0,0,0,138,140,3,2,1,0,139,138,1,0,0,0,140,141,1,0,0,
        0,141,139,1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,144,5,0,0,
        1,144,1,1,0,0,0,145,152,3,10,5,0,146,152,3,18,9,0,147,152,3,34,17,
        0,148,152,3,36,18,0,149,152,3,40,20,0,150,152,3,44,22,0,151,145,
        1,0,0,0,151,146,1,0,0,0,151,147,1,0,0,0,151,148,1,0,0,0,151,149,
        1,0,0,0,151,150,1,0,0,0,152,3,1,0,0,0,153,160,5,11,0,0,154,160,5,
        12,0,0,155,160,5,13,0,0,156,160,5,10,0,0,157,160,3,6,3,0,158,160,
        5,53,0,0,159,153,1,0,0,0,159,154,1,0,0,0,159,155,1,0,0,0,159,156,
        1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,5,1,0,0,0,161,162,3,
        8,4,0,162,163,7,0,0,0,163,7,1,0,0,0,164,165,5,49,0,0,165,166,7,1,
        0,0,166,167,5,50,0,0,167,172,3,8,4,0,168,169,5,49,0,0,169,170,7,
        1,0,0,170,172,5,50,0,0,171,164,1,0,0,0,171,168,1,0,0,0,172,9,1,0,
        0,0,173,174,5,7,0,0,174,175,5,53,0,0,175,176,5,8,0,0,176,177,5,47,
        0,0,177,178,3,12,6,0,178,179,5,48,0,0,179,180,5,52,0,0,180,11,1,
        0,0,0,181,182,3,14,7,0,182,13,1,0,0,0,183,184,3,16,8,0,184,185,3,
        14,7,0,185,188,1,0,0,0,186,188,3,16,8,0,187,183,1,0,0,0,187,186,
        1,0,0,0,188,15,1,0,0,0,189,190,5,53,0,0,190,191,3,4,2,0,191,192,
        5,52,0,0,192,17,1,0,0,0,193,194,5,7,0,0,194,195,5,53,0,0,195,196,
        5,9,0,0,196,197,5,47,0,0,197,198,3,20,10,0,198,199,5,48,0,0,199,
        200,5,52,0,0,200,19,1,0,0,0,201,202,3,22,11,0,202,21,1,0,0,0,203,
        204,3,24,12,0,204,205,3,22,11,0,205,208,1,0,0,0,206,208,3,24,12,
        0,207,203,1,0,0,0,207,206,1,0,0,0,208,23,1,0,0,0,209,210,5,53,0,
        0,210,211,5,45,0,0,211,212,3,26,13,0,212,214,5,46,0,0,213,215,3,
        4,2,0,214,213,1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,0,216,217,5,
        52,0,0,217,25,1,0,0,0,218,221,3,28,14,0,219,221,1,0,0,0,220,218,
        1,0,0,0,220,219,1,0,0,0,221,27,1,0,0,0,222,223,3,30,15,0,223,224,
        5,51,0,0,224,225,3,28,14,0,225,228,1,0,0,0,226,228,3,30,15,0,227,
        222,1,0,0,0,227,226,1,0,0,0,228,29,1,0,0,0,229,230,3,32,16,0,230,
        231,3,4,2,0,231,31,1,0,0,0,232,233,5,53,0,0,233,234,5,51,0,0,234,
        237,3,32,16,0,235,237,5,53,0,0,236,232,1,0,0,0,236,235,1,0,0,0,237,
        33,1,0,0,0,238,239,5,15,0,0,239,247,5,53,0,0,240,241,3,4,2,0,241,
        242,5,36,0,0,242,243,3,70,35,0,243,248,1,0,0,0,244,245,5,36,0,0,
        245,248,3,70,35,0,246,248,3,4,2,0,247,240,1,0,0,0,247,244,1,0,0,
        0,247,246,1,0,0,0,248,249,1,0,0,0,249,250,5,52,0,0,250,35,1,0,0,
        0,251,252,5,14,0,0,252,253,5,53,0,0,253,256,5,36,0,0,254,257,3,38,
        19,0,255,257,3,70,35,0,256,254,1,0,0,0,256,255,1,0,0,0,257,258,1,
        0,0,0,258,259,5,52,0,0,259,37,1,0,0,0,260,261,7,2,0,0,261,39,1,0,
        0,0,262,263,5,6,0,0,263,264,5,53,0,0,264,265,5,45,0,0,265,266,3,
        26,13,0,266,268,5,46,0,0,267,269,3,4,2,0,268,267,1,0,0,0,268,269,
        1,0,0,0,269,270,1,0,0,0,270,271,5,47,0,0,271,272,3,42,21,0,272,273,
        5,48,0,0,273,274,5,52,0,0,274,41,1,0,0,0,275,276,3,92,46,0,276,43,
        1,0,0,0,277,278,5,6,0,0,278,279,5,45,0,0,279,280,5,53,0,0,280,281,
        5,53,0,0,281,282,5,46,0,0,282,283,5,53,0,0,283,284,5,45,0,0,284,
        285,3,26,13,0,285,287,5,46,0,0,286,288,3,4,2,0,287,286,1,0,0,0,287,
        288,1,0,0,0,288,289,1,0,0,0,289,290,5,47,0,0,290,291,3,42,21,0,291,
        292,5,48,0,0,292,293,5,52,0,0,293,45,1,0,0,0,294,295,3,6,3,0,295,
        296,3,48,24,0,296,47,1,0,0,0,297,298,5,47,0,0,298,299,3,50,25,0,
        299,300,5,48,0,0,300,49,1,0,0,0,301,302,3,52,26,0,302,303,5,51,0,
        0,303,304,3,50,25,0,304,307,1,0,0,0,305,307,3,52,26,0,306,301,1,
        0,0,0,306,305,1,0,0,0,307,51,1,0,0,0,308,312,3,38,19,0,309,312,3,
        54,27,0,310,312,3,48,24,0,311,308,1,0,0,0,311,309,1,0,0,0,311,310,
        1,0,0,0,312,53,1,0,0,0,313,314,5,53,0,0,314,315,5,47,0,0,315,316,
        3,56,28,0,316,317,5,48,0,0,317,55,1,0,0,0,318,321,3,58,29,0,319,
        321,1,0,0,0,320,318,1,0,0,0,320,319,1,0,0,0,321,57,1,0,0,0,322,323,
        3,60,30,0,323,324,5,51,0,0,324,325,3,58,29,0,325,328,1,0,0,0,326,
        328,3,60,30,0,327,322,1,0,0,0,327,326,1,0,0,0,328,59,1,0,0,0,329,
        330,5,53,0,0,330,331,5,44,0,0,331,332,3,70,35,0,332,61,1,0,0,0,333,
        334,5,53,0,0,334,335,5,45,0,0,335,336,3,64,32,0,336,337,5,46,0,0,
        337,63,1,0,0,0,338,341,3,66,33,0,339,341,1,0,0,0,340,338,1,0,0,0,
        340,339,1,0,0,0,341,65,1,0,0,0,342,343,3,68,34,0,343,344,5,51,0,
        0,344,345,3,66,33,0,345,348,1,0,0,0,346,348,3,68,34,0,347,342,1,
        0,0,0,347,346,1,0,0,0,348,67,1,0,0,0,349,352,3,70,35,0,350,352,3,
        48,24,0,351,349,1,0,0,0,351,350,1,0,0,0,352,69,1,0,0,0,353,354,6,
        35,-1,0,354,355,3,72,36,0,355,361,1,0,0,0,356,357,10,2,0,0,357,358,
        5,34,0,0,358,360,3,72,36,0,359,356,1,0,0,0,360,363,1,0,0,0,361,359,
        1,0,0,0,361,362,1,0,0,0,362,71,1,0,0,0,363,361,1,0,0,0,364,365,6,
        36,-1,0,365,366,3,74,37,0,366,372,1,0,0,0,367,368,10,2,0,0,368,369,
        5,33,0,0,369,371,3,74,37,0,370,367,1,0,0,0,371,374,1,0,0,0,372,370,
        1,0,0,0,372,373,1,0,0,0,373,73,1,0,0,0,374,372,1,0,0,0,375,376,6,
        37,-1,0,376,377,3,76,38,0,377,383,1,0,0,0,378,379,10,2,0,0,379,380,
        7,3,0,0,380,382,3,76,38,0,381,378,1,0,0,0,382,385,1,0,0,0,383,381,
        1,0,0,0,383,384,1,0,0,0,384,75,1,0,0,0,385,383,1,0,0,0,386,387,6,
        38,-1,0,387,388,3,78,39,0,388,394,1,0,0,0,389,390,10,2,0,0,390,391,
        7,4,0,0,391,393,3,78,39,0,392,389,1,0,0,0,393,396,1,0,0,0,394,392,
        1,0,0,0,394,395,1,0,0,0,395,77,1,0,0,0,396,394,1,0,0,0,397,398,6,
        39,-1,0,398,399,3,80,40,0,399,405,1,0,0,0,400,401,10,2,0,0,401,402,
        7,5,0,0,402,404,3,80,40,0,403,400,1,0,0,0,404,407,1,0,0,0,405,403,
        1,0,0,0,405,406,1,0,0,0,406,79,1,0,0,0,407,405,1,0,0,0,408,409,7,
        6,0,0,409,412,3,80,40,0,410,412,3,82,41,0,411,408,1,0,0,0,411,410,
        1,0,0,0,412,81,1,0,0,0,413,414,6,41,-1,0,414,415,3,84,42,0,415,429,
        1,0,0,0,416,417,10,4,0,0,417,418,5,49,0,0,418,419,3,70,35,0,419,
        420,5,50,0,0,420,428,1,0,0,0,421,422,10,3,0,0,422,423,5,43,0,0,423,
        428,5,53,0,0,424,425,10,2,0,0,425,426,5,43,0,0,426,428,3,62,31,0,
        427,416,1,0,0,0,427,421,1,0,0,0,427,424,1,0,0,0,428,431,1,0,0,0,
        429,427,1,0,0,0,429,430,1,0,0,0,430,83,1,0,0,0,431,429,1,0,0,0,432,
        433,5,45,0,0,433,434,3,70,35,0,434,435,5,46,0,0,435,438,1,0,0,0,
        436,438,3,86,43,0,437,432,1,0,0,0,437,436,1,0,0,0,438,85,1,0,0,0,
        439,443,3,88,44,0,440,443,3,62,31,0,441,443,5,53,0,0,442,439,1,0,
        0,0,442,440,1,0,0,0,442,441,1,0,0,0,443,87,1,0,0,0,444,448,3,38,
        19,0,445,448,3,46,23,0,446,448,3,54,27,0,447,444,1,0,0,0,447,445,
        1,0,0,0,447,446,1,0,0,0,448,89,1,0,0,0,449,459,3,94,47,0,450,459,
        3,96,48,0,451,459,3,98,49,0,452,459,3,106,53,0,453,459,3,112,56,
        0,454,459,3,130,65,0,455,459,3,132,66,0,456,459,3,134,67,0,457,459,
        3,136,68,0,458,449,1,0,0,0,458,450,1,0,0,0,458,451,1,0,0,0,458,452,
        1,0,0,0,458,453,1,0,0,0,458,454,1,0,0,0,458,455,1,0,0,0,458,456,
        1,0,0,0,458,457,1,0,0,0,459,460,1,0,0,0,460,461,5,52,0,0,461,91,
        1,0,0,0,462,463,3,90,45,0,463,464,3,92,46,0,464,467,1,0,0,0,465,
        467,3,90,45,0,466,462,1,0,0,0,466,465,1,0,0,0,467,93,1,0,0,0,468,
        469,5,15,0,0,469,477,5,53,0,0,470,471,3,4,2,0,471,472,5,36,0,0,472,
        473,3,70,35,0,473,478,1,0,0,0,474,475,5,36,0,0,475,478,3,70,35,0,
        476,478,3,4,2,0,477,470,1,0,0,0,477,474,1,0,0,0,477,476,1,0,0,0,
        478,95,1,0,0,0,479,480,5,14,0,0,480,481,5,53,0,0,481,484,5,36,0,
        0,482,485,3,38,19,0,483,485,3,70,35,0,484,482,1,0,0,0,484,483,1,
        0,0,0,485,97,1,0,0,0,486,487,3,100,50,0,487,488,3,102,51,0,488,489,
        3,104,52,0,489,99,1,0,0,0,490,491,6,50,-1,0,491,492,5,53,0,0,492,
        503,1,0,0,0,493,494,10,3,0,0,494,495,5,49,0,0,495,496,3,70,35,0,
        496,497,5,50,0,0,497,502,1,0,0,0,498,499,10,2,0,0,499,500,5,43,0,
        0,500,502,5,53,0,0,501,493,1,0,0,0,501,498,1,0,0,0,502,505,1,0,0,
        0,503,501,1,0,0,0,503,504,1,0,0,0,504,101,1,0,0,0,505,503,1,0,0,
        0,506,507,7,7,0,0,507,103,1,0,0,0,508,509,3,70,35,0,509,105,1,0,
        0,0,510,511,5,2,0,0,511,512,5,45,0,0,512,513,3,70,35,0,513,514,5,
        46,0,0,514,515,5,47,0,0,515,516,3,92,46,0,516,517,5,48,0,0,517,523,
        3,108,54,0,518,519,5,3,0,0,519,520,5,47,0,0,520,521,3,92,46,0,521,
        522,5,48,0,0,522,524,1,0,0,0,523,518,1,0,0,0,523,524,1,0,0,0,524,
        107,1,0,0,0,525,526,3,110,55,0,526,527,3,108,54,0,527,530,1,0,0,
        0,528,530,1,0,0,0,529,525,1,0,0,0,529,528,1,0,0,0,530,109,1,0,0,
        0,531,532,5,3,0,0,532,533,5,2,0,0,533,534,5,45,0,0,534,535,3,70,
        35,0,535,536,5,46,0,0,536,537,5,47,0,0,537,538,3,92,46,0,538,539,
        5,48,0,0,539,111,1,0,0,0,540,544,3,114,57,0,541,544,3,116,58,0,542,
        544,3,128,64,0,543,540,1,0,0,0,543,541,1,0,0,0,543,542,1,0,0,0,544,
        113,1,0,0,0,545,546,5,4,0,0,546,547,3,70,35,0,547,548,5,47,0,0,548,
        549,3,92,46,0,549,550,5,48,0,0,550,115,1,0,0,0,551,552,5,4,0,0,552,
        553,3,118,59,0,553,554,5,52,0,0,554,555,3,122,61,0,555,556,5,52,
        0,0,556,557,3,124,62,0,557,558,5,47,0,0,558,559,3,92,46,0,559,560,
        5,48,0,0,560,117,1,0,0,0,561,564,3,126,63,0,562,564,3,120,60,0,563,
        561,1,0,0,0,563,562,1,0,0,0,564,119,1,0,0,0,565,566,5,15,0,0,566,
        568,5,53,0,0,567,569,3,4,2,0,568,567,1,0,0,0,568,569,1,0,0,0,569,
        570,1,0,0,0,570,571,5,36,0,0,571,572,3,70,35,0,572,121,1,0,0,0,573,
        574,3,70,35,0,574,123,1,0,0,0,575,576,3,126,63,0,576,125,1,0,0,0,
        577,578,5,53,0,0,578,579,3,102,51,0,579,580,3,70,35,0,580,127,1,
        0,0,0,581,582,5,4,0,0,582,583,7,8,0,0,583,584,5,51,0,0,584,585,5,
        53,0,0,585,586,5,37,0,0,586,587,5,18,0,0,587,588,3,70,35,0,588,589,
        5,47,0,0,589,590,3,92,46,0,590,591,5,48,0,0,591,129,1,0,0,0,592,
        593,5,17,0,0,593,131,1,0,0,0,594,595,5,16,0,0,595,133,1,0,0,0,596,
        602,3,62,31,0,597,598,3,70,35,0,598,599,5,43,0,0,599,600,3,62,31,
        0,600,602,1,0,0,0,601,596,1,0,0,0,601,597,1,0,0,0,602,135,1,0,0,
        0,603,605,5,5,0,0,604,606,3,70,35,0,605,604,1,0,0,0,605,606,1,0,
        0,0,606,137,1,0,0,0,45,141,151,159,171,187,207,214,220,227,236,247,
        256,268,287,306,311,320,327,340,347,351,361,372,383,394,405,411,
        427,429,437,442,447,458,466,477,484,501,503,523,529,543,563,568,
        601,605
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                      "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                      "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", 
                      "MULTI", "DIV", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                      "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "AND", 
                      "OR", "NOT", "ASSIGN", "ASSIGN1", "PLUS_EQUAL", "MINUS_EQUAL", 
                      "MULTI_EQUAL", "DIV_EQUAL", "MODULO_EQUAL", "DOT", 
                      "COLON", "OPEN_ROUND", "CLOSE_ROUND", "OPEN_CURVE", 
                      "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", "COMMA", 
                      "SEMICOLON", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_typee = 2
    RULE_arrType = 3
    RULE_dimenList = 4
    RULE_structDecl = 5
    RULE_structBody = 6
    RULE_listField = 7
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
    RULE_funcBody = 21
    RULE_methodStructDecl = 22
    RULE_arrLit = 23
    RULE_arrBody = 24
    RULE_elementList = 25
    RULE_element = 26
    RULE_structLit = 27
    RULE_structElList = 28
    RULE_structELPrime = 29
    RULE_structEL = 30
    RULE_funcCall = 31
    RULE_argumentList = 32
    RULE_argumentListPrime = 33
    RULE_argument = 34
    RULE_expr = 35
    RULE_expr1 = 36
    RULE_expr2 = 37
    RULE_expr3 = 38
    RULE_expr4 = 39
    RULE_expr5 = 40
    RULE_expr6 = 41
    RULE_expr7 = 42
    RULE_operand = 43
    RULE_literal = 44
    RULE_statement = 45
    RULE_statementList = 46
    RULE_varDeclStatement = 47
    RULE_constDeclStatement = 48
    RULE_assignment = 49
    RULE_lhs = 50
    RULE_assignOperator = 51
    RULE_rhs = 52
    RULE_ifStatement = 53
    RULE_elifList = 54
    RULE_eliff = 55
    RULE_forStatement = 56
    RULE_forBasic = 57
    RULE_forInitial = 58
    RULE_initialization = 59
    RULE_varDeclInitial = 60
    RULE_condition = 61
    RULE_update = 62
    RULE_assignScalar = 63
    RULE_forRange = 64
    RULE_breakStatement = 65
    RULE_continueStatement = 66
    RULE_callStatement = 67
    RULE_returnStatement = 68

    ruleNames =  [ "program", "decl", "typee", "arrType", "dimenList", "structDecl", 
                   "structBody", "listField", "field", "interfaceDecl", 
                   "interfaceBody", "listMethod", "method", "paramList", 
                   "paramPrime", "param", "nameList", "varDecl", "constDecl", 
                   "literalConst", "funcDecl", "funcBody", "methodStructDecl", 
                   "arrLit", "arrBody", "elementList", "element", "structLit", 
                   "structElList", "structELPrime", "structEL", "funcCall", 
                   "argumentList", "argumentListPrime", "argument", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "operand", "literal", "statement", "statementList", 
                   "varDeclStatement", "constDeclStatement", "assignment", 
                   "lhs", "assignOperator", "rhs", "ifStatement", "elifList", 
                   "eliff", "forStatement", "forBasic", "forInitial", "initialization", 
                   "varDeclInitial", "condition", "update", "assignScalar", 
                   "forRange", "breakStatement", "continueStatement", "callStatement", 
                   "returnStatement" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    CONST=14
    VAR=15
    CONTINUE=16
    BREAK=17
    RANGE=18
    NIL=19
    TRUE=20
    FALSE=21
    PLUS=22
    MINUS=23
    MULTI=24
    DIV=25
    MODULO=26
    EQUAL=27
    NOT_EQUAL=28
    LESS_THAN=29
    LESS_EQUAL=30
    GREATER_THAN=31
    GREATER_EQUAL=32
    AND=33
    OR=34
    NOT=35
    ASSIGN=36
    ASSIGN1=37
    PLUS_EQUAL=38
    MINUS_EQUAL=39
    MULTI_EQUAL=40
    DIV_EQUAL=41
    MODULO_EQUAL=42
    DOT=43
    COLON=44
    OPEN_ROUND=45
    CLOSE_ROUND=46
    OPEN_CURVE=47
    CLOSE_CURVE=48
    OPEN_SQUARE=49
    CLOSE_SQUARE=50
    COMMA=51
    SEMICOLON=52
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
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self.decl()
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 49344) != 0)):
                    break

            self.state = 143
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




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.structDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.interfaceDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
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




    def typee(self):

        localctx = MiniGoParser.TypeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typee)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 153
                self.match(MiniGoParser.INT)
                pass
            elif token in [12]:
                self.state = 154
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [13]:
                self.state = 155
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [10]:
                self.state = 156
                self.match(MiniGoParser.STRING)
                pass
            elif token in [49]:
                self.state = 157
                self.arrType()
                pass
            elif token in [53]:
                self.state = 158
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




    def arrType(self):

        localctx = MiniGoParser.ArrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.dimenList()
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254756352) != 0)):
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




    def dimenList(self):

        localctx = MiniGoParser.DimenListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimenList)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 165
                _la = self._input.LA(1)
                if not(_la==53 or _la==54):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 167
                self.dimenList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==53 or _la==54):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 170
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

        def structBody(self):
            return self.getTypedRuleContext(MiniGoParser.StructBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structDecl




    def structDecl(self):

        localctx = MiniGoParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_structDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MiniGoParser.TYPE)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.match(MiniGoParser.STRUCT)
            self.state = 176
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 177
            self.structBody()
            self.state = 178
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 179
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listField(self):
            return self.getTypedRuleContext(MiniGoParser.ListFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structBody




    def structBody(self):

        localctx = MiniGoParser.StructBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_structBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.listField()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def listField(self):
            return self.getTypedRuleContext(MiniGoParser.ListFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listField




    def listField(self):

        localctx = MiniGoParser.ListFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listField)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.field()
                self.state = 184
                self.listField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.field()
                pass


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




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.ID)
            self.state = 190
            self.typee()
            self.state = 191
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




    def interfaceDecl(self):

        localctx = MiniGoParser.InterfaceDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interfaceDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.TYPE)
            self.state = 194
            self.match(MiniGoParser.ID)
            self.state = 195
            self.match(MiniGoParser.INTERFACE)
            self.state = 196
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 197
            self.interfaceBody()
            self.state = 198
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 199
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




    def interfaceBody(self):

        localctx = MiniGoParser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_interfaceBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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




    def listMethod(self):

        localctx = MiniGoParser.ListMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listMethod)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.method()
                self.state = 204
                self.listMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.ID)
            self.state = 210
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 211
            self.paramList()
            self.state = 212
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208177664) != 0):
                self.state = 213
                self.typee()


            self.state = 216
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




    def paramList(self):

        localctx = MiniGoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.paramPrime()
                pass
            elif token in [46]:
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




    def paramPrime(self):

        localctx = MiniGoParser.ParamPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramPrime)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.param()
                self.state = 223
                self.match(MiniGoParser.COMMA)
                self.state = 224
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
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




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.nameList()
            self.state = 230
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




    def nameList(self):

        localctx = MiniGoParser.NameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nameList)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(MiniGoParser.ID)
                self.state = 233
                self.match(MiniGoParser.COMMA)
                self.state = 234
                self.nameList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.VAR)
            self.state = 239
            self.match(MiniGoParser.ID)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 240
                self.typee()
                self.state = 241
                self.match(MiniGoParser.ASSIGN)
                self.state = 242
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 244
                self.match(MiniGoParser.ASSIGN)
                self.state = 245
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 246
                self.typee()
                pass


            self.state = 249
            self.match(MiniGoParser.SEMICOLON)
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MiniGoParser.CONST)
            self.state = 252
            self.match(MiniGoParser.ID)
            self.state = 253
            self.match(MiniGoParser.ASSIGN)
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 254
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 255
                self.expr(0)
                pass


            self.state = 258
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




    def literalConst(self):

        localctx = MiniGoParser.LiteralConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literalConst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126100789570043904) != 0)):
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

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


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




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MiniGoParser.FUNC)
            self.state = 263
            self.match(MiniGoParser.ID)
            self.state = 264
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 265
            self.paramList()
            self.state = 266
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208177664) != 0):
                self.state = 267
                self.typee()


            self.state = 270
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 271
            self.funcBody()
            self.state = 272
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 273
            self.match(MiniGoParser.SEMICOLON)
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




    def funcBody(self):

        localctx = MiniGoParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_funcBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
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

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


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




    def methodStructDecl(self):

        localctx = MiniGoParser.MethodStructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_methodStructDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MiniGoParser.FUNC)
            self.state = 278
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 279
            self.match(MiniGoParser.ID)
            self.state = 280
            self.match(MiniGoParser.ID)
            self.state = 281
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 282
            self.match(MiniGoParser.ID)
            self.state = 283
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 284
            self.paramList()
            self.state = 285
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208177664) != 0):
                self.state = 286
                self.typee()


            self.state = 289
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 290
            self.funcBody()
            self.state = 291
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 292
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

        def arrType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrTypeContext,0)


        def arrBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrLit




    def arrLit(self):

        localctx = MiniGoParser.ArrLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arrLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.arrType()
            self.state = 295
            self.arrBody()
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




    def arrBody(self):

        localctx = MiniGoParser.ArrBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arrBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 298
            self.elementList()
            self.state = 299
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




    def elementList(self):

        localctx = MiniGoParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elementList)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.element()
                self.state = 302
                self.match(MiniGoParser.COMMA)
                self.state = 303
                self.elementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_element




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_element)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.literalConst()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.structLit()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.arrBody()
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




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MiniGoParser.ID)
            self.state = 314
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 315
            self.structElList()
            self.state = 316
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




    def structElList(self):

        localctx = MiniGoParser.StructElListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_structElList)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.structELPrime()
                pass
            elif token in [48]:
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




    def structELPrime(self):

        localctx = MiniGoParser.StructELPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_structELPrime)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.structEL()
                self.state = 323
                self.match(MiniGoParser.COMMA)
                self.state = 324
                self.structELPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
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




    def structEL(self):

        localctx = MiniGoParser.StructELContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_structEL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MiniGoParser.ID)
            self.state = 330
            self.match(MiniGoParser.COLON)
            self.state = 331
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




    def funcCall(self):

        localctx = MiniGoParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.ID)
            self.state = 334
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 335
            self.argumentList()
            self.state = 336
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




    def argumentList(self):

        localctx = MiniGoParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argumentList)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 23, 35, 45, 47, 49, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.argumentListPrime()
                pass
            elif token in [46]:
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




    def argumentListPrime(self):

        localctx = MiniGoParser.ArgumentListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_argumentListPrime)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.argument()
                self.state = 343
                self.match(MiniGoParser.COMMA)
                self.state = 344
                self.argumentListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
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


        def arrBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_argument)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 23, 35, 45, 49, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.expr(0)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.arrBody()
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    self.match(MiniGoParser.OR)
                    self.state = 358
                    self.expr1(0) 
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    self.match(MiniGoParser.AND)
                    self.state = 369
                    self.expr2(0) 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 378
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 379
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8455716864) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 380
                    self.expr3(0) 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 391
                    self.expr4(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.expr5() 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                _la = self._input.LA(1)
                if not(_la==23 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 409
                self.expr5()
                pass
            elif token in [19, 20, 21, 45, 49, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
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


        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 427
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 416
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 417
                        self.match(MiniGoParser.OPEN_SQUARE)
                        self.state = 418
                        self.expr(0)
                        self.state = 419
                        self.match(MiniGoParser.CLOSE_SQUARE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 421
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 422
                        self.match(MiniGoParser.DOT)
                        self.state = 423
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 424
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 425
                        self.match(MiniGoParser.DOT)
                        self.state = 426
                        self.funcCall()
                        pass

             
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr7)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 433
                self.expr(0)
                self.state = 434
                self.match(MiniGoParser.CLOSE_ROUND)
                pass
            elif token in [19, 20, 21, 49, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
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




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operand)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.funcCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
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




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literal)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.literalConst()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.arrLit()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def varDeclStatement(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclStatementContext,0)


        def constDeclStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclStatementContext,0)


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




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 449
                self.varDeclStatement()
                pass

            elif la_ == 2:
                self.state = 450
                self.constDeclStatement()
                pass

            elif la_ == 3:
                self.state = 451
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 452
                self.ifStatement()
                pass

            elif la_ == 5:
                self.state = 453
                self.forStatement()
                pass

            elif la_ == 6:
                self.state = 454
                self.breakStatement()
                pass

            elif la_ == 7:
                self.state = 455
                self.continueStatement()
                pass

            elif la_ == 8:
                self.state = 456
                self.callStatement()
                pass

            elif la_ == 9:
                self.state = 457
                self.returnStatement()
                pass


            self.state = 460
            self.match(MiniGoParser.SEMICOLON)
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

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_statementList)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.statement()
                self.state = 463
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclStatementContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclStatement




    def varDeclStatement(self):

        localctx = MiniGoParser.VarDeclStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_varDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(MiniGoParser.VAR)
            self.state = 469
            self.match(MiniGoParser.ID)
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 470
                self.typee()
                self.state = 471
                self.match(MiniGoParser.ASSIGN)
                self.state = 472
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 474
                self.match(MiniGoParser.ASSIGN)
                self.state = 475
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 476
                self.typee()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclStatementContext(ParserRuleContext):
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

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDeclStatement




    def constDeclStatement(self):

        localctx = MiniGoParser.ConstDeclStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_constDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(MiniGoParser.CONST)
            self.state = 480
            self.match(MiniGoParser.ID)
            self.state = 481
            self.match(MiniGoParser.ASSIGN)
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 482
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 483
                self.expr(0)
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


        def assignOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOperatorContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.lhs(0)
            self.state = 487
            self.assignOperator()
            self.state = 488
            self.rhs()
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

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 503
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 501
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 493
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 494
                        self.match(MiniGoParser.OPEN_SQUARE)
                        self.state = 495
                        self.expr(0)
                        self.state = 496
                        self.match(MiniGoParser.CLOSE_SQUARE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 498
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 499
                        self.match(MiniGoParser.DOT)
                        self.state = 500
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 505
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return MiniGoParser.RULE_assignOperator




    def assignOperator(self):

        localctx = MiniGoParser.AssignOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assignOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8658654068736) != 0)):
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


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
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

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def OPEN_CURVE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_CURVE)
            else:
                return self.getToken(MiniGoParser.OPEN_CURVE, i)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementListContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementListContext,i)


        def CLOSE_CURVE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_CURVE)
            else:
                return self.getToken(MiniGoParser.CLOSE_CURVE, i)

        def elifList(self):
            return self.getTypedRuleContext(MiniGoParser.ElifListContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(MiniGoParser.IF)
            self.state = 511
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 512
            self.expr(0)
            self.state = 513
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 514
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 515
            self.statementList()
            self.state = 516
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 517
            self.elifList()
            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 518
                self.match(MiniGoParser.ELSE)
                self.state = 519
                self.match(MiniGoParser.OPEN_CURVE)
                self.state = 520
                self.statementList()
                self.state = 521
                self.match(MiniGoParser.CLOSE_CURVE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eliff(self):
            return self.getTypedRuleContext(MiniGoParser.EliffContext,0)


        def elifList(self):
            return self.getTypedRuleContext(MiniGoParser.ElifListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elifList




    def elifList(self):

        localctx = MiniGoParser.ElifListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_elifList)
        try:
            self.state = 529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.eliff()
                self.state = 526
                self.elifList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliffContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_eliff




    def eliff(self):

        localctx = MiniGoParser.EliffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_eliff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(MiniGoParser.ELSE)
            self.state = 532
            self.match(MiniGoParser.IF)
            self.state = 533
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 534
            self.expr(0)
            self.state = 535
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 536
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 537
            self.statementList()
            self.state = 538
            self.match(MiniGoParser.CLOSE_CURVE)
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




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_forStatement)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.forBasic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.forInitial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 542
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_forBasic




    def forBasic(self):

        localctx = MiniGoParser.ForBasicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_forBasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(MiniGoParser.FOR)
            self.state = 546
            self.expr(0)
            self.state = 547
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 548
            self.statementList()
            self.state = 549
            self.match(MiniGoParser.CLOSE_CURVE)
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




    def forInitial(self):

        localctx = MiniGoParser.ForInitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_forInitial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(MiniGoParser.FOR)
            self.state = 552
            self.initialization()
            self.state = 553
            self.match(MiniGoParser.SEMICOLON)
            self.state = 554
            self.condition()
            self.state = 555
            self.match(MiniGoParser.SEMICOLON)
            self.state = 556
            self.update()
            self.state = 557
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 558
            self.statementList()
            self.state = 559
            self.match(MiniGoParser.CLOSE_CURVE)
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




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_initialization)
        try:
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
                self.assignScalar()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
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




    def varDeclInitial(self):

        localctx = MiniGoParser.VarDeclInitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_varDeclInitial)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(MiniGoParser.VAR)
            self.state = 566
            self.match(MiniGoParser.ID)
            self.state = 568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208177664) != 0):
                self.state = 567
                self.typee()


            self.state = 570
            self.match(MiniGoParser.ASSIGN)
            self.state = 571
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




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
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




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
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

        def assignOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOperatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignScalar




    def assignScalar(self):

        localctx = MiniGoParser.AssignScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_assignScalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.match(MiniGoParser.ID)
            self.state = 578
            self.assignOperator()
            self.state = 579
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_forRange




    def forRange(self):

        localctx = MiniGoParser.ForRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_forRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.FOR)
            self.state = 582
            _la = self._input.LA(1)
            if not(_la==1 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 583
            self.match(MiniGoParser.COMMA)
            self.state = 584
            self.match(MiniGoParser.ID)
            self.state = 585
            self.match(MiniGoParser.ASSIGN1)
            self.state = 586
            self.match(MiniGoParser.RANGE)
            self.state = 587
            self.expr(0)
            self.state = 588
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 589
            self.statementList()
            self.state = 590
            self.match(MiniGoParser.CLOSE_CURVE)
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(MiniGoParser.BREAK)
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(MiniGoParser.CONTINUE)
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

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_callStatement)
        try:
            self.state = 601
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 596
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.expr(0)
                self.state = 598
                self.match(MiniGoParser.DOT)
                self.state = 599
                self.funcCall()
                pass


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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(MiniGoParser.RETURN)
            self.state = 605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135706157518422016) != 0):
                self.state = 604
                self.expr(0)


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
        self._predicates[35] = self.expr_sempred
        self._predicates[36] = self.expr1_sempred
        self._predicates[37] = self.expr2_sempred
        self._predicates[38] = self.expr3_sempred
        self._predicates[39] = self.expr4_sempred
        self._predicates[41] = self.expr6_sempred
        self._predicates[50] = self.lhs_sempred
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




