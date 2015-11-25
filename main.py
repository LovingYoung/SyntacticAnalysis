# coding: utf-8
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

if __name__ == '__main__':
    a = LexAnalysis.LexAnalysis()
    a.readFromFile("testLex")
    ans = a.lex()
    try:
        processAns = Syntactic.PROG.process(ans)
        parseTreeRoot = processAns[1]
        print(processAns[0])
        printParseTree(parseTreeRoot)
    except Syntactic.myException as e:
        print(str(e))


def analysis(string = None, readFile = "testLex"):
    a = LexAnalysis.LexAnalysis()
    if string is not None:
        a.readFromString(string)
    elif readFile is not None:
        a.readFromFile(readFile)
    else:
        print("Error: Please input your code")
        return
    ans = a.lex()
    try:
        processAns = Syntactic.PROG.process(ans)
        parseTreeRoot = processAns[1]
        print(processAns[0])
        printParseTree(parseTreeRoot)
    except Syntactic.myException as e:
        print(str(e))

