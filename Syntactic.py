class PROG:
    @staticmethod
    def process(inStr):
        root = TreeNode(type = "PROGRAM")
        a1 = PROGHEAD.process(inStr)
        a2 = OTHER.process(inStr)
        return a1 and a2

class PROGHEAD:
    @staticmethod
    def process(inStr):
        a1 = (inStr[0].getTypeId() == 1)
        a2 = (inStr[1].getTypeId() >= 1000 and inStr[0].getTypeId() < 100000 )
        if a1 and a2:
            inStr.pop(0)
            inStr.pop(0)
            return True
        else:
            return False

class OTHER:
    @staticmethod
    def getFirst():
        return [4, 5, 2, 1000, 8, 6]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() in CONSTINFO.getFirst():
            if False == CONSTINFO.process(inStr): return False
        if inStr[0].getTypeId() in PARAINFO.getFirst():
            if False == PARAINFO.process(inStr): return False
        return SENTENCEPART.process(inStr)

class CONSTINFO:
    @staticmethod
    def getFirst():
        return [4]

    @staticmethod
    def process(inStr):
        a1 = (inStr[0].getTypeId() == 4)
        if a1 == True:
            inStr.pop(0)
            a2 = CONSTDEF.process(inStr)
            if a2 == True:
                while True == CONSTDEF.process(inStr):
                    pass
                return True
            else:
                return False

class CONSTDEF:
    @staticmethod
    def getFirst():
        return [1000]

    @staticmethod
    def process(inStr):
        a1 = (inStr[0].getTypeId() == 1000)
        if a1 == True:
            inStr.pop(0)
        else:
            return False
        a2 = (inStr[0].getTypeId() == 305)
        if a2 == True:
            inStr.pop(0)
        else:
            return False
        a3 = (inStr[0].getTypeId() == 200)
        if a3 == True:
            inStr.pop(0)
        else:
            return False
        return True

class PARAINFO:
    @staticmethod
    def getFirst():
        return [5]

    @staticmethod
    def process(inStr):
        a1 = (inStr[0].getTypeId() == 5)
        if a1 == True:
            inStr.pop(0)
        else:
            return False

        a2 = (inStr[0].getTypeId() == 1000)
        if a2 == True:
            inStr.pop(0)
        else:
            return False

        while(inStr[0].getTypeId() == 1000):
            inStr.pop(0)

        return True

class SENTENCEPART:
    @staticmethod
    def getFirst():
        return [2, 1000, 8, 6]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() in SENTENCE.getFirst():
            return SENTENCE.process(inStr)
        elif inStr[0].getTypeId() in COMPLEXSENTENCE.getFirst():
            return COMPLEXSENTENCE.process(inStr)
        return False

class COMPLEXSENTENCE:
    @staticmethod
    def getFirst():
        return [2]

    @staticmethod
    def process(inStr):
        a1 = (inStr[0].getTypeId() == 2)
        if a1 == False:
            return False
        inStr.pop(0)

        a2 = SENTENCE.process(inStr)
        if a2 == False:
            return False

        while(SENTENCE.process(inStr) == True): pass

        a3 = (inStr[0].getTypeId() == 3)
        if a3 == False:
            return False

        return a1 and a2 and a3

class SENTENCE:
    @staticmethod
    def getFirst():
        return [2, 1000, 8 ,6]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() in ASSIGNMENT.getFirst():
            return ASSIGNMENT.process(inStr)

        if inStr[0].getTypeId() in CONDITIONSENTENCE.getFirst():
            return CONDITIONSENTENCE.process(inStr)

        if inStr[0].getTypeId() in LOOP.getFirst():
            return LOOP.process(inStr)

        if inStr[0].getTypeId() in COMPLEXSENTENCE.getFirst():
            return COMPLEXSENTENCE.process(inStr)

        return False

class ASSIGNMENT:
    @staticmethod
    def getFirst():
        return [1000]

    @staticmethod
    def process(inStr):
        a1 = (inStr[0].getTypeId() == 1000)
        if a1 == False:
            return False
        inStr.pop(0)

        a2 = (inStr[0].getTypeId() == 305)
        if a2 == False:
            return False
        inStr.pop(0)

        return EXPRESSION.process(inStr)

class EXPRESSION:
    @staticmethod
    def getFirst():
        return [301, 302, 1000, 200, 400]

    @staticmethod
    def process(inStr):
        a1 = PLUSOP.process(inStr)
        a2 = TERM.process(inStr)
        if a2 == False:
            return False
        temp = list(inStr)
        while(PLUSOP.process(temp) and TERM.process(temp)):
            PLUSOP.process(inStr)
            TERM.process(inStr)
        return True

class TERM:
    @staticmethod
    def getFirst():
        return [1000, 200, 400]

    @staticmethod
    def process(inStr):
        a1 = FACTOR.process(inStr)
        if a1 == False:
            return False
        temp = list(inStr)
        while(MULTIOP.process(temp) and TERM.process(temp)):
            MULTIOP.process(inStr)
            TERM.process(inStr)
        return True

class FACTOR:
    @staticmethod
    def getFirst():
        return [1000, 200, 400]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() == 1000:
            inStr.pop(0)
            return True

        if inStr[0].getTypeId() == 200:
            inStr.pop(0)
            return True

        temp = list(inStr)
        a1 = (temp[0].getTypeId() == 400)
        if a1 == True:
            temp.pop(0)
            if EXPRESSION.process(temp):
                if temp[0].getTypeId() == 401:
                    inStr.pop(0)
                    EXPRESSION.process(inStr)
                    inStr.pop(0)
                    return True
        return False

class PLUSOP:
    @staticmethod
    def getFirst():
        return [301, 302]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() == 301:
            inStr.pop(0)
            return True
        if inStr[0].getTypeId() == 302:
            inStr.pop(0)
            return True
        return False

class MULTIOP:
    @staticmethod
    def getFirst():
        return [303, 304]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() == 303:
            inStr.pop(0)
            return True
        if inStr[0].getTypeId() == 304:
            inStr.pop(0)
            return True

class CONDITIONSENTENCE:
    @staticmethod
    def getFirst():
        return [8]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() == 8:
            inStr.pop(0)
            CONDITION.process(inStr)
            if inStr[0].getTypeId() == 9:
                inStr.pop(0)
                if SENTENCE.process(inStr) == True: return True
        return False

class LOOP:
    @staticmethod
    def getFirst():
        return [6]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() == 6:
            inStr.pop(0)
            CONDITION.process(inStr)
            if inStr[0].getTypeId() == 7:
                inStr.pop(0)
                if SENTENCE.process(inStr) == True: return True
        return False

class CONDITION:
    @staticmethod
    def getFirst():
        return [301, 302, 1000, 200, 400]

    @staticmethod
    def process(inStr):
        if EXPRESSION.process(inStr):
            if RELATIONOP.process(inStr):
                if EXPRESSION.process(inStr):
                    return True
        return False

class RELATIONOP:
    @staticmethod
    def getFirst():
        return [306, 307, 308, 309, 310, 311]

    @staticmethod
    def process(inStr):
        if inStr[0].getTypeId() in RELATIONOP.getFirst():
            inStr.pop(0)
            return True
        else:
            return False


class TreeNode:
    def __init__(self, children = [], parent = None, type = None, value = None):
        self._children = children
        self._parent = parent
        self._type = type
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

    def setType(self, type):
        self._type = type
        return self._type

    def setValue(self, value):
        self._value = value
        return self._value
