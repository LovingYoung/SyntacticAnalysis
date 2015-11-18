class Token:
    def __init__(self, typeId = 0, value = ""):
        self.typeId = typeId
        self.value = value

    def getTypeId(self):
        return self.typeId

    def getValue(self):
        return self.value

    def setTypeId(self, typeId):
        self.typeId = typeId
        return

    def setValue(self, value):
        self.value = value
        return

class LexAnalysis:
    def __init__(self):
        self._result = []
        self._buffer = ""
        self._string = ""
        self._keywords = ["PROGRAM", "BEGIN", "END", "CONST", "VAR", "WHILE", "DO", "IF", "THEN"]
        self._delimiters = ['(', ')', ';', ',', ' ', '\t', '\n']
        self._operators = ['+', '-', '*', '/', ':=', '=', '<>', '>', '>=', '<', '<=']
        self._stringToToken = {"PROGRAM":1, "BEGIN":2, "END":3, "CONST": 4, "VAR":5, "WHILE":6, "DO":7, "IF":8, "THEN":9, "INTEGER":200, "+":301, "-":302, "*":303, "/":304, ":=":305, "=":306, "<>":307, ">":308, ">=":309, "<":310, "<=":311, "(":400, ")":401, ";":402, ",":403, "\n":404, '\t':405, ' ':406}
        self._media = []
        for temp in self._stringToToken.keys():
            self._media += temp[0]
        self._nextIdentifier = 1000

    def getStringToToken(self):
        return self._stringToToken

    def lex(self):
        length = len(self._string)
        ans = []
        i = 0
        while(i <= length):
            if i == length:
                if self._buffer != "":
                    ans.append(self._toToken(self._buffer))
                    self._buffer = ""
                break

            origin = self._buffer

            inStr = self._string[i]
            i += 1
            if self._isDelimiter(inStr):
                if self._buffer != "":
                    ans.append(self._toToken(self._buffer))
                    self._buffer = ""
                self._buffer += inStr
                ans.append(self._toToken(self._buffer))
                self._buffer = ""
                continue

            new = origin + inStr
            if self._isOperator(new) or self._isIdentifier(new) or self._isKeyword(new) or self._isInteger(new) or self._isMedia(new):
                self._buffer += inStr
            else:
                ans.append(self._toToken(origin))
                self._buffer = inStr
        return ans

    def readFromString(self, string):
        self._string = string

    def readFromFile(self, file):
        file = open(file)
        self._string = ""
        for line in file:
            self._string += line

    def _isKeyword(self, word):
        if word in self._keywords:
            return True
        else:
            return False

    def _isIdentifier(self, word):
        if word == "":
            return False
        if (word[0] < 'a' or word[0] > 'z') and (word[0] < 'A' or word[0] > 'Z'):
            return False
        for i in word[1:]:
            if (i < 'a' or i > 'z') and (i < 'A' or i > 'Z') and (i < '0' or i > '9'):
                return False
        return True

    def _isInteger(self, word):
        for i in word:
            if i < '0' or i > '9':
                return False
        return True

    def _isDelimiter(self, word):
        if word in self._delimiters:
            return True
        else:
            return False

    def _isOperator(self, word):
        if word in self._operators:
            return True
        else:
            return False

    def _isMedia(self, word):
        if word in self._media:
            return True
        else:
            return False

    def _toToken(self, word):
        newToken = Token()
        if self._isKeyword(word) or self._isDelimiter(word) or self._isOperator(word):
            newToken.setTypeId(self._stringToToken[word])
            newToken.setValue(word)
            return newToken
        elif self._isInteger(word):
            newToken.setTypeId(200)
            newToken.setValue(word)
            return newToken
        elif self._isIdentifier(word):
            newToken.setTypeId(self._nextIdentifier)
            # self._nextIdentifier += 1
            newToken.setValue(word)
            # if self._nextIdentifier > 100000:
            #     print("WRONG!!!, the number of Identifiers is too large")
            return  newToken
        else:
            print("WRONG!!!!: word is " + word)
            return newToken
