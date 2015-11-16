## Design for Lex and Syntactic Analysis ##

- Part 1: Lex Anlysis
- Part 2: Syntactic Anlysis


1. Overview

2. Structure

3. Relationship

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
        5. Delimiter(Every Delimiter should have different typeID): '('(400), ')'(401), ;(402), ','(403)
    
    2. Definition: Struct of tokens
        1. Struct name: Token
        2. int typeID
        3. string value
    3. Definition: Class LexAnalysis
        1. Class name: LexAnalysis
        2. Init Parameters:
        3. Interfaces:
            1. def lex():
                - input None
                - output list[Token]
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
                - _index(where we have read)
                - _string(raw input, default value is "")
                - _keywords(the keywords)
                - _delimiters(the delimiters)
                - _Operators(the operators)
            2. methods:
                - _readAChar():
                    1. judge what origin buffer is
                    1. in = _string[_index]
                    2. _index += 1
                    2. if in is Delimiter or EOF, and origin is not "", origin buffer -> token, continue
                    3. judge what buffer is now
                    4. if buffer now is Wrong . throw exception
                - _isKeyword(t):
                    1. if t in _keywords, return True
                    2. else return False
                - _isInteger(t):
                    1. for i in t, if i is not a digit return False
                    2. return True
                - _isDelimiters(t):
                    1. if t in _delimiters, return True, else return False
                - _isOperators(t):
                    1. if t in _operators, return True, else return False
                - _isIdentifier(t):
                    1. t[0] is char, t[i] is char or digit
