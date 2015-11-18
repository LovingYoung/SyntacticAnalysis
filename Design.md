## Design for Lex and Syntactic Analysis ##

- Part 1: Lex Anlysis
- Part 2: Syntactic Anlysis


1. Overview

2. Structure

* * * * * 
### Design for Lex Analysis ###

1. Overview
    1. Input: a String.(piece of Code that make sense(or not))
    2. Output: An array of tokens. the token is the meaning of every word and his value
    3. Think: status change

2. Structure
    1. Definition: kinds of tokens
        1. Keywords(Every Keyword should have different typeID): PROGRAM(1), BEGIN(2), END(3), CONST(4), VAR(5), WHILE(6), DO(7), IF(8), THEN(9).
        2. Identifier(Every Identifier should have different typeID(1000 -> INT_MAX)): Begin with character and organized by characters and digits.
        3. Interger(Every Integer should have the same typeID(200)): Begin with digit and organized by digits.
        4. Operator(Every Integer should have different typeID):+(301), -(302), *(303), /(304), :=(305), =(306), <>(307), >(308), >=(309), <(310), <=(311),
        5. Delimiter(Every Delimiter should have different typeID): [EMPTY](0) '('(400), ')'(401), ;(402), ','(403), '\n'(404), '\t'(405), ' '(406)
    
    2. Definition: Struct of tokens
        1. Struct name: Token
        2. int typeID
        3. string value
    3. Definition: Class LexAnalysis
        1. Class name: LexAnalysis
        2. Init Parameters:
        3. Interfaces:
            1. def lex():
                1. input None
                2. output list[Token]
                1. if i comes to EOF, and origin buffer is not "", origin buffer -> token, break
                1. in = _string[i]
                2. i += 1
                2. if in is Delimiter, and origin buffer is not "", origin buffer -> token, continue
                2. buffer += in
                3. judge what buffer is now
                4. if buffer now is Wrong . throw exception
            2. def readFromString(string):
                - input string(type str)
                - output None
            3. def readFromFile(file):
                - input file
                - output None
        4. Private:
            1. parameters:
                - _result(List of all tokens)
                - _buffer(the word have been read but not end)
                - _string(raw input, default value is "")
                - _keywords(the keywords)
                - _delimiters(the delimiters)
                - _Operators(the operators)
                - _stringToToken(Map from strings to token)
                - _nextIdentifier(default is 1000, and add when a token of Identifier added)
            2. methods:
                - _readAChar():
                - _isKeyword(t):
                    1. if t in _keywords, return True
                    2. else return False
                - _isInteger(t):
                    1. for i in t, if i is not a digit return False
                    2. return True
                - _isDelimiter(t):
                    1. if t in _delimiters, return True, else return False
                - _isOperator(t):
                    1. if t in _operators, return True, else return False
                - _isIdentifier(t):
                    1. t[0] is char, t[i] is char or digit
                - _toToken(t):
                    1. take a map. from string to int
                    2. if new token's id >= 1000 and id < 100000, self._nextIdentifier += 1

* * * * *

1. Overview
    1. Input: an array of Tokens
    2. Output: the types of every sentence
    3. Think: recussive descent

2. Structure
    1. Definition of struct Sentence:
        - typeId(100000 -> 200000) -> build-in sentences: 100000->110000, running temp sentences 110000 -> 200000
        - typeName
        - consist -> a list of tokens' or sentences' typeId
        - _buildFirst() -> build first list
        - _buildFollow() -> build follow list
        - _first -> storage first list
        - _follow -> storage follow list
        - getFirst(): return first list
        - getFollow(): return fllow list
        - process(): judge next some tokens, if next some tokens is OK return (True,sons) else return (False, [])
        
    2. Definition of struct Instance:
        - maps -> a map from typeId to sentence (the same as Solution.maps)
        - typeId: what is the instance belong to Sentence
        - typeName: the typeName
        - token: the token has been read
        - sons

    3. Definition of Solution:
        1. Interfaces:
            - getSolution(): input[an array of Tokens], output[the definition of the whole text].
            - Implement:
                1. instantiate the sentence whose id is 100000. and run it's process().
                2. return the root of parseTree
        2. Private Parameters and Methods:
            - Parameters: 
                - sentences -> a list of all sentences
                - tokenArrays -> the array of all tokens
                - maps -> a map from typeId to sentence
                - parseTree-> default is None, after process, point to the root of parse tree
            - Methods:
                - __init__():
                    - instantiate all the definition of sentence
                    - self.tokenArrays = LexAnalysis.lex()
