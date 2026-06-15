from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional

class TokenType(Enum):
    # Literals
    NUMBER_INT = auto()
    NUMBER_FLOAT = auto()
    STRING = auto()
    BOOL_TRUE = auto()
    BOOL_FALSE = auto()
    NULL = auto()
    IDENTIFIER = auto()

    # Keywords
    VAR = auto()
    CONST = auto()
    PUBLIC = auto()
    PRIVATE = auto()
    PROTECTED = auto()
    STATIC = auto()
    ABSTRACT = auto()
    OVERRIDE = auto()
    VIRTUAL = auto()
    CLASS = auto()
    INTERFACE = auto()
    ENUM = auto()
    EXTENDS = auto()
    IMPLEMENTS = auto()
    FUNC = auto()
    RETURN = auto()
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    DO = auto()
    FOREACH = auto()
    IN = auto()
    BREAK = auto()
    CONTINUE = auto()
    SWITCH = auto()
    CASE = auto()
    DEFAULT = auto()
    MATCH = auto()
    WHEN = auto()
    TRY = auto()
    CATCH = auto()
    FINALLY = auto()
    THROW = auto()
    NEW = auto()
    THIS = auto()
    BASE = auto()
    NULL_COALESCING = auto()
    AS = auto()
    IS = auto()
    TYPEOF = auto()
    USE = auto()
    IMPORT = auto()
    ASYNC = auto()
    AWAIT = auto()
    TASK = auto()
    SCHEDULE = auto()
    DEBUG = auto()
    VAR_KW = auto()
    OBJECT = auto()

    # Types as keywords
    TYPE_INT = auto()
    TYPE_FLOAT = auto()
    TYPE_DOUBLE = auto()
    TYPE_STRING = auto()
    TYPE_BOOL = auto()
    TYPE_CHAR = auto()
    TYPE_BYTE = auto()
    TYPE_LONG = auto()
    TYPE_VOID = auto()
    TYPE_OBJECT = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    STAR_STAR = auto()
    SLASH_SLASH = auto()

    # Comparison
    EQUALS = auto()
    NOT_EQUALS = auto()
    LESS = auto()
    GREATER = auto()
    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()

    # Logical
    AND = auto()
    OR = auto()
    NOT = auto()

    # Bitwise
    BIT_AND = auto()
    BIT_OR = auto()
    BIT_XOR = auto()
    BIT_NOT = auto()
    SHIFT_LEFT = auto()
    SHIFT_RIGHT = auto()

    # Assignment
    ASSIGN = auto()
    PLUS_ASSIGN = auto()
    MINUS_ASSIGN = auto()
    STAR_ASSIGN = auto()
    SLASH_ASSIGN = auto()
    PERCENT_ASSIGN = auto()

    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    SEMICOLON = auto()
    COLON = auto()
    COMMA = auto()
    DOT = auto()
    ARROW = auto()
    DOT_DOT = auto()
    QUESTION = auto()
    QUESTION_DOT = auto()
    QUESTION_QUESTION = auto()
    AT = auto()
    HASH = auto()

    # Special
    EOF = auto()
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()

    # Directives
    DIRECTIVE = auto()
    ANNOTATION = auto()


@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    column: int
    literal: Optional[str] = None

    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r}, L{self.line}:{self.column})"
