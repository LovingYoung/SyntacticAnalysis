import LexAnalysis
import Syntactic

a = LexAnalysis.LexAnalysis()
a.readFromFile("testLex")
ans = a.lex()
print(Syntactic.PROG.process(ans))
