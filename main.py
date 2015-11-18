import LexAnalysis

a = LexAnalysis.LexAnalysis()
a.readFromFile("testLex")
ans = a.lex()
for i in ans:
    print("typeID:" + str(i.getTypeId()) + "  value:" + i.getValue())