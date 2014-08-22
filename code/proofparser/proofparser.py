# Bismillahi-r-Rahmani-r-Rahim

import re

class Token(object):
    lbp = 0
    def __repr__(self):
        return 'Token(%r)' % self.id

class EndToken(Token):
    id = 'END'

class LiteralToken(Token):
    def __init__(self, parser, value):
        self.id = value

    def nud(self):
        return self.id

class OperatorToken(Token):
    def __init__(self, parser, id_):
        self.parser = parser
        self.id = id_
    
    lbp = 10
    def led(self, left):
        right = self.parser.expression(10)
        return left + right

class LeftBracketToken(Token):
    def __init__(self, parser):
        self.parser = parser
        self.id = '('

    def nud(self):
        expr = self.parser.expression()
        self.parser.advance(")")
        return expr

class ProofParser(object):
    def __init__(self):
        self.token = None

    def expression(self, rbp=0):
        t = self.token
        self.token = self.next()
        left = t.nud()
        while rbp < self.token.lbp:
            t = self.token
            self.token = self.next()
            left = t.led(left)
        return left

    def advance(id=None):
        if id and self.token.id != id:
            raise SyntaxError("Expected %r" % id)
        self.token = self.next()

    token_pat = re.compile("\s*(?:(\w+)|(.))")

    def tokenize(self, program):
        for literal, operator in self.token_pat.findall(program):
            if literal:
                yield LiteralToken(self, literal)
            elif operator in {'P', '=>', ')'}:
                yield OperatorToken(self, operator)
            elif operator == '(':
                yield LeftBracketToken(self)
            else:
                raise SyntaxError("Unknown operator: %r" % operator)
        yield EndToken()

    def parse(self, source):
        tokens = self.tokenize(source)
        self.next = tokens.next
        self.token = self.next()
        return self.expression()
    
            

        
