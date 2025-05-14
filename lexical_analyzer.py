import re
from enum import Enum, auto


class TokenType(Enum):
    IDENTIFIER = auto()
    INTEGER = auto()
    OPERATOR = auto()
    STRING = auto()
    LPAREN = auto()  # (
    RPAREN = auto()  # )
    SEMICOLON = auto()  # ;
    COMMA = auto()  # ,
    EOF = auto()  # End of file
    KEYWORD = auto()  # Keywords like 'let', 'in', etc.


class Token:
    def __init__(self, type, value, line, column):
        self.type = type  # What kind of token (e.g., IDENTIFIER, INTEGER)
        self.value = value  # The actual text/number (e.g., "x", 42)
        self.line = line  # Source code line number
        self.column = column  # Position in the line

    # Returns raw value for punctuation otherwise return the correct token
    def __str__(self):
        if self.type in [TokenType.LPAREN, TokenType.RPAREN,
                         TokenType.SEMICOLON, TokenType.COMMA]:
            return self.value
        return f"<{self.type.name}:{self.value}>"

    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code             # The complete program text
        self.position = 0                          # Current character position
        self.line = 1                              # Current line number
        self.column = 1                            # Current column number
        self.current_char = self.source_code[0] if source_code else None

    # Moves to the next character in the source code
    def advance(self):
        self.position += 1
        if self.position < len(self.source_code):
            self.current_char = self.source_code[self.position]
            self.column += 1
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char and self.current_char in ' \t\n':
            if self.current_char == '\n':  # Eol
                self.line += 1
                self.column = 0
            elif self.current_char == '\t':  # ht (horizontal tab)
                self.column += 8 - (self.column % 8)
            self.advance()

    def skip_comment(self):
        """Handle // comments until end of line"""
        if self.current_char == '/' and self.peek() == '/':
            self.advance()  # Skip first /
            self.advance()  # Skip second /

            while self.current_char and self.current_char != '\n':
                if not (self.current_char in "'();,\\ " or
                        self.current_char == '\t' or
                        self.current_char.isalpha() or
                        self.current_char.isdigit() or
                        self.current_char in '+-*<>&.@/:~|$!#%^_[]{}"`?'):
                    raise SyntaxError(f"Invalid comment character '{self.current_char}' at {self.line}:{self.column}")
                self.advance()
            if self.current_char == '\n':
                self.advance()

    def get_string(self):
        result = []
        self.advance()  # Skip opening quote

        escape_map = {'t': '\t', 'n': '\n', '\\': '\\', "'": "'"}
        allowed_punctuation = {'(', ')', ';', ',', ' '}
        operator_symbols = {
            '+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=', '~',
            '|', '$', '!', '#', '%', '^', '_', '[', ']', '{', '}', '"', '`', '?'
        }
        keywords = {
            'let', 'in', 'fn', 'where', 'rec', 'within', 'and', 'or', 'not', 'gr', 
            'ge', 'ls', 'le', 'eq', 'ne', 'dummy'
        }

        while self.current_char and self.current_char != "'":
            if self.current_char == '\\':
                # Handle escape sequences
                self.advance()
                if self.current_char in escape_map:
                    result.append(escape_map[self.current_char])
                else:
                    raise SyntaxError(
                        f"Invalid escape sequence '\\{self.current_char}' at {self.line}:{self.column}. "
                        f"Only \\t, \\n, \\\\, and \\' are allowed."
                    )
            else:
                # Validate allowed characters
                if not (self.current_char in allowed_punctuation or
                        self.current_char.isalpha() or
                        self.current_char.isdigit() or
                        self.current_char in operator_symbols or
                        self.current_char in keywords):
                    raise SyntaxError(
                        f"Invalid character '{self.current_char}' in string at {self.line}:{self.column}. "
                        f"Only letters, digits, specified punctuation, and operator symbols allowed."
                    )
                result.append(self.current_char)
            self.advance()

        if not self.current_char:
            raise SyntaxError(f"Unterminated string at {self.line}:{self.column}")

        self.advance()  # Skip closing quote
        return ''.join(result)

    def get_identifier(self):
        result = []
        while (self.current_char and
               (self.current_char.isalpha() or
                self.current_char.isdigit() or
                self.current_char == '_')):
            result.append(self.current_char)
            self.advance()
        return ''.join(result)

    def get_integer(self):
        result = []
        while self.current_char and self.current_char.isdigit():
            result.append(self.current_char)
            self.advance()
        return int(''.join(result))

    def get_operator(self):
        operator_symbols = {
            '+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=', '~',
            '|', '$', '!', '#', '%', '^', '_', '[', ']', '{', '}', '"', '`', '?'
        }
        result = []
        while self.current_char and self.current_char in operator_symbols:
            result.append(self.current_char)
            self.advance()
        return ''.join(result)
    
    def get_keyword(self):
        keywords = {
            'let', 'in', 'fn', 'where', 'rec', 'within', 'and', 'or', 'not', 'gr', 
            'ge', 'ls', 'le', 'eq', 'ne', 'dummy'
        }
        result = self.get_identifier()
        if result in keywords:
            return result

    def get_next_token(self):
        while self.current_char:
            # Handle DELETE tokens (whitespace/comments)
            if self.current_char in ' \t\n':
                self.skip_whitespace()
                continue

            if self.current_char == '/' and self.peek() == '/':
                self.skip_comment()
                continue

            # Handle STRING tokens
            if self.current_char == "'":
                return Token(TokenType.STRING, self.get_string(), self.line, self.column)

            # Handle IDENTIFIER tokens
            if self.current_char.isalpha():
                return Token(TokenType.IDENTIFIER, self.get_identifier(), self.line, self.column)

            # Handle INTEGER tokens
            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.get_integer(), self.line, self.column)

            # Handle punctuation
            if self.current_char == '(':
                token = Token(TokenType.LPAREN, '(', self.line, self.column)
                self.advance()
                return token

            if self.current_char == ')':
                token = Token(TokenType.RPAREN, ')', self.line, self.column)
                self.advance()
                return token

            if self.current_char == ';':
                token = Token(TokenType.SEMICOLON, ';', self.line, self.column)
                self.advance()
                return token

            if self.current_char == ',':
                token = Token(TokenType.COMMA, ',', self.line, self.column)
                self.advance()
                return token

            # Handle OPERATOR tokens
            if self.current_char in {'+', '-', '*', '<', '>', '&', '.', '@',
                                     '/', ':', '=', '~', '|', '$', '!', '#',
                                     '%', '^', '_', '[', ']', '{', '}', '"', '`', '?'}:
                return Token(TokenType.OPERATOR, self.get_operator(), self.line, self.column)

            raise SyntaxError(f"Unexpected character '{self.current_char}' at {self.line}:{self.column}")

        return Token(TokenType.EOF, None, self.line, self.column)

    def check_keywords(self, token):
        keywords = {
            'let', 'in', 'fn', 'where', 'rec', 'within', 'and', 'or', 'not', 'gr',
            'ge', 'ls', 'le', 'eq', 'ne', 'dummy'
        }
        if token.value in keywords:
            return Token(TokenType.KEYWORD, token.value, token.line, token.column)
        return token

    def peek(self):
        peek_pos = self.position + 1
        return self.source_code[peek_pos] if peek_pos < len(self.source_code) else None

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            token = self.check_keywords(token)
            if token.type == TokenType.EOF:
                break
            tokens.append(token)
        return tokens

# source_code = """
# let x = 53 + 39 // This is a comment
# in Print('Hello World')
# """

source_code = """
let Sum(A) = Psum (A,Order A )
where rec Psum (T,N) = N eq 0 -> 0
 | Psum(T,N-1)+T N
in Print ( Sum (1,2,3,4,5) )
"""

lexer = Lexer(source_code)
tokens = lexer.tokenize()

# for token in tokens:
#     print(token)
