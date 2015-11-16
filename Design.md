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
>            def lex():
>                """
>                input string(type str)
>                output list[Token]
>                """
>            def readFromString(string):
>                 """
>                 input string(type str)
>                 output None
>                 """
>            def readFromFile(file):
>                 """
>                 input file
>                 """
        4. Private:
            1. parameters:
                1. _result(List of all tokens)
                2. _buffer(the word have been read but not end)
                3. _index(where we have read)
            2. methods:
                1. _
