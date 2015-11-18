import LexAnalysis
import Syntactic

def printParseTree(root, level = 1, parent = -1, up = list(), lastChild = False):
    if parent == -1:
        prefix = '└── '
    else:
        if parent not in up:
            up.append(parent)
        prefix = list(4 * level * ' ')
        for i in up:
            prefix[i] = '│'
        if lastChild:
            prefix[parent] = '└'
            up.remove(parent)
        else:
            prefix[parent] = '├'
        i = parent + 1
        while i < len(prefix) - 1:
            prefix[i] = '─'
            i += 1
        i = len(prefix) - 1
        prefix[i] = ' '
        prefix = ''.join(prefix)

    if root.getType() == 'Terminator':
        print(prefix + 'Type:' + 'Terminator' + ' Value:' + root.getValue().getValue())
    else:
        print(prefix + 'Type:' + root.getType())

    l = root.getChildren()
    i = 0
    if len(l) > 0:
        while i < len(l) - 1:
            printParseTree(l[i], level + 1, parent=level * 4, up=up, lastChild=False)
            i += 1
        printParseTree(l[len(l) - 1], level + 1, parent=level * 4, up=up, lastChild=True)

a = LexAnalysis.LexAnalysis()
a.readFromFile("testLex")
ans = a.lex()
processAns = Syntactic.PROG.process(ans)
parseTreeRoot = processAns[1]
print(processAns[0])
printParseTree(parseTreeRoot)
