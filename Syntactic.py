import LexAnalysis

class PROG:
    @staticmethod
    def process(inStr):
        a1 = PROGHEAD.process(inStr)
        a2 = OTHER.process(inStr)
        if a1 and a2:
            return True
        else:
            return False

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
        #TODO

    @staticmethod
    def process(inStr):
        if inStr[0] in CONSTINFO.getFirst():
            a1 = CONSTINFO.process()
        if inStr[0] in PARAINFO.getFirst():
            a2 = PARAINFO.process()
        a3 = SENTENCEPART.process()
        return a1 and a2 and a3

class CONSTINFO:
    @staticmethod
    def getFirst():
        #TODO

    @staticmethod
    def process(inStr):
        a1 = (inStr[0].getTypeId() == 4)
        if a1 == True:
            inStr.pop(0)
            a2 = CONSTDEF.process()
            if a2 == True:
                while True == CONSTDEF.process()
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
        #TODO

    @staticmethod
    def process(inStr):
        if inStr[0] in SENTENCE.process(inStr):
            return SENTENCE.process(inStr)
        elif inStr[0] in COMPLEXSENTENCE.process(inStr):
            return COMPLEXSENTECE.process(inStr)
        return False

class COMPLEXSENTECN:
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

        while(SENTENCE.process(inStr) == True)

        a3 = (inStr[0].getTypeId() == 3)
        if a3 == False:
            return False

        return a1 and a2 and a3

class SENTECNE:
    @staticmethod
    def getFirst():
        #TODO
        pass

    @staticmethod
    def process(inStr):
        if inStr[0] in ASSIGNMENT.getFirst():
            return ASSIGNMENT.process(inStr)

        if inStr[0] in CONDITION.getFirst()
            return CONDITION.process(inStr)

        if inStr[0] in LOOP.getFirst()
            return LOOP.process(inStr)

        if inStr[0] in COMPLEXSENTECN.getFirst()
            return COMPLEXSENTECN.process(inStr)

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

        return EXPRESSION.process()

class EXPRESSION:
    @staticmethod
    def getFirst():
