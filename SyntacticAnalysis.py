import LexAnalysis

class Instance:
    def __init__(self, maps, typeId = 0):
        self.maps = maps
        self.typeId = typeId
        if(self.typeId != 0):
            self.typeName = maps[self.typeId]
        else:
            self.typeName = ""
        self._tokens = []
        self._sons = []

    def getTypeId(self):
        return self.typeId

    def getTypeName(self):
        return self.typeName

    def getToken(self):
        return self._tokens

    def getSons(self):
        return self._sons

    def SetTypeId(self, newId):
        self.typeId = newId
        self.typeName = maps[self.typeId]

    def addSons(self, son):
        self._sons.append(son)


class Sentence:
    def __init__(self, typeId, typeName, consist = [], nameToId):
        self.typeId = typeId
        self.typeName = typeName
        self.consist = []
        for i in consisit:
            self.consist.append(nameToId[i])
        self._first = []
        self._follow = []
        self._built = False

    def getFirst(self):
        if self._built = False:
            self._buildFirst()
            self._buildFollow()
            self._built = True
        return self._first

    def getFollow(self):
        if self._built = False:
            self._buildFirst()
            self._buildFollow()
            self._built = True
        return self._follow

    def _buildFirst(self):
        pass #TODO: implement

    def _buildFollow(self):
        pass #TODO: implement

    def process(self):
        pass #TODO: implement

class Solution:
    def __init__(self):
        #TODO: implement all the definition of sentence
        lex = LexAnalysis.LexAnalysis()
        lex.readFromFile("testLex")

        self.tokenArrays = lex.lex()
        self.sentences = []
        self.parseTree = None
        self.maps = []

        self.PROG = Sentence(100000, "PROG",[["PROGHEAD","OTHERPROG"]], self.maps)
        self.PROGHEAD = Sentence(100001, "PROGHEAD", [["PROGRAM", "IDENTITY"]], self.maps)
        self.OTHERPROG = Sentence(100002, "OTHERPROG", [["CONSTINFO","PARAINFO","SENTENCEPART"], ["PARAINFO", "SENTENCEPART"], ["CONSTINFO", "SENTECEPART"], ["SENTENCEPART"]], self.maps)
        self.CONSTINFO = Sentence(100003, "CONSTINFO", [["CONST", "CONSTDEF"]], self.maps) #TODO: BUG HERE
        self.CONSTMULTIDEF = Sentence(100100, "CONSTMULTIDEF", [[],["CONSTDEF","CONSTMULTIDEF"]], self.maps)
        self.CONSTDEF = Sentence(100004, "CONSTDEF", [["IDENTITY", "=", "INTEGER"]], self.maps)
        self.INTEGER = Sentence(100005, "INTEGER", [["DIGIT"], ["DIGIT", "INTEGER"]], self.maps)
        self.PARAINFO = Sentence(100006, "PARAINFO",[["VAR", "MULTIID"]], self.maps)
        self.MULTIID = Sentence(100101, "MULTIID",[["IDENTITY"], ["IDENTITY", "MULTIID"]])
        self.IDENTITY= Sentence(100007, "IDENTITY", [], self.maps)
        self.SENTENCEPART = Sentence(100008, "SENTECEPART",[], self.maps)
        self.COMSTATEMENT = Sentence(100009, "COMSTATEMENT", [], self.maps)
        self.STATEMENT = Sentence(100010, "STATEMENT", [], self.maps)
        self.ASSIGNMENT = Sentence(100011, "ASSIGNMENT", [], self.maps)
        self.EXPRESSION = Sentence(100012, "EXPRESSION", [], self.maps)
        self.TERM = Sentence(100013, "TERM", [], self.maps)
        self.FACTOR = Sentence(100014, "FACTOR", [], self.maps)
        self.PLUSOP = Sentence(100015, "PLUSOP", [], self.maps)
        self.MULTIOP = Sentence(100016, "MULTIOP", [], self.maps)
        self.CONDITIONSTATE = Sentence(100017, "CONDITIONSTATE", [], self.maps)
        self.LOOP = Sentence(100018, "LOOP", [], self.maps)
        self.CONDITION = Sentence(100019, "CONDITION", [], self.maps)
        self.RELATIONOP = Sentence(100020, "RELATIONOP", [], self.maps)
        self.CHAR = Sentence(100021, "CHAR", [], self.maps)
        self.DIGIT = Sentence(100022, "DIGIT", [], self.maps)
