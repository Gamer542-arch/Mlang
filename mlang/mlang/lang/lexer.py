from .tokens import Token, TokenType


class LexerError(Exception):
    def __init__(self, message: str, line: int, column: int):
        self.line = line
        self.column = column
        super().__init__(f"LexerError at {line}:{column}: {message}")


KEYWORDS = {
    "var": TokenType.VAR,
    "const": TokenType.CONST,
    "public": TokenType.PUBLIC,
    "private": TokenType.PRIVATE,
    "protected": TokenType.PROTECTED,
    "static": TokenType.STATIC,
    "abstract": TokenType.ABSTRACT,
    "override": TokenType.OVERRIDE,
    "virtual": TokenType.VIRTUAL,
    "class": TokenType.CLASS,
    "enum": TokenType.ENUM,
    "interface": TokenType.INTERFACE,
    "extends": TokenType.EXTENDS,
    "implements": TokenType.IMPLEMENTS,
    "func": TokenType.FUNC,
    "return": TokenType.RETURN,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "for": TokenType.FOR,
    "while": TokenType.WHILE,
    "do": TokenType.DO,
    "foreach": TokenType.FOREACH,
    "in": TokenType.IN,
    "break": TokenType.BREAK,
    "continue": TokenType.CONTINUE,
    "switch": TokenType.SWITCH,
    "case": TokenType.CASE,
    "default": TokenType.DEFAULT,
    "match": TokenType.MATCH,
    "when": TokenType.WHEN,
    "try": TokenType.TRY,
    "catch": TokenType.CATCH,
    "finally": TokenType.FINALLY,
    "throw": TokenType.THROW,
    "new": TokenType.NEW,
    "this": TokenType.THIS,
    "base": TokenType.BASE,
    "as": TokenType.AS,
    "is": TokenType.IS,
    "typeof": TokenType.TYPEOF,
    "use": TokenType.USE,
    "import": TokenType.IMPORT,
    "async": TokenType.ASYNC,
    "await": TokenType.AWAIT,
    "Task": TokenType.TASK,
    "Schedule": TokenType.SCHEDULE,
    "Debug": TokenType.DEBUG,
    "object": TokenType.OBJECT,
    "true": TokenType.BOOL_TRUE,
    "false": TokenType.BOOL_FALSE,
    "null": TokenType.NULL,
    "int": TokenType.TYPE_INT,
    "float": TokenType.TYPE_FLOAT,
    "double": TokenType.TYPE_DOUBLE,
    "string": TokenType.TYPE_STRING,
    "bool": TokenType.TYPE_BOOL,
    "char": TokenType.TYPE_CHAR,
    "byte": TokenType.TYPE_BYTE,
    "long": TokenType.TYPE_LONG,
    "void": TokenType.TYPE_VOID,
}


class Lexer:
    def __init__(self, source: str, filename: str = "<stdin>"):
        self.source = source
        self.filename = filename
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: list[Token] = []
        self.start = 0

    def error(self, message: str):
        raise LexerError(message, self.line, self.column)

    def peek(self, offset: int = 0) -> str:
        idx = self.pos + offset
        if idx >= len(self.source):
            return "\0"
        return self.source[idx]

    def advance(self) -> str:
        ch = self.source[self.pos]
        self.pos += 1
        self.column += 1
        return ch

    def match(self, expected: str) -> bool:
        if self.peek() == expected:
            self.pos += 1
            self.column += 1
            return True
        return False

    def skip_whitespace(self):
        while self.pos < len(self.source):
            ch = self.peek()
            if ch in " \t\r":
                self.advance()
            elif ch == "\n":
                self.advance()
                self.line += 1
                self.column = 1
            else:
                break

    def read_string(self, quote: str):
        result = []
        while self.pos < len(self.source):
            ch = self.advance()
            if ch == "\\":
                if self.pos < len(self.source):
                    esc = self.advance()
                    result.append({
                        "n": "\n", "t": "\t", "r": "\r",
                        "0": "\0", "\\": "\\", '"': '"', "'": "'",
                    }.get(esc, esc))
            elif ch == quote:
                return "".join(result)
            else:
                result.append(ch)
        self.error("Unterminated string")

    def read_number(self):
        result = []
        is_float = False
        while self.pos < len(self.source) and (self.peek().isdigit() or self.peek() == "."):
            if self.peek() == ".":
                if is_float:
                    break
                is_float = True
            result.append(self.advance())
        num_str = "".join(result)
        if is_float:
            return float(num_str), TokenType.NUMBER_FLOAT
        return int(num_str), TokenType.NUMBER_INT

    def read_identifier(self):
        result = []
        while self.pos < len(self.source) and (self.peek().isalnum() or self.peek() == "_"):
            result.append(self.advance())
        word = "".join(result)
        token_type = KEYWORDS.get(word)
        if token_type is None:
            token_type = TokenType.IDENTIFIER
        return word, token_type

    def read_directive(self):
        result = []
        while self.pos < len(self.source) and self.peek() != "\n":
            result.append(self.advance())
        return "".join(result).strip()

    def tokenize(self) -> list[Token]:
        while self.pos < len(self.source):
            self.skip_whitespace()
            if self.pos >= len(self.source):
                break

            self.start = self.pos
            ch = self.advance()

            # Directives (#version, #name, etc.)
            if ch == "#" and self.peek().isalpha():
                directive = self.read_directive()
                self.tokens.append(Token(TokenType.DIRECTIVE, directive, self.line, self.column, self.filename))
                continue

            # Single-line comments
            if ch == "/" and self.peek() == "/":
                while self.pos < len(self.source) and self.peek() != "\n":
                    self.advance()
                continue

            # Block comments
            if ch == "/" and self.peek() == "*":
                self.advance()  # consume *
                nesting = 1
                while nesting > 0 and self.pos < len(self.source):
                    if self.peek() == "/" and self.pos + 1 < len(self.source) and self.source[self.pos + 1] == "*":
                        self.advance()
                        self.advance()
                        nesting += 1
                    elif self.peek() == "*" and self.pos + 1 < len(self.source) and self.source[self.pos + 1] == "/":
                        self.advance()
                        self.advance()
                        nesting -= 1
                    elif self.peek() == "\n":
                        self.advance()
                        self.line += 1
                        self.column = 1
                    else:
                        self.advance()
                continue

            # Strings
            if ch in "\"'":
                value = self.read_string(ch)
                self.tokens.append(Token(TokenType.STRING, value, self.line, self.column))
                continue

            # Numbers
            if ch.isdigit():
                self.pos -= 1
                self.column -= 1
                value, ttype = self.read_number()
                self.tokens.append(Token(ttype, value, self.line, self.column))
                continue

            # Identifiers and keywords
            if ch.isalpha() or ch == "_":
                self.pos -= 1
                self.column -= 1
                word, ttype = self.read_identifier()
                self.tokens.append(Token(ttype, word, self.line, self.column))
                continue

            # Operators and delimiters
            token = self._make_single_char_token(ch)
            if token:
                self.tokens.append(token)
                continue

            self.error(f"Unexpected character: {ch!r}")

        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens

    def _make_single_char_token(self, ch: str) -> Token:
        column = self.column
        line = self.line

        two_char = {
            "==": TokenType.EQUALS,
            "!=": TokenType.NOT_EQUALS,
            "<=": TokenType.LESS_EQUAL,
            ">=": TokenType.GREATER_EQUAL,
            "&&": TokenType.AND,
            "||": TokenType.OR,
            "++": None,  # handled later
            "--": None,
            "->": TokenType.ARROW,
            "..": TokenType.DOT_DOT,
            "??": TokenType.QUESTION_QUESTION,
            "?.": TokenType.QUESTION_DOT,
            "**": TokenType.STAR_STAR,
            "//": TokenType.SLASH_SLASH,
            "+=": TokenType.PLUS_ASSIGN,
            "-=": TokenType.MINUS_ASSIGN,
            "*=": TokenType.STAR_ASSIGN,
            "/=": TokenType.SLASH_ASSIGN,
            "%=": TokenType.PERCENT_ASSIGN,
            "<<": TokenType.SHIFT_LEFT,
            ">>": TokenType.SHIFT_RIGHT,
        }

        if self.pos < len(self.source):
            two = ch + self.peek()
            if two in two_char:
                self.advance()
                return Token(two_char[two], two, line, column)

        single = {
            "+": TokenType.PLUS, "-": TokenType.MINUS,
            "*": TokenType.STAR, "/": TokenType.SLASH,
            "%": TokenType.PERCENT,
            "=": TokenType.ASSIGN,
            "<": TokenType.LESS, ">": TokenType.GREATER,
            "!": TokenType.NOT,
            "&": TokenType.BIT_AND, "|": TokenType.BIT_OR,
            "^": TokenType.BIT_XOR, "~": TokenType.BIT_NOT,
            "(": TokenType.LPAREN, ")": TokenType.RPAREN,
            "{": TokenType.LBRACE, "}": TokenType.RBRACE,
            "[": TokenType.LBRACKET, "]": TokenType.RBRACKET,
            ";": TokenType.SEMICOLON, ":": TokenType.COLON,
            ",": TokenType.COMMA, ".": TokenType.DOT,
            "?": TokenType.QUESTION,
            "@": TokenType.AT,
        }

        if ch in single:
            return Token(single[ch], ch, line, column)

        return None
