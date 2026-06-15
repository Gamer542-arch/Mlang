"""GLanguage errors."""

class GLangError(Exception):
    """Base GLanguage error."""

class LexerError(GLangError):
    def __init__(self, message: str, line: int = 0, column: int = 0):
        self.line = line
        self.column = column
        super().__init__(f"Lexer error at {line}:{column}: {message}")

class ParserError(GLangError):
    def __init__(self, message: str, line: int = 0, column: int = 0):
        self.line = line
        self.column = column
        super().__init__(f"Parser error at {line}:{column}: {message}")

class RuntimeError_(GLangError):
    def __init__(self, message: str, line: int = 0):
        self.line = line
        super().__init__(f"Runtime error at line {line}: {message}")

class TypeError_(GLangError):
    def __init__(self, message: str, line: int = 0):
        self.line = line
        super().__init__(f"Type error at line {line}: {message}")
