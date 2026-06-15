from typing import Any, Optional, Callable

from .tokens import Token, TokenType
from .ast_nodes import *
from .environment import Environment


# Global counter for unique expression IDs
_expr_id_counter = [0]


def _expr_key(expr: Expr) -> int:
    _expr_id_counter[0] += 1
    return _expr_id_counter[0]


class ReturnSignal(Exception):
    def __init__(self, value: Any):
        self.value = value


class BreakSignal(Exception):
    pass


class ContinueSignal(Exception):
    pass


class GLangCallable:
    """Callable GLanguage function/method."""

    def __init__(self, decl: FunctionDecl, closure: Environment, is_initializer: bool = False):
        self.decl = decl
        self.closure = closure
        self.is_initializer = is_initializer

    @property
    def name(self) -> str:
        return self.decl.name

    @property
    def arity(self) -> int:
        return len(self.decl.params)

    def call(self, interpreter: "Interpreter", arguments: list[Any]) -> Any:
        env = Environment(self.closure)
        for i, param in enumerate(self.decl.params):
            if param.is_variadic:
                value = arguments[i:]
            else:
                value = arguments[i] if i < len(arguments) else None
            env.define(param.name, value, False)

        try:
            interpreter.execute_block(self.decl.body.statements, env)
        except ReturnSignal as ret:
            return ret.value
        return None


class NativeFunction:
    """Built-in function implemented in Python."""

    def __init__(self, name: str, arity: int, func: Callable):
        self._name = name
        self._arity = arity
        self._func = func

    @property
    def name(self) -> str:
        return self._name

    @property
    def arity(self) -> int:
        return self._arity

    def call(self, interpreter: "Interpreter", arguments: list[Any]) -> Any:
        return self._func(*arguments)


class GLangInstance:
    """Instance of a GLanguage class."""

    def __init__(self, klass: "GLangClass"):
        self.klass = klass
        self.fields: dict[str, Any] = {}

    def get(self, name: str) -> Any:
        if name in self.fields:
            return self.fields[name]
        method = self.klass.find_method(name)
        if method:
            return method.bind(self)
        raise RuntimeError(f"Undefined property '{name}' on {self.klass.name}")

    def set(self, name: str, value: Any):
        self.fields[name] = value


class GLangClass:
    """GLanguage class definition."""

    def __init__(self, name: str, parent: Optional["GLangClass"],
                 methods: dict[str, GLangCallable]):
        self.name = name
        self.parent = parent
        self.methods = methods

    def find_method(self, name: str) -> Optional[GLangCallable]:
        if name in self.methods:
            return self.methods[name]
        if self.parent is not None:
            return self.parent.find_method(name)
        return None

    def call(self, interpreter: "Interpreter", arguments: list[Any]) -> Any:
        instance = GLangInstance(self)
        initializer = self.find_method("init")
        if initializer:
            initializer.bind(instance).call(interpreter, arguments)
        return instance


class BoundMethod:
    """Bound method (instance + method)."""

    def __init__(self, instance: GLangInstance, method: GLangCallable):
        self.instance = instance
        self.method = method

    @property
    def name(self) -> str:
        return self.method.name

    @property
    def arity(self) -> int:
        return self.method.arity

    def call(self, interpreter: "Interpreter", arguments: list[Any]) -> Any:
        env = Environment(self.method.closure)
        env.define("this", self.instance, False)
        for i, param in enumerate(self.method.decl.params):
            if param.is_variadic:
                value = arguments[i:]
            else:
                value = arguments[i] if i < len(arguments) else None
            env.define(param.name, value, False)
        try:
            interpreter.execute_block(self.method.decl.body.statements, env)
        except ReturnSignal as ret:
            return ret.value
        return None


class Interpreter:
    """Tree-walk interpreter for GLanguage AST."""

    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals
        self.locals: dict[int, int] = {}
        self.classes: dict[str, GLangClass] = {}
        self.functions: dict[str, GLangCallable] = {}

        self._define_natives()

    def _define_natives(self):
        natives = {
            "print": NativeFunction("print", -1, lambda *args: print(*args)),
            "println": NativeFunction("println", -1, lambda *args: print(*args)),
            "type": NativeFunction("type", 1, lambda x: type(x).__name__),
            "str": NativeFunction("str", 1, str),
            "int": NativeFunction("int", 1, lambda x: int(x) if x is not None else 0),
            "float": NativeFunction("float", 1, lambda x: float(x) if x is not None else 0.0),
            "bool": NativeFunction("bool", 1, bool),
            "len": NativeFunction("len", 1, lambda x: len(x) if x is not None else 0),
            "input": NativeFunction("input", 0, input),
            "range": NativeFunction("range", 3, lambda *a: NativeRange(a)),
            "Range": NativeFunction("Range", 2, lambda s, e: list(range(s, e))),
        }
        for name, func in natives.items():
            self.globals.define(name, func, True)

    def resolve(self, expr: Expr, depth: int):
        self.locals[id(expr)] = depth

    def interpret(self, statements: list[Stmt]):
        try:
            for stmt in statements:
                self.execute(stmt)
        except ReturnSignal as ret:
            return ret.value
        except BreakSignal:
            raise RuntimeError("'break' outside loop")
        except ContinueSignal:
            raise RuntimeError("'continue' outside loop")

    def execute(self, stmt: Stmt):
        if isinstance(stmt, Block):
            self.execute_block(stmt.statements, Environment(self.environment))
        elif isinstance(stmt, ExpressionStmt):
            self.evaluate(stmt.expression)
        elif isinstance(stmt, VarDecl):
            self._execute_var_decl(stmt)
        elif isinstance(stmt, FunctionDecl):
            self._execute_function_decl(stmt)
        elif isinstance(stmt, ClassDecl):
            self._execute_class_decl(stmt)
        elif isinstance(stmt, IfStmt):
            self._execute_if(stmt)
        elif isinstance(stmt, WhileStmt):
            self._execute_while(stmt)
        elif isinstance(stmt, DoWhileStmt):
            self._execute_do_while(stmt)
        elif isinstance(stmt, ForStmt):
            self._execute_for(stmt)
        elif isinstance(stmt, ForEachStmt):
            self._execute_foreach(stmt)
        elif isinstance(stmt, ReturnStmt):
            self._execute_return(stmt)
        elif isinstance(stmt, BreakStmt):
            raise BreakSignal()
        elif isinstance(stmt, ContinueStmt):
            raise ContinueSignal()
        elif isinstance(stmt, SwitchStmt):
            self._execute_switch(stmt)
        elif isinstance(stmt, TryStmt):
            self._execute_try(stmt)
        elif isinstance(stmt, ThrowStmt):
            self._execute_throw(stmt)
        elif isinstance(stmt, Directive):
            pass  # directives handled at lexer level
        elif isinstance(stmt, UseStmt):
            pass  # modules not yet implemented
        else:
            raise RuntimeError(f"Unknown statement type: {type(stmt)}")

    def execute_block(self, statements: list[Stmt], env: Environment):
        previous = self.environment
        try:
            self.environment = env
            for stmt in statements:
                self.execute(stmt)
        finally:
            self.environment = previous

    def evaluate(self, expr: Expr) -> Any:
        if isinstance(expr, Literal):
            return expr.value
        elif isinstance(expr, Variable):
            return self._lookup_variable(expr.name, expr)
        elif isinstance(expr, Binary):
            return self._evaluate_binary(expr)
        elif isinstance(expr, Unary):
            return self._evaluate_unary(expr)
        elif isinstance(expr, Call):
            return self._evaluate_call(expr)
        elif isinstance(expr, GetAttr):
            return self._evaluate_getattr(expr)
        elif isinstance(expr, Index):
            return self._evaluate_index(expr)
        elif isinstance(expr, Ternary):
            return self._evaluate_ternary(expr)
        elif isinstance(expr, ArrayLiteral):
            return [self.evaluate(e) for e in expr.elements]
        elif isinstance(expr, DictLiteral):
            return {self.evaluate(k): self.evaluate(v) for k, v in expr.pairs}
        elif isinstance(expr, Lambda):
            return self._evaluate_lambda(expr)
        elif isinstance(expr, AnonymousFunction):
            return self._evaluate_lambda(expr)
        elif isinstance(expr, NullCoalescing):
            left = self.evaluate(expr.left)
            return left if left is not None else self.evaluate(expr.right)
        elif isinstance(expr, IsCheck):
            return self._evaluate_is(expr)
        elif isinstance(expr, Cast):
            return self._evaluate_cast(expr)
        raise RuntimeError(f"Unknown expression type: {type(expr)}")

    def _lookup_variable(self, name: str, expr: Expr) -> Any:
        key = id(expr)
        if key in self.locals:
            return self.environment.get_at(self.locals[key], name)
        if self.environment.has(name):
            return self.environment.get(name)
        return self.globals.get(name)

    def _evaluate_binary(self, expr: Binary) -> Any:
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        op = expr.operator.type

        if op in (TokenType.PLUS, TokenType.MINUS, TokenType.STAR, TokenType.SLASH,
                   TokenType.PERCENT, TokenType.STAR_STAR, TokenType.SLASH_SLASH):
            return self._arithmetic(left, right, op)
        elif op == TokenType.PLUS_ASSIGN:
            val = self._arithmetic(left, right, TokenType.PLUS)
            self.environment.assign(expr.left.name if isinstance(expr.left, Variable) else "", val)
            return val
        elif op in (TokenType.EQUALS, TokenType.NOT_EQUALS, TokenType.LESS,
                     TokenType.GREATER, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL):
            return self._compare(left, right, op)
        elif op == TokenType.AND:
            return left and right
        elif op == TokenType.OR:
            return left or right
        elif op == TokenType.BIT_AND:
            return (left or 0) & (right or 0)
        elif op == TokenType.BIT_OR:
            return (left or 0) | (right or 0)
        elif op == TokenType.BIT_XOR:
            return (left or 0) ^ (right or 0)
        elif op == TokenType.SHIFT_LEFT:
            return (left or 0) << (right or 0)
        elif op == TokenType.SHIFT_RIGHT:
            return (left or 0) >> (right or 0)
        elif op == TokenType.ASSIGN:
            if isinstance(expr.left, Variable):
                self._assign_variable(expr.left, right)
            elif isinstance(expr.left, GetAttr):
                obj = self.evaluate(expr.left.obj)
                if isinstance(obj, GLangInstance):
                    obj.set(expr.left.name, right)
            elif isinstance(expr.left, Index):
                obj = self.evaluate(expr.left.obj)
                index = self.evaluate(expr.left.index)
                if isinstance(obj, list):
                    obj[index] = right
                elif isinstance(obj, dict):
                    obj[index] = right
            return right
        raise RuntimeError(f"Unknown operator: {op}")

    def _assign_variable(self, expr: Variable, value: Any):
        key = id(expr)
        if key in self.locals:
            self.environment.assign_at(self.locals[key], expr.name, value)
        elif self.environment.has(expr.name):
            self.environment.assign(expr.name, value)
        else:
            self.globals.assign(expr.name, value)

    def _arithmetic(self, left: Any, right: Any, op: TokenType) -> Any:
        if op == TokenType.PLUS:
            if isinstance(left, str):
                return left + (str(right) if right is not None else "")
            if isinstance(right, str):
                return (str(left) if left is not None else "") + right
        if isinstance(left, str) and op in (TokenType.STAR,):
            return left * right

        left = left if left is not None else 0
        right = right if right is not None else 0

        ops = {
            TokenType.PLUS: lambda: left + right,
            TokenType.MINUS: lambda: left - right,
            TokenType.STAR: lambda: left * right,
            TokenType.SLASH: lambda: left / right,
            TokenType.PERCENT: lambda: left % right,
            TokenType.STAR_STAR: lambda: left ** right,
            TokenType.SLASH_SLASH: lambda: left // right,
        }
        func = ops.get(op)
        if func:
            return func()
        raise RuntimeError(f"Unknown arithmetic operator: {op}")

    def _compare(self, left: Any, right: Any, op: TokenType) -> bool:
        ops = {
            TokenType.EQUALS: lambda: left == right,
            TokenType.NOT_EQUALS: lambda: left != right,
            TokenType.LESS: lambda: left < right,
            TokenType.GREATER: lambda: left > right,
            TokenType.LESS_EQUAL: lambda: left <= right,
            TokenType.GREATER_EQUAL: lambda: left >= right,
        }
        func = ops.get(op)
        if func:
            return func()
        raise RuntimeError(f"Unknown comparison operator: {op}")

    def _evaluate_unary(self, expr: Unary) -> Any:
        right = self.evaluate(expr.right)
        if expr.operator.type == TokenType.MINUS:
            return -right
        elif expr.operator.type == TokenType.NOT:
            return not right
        elif expr.operator.type == TokenType.BIT_NOT:
            return ~right
        return right

    def _evaluate_call(self, expr: Call) -> Any:
        callee = self.evaluate(expr.callee)
        arguments = [self.evaluate(arg) for arg in expr.arguments]

        if isinstance(callee, (GLangCallable, NativeFunction, BoundMethod)):
            if callee.arity != -1 and len(arguments) != callee.arity:
                raise RuntimeError(f"Expected {callee.arity} arguments but got {len(arguments)}")
            return callee.call(self, arguments)
        if callable(callee):
            return callee(*arguments)
        raise RuntimeError(f"Can't call {callee}")

    def _evaluate_getattr(self, expr: GetAttr) -> Any:
        obj = self.evaluate(expr.obj)
        if isinstance(obj, GLangInstance):
            return obj.get(expr.name)
        if isinstance(obj, dict):
            return obj.get(expr.name)
        if hasattr(obj, expr.name):
            return getattr(obj, expr.name)
        raise RuntimeError(f"Undefined property '{expr.name}' on {type(obj).__name__}")

    def _evaluate_index(self, expr: Index) -> Any:
        obj = self.evaluate(expr.obj)
        index = self.evaluate(expr.index)
        if isinstance(obj, list):
            return obj[int(index)]
        if isinstance(obj, dict):
            return obj[index]
        if isinstance(obj, str):
            return obj[int(index)]
        raise RuntimeError(f"Can't index {type(obj).__name__}")

    def _evaluate_ternary(self, expr: Ternary) -> Any:
        condition = self.evaluate(expr.condition)
        if condition:
            return self.evaluate(expr.then_branch)
        return self.evaluate(expr.else_branch)

    def _evaluate_lambda(self, expr) -> GLangCallable:
        params = []
        if hasattr(expr, 'params'):
            params = expr.params
        decl = FunctionDecl("<lambda>", params, None,
                           Block([ReturnStmt(eval('expr'))] if hasattr(expr, 'body') and not isinstance(getattr(expr, 'body', None), list) else Block(expr.body if hasattr(expr, 'body') else [])))
        # Simplify - for now just return native wrapper
        return NativeFunction("<lambda>", len(params), lambda *a: None)

    def _evaluate_is(self, expr: IsCheck) -> bool:
        value = self.evaluate(expr.expr)
        return type(value).__name__ == expr.type_name

    def _evaluate_cast(self, expr: Cast) -> Any:
        value = self.evaluate(expr.expr)
        if expr.type_name == "int":
            return int(value) if value is not None else 0
        if expr.type_name == "float" or expr.type_name == "double":
            return float(value) if value is not None else 0.0
        if expr.type_name == "string":
            return str(value) if value is not None else ""
        if expr.type_name == "bool":
            return bool(value) if value is not None else False
        return value

    def _execute_var_decl(self, stmt: VarDecl):
        value = None
        if stmt.initializer:
            value = self.evaluate(stmt.initializer)
        self.environment.define(stmt.name, value, stmt.is_const)

    def _execute_function_decl(self, stmt: FunctionDecl):
        func = GLangCallable(stmt, self.environment)
        self.environment.define(stmt.name, func, True)

    def _execute_class_decl(self, stmt: ClassDecl):
        parent_class = None
        if stmt.parent:
            parent = self.environment.get(stmt.parent)
            if not isinstance(parent, GLangClass):
                raise RuntimeError(f"'{stmt.parent}' is not a class")
            parent_class = parent

        methods = {}
        for method in stmt.methods:
            func = GLangCallable(method, self.environment, method.name == "init")
            methods[method.name] = func

        klass = GLangClass(stmt.name, parent_class, methods)
        self.environment.define(stmt.name, klass, True)

    def _execute_if(self, stmt: IfStmt):
        if self.evaluate(stmt.condition):
            self.execute(stmt.then_branch)
        elif stmt.else_branch:
            self.execute(stmt.else_branch)

    def _execute_while(self, stmt: WhileStmt):
        try:
            while self.evaluate(stmt.condition):
                try:
                    self.execute(stmt.body)
                except ContinueSignal:
                    continue
        except BreakSignal:
            pass

    def _execute_do_while(self, stmt: DoWhileStmt):
        try:
            while True:
                try:
                    self.execute(stmt.body)
                except ContinueSignal:
                    continue
                if not self.evaluate(stmt.condition):
                    break
        except BreakSignal:
            pass

    def _execute_for(self, stmt: ForStmt):
        env = Environment(self.environment)
        previous = self.environment
        self.environment = env
        try:
            if stmt.initializer:
                self.execute(stmt.initializer)
            try:
                while True:
                    if stmt.condition and not self.evaluate(stmt.condition):
                        break
                    try:
                        self.execute(stmt.body)
                    except ContinueSignal:
                        pass
                    if stmt.increment:
                        self.evaluate(stmt.increment)
            except BreakSignal:
                pass
        finally:
            self.environment = previous

    def _execute_foreach(self, stmt: ForEachStmt):
        iterable = self.evaluate(stmt.iterable)
        if isinstance(iterable, list):
            self._foreach_list(stmt, iterable)
        elif isinstance(iterable, dict):
            self._foreach_dict(stmt, iterable)
        else:
            try:
                it = iter(iterable)
                self._foreach_iter(stmt, it)
            except TypeError:
                raise RuntimeError(f"Cannot iterate over {type(iterable).__name__}")

    def _foreach_list(self, stmt: ForEachStmt, items: list):
        env = Environment(self.environment)
        previous = self.environment
        self.environment = env
        try:
            for i, item in enumerate(items):
                if stmt.index_var:
                    env.define(stmt.index_var, i, False)
                env.define(stmt.variable, item, False)
                try:
                    self.execute(stmt.body)
                except ContinueSignal:
                    continue
                except BreakSignal:
                    break
        finally:
            self.environment = previous

    def _foreach_dict(self, stmt: ForEachStmt, items: dict):
        env = Environment(self.environment)
        previous = self.environment
        self.environment = env
        try:
            for i, (key, val) in enumerate(items.items()):
                if stmt.index_var:
                    env.define(stmt.index_var, i, False)
                env.define(stmt.variable, (key, val), False)
                try:
                    self.execute(stmt.body)
                except ContinueSignal:
                    continue
                except BreakSignal:
                    break
        finally:
            self.environment = previous

    def _foreach_iter(self, stmt: ForEachStmt, it):
        env = Environment(self.environment)
        previous = self.environment
        self.environment = env
        try:
            i = 0
            for item in it:
                if stmt.index_var:
                    env.define(stmt.index_var, i, False)
                env.define(stmt.variable, item, False)
                try:
                    self.execute(stmt.body)
                except ContinueSignal:
                    continue
                except BreakSignal:
                    break
                i += 1
        finally:
            self.environment = previous

    def _execute_return(self, stmt: ReturnStmt):
        value = None
        if stmt.value:
            value = self.evaluate(stmt.value)
        raise ReturnSignal(value)

    def _execute_switch(self, stmt: SwitchStmt):
        value = self.evaluate(stmt.value)
        matched = False
        for case_val, case_stmts in stmt.cases:
            if case_val is None or (isinstance(case_val, Literal) and case_val.value == value):
                matched = True
                for s in case_stmts:
                    self.execute(s)
            if matched:
                break

    def _execute_try(self, stmt: TryStmt):
        try:
            self.execute_block(stmt.try_block.statements, Environment(self.environment))
        except ReturnSignal:
            raise
        except BreakSignal:
            raise
        except ContinueSignal:
            raise
        except Exception as e:
            if stmt.catch_block:
                env = Environment(self.environment)
                if stmt.catch_var:
                    env.define(stmt.catch_var, str(e), False)
                self.execute_block(stmt.catch_block.statements, env)
        finally:
            if stmt.finally_block:
                self.execute_block(stmt.finally_block.statements, Environment(self.environment))

    def _execute_throw(self, stmt: ThrowStmt):
        value = self.evaluate(stmt.expression)
        raise RuntimeError(str(value))


class NativeRange:
    """Lazy range wrapper."""

    def __init__(self, args: tuple):
        self.args = args

    def __iter__(self):
        return iter(range(*[int(a) for a in self.args]))
