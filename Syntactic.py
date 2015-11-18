class PROG:
    @staticmethod
    def process(instr):
        a1 = PROGHEAD.process(instr)
        a2 = OTHER.process(instr)
        return a1 and a2


class PROGHEAD:
    @staticmethod
    def process(instr):
        a1 = (instr[0].getTypeId() == 1)
        a2 = (instr[1].getTypeId() >= 1000 and instr[0].getTypeId() < 100000)
        if a1 and a2:
            instr.pop(0)
            instr.pop(0)
            return True
        else:
            return False


class OTHER:
    @staticmethod
    def getfirst():
        return [4, 5, 2, 1000, 8, 6]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() in CONSTINFO.getfirst():
            if not CONSTINFO.process(instr): return False
        if instr[0].getTypeId() in PARAINFO.getfirst():
            if not PARAINFO.process(instr): return False
        return SENTENCEPART.process(instr)


class CONSTINFO:
    @staticmethod
    def getfirst():
        return [4]

    @staticmethod
    def process(instr):
        a1 = (instr[0].getTypeId() == 4)
        if a1:
            instr.pop(0)
            a2 = CONSTDEF.process(instr)
            if a2:
                while CONSTDEF.process(instr):
                    pass
                return True
            else:
                return False


class CONSTDEF:
    @staticmethod
    def getfirst():
        return [1000]

    @staticmethod
    def process(instr):
        a1 = (instr[0].getTypeId() == 1000)
        if a1 == True:
            instr.pop(0)
        else:
            return False
        a2 = (instr[0].getTypeId() == 305)
        if a2 == True:
            instr.pop(0)
        else:
            return False
        a3 = (instr[0].getTypeId() == 200)
        if a3 == True:
            instr.pop(0)
        else:
            return False
        return True


class PARAINFO:
    @staticmethod
    def getfirst():
        return [5]

    @staticmethod
    def process(instr):
        a1 = (instr[0].getTypeId() == 5)
        if a1:
            instr.pop(0)
        else:
            return False

        a2 = (instr[0].getTypeId() == 1000)
        if a2 == True:
            instr.pop(0)
        else:
            return False

        while(instr[0].getTypeId() == 1000):
            instr.pop(0)

        return True


class SENTENCEPART:
    @staticmethod
    def getfirst():
        return [2, 1000, 8, 6]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() in SENTENCE.getfirst():
            return SENTENCE.process(instr)
        elif instr[0].getTypeId() in COMPLEXSENTENCE.getfirst():
            return COMPLEXSENTENCE.process(instr)
        return False


class COMPLEXSENTENCE:
    @staticmethod
    def getfirst():
        return [2]

    @staticmethod
    def process(instr):
        a1 = (instr[0].getTypeId() == 2)
        if not a1:
            return False
        instr.pop(0)

        a2 = SENTENCE.process(instr)
        if not a2:
            return False

        while(SENTENCE.process(instr) == True): pass

        a3 = (instr[0].getTypeId() == 3)
        if a3 == False:
            return False

        return a1 and a2 and a3


class SENTENCE:
    @staticmethod
    def getfirst():
        return [2, 1000, 8 ,6]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() in ASSIGNMENT.getfirst():
            return ASSIGNMENT.process(instr)

        if instr[0].getTypeId() in CONDITIONSENTENCE.getfirst():
            return CONDITIONSENTENCE.process(instr)

        if instr[0].getTypeId() in LOOP.getfirst():
            return LOOP.process(instr)

        if instr[0].getTypeId() in COMPLEXSENTENCE.getfirst():
            return COMPLEXSENTENCE.process(instr)

        return False


class ASSIGNMENT:
    @staticmethod
    def getfirst():
        return [1000]

    @staticmethod
    def process(instr):
        a1 = (instr[0].getTypeId() == 1000)
        if a1 == False:
            return False
        instr.pop(0)

        a2 = (instr[0].getTypeId() == 305)
        if a2 == False:
            return False
        instr.pop(0)

        return EXPRESSION.process(instr)


class EXPRESSION:
    @staticmethod
    def getfirst():
        return [301, 302, 1000, 200, 400]

    @staticmethod
    def process(instr):
        a1 = PLUSOP.process(instr)
        a2 = TERM.process(instr)
        if a2 == False:
            return False
        temp = list(instr)
        while(PLUSOP.process(temp) and TERM.process(temp)):
            PLUSOP.process(instr)
            TERM.process(instr)
        return True


class TERM:
    @staticmethod
    def getfirst():
        return [1000, 200, 400]

    @staticmethod
    def process(instr):
        a1 = FACTOR.process(instr)
        if a1 == False:
            return False
        temp = list(instr)
        while(MULTIOP.process(temp) and TERM.process(temp)):
            MULTIOP.process(instr)
            TERM.process(instr)
        return True


class FACTOR:
    @staticmethod
    def getfirst():
        return [1000, 200, 400]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() == 1000:
            instr.pop(0)
            return True

        if instr[0].getTypeId() == 200:
            instr.pop(0)
            return True

        temp = list(instr)
        a1 = (temp[0].getTypeId() == 400)
        if a1:
            temp.pop(0)
            if EXPRESSION.process(temp):
                if temp[0].getTypeId() == 401:
                    instr.pop(0)
                    EXPRESSION.process(instr)
                    instr.pop(0)
                    return True
        return False


class PLUSOP:
    @staticmethod
    def getfirst():
        return [301, 302]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() == 301:
            instr.pop(0)
            return True
        if instr[0].getTypeId() == 302:
            instr.pop(0)
            return True
        return False


class MULTIOP:
    @staticmethod
    def getfirst():
        return [303, 304]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() == 303:
            instr.pop(0)
            return True
        if instr[0].getTypeId() == 304:
            instr.pop(0)
            return True


class CONDITIONSENTENCE:
    @staticmethod
    def getfirst():
        return [8]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() == 8:
            instr.pop(0)
            CONDITION.process(instr)
            if instr[0].getTypeId() == 9:
                instr.pop(0)
                if SENTENCE.process(instr): return True
        return False


class LOOP:
    @staticmethod
    def getfirst():
        return [6]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() == 6:
            instr.pop(0)
            CONDITION.process(instr)
            if instr[0].getTypeId() == 7:
                instr.pop(0)
                if SENTENCE.process(instr) == True: return True
        return False


class CONDITION:
    @staticmethod
    def getfirst():
        return [301, 302, 1000, 200, 400]

    @staticmethod
    def process(instr):
        if EXPRESSION.process(instr):
            if RELATIONOP.process(instr):
                if EXPRESSION.process(instr):
                    return True
        return False


class RELATIONOP:
    @staticmethod
    def getfirst():
        return [306, 307, 308, 309, 310, 311]

    @staticmethod
    def process(instr):
        if instr[0].getTypeId() in RELATIONOP.getfirst():
            instr.pop(0)
            return True
        else:
            return False


class TreeNode:
    def __init__(self, children=[], parent=None, typename=None, value=None):
        self._children = children
        self._parent = parent
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
        self._children.append(children)
        return self._children

    def setParent(self, parent):
        self._parent = parent
        return self._parent

    def setType(self, typename):
        self._type = typename
        return self._type

    def setValue(self, value):
        self._value = value
        return self._value
