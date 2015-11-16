import LexAnalysis

a = LexAnalysis.LexAnalysis()
a.readFromString(":=")
ans = a.lex()
for i in ans:
    print("typeID:" + str(i.getTypeId()) + "  value:" + i.getValue())