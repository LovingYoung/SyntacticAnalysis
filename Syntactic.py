class PROG:
    @staticmethod
    def process(instr):
        root = TreeNode(typename='PROGRAM')
        a1 = PROGHEAD.process(instr, root)
        a2 = BLOCK.process(instr, root)
        return (a1 and a2, root)


class PROGHEAD:
    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Program_Head')
        a1 = (instr[0].getTypeId() == 1)
        if not a1:
            Analysis.raiseException(instr)
            return False
        son = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
        instr.pop(0)
        a2 = (instr[0].getTypeId() == 1000)
        if not a2:
            Analysis.raiseException(instr)
            return False
        son = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
        instr.pop(0)
        return True


class BLOCK:
    @staticmethod
    def getfirst():
        return [4, 5, 2, 1000, 8, 6]

    @staticmethod
    def process(instr,root):
        myroot = TreeNode(parent=root, typename='Block')
        if instr[0].getTypeId() in CONSTINFO.getfirst():
            if not CONSTINFO.process(instr, myroot):
                Analysis.raiseException(instr)
                return False
        if instr[0].getTypeId() in PARAINFO.getfirst():
            if not PARAINFO.process(instr, myroot):
                Analysis.raiseException(instr)
                return False
        return SENTENCEPART.process(instr, myroot)


class CONSTINFO:
    @staticmethod
    def getfirst():
        return [4]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root,typename='Const_Statement')
        a1 = (instr[0].getTypeId() == 4)
        if a1:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            a2 = CONSTDEF.process(instr,myroot)
            if a2:
                while CONSTDEF.process(instr,myroot):
                    pass
                return True
            else:
                Analysis.raiseException(instr)
                return False


class CONSTDEF:
    @staticmethod
    def getfirst():
        return [1000]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Const Definition')
        a1 = (instr[0].getTypeId() == 1000)
        if a1:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
        else:
            Analysis.raiseException(instr)
            return False
        a2 = (instr[0].getTypeId() == 305)
        if a2 == True:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
        else:
            Analysis.raiseException(instr)
            return False
        a3 = (instr[0].getTypeId() == 200)
        if a3 == True:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
        else:
            Analysis.raiseException(instr)
            return False
        return True


class PARAINFO:
    @staticmethod
    def getfirst():
        return [5]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root,typename='Parameter_Statement')
        a1 = (instr[0].getTypeId() == 5)
        if a1:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
        else:
            Analysis.raiseException(instr)
            return False

        a2 = (instr[0].getTypeId() == 1000)
        if a2 == True:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
        else:
            Analysis.raiseException(instr)
            return False

        while(instr[0].getTypeId() == 1000):
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)

        return True


class SENTENCEPART:
    @staticmethod
    def getfirst():
        return [2, 1000, 8, 6]

    @staticmethod
    def process(instr,root):
        myroot = TreeNode(parent=root, typename='Sentence_Part')
        if instr[0].getTypeId() in SENTENCE.getfirst():
            return SENTENCE.process(instr, myroot)
        elif instr[0].getTypeId() in COMPLEXSENTENCE.getfirst():
            return COMPLEXSENTENCE.process(instr, myroot)
        Analysis.raiseException(instr)
        return False


class COMPLEXSENTENCE:
    @staticmethod
    def getfirst():
        return [2]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root,typename='Complex_Sentences')
        a1 = (instr[0].getTypeId() == 2)
        if not a1:
            Analysis.raiseException(instr)
            return False
        ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
        instr.pop(0)

        a2 = SENTENCE.process(instr,myroot)
        if not a2:
            Analysis.raiseException(instr)
            return False

        while SENTENCE.process(instr, myroot): pass

        a3 = (instr[0].getTypeId() == 3)
        ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
        instr.pop(0)
        if not a3:
            Analysis.raiseException(instr)
            return False

        return True


class SENTENCE:
    @staticmethod
    def getfirst():
        return [2, 1000, 8 ,6]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Sentence')
        if instr[0].getTypeId() in ASSIGNMENT.getfirst():
            return ASSIGNMENT.process(instr, myroot)

        if instr[0].getTypeId() in CONDITIONSENTENCE.getfirst():
            return CONDITIONSENTENCE.process(instr, myroot)

        if instr[0].getTypeId() in LOOP.getfirst():
            return LOOP.process(instr, myroot)

        if instr[0].getTypeId() in COMPLEXSENTENCE.getfirst():
            return COMPLEXSENTENCE.process(instr, myroot)

        return False


class ASSIGNMENT:
    @staticmethod
    def getfirst():
        return [1000]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Assignment')
        a1 = (instr[0].getTypeId() == 1000)
        if not a1:
            Analysis.raiseException(instr)
            return False
        ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
        instr.pop(0)

        a2 = (instr[0].getTypeId() == 305)
        if not a2:
            Analysis.raiseException(instr)
            return False
        ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
        instr.pop(0)

        return EXPRESSION.process(instr, myroot)


class EXPRESSION:
    @staticmethod
    def getfirst():
        return [301, 302, 1000, 200, 400]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Expression')
        a1 = PLUSOP.process(instr, myroot)
        a2 = TERM.process(instr, myroot)
        if not a2:
            Analysis.raiseException(instr)
            return False
        temp = list(instr)
        while(PLUSOP.process(temp, myroot) and TERM.process(temp, myroot)):
            PLUSOP.process(instr, myroot)
            TERM.process(instr, myroot)
        return True


class TERM:
    @staticmethod
    def getfirst():
        return [1000, 200, 400]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Term')
        a1 = FACTOR.process(instr, myroot)
        if not a1:
            Analysis.raiseException(instr)
            return False
        temp = list(instr)
        while(MULTIOP.process(temp, None) and TERM.process(temp, None)):
            MULTIOP.process(instr, myroot)
            TERM.process(instr, myroot)
        return True


class FACTOR:
    @staticmethod
    def getfirst():
        return [1000, 200, 400]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Factor')
        if instr[0].getTypeId() == 1000:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            return True

        if instr[0].getTypeId() == 200:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            return True

        temp = list(instr)
        a1 = (temp[0].getTypeId() == 400)
        if a1:
            temp.pop(0)
            if EXPRESSION.process(temp, None):
                if temp[0].getTypeId() == 401:
                    ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
                    instr.pop(0)
                    EXPRESSION.process(instr, myroot)
                    ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
                    instr.pop(0)
                    return True
        Analysis.raiseException(instr)
        return False


class PLUSOP:
    @staticmethod
    def getfirst():
        return [301, 302]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Plus_Operator')
        if instr[0].getTypeId() == 301:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            return True
        if instr[0].getTypeId() == 302:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            return True
        return False


class MULTIOP:
    @staticmethod
    def getfirst():
        return [303, 304]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Multiply_Operator')
        if instr[0].getTypeId() == 303:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            return True
        if instr[0].getTypeId() == 304:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            return True


class CONDITIONSENTENCE:
    @staticmethod
    def getfirst():
        return [8]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Condition_Sentence')
        if instr[0].getTypeId() == 8:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            CONDITION.process(instr, myroot)
            if instr[0].getTypeId() == 9:
                ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
                instr.pop(0)
                if SENTENCE.process(instr, myroot):
                    return True
        Analysis.raiseException(instr)
        return False


class LOOP:
    @staticmethod
    def getfirst():
        return [6]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Loop_Sentence')
        if instr[0].getTypeId() == 6:
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            CONDITION.process(instr, myroot)
            if instr[0].getTypeId() == 7:
                ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
                instr.pop(0)
                if SENTENCE.process(instr, myroot):
                    return True
        Analysis.raiseException(instr)
        return False


class CONDITION:
    @staticmethod
    def getfirst():
        return [301, 302, 1000, 200, 400]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Condition_Sentence')
        if EXPRESSION.process(instr, myroot):
            if RELATIONOP.process(instr, myroot):
                if EXPRESSION.process(instr, myroot):
                    return True
        Analysis.raiseException(instr)
        return False


class RELATIONOP:
    @staticmethod
    def getfirst():
        return [306, 307, 308, 309, 310, 311]

    @staticmethod
    def process(instr, root):
        myroot = TreeNode(parent=root, typename='Relationship_Sentence')
        if instr[0].getTypeId() in RELATIONOP.getfirst():
            ter = TreeNode(parent=myroot, typename='Terminator', value=instr[0])
            instr.pop(0)
            return True
        else:
            Analysis.raiseException(instr)
            return False


class TreeNode:
    def __init__(self, parent=None, typename=None, value=None):
        self._children = list([])
        self._parent = parent
        if parent != None:
            parent.addChildren(self)
        self._type = typename
        self._value = value

    def getChildren(self):
        return self._children

    def getParent(self):
        return self._parent

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

    def addChildren(self, children):
        if children not in self._children:
            self._children.append(children)
        return self._children

    def setParent(self, parent):
        self._parent = parent
        if parent != None:
            parent.addChildren(self)
        return self._parent

    def setType(self, typename):
        self._type = typename
        return self._type

    def setValue(self, value):
        self._value = value
        return self._value

class myException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Some Errors has occured before " + '"' + str(self.value) + '"'

class Analysis:
    @staticmethod
    def analysis(instr):
        return PROG.process(instr)

    @staticmethod
    def raiseException(instr):
        i = 0
        sum = ""
        while i < len(instr) and i < 10:
            sum += instr[i].value + ' '
            i += 1
        raise myException(sum)
