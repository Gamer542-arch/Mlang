from dataclasses import dataclass, field
from typing import Any, Optional, Union

from .tokens import Token


class Node:
    """Base AST node."""
    def __init__(self, token: Token = None):
        self.token = token

    @property
    def line(self):
        return self.token.line if self.token else 0

    @property
    def column(self):
        return self.token.column if self.token else 0


# --- Expressions ---
class Expr(Node):
    """Base expression node."""

@dataclass
class Literal(Expr):
    value: Any
    token: Token = None

@dataclass
class Variable(Expr):
    name: str
    token: Token = None

@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

@dataclass
class Unary(Expr):
    operator: Token
    right: Expr

@dataclass
class Call(Expr):
    callee: Expr
    arguments: list[Expr]
    token: Token = None

@dataclass
class GetAttr(Expr):
    obj: Expr
    name: str
    token: Token = None

@dataclass
class Index(Expr):
    obj: Expr
    index: Expr
    token: Token = None

@dataclass
class Ternary(Expr):
    condition: Expr
    then_branch: Expr
    else_branch: Expr

@dataclass
class Lambda(Expr):
    params: list["Parameter"]
    body: Union[Expr, list[Node]]
    token: Token = None

@dataclass
class ArrayLiteral(Expr):
    elements: list[Expr]
    token: Token = None

@dataclass
class DictLiteral(Expr):
    pairs: list[tuple[Expr, Expr]]
    token: Token = None

@dataclass
class Cast(Expr):
    type_name: str
    expr: Expr
    token: Token = None

@dataclass
class IsCheck(Expr):
    expr: Expr
    type_name: str
    target: Optional["Variable"] = None

@dataclass
class NullCoalescing(Expr):
    left: Expr
    right: Expr

@dataclass
class AnonymousFunction(Expr):
    params: list["Parameter"]
    body: list[Node]
    return_type: str = None

    @property
    def name(self):
        return "<anonymous>"


# --- Statements ---
class Stmt(Node):
    """Base statement node."""

@dataclass
class ExpressionStmt(Stmt):
    expression: Expr

@dataclass
class VarDecl(Stmt):
    name: str
    type_name: Optional[str]
    initializer: Optional[Expr]
    is_const: bool = False
    token: Token = None

@dataclass
class Block(Stmt):
    statements: list[Stmt]

@dataclass
class IfStmt(Stmt):
    condition: Expr
    then_branch: Stmt
    else_branch: Optional[Stmt]

@dataclass
class WhileStmt(Stmt):
    condition: Expr
    body: Stmt

@dataclass
class DoWhileStmt(Stmt):
    body: Stmt
    condition: Expr

@dataclass
class ForStmt(Stmt):
    initializer: Optional[Stmt]
    condition: Optional[Expr]
    increment: Optional[Expr]
    body: Stmt

@dataclass
class ForEachStmt(Stmt):
    variable: str
    index_var: Optional[str]
    iterable: Expr
    body: Stmt

@dataclass
class BreakStmt(Stmt):
    pass

@dataclass
class ContinueStmt(Stmt):
    pass

@dataclass
class ReturnStmt(Stmt):
    value: Optional[Expr]

@dataclass
class SwitchStmt(Stmt):
    value: Expr
    cases: list[tuple[Optional[Expr], list[Stmt]]]

@dataclass
class MatchStmt(Stmt):
    value: Expr
    arms: list[tuple[Optional[Expr], str, Expr]]

@dataclass
class TryStmt(Stmt):
    try_block: Block
    catch_var: Optional[str]
    catch_type: Optional[str]
    catch_block: Optional[Block]
    finally_block: Optional[Block]

@dataclass
class ThrowStmt(Stmt):
    expression: Expr

@dataclass
class FunctionDecl(Stmt):
    name: str
    params: list["Parameter"]
    return_type: Optional[str]
    body: Block
    is_public: bool = True
    is_static: bool = False
    is_abstract: bool = False
    is_override: bool = False
    is_virtual: bool = False
    is_async: bool = False
    token: Token = None

@dataclass
class ClassDecl(Stmt):
    name: str
    parent: Optional[str]
    interfaces: list[str] = field(default_factory=list)
    fields: list["FieldDecl"] = field(default_factory=list)
    methods: list[FunctionDecl] = field(default_factory=list)
    is_abstract: bool = False
    is_public: bool = True
    token: Token = None

@dataclass
class FieldDecl(Stmt):
    name: str
    type_name: Optional[str]
    initializer: Optional[Expr]
    is_public: bool = True
    is_private: bool = False
    is_protected: bool = False
    is_static: bool = False
    is_const: bool = False
    token: Token = None

@dataclass
class PropertyDecl(Stmt):
    name: str
    type_name: Optional[str]
    getter: Optional[Block]
    setter: Optional[Block]
    token: Token = None

@dataclass
class InterfaceDecl(Stmt):
    name: str
    methods: list[FunctionDecl]
    token: Token = None

@dataclass
class Directive(Stmt):
    name: str
    value: Any
    token: Token = None

@dataclass
class UseStmt(Stmt):
    module: str
    token: Token = None

@dataclass
class ImportStmt(Stmt):
    path: str
    token: Token = None

@dataclass
class Annotation(Stmt):
    name: str
    args: dict
    token: Token = None

@dataclass
class Parameter:
    name: str
    type_name: Optional[str] = None
    default_value: Optional[Expr] = None
    is_variadic: bool = False
    token: Token = None
