import re
from enum import Enum, auto


class TokenType(Enum):
    ID = auto()
    INT = auto()
    OP = auto()
    STR = auto()
    LPAREN = auto()  # (
    RPAREN = auto()  # )
    SEMICOLON = auto()  # ;
    COMMA = auto()  # ,
    EOF = auto()  # End of file
    KW = auto()  # KWs like 'let', 'in', etc.
    NIL = auto()
    DUMMY = auto()  # Special token for 'dummy'


class Token:
    def __init__(self, type, value, line, column):
        self.type = type  # What kind of token (e.g., ID, INT)
        self.value = value  # The actual text/number (e.g., "x", 42)
        self.line = line  # Source code line number
        self.column = column  # Position in the line

    # Returns raw value for punctuation otherwise return the correct token
    def __str__(self):
        if self.type in [TokenType.LPAREN, TokenType.RPAREN,
                         TokenType.SEMICOLON, TokenType.COMMA]:
            return self.value
        elif self.type == TokenType.STR:
            return f"<{self.type.name}:'{self.value}'>"
        elif self.value == 'nil':
            self.type = TokenType.NIL
            return f"<{self.value}>"
        elif self.value == 'dummy':
            self.type = TokenType.DUMMY
            return f"<{self.value}>"
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

    def get_str(self):
        result = []
        self.advance()  # Skip opening quote

        escape_map = {'t': '\t', 'n': '\n', '\\': '\\', "'": "'"}
        allowed_punctuation = {'(', ')', ';', ',', ' '}
        op_symbols = {
            '+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=', '~',
            '|', '$', '!', '#', '%', '^', '_', '[', ']', '{', '}', '"', '`', '?'
        }
        KWs = {
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
                        self.current_char in op_symbols or
                        self.current_char in KWs):
                    raise SyntaxError(
                        f"Invalid character '{self.current_char}' in str at {self.line}:{self.column}. "
                        f"Only letters, digits, specified punctuation, and op symbols allowed."
                    )
                result.append(self.current_char)
            self.advance()

        if not self.current_char:
            raise SyntaxError(f"Unterminated str at {self.line}:{self.column}")

        self.advance()  # Skip closing quote
        return ''.join(result)

    def get_id(self):
        result = []
        while (self.current_char and
               (self.current_char.isalpha() or
                self.current_char.isdigit() or
                self.current_char == '_')):
            result.append(self.current_char)
            self.advance()
        return ''.join(result)

    def get_int(self):
        result = []
        while self.current_char and self.current_char.isdigit():
            result.append(self.current_char)
            self.advance()
        return int(''.join(result))

    def get_op(self):
        op_symbols = {
            '+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=', '~',
            '|', '$', '!', '#', '%', '^', '_', '[', ']', '{', '}', '"', '`', '?'
        }
        result = []
        while self.current_char and self.current_char in op_symbols:
            result.append(self.current_char)
            self.advance()
        return ''.join(result)
    
    def get_KW(self):
        KWs = {
            'let', 'in', 'fn', 'where', 'rec', 'within', 'and', 'or', 'not', 'gr', 
            'ge', 'ls', 'le', 'eq', 'ne'
        }
        result = self.get_id()
        if result in KWs:
            return result
    
    def get_dummy(self):
        if self.current_char == 'd' and self.peek() == 'u' and self.peek(2) == 'm' and self.peek(3) == 'm' and self.peek(4) == 'y':
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            return Token(TokenType.DUMMY, 'dummy', self.line, self.column)
        return None

    def get_next_token(self):
        while self.current_char:
            # Handle DELETE tokens (whitespace/comments)
            if self.current_char in ' \t\n':
                self.skip_whitespace()
                continue

            if self.current_char == '/' and self.peek() == '/':
                self.skip_comment()
                continue

            # Handle STR tokens
            if self.current_char == "'":
                return Token(TokenType.STR, self.get_str(), self.line, self.column)

            # Handle NIL tokens
            if self.current_char == 'n' and self.peek() == 'i' and self.peek(2) == 'l':
                self.advance()
                return Token(TokenType.NIL, 'nil', self.line, self.column)
            
            # Handle dummy tokens
            if self.current_char == 'd' and self.peek() == 'u' and self.peek(2) == 'm' and self.peek(3) == 'm' and self.peek(4) == 'y':
                self.advance()
                return self.get_dummy()
            
            # Handle ID tokens
            if self.current_char.isalpha():
                return Token(TokenType.ID, self.get_id(), self.line, self.column)

            # Handle INT tokens
            if self.current_char.isdigit():
                return Token(TokenType.INT, self.get_int(), self.line, self.column)

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

            # Handle OP tokens
            if self.current_char in {'+', '-', '*', '<', '>', '&', '.', '@',
                                     '/', ':', '=', '~', '|', '$', '!', '#',
                                     '%', '^', '_', '[', ']', '{', '}', '"', '`', '?'}:
                return Token(TokenType.OP, self.get_op(), self.line, self.column)

            raise SyntaxError(f"Unexpected character '{self.current_char}' at {self.line}:{self.column}")

        return Token(TokenType.EOF, None, self.line, self.column)

    def check_KWs(self, token):
        KWs = {
            'let', 'in', 'fn', 'where', 'rec', 'within', 'and', 'or', 'not', 'gr',
            'ge', 'ls', 'le', 'eq', 'ne'
        }
        if token.value in KWs:
            return Token(TokenType.KW, token.value, token.line, token.column)
        return token
    
    def check_NIL(self, token):
        if token.value == 'nil':
            return Token(TokenType.NIL, token.value, token.line, token.column)
        return token
    
    def check_dummy(self, token):
        if token.value == 'dummy':
            return Token(TokenType.DUMMY, token.value, token.line, token.column)
        return token

    def peek(self, offset=1):
        peek_pos = self.position + 1
        return self.source_code[peek_pos] if peek_pos < len(self.source_code) else None

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            token = self.check_KWs(token)
            if token.type == TokenType.EOF:
                break
            tokens.append(token)
        # print("Tokens:", tokens)
        return tokens

# source_code = """
# let x = 53 + 39 // This is a comment
# in Print('Hello World')
# """

# source_code = """
# let Sum(A) = Psum (A,Order A )
# where rec Psum (T,N) = N eq 0 -> 0
#  | Psum(T,N-1)+T N
# in Print ( Sum (1,2,3,4,5) )
# """

# lexer = Lexer(source_code)
# tokens = lexer.tokenize()

# for token in tokens:
#     print(token)
