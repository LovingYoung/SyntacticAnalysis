import LexAnalysis
import Syntactic

def printParseTree(root, level = 0):
    children = root.getChildren()
    if root.getType() == 'Terminator':
        print(level * 2 * ' ' + 'Type:' + 'Terminator' + ' Value:' + root.getValue().getValue())
    else:
        print(level * 2 * ' ' + 'Type:' + root.getType())

    for i in root.getChildren():
        printParseTree(i, level + 1)

a = LexAnalysis.LexAnalysis()
a.readFromFile("testLex")
ans = a.lex()
processAns = Syntactic.PROG.process(ans)
parseTreeRoot = processAns[1]
print(processAns[0])
printParseTree(parseTreeRoot)
