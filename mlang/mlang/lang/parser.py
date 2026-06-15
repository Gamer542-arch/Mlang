from typing import Optional

from .tokens import Token, TokenType
from .ast_nodes import *
from .lexer import Lexer


class ParserError(Exception):
    def __init__(self, message: str, token: Token):
        self.token = token
        super().__init__(f"ParserError at {token.line}:{token.column}: {message}")


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    def error(self, message: str):
        raise ParserError(message, self.current)

    @property
    def current(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def peek(self, offset: int = 0) -> Token:
        idx = self.pos + offset
        if idx >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[idx]

    def check(self, *types: TokenType) -> bool:
        return self.current.type in types

    def match(self, *types: TokenType) -> Optional[Token]:
        if self.current.type in types:
            token = self.current
            self.pos += 1
            return token
        return None

    def consume(self, type_: TokenType, message: str) -> Token:
        if self.current.type == type_:
            token = self.current
            self.pos += 1
            return token
        self.error(message)

    def parse(self) -> list[Stmt]:
        statements = []
        while not self.check(TokenType.EOF):
            stmt = self.declaration()
            if stmt:
                statements.append(stmt)
        return statements

    def declaration(self) -> Optional[Stmt]:
        if self.check(TokenType.DIRECTIVE):
            return self.directive()
        if self.check(TokenType.USE):
            return self.use_stmt()
        if self.check(TokenType.IMPORT):
            return self.import_stmt()
        if self.check(TokenType.ANNOTATION):
            return self.annotation()
        if self.check(TokenType.ABSTRACT):
            return self.class_decl()
        if self.check(TokenType.CLASS):
            return self.class_decl()
        if self.check(TokenType.INTERFACE):
            return self.interface_decl()
        if self.check(TokenType.PUBLIC, TokenType.PRIVATE, TokenType.PROTECTED):
            return self.class_member()
        if self.check(TokenType.FUNC):
            return self.function_decl()
        return self.statement()

    def directive(self) -> Directive:
        token = self.consume(TokenType.DIRECTIVE, "Expected directive")
        parts = token.value.split(None, 1)
        name = parts[0]
        value = parts[1] if len(parts) > 1 else True
        if value and value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif isinstance(value, str) and value.isdigit():
            value = int(value)
        return Directive(name, value, token)

    def use_stmt(self) -> UseStmt:
        token = self.consume(TokenType.USE, "Expected 'use'")
        module = self.consume(TokenType.IDENTIFIER, "Expected module name")
        while self.match(TokenType.DOT):
            module.value += "." + self.consume(TokenType.IDENTIFIER, "Expected identifier").value
        return UseStmt(module.value, token)

    def import_stmt(self) -> ImportStmt:
        token = self.consume(TokenType.IMPORT, "Expected 'import'")
        path = self.consume(TokenType.STRING, "Expected file path").value
        return ImportStmt(path, token)

    def annotation(self) -> Annotation:
        token = self.consume(TokenType.ANNOTATION, "Expected @")
        name = self.consume(TokenType.IDENTIFIER, "Expected annotation name").value
        args = {}
        if self.match(TokenType.LPAREN):
            if not self.check(TokenType.RPAREN):
                key = self.consume(TokenType.IDENTIFIER, "Expected parameter name").value
                self.consume(TokenType.COLON, "Expected ':'")
                value = self.expression()
                args[key] = value
            self.consume(TokenType.RPAREN, "Expected ')'")
        return Annotation(name, args, token)

    def class_member(self) -> Stmt:
        if self.check(TokenType.PUBLIC, TokenType.PRIVATE, TokenType.PROTECTED):
            return None  # handled within class_decl
        return self.statement()

    # --- Statements ---
    def statement(self) -> Stmt:
        if self.check(TokenType.LBRACE):
            return self.block()
        if self.check(TokenType.IF):
            return self.if_stmt()
        if self.check(TokenType.WHILE):
            return self.while_stmt()
        if self.check(TokenType.DO):
            return self.do_while_stmt()
        if self.check(TokenType.FOR):
            return self.for_stmt()
        if self.check(TokenType.FOREACH):
            return self.foreach_stmt()
        if self.check(TokenType.BREAK):
            return self.break_stmt()
        if self.check(TokenType.CONTINUE):
            return self.continue_stmt()
        if self.check(TokenType.RETURN):
            return self.return_stmt()
        if self.check(TokenType.SWITCH):
            return self.switch_stmt()
        if self.check(TokenType.MATCH):
            return self.match_stmt()
        if self.check(TokenType.TRY):
            return self.try_stmt()
        if self.check(TokenType.THROW):
            return self.throw_stmt()
        if self.check(TokenType.VAR, TokenType.CONST):
            return self.var_decl()
        if self.check(TokenType.TYPE_INT, TokenType.TYPE_FLOAT, TokenType.TYPE_DOUBLE,
                      TokenType.TYPE_STRING, TokenType.TYPE_BOOL, TokenType.TYPE_CHAR,
                      TokenType.TYPE_BYTE, TokenType.TYPE_LONG, TokenType.TYPE_VOID,
                      TokenType.TYPE_OBJECT, TokenType.IDENTIFIER):
            # Could be variable declaration or expression
            if self.peek(1).type == TokenType.IDENTIFIER and self.peek(2).type in (
                TokenType.ASSIGN, TokenType.SEMICOLON):
                return self.var_decl()
        return self.expression_stmt()

    def block(self) -> Block:
        token = self.consume(TokenType.LBRACE, "Expected '{'")
        statements = []
        while not self.check(TokenType.RBRACE) and not self.check(TokenType.EOF):
            stmt = self.declaration()
            if stmt:
                statements.append(stmt)
        self.consume(TokenType.RBRACE, "Expected '}'")
        return Block(statements)

    def if_stmt(self) -> IfStmt:
        self.consume(TokenType.IF, "Expected 'if'")
        self.consume(TokenType.LPAREN, "Expected '('")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')'")
        then_branch = self.statement()
        else_branch = None
        if self.match(TokenType.ELSE):
            else_branch = self.statement()
        return IfStmt(condition, then_branch, else_branch)

    def while_stmt(self) -> WhileStmt:
        self.consume(TokenType.WHILE, "Expected 'while'")
        self.consume(TokenType.LPAREN, "Expected '('")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')'")
        body = self.statement()
        return WhileStmt(condition, body)

    def do_while_stmt(self) -> DoWhileStmt:
        self.consume(TokenType.DO, "Expected 'do'")
        body = self.statement()
        self.consume(TokenType.WHILE, "Expected 'while'")
        self.consume(TokenType.LPAREN, "Expected '('")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')'")
        return DoWhileStmt(body, condition)

    def for_stmt(self) -> ForStmt:
        self.consume(TokenType.FOR, "Expected 'for'")
        self.consume(TokenType.LPAREN, "Expected '('")
        if self.check(TokenType.SEMICOLON):
            initializer = None
        else:
            initializer = self.var_decl() if self.check(TokenType.VAR, TokenType.CONST, TokenType.TYPE_INT) else self.expression_stmt()
        self.consume(TokenType.SEMICOLON, "Expected ';'")
        condition = None if self.check(TokenType.SEMICOLON) else self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';'")
        increment = None if self.check(TokenType.RPAREN) else self.expression()
        self.consume(TokenType.RPAREN, "Expected ')'")
        body = self.statement()
        return ForStmt(initializer, condition, increment, body)

    def foreach_stmt(self) -> ForEachStmt:
        self.consume(TokenType.FOREACH, "Expected 'foreach'")
        self.consume(TokenType.LPAREN, "Expected '('")
        index_var = None
        if self.check(TokenType.TYPE_INT):
            self.consume(TokenType.TYPE_INT, "")
        if self.peek(1).type == TokenType.COMMA:
            index_var = self.consume(TokenType.IDENTIFIER, "Expected index variable").value
            self.consume(TokenType.COMMA, "Expected ','")
        variable = self.consume(TokenType.IDENTIFIER, "Expected variable name").value
        self.consume(TokenType.IN, "Expected 'in'")
        iterable = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')'")
        body = self.statement()
        return ForEachStmt(variable, index_var, iterable, body)

    def break_stmt(self) -> BreakStmt:
        self.consume(TokenType.BREAK, "Expected 'break'")
        return BreakStmt()

    def continue_stmt(self) -> ContinueStmt:
        self.consume(TokenType.CONTINUE, "Expected 'continue'")
        return ContinueStmt()

    def return_stmt(self) -> ReturnStmt:
        token = self.consume(TokenType.RETURN, "Expected 'return'")
        value = None if self.check(TokenType.SEMICOLON) else self.expression()
        return ReturnStmt(value)

    def switch_stmt(self) -> SwitchStmt:
        self.consume(TokenType.SWITCH, "Expected 'switch'")
        self.consume(TokenType.LPAREN, "Expected '('")
        value = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')'")
        self.consume(TokenType.LBRACE, "Expected '{'")
        cases = []
        current_case = None
        while not self.check(TokenType.RBRACE) and not self.check(TokenType.EOF):
            if self.match(TokenType.CASE):
                case_value = self.expression()
                self.consume(TokenType.COLON, "Expected ':'")
                current_case = (case_value, [])
                cases.append(current_case)
            elif self.match(TokenType.DEFAULT):
                self.consume(TokenType.COLON, "Expected ':'")
                current_case = (None, [])
                cases.append(current_case)
            else:
                if current_case:
                    current_case[1].append(self.statement())
                else:
                    self.error("Unexpected statement in switch")
        self.consume(TokenType.RBRACE, "Expected '}'")
        return SwitchStmt(value, cases)

    def match_stmt(self) -> MatchStmt:
        self.consume(TokenType.MATCH, "Expected 'match'")
        self.consume(TokenType.LPAREN, "Expected '('")
        value = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')'")
        self.consume(TokenType.LBRACE, "Expected '{'")
        arms = []
        while not self.check(TokenType.RBRACE) and not self.check(TokenType.EOF):
            if self.match(TokenType.WHEN):
                # when > 15 => Chat.Send("...")
                op = self.expression()
                self.consume(TokenType.ARROW, "Expected '=>'")
                body = self.expression()
                arms.append((None, "when", body))  # simplified
            elif self.match(TokenType.ELSE):
                self.consume(TokenType.ARROW, "Expected '=>'")
                body = self.expression()
                arms.append((None, "else", body))
            else:
                case_val = self.expression()
                self.consume(TokenType.ARROW, "Expected '=>'")
                body = self.expression()
                arms.append((case_val, "", body))
        self.consume(TokenType.RBRACE, "Expected '}'")
        return MatchStmt(value, arms)

    def try_stmt(self) -> TryStmt:
        self.consume(TokenType.TRY, "Expected 'try'")
        try_block = self.block()
        catch_var = None
        catch_type = None
        catch_block = None
        if self.match(TokenType.CATCH):
            self.consume(TokenType.LPAREN, "Expected '('")
            if self.check(TokenType.IDENTIFIER):
                catch_type = self.consume(TokenType.IDENTIFIER, "").value
            catch_var = self.consume(TokenType.IDENTIFIER, "Expected catch variable").value
            self.consume(TokenType.RPAREN, "Expected ')'")
            catch_block = self.block()
        finally_block = None
        if self.match(TokenType.FINALLY):
            finally_block = self.block()
        return TryStmt(try_block, catch_var, catch_type, catch_block, finally_block)

    def throw_stmt(self) -> ThrowStmt:
        self.consume(TokenType.THROW, "Expected 'throw'")
        value = self.expression()
        return ThrowStmt(value)

    # --- Declarations ---
    def var_decl(self) -> VarDecl:
        is_const = self.match(TokenType.CONST) is not None
        type_name = None
        if self.check(TokenType.VAR):
            self.consume(TokenType.VAR, "Expected 'var'")
        elif self.check(TokenType.TYPE_INT, TokenType.TYPE_FLOAT, TokenType.TYPE_DOUBLE,
                        TokenType.TYPE_STRING, TokenType.TYPE_BOOL, TokenType.TYPE_CHAR,
                        TokenType.TYPE_BYTE, TokenType.TYPE_LONG, TokenType.TYPE_VOID,
                        TokenType.TYPE_OBJECT):
            type_name = self.consume(self.current.type, "Expected type").value
        elif self.check(TokenType.IDENTIFIER):
            type_name = self.consume(TokenType.IDENTIFIER, "Expected type").value
        else:
            self.error("Expected variable declaration")
        name = self.consume(TokenType.IDENTIFIER, "Expected variable name").value
        initializer = None
        if self.match(TokenType.ASSIGN):
            initializer = self.expression()
        return VarDecl(name, type_name, initializer, is_const)

    def function_decl(self) -> FunctionDecl:
        token = self.consume(TokenType.FUNC, "Expected 'func'")
        if self.check(TokenType.LPAREN):
            # Anonymous function
            return self.anonymous_function(token)
        name = self.consume(TokenType.IDENTIFIER, "Expected function name").value
        self.consume(TokenType.LPAREN, "Expected '('")
        params = self.parameters()
        self.consume(TokenType.RPAREN, "Expected ')'")
        return_type = None
        if self.current.type in (TokenType.TYPE_INT, TokenType.TYPE_FLOAT, TokenType.TYPE_DOUBLE,
                                  TokenType.TYPE_STRING, TokenType.TYPE_BOOL, TokenType.TYPE_CHAR,
                                  TokenType.TYPE_BYTE, TokenType.TYPE_LONG, TokenType.TYPE_VOID,
                                  TokenType.TYPE_OBJECT, TokenType.IDENTIFIER):
            return_type = self.current.value
            self.pos += 1
        body = self.block()
        return FunctionDecl(name, params, return_type, body, token=token)

    def anonymous_function(self, token: Token) -> AnonymousFunction:
        self.consume(TokenType.LPAREN, "Expected '('")
        params = self.parameters()
        self.consume(TokenType.RPAREN, "Expected ')'")
        return_type = None
        if self.current.type in (TokenType.TYPE_INT, TokenType.TYPE_FLOAT):
            return_type = self.current.value
            self.pos += 1
        body = self.block()
        return AnonymousFunction(params, body.statements if isinstance(body, Block) else [body], return_type)

    def parameters(self) -> list[Parameter]:
        params = []
        if not self.check(TokenType.RPAREN):
            params.append(self.parameter())
            while self.match(TokenType.COMMA):
                params.append(self.parameter())
        return params

    def parameter(self) -> Parameter:
        is_variadic = self.match(TokenType.DOT) is not None
        type_name = None
        if self.current.type in (TokenType.TYPE_INT, TokenType.TYPE_FLOAT, TokenType.TYPE_DOUBLE,
                                  TokenType.TYPE_STRING, TokenType.TYPE_BOOL, TokenType.TYPE_CHAR,
                                  TokenType.TYPE_BYTE, TokenType.TYPE_LONG, TokenType.TYPE_VOID,
                                  TokenType.TYPE_OBJECT):
            type_name = self.current.value
            self.pos += 1
        elif self.current.type == TokenType.IDENTIFIER and self.peek(1).type == TokenType.IDENTIFIER:
            type_name = self.current.value
            self.pos += 1
        name = self.consume(TokenType.IDENTIFIER, "Expected parameter name").value
        default_value = None
        if self.match(TokenType.ASSIGN):
            default_value = self.expression()
        return Parameter(name, type_name, default_value, is_variadic)

    def class_decl(self) -> ClassDecl:
        is_abstract = self.match(TokenType.ABSTRACT) is not None
        self.consume(TokenType.CLASS, "Expected 'class'")
        token = self.current
        name = self.consume(TokenType.IDENTIFIER, "Expected class name").value
        parent = None
        interfaces = []
        if self.match(TokenType.COLON) or self.match(TokenType.EXTENDS):
            parent = self.consume(TokenType.IDENTIFIER, "Expected parent class").value
            while self.match(TokenType.COMMA):
                interfaces.append(self.consume(TokenType.IDENTIFIER, "Expected interface").value)
        elif self.match(TokenType.IMPLEMENTS):
            interfaces.append(self.consume(TokenType.IDENTIFIER, "Expected interface").value)
            while self.match(TokenType.COMMA):
                interfaces.append(self.consume(TokenType.IDENTIFIER, "Expected interface").value)

        self.consume(TokenType.LBRACE, "Expected '{'")
        fields = []
        methods = []
        while not self.check(TokenType.RBRACE) and not self.check(TokenType.EOF):
            member = self.class_member_decl()
            if isinstance(member, FieldDecl):
                fields.append(member)
            elif isinstance(member, FunctionDecl):
                methods.append(member)
        self.consume(TokenType.RBRACE, "Expected '}'")
        return ClassDecl(name, parent, interfaces, fields, methods, is_abstract, token=token)

    def class_member_decl(self) -> Stmt:
        is_public = False
        is_private = False
        is_protected = False
        is_static = False
        is_abstract_member = False
        is_override = False
        is_virtual = False

        if self.match(TokenType.PUBLIC):
            is_public = True
        elif self.match(TokenType.PRIVATE):
            is_private = True
        elif self.match(TokenType.PROTECTED):
            is_protected = True

        if self.match(TokenType.STATIC):
            is_static = True
        if self.match(TokenType.ABSTRACT):
            is_abstract_member = True
        if self.match(TokenType.OVERRIDE):
            is_override = True
        if self.match(TokenType.VIRTUAL):
            is_virtual = True

        if self.check(TokenType.FUNC):
            decl = self.function_decl()
            decl.is_public = is_public
            decl.is_static = is_static
            decl.is_abstract = is_abstract_member
            decl.is_override = is_override
            decl.is_virtual = is_virtual
            return decl

        if self.check(TokenType.VAR, TokenType.CONST, TokenType.TYPE_INT, TokenType.TYPE_STRING,
                       TokenType.TYPE_FLOAT, TokenType.TYPE_DOUBLE, TokenType.TYPE_BOOL):
            decl = self.var_decl()
            decl.is_public = is_public
            decl.is_private = is_private
            decl.is_protected = is_protected
            decl.is_static = is_static
            decl.is_const = decl.is_const or self.match(TokenType.CONST) is not None
            return decl

        # Getter/setter property
        if self.check(TokenType.IDENTIFIER) and self.peek(1).type == TokenType.IDENTIFIER:
            type_name = self.consume(TokenType.IDENTIFIENTIFIER, "").value
            name = self.consume(TokenType.IDENTIFIER, "Expected property name").value
            self.consume(TokenType.LBRACE, "Expected '{'")
            getter = None
            setter = None
            if self.match(TokenType.GET):
                getter = self.block()
            if self.match(TokenType.SET):
                setter = self.block()
            self.consume(TokenType.RBRACE, "Expected '}'")
            return PropertyDecl(name, type_name, getter, setter)

        self.error("Expected class member")

    def interface_decl(self) -> InterfaceDecl:
        self.consume(TokenType.INTERFACE, "Expected 'interface'")
        name = self.consume(TokenType.IDENTIFIER, "Expected interface name").value
        self.consume(TokenType.LBRACE, "Expected '{'")
        methods = []
        while not self.check(TokenType.RBRACE) and not self.check(TokenType.EOF):
            self.match(TokenType.PUBLIC)
            if self.check(TokenType.FUNC):
                methods.append(self.function_decl())
        self.consume(TokenType.RBRACE, "Expected '}'")
        return InterfaceDecl(name, methods)

    # --- Expressions ---
    def expression_stmt(self) -> ExpressionStmt:
        expr = self.expression()
        return ExpressionStmt(expr)

    def expression(self) -> Expr:
        return self.assignment()

    def assignment(self) -> Expr:
        expr = self.ternary()
        if self.check(TokenType.ASSIGN, TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
                       TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN, TokenType.PERCENT_ASSIGN):
            op = self.current
            self.pos += 1
            value = self.assignment()
            if isinstance(expr, Variable):
                return Binary(expr, op, value)
            elif isinstance(expr, (GetAttr, Index)):
                return Binary(expr, op, value)
            self.error("Invalid assignment target")
        return expr

    def ternary(self) -> Expr:
        expr = self.null_coalescing()
        if self.match(TokenType.QUESTION):
            then_branch = self.expression()
            self.consume(TokenType.COLON, "Expected ':' in ternary")
            else_branch = self.expression()
            return Ternary(expr, then_branch, else_branch)
        return expr

    def null_coalescing(self) -> Expr:
        expr = self.logical_or()
        if self.match(TokenType.QUESTION_QUESTION):
            right = self.null_coalescing()
            return NullCoalescing(expr, right)
        return expr

    def logical_or(self) -> Expr:
        expr = self.logical_and()
        while self.match(TokenType.OR):
            op = self.current
            self.pos -= 1
            self.pos += 1
            right = self.logical_and()
            expr = Binary(expr, Token(TokenType.OR, "||", 0, 0), right)
        return expr

    def logical_and(self) -> Expr:
        expr = self.bitwise_or()
        while self.match(TokenType.AND):
            right = self.bitwise_or()
            expr = Binary(expr, Token(TokenType.AND, "&&", 0, 0), right)
        return expr

    def bitwise_or(self) -> Expr:
        expr = self.bitwise_xor()
        while self.match(TokenType.BIT_OR):
            right = self.bitwise_xor()
            expr = Binary(expr, Token(TokenType.BIT_OR, "|", 0, 0), right)
        return expr

    def bitwise_xor(self) -> Expr:
        expr = self.bitwise_and()
        while self.match(TokenType.BIT_XOR):
            right = self.bitwise_and()
            expr = Binary(expr, Token(TokenType.BIT_XOR, "^", 0, 0), right)
        return expr

    def bitwise_and(self) -> Expr:
        expr = self.equality()
        while self.match(TokenType.BIT_AND):
            right = self.equality()
            expr = Binary(expr, Token(TokenType.BIT_AND, "&", 0, 0), right)
        return expr

    def equality(self) -> Expr:
        expr = self.comparison()
        op_token = self.match(TokenType.EQUALS, TokenType.NOT_EQUALS)
        while op_token:
            right = self.comparison()
            expr = Binary(expr, op_token, right)
            op_token = self.match(TokenType.EQUALS, TokenType.NOT_EQUALS)
        return expr

    def comparison(self) -> Expr:
        expr = self.shift()
        op_token = self.match(TokenType.LESS, TokenType.GREATER, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL)
        while op_token:
            right = self.shift()
            expr = Binary(expr, op_token, right)
            op_token = self.match(TokenType.LESS, TokenType.GREATER, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL)
        return expr

    def shift(self) -> Expr:
        expr = self.term()
        op_token = self.match(TokenType.SHIFT_LEFT, TokenType.SHIFT_RIGHT)
        while op_token:
            right = self.term()
            expr = Binary(expr, op_token, right)
            op_token = self.match(TokenType.SHIFT_LEFT, TokenType.SHIFT_RIGHT)
        return expr

    def term(self) -> Expr:
        expr = self.factor()
        op_token = self.match(TokenType.PLUS, TokenType.MINUS)
        while op_token:
            right = self.factor()
            expr = Binary(expr, op_token, right)
            op_token = self.match(TokenType.PLUS, TokenType.MINUS)
        return expr

    def factor(self) -> Expr:
        expr = self.unary()
        op_token = self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT,
                              TokenType.STAR_STAR, TokenType.SLASH_SLASH)
        while op_token:
            right = self.unary()
            expr = Binary(expr, op_token, right)
            op_token = self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT,
                                  TokenType.STAR_STAR, TokenType.SLASH_SLASH)
        return expr

    def unary(self) -> Expr:
        op_token = self.match(TokenType.MINUS, TokenType.NOT, TokenType.BIT_NOT, TokenType.PLUS)
        if op_token:
            right = self.unary()
            return Unary(op_token, right)
        return self.cast()

    def cast(self) -> Expr:
        if self.check(TokenType.LPAREN) and self.peek(1).type in (
            TokenType.TYPE_INT, TokenType.TYPE_FLOAT, TokenType.TYPE_DOUBLE,
            TokenType.TYPE_STRING, TokenType.TYPE_BOOL, TokenType.TYPE_CHAR,
            TokenType.TYPE_BYTE, TokenType.TYPE_LONG, TokenType.IDENTIFIER):
            if self.peek(2).type == TokenType.RPAREN:
                self.pos += 1  # LPAREN
                type_name = self.current.value
                self.pos += 1
                self.pos += 1  # RPAREN
                expr = self.cast()
                return Cast(type_name, expr)
        return self.is_check()

    def is_check(self) -> Expr:
        expr = self.power()
        if self.match(TokenType.IS):
            type_name = self.consume(TokenType.IDENTIFIER, "Expected type name").value
            target = None
            if self.check(TokenType.IDENTIFIER):
                target = Variable(self.consume(TokenType.IDENTIFIER, "").value)
            return IsCheck(expr, type_name, target)
        if self.match(TokenType.AS):
            type_name = self.consume(TokenType.IDENTIFIER, "Expected type name").value
            return Cast(type_name, expr)
        return expr

    def power(self) -> Expr:
        expr = self.call()
        if self.match(TokenType.STAR_STAR):
            right = self.power()
            return Binary(expr, Token(TokenType.STAR_STAR, "**", 0, 0), right)
        return expr

    def call(self) -> Expr:
        expr = self.primary()
        while True:
            if self.match(TokenType.LPAREN):
                args = []
                if not self.check(TokenType.RPAREN):
                    args.append(self.expression())
                    while self.match(TokenType.COMMA):
                        args.append(self.expression())
                self.consume(TokenType.RPAREN, "Expected ')' after arguments")
                expr = Call(expr, args)
            elif self.match(TokenType.DOT):
                name = self.consume(TokenType.IDENTIFIER, "Expected attribute name").value
                if self.match(TokenType.LPAREN):
                    args = []
                    if not self.check(TokenType.RPAREN):
                        args.append(self.expression())
                        while self.match(TokenType.COMMA):
                            args.append(self.expression())
                    self.consume(TokenType.RPAREN, "Expected ')'")
                    expr = Call(GetAttr(expr, name), args)
                else:
                    expr = GetAttr(expr, name)
            elif self.match(TokenType.LBRACKET):
                index = self.expression()
                self.consume(TokenType.RBRACKET, "Expected ']'")
                expr = Index(expr, index)
            else:
                break
        return expr

    def primary(self) -> Expr:
        token = self.match(TokenType.NUMBER_INT, TokenType.NUMBER_FLOAT, TokenType.STRING,
                           TokenType.BOOL_TRUE, TokenType.BOOL_FALSE, TokenType.NULL)
        if token:
            return Literal(token.value, token)
        if self.match(TokenType.THIS):
            return Variable("this")
        if self.match(TokenType.BASE):
            return Variable("base")
        token = self.match(TokenType.IDENTIFIER)
        if token:
            return Variable(token.value, token)
        if self.match(TokenType.LPAREN):
            expr = self.expression()
            self.consume(TokenType.RPAREN, "Expected ')'")
            return expr
        if self.match(TokenType.LBRACKET):
            if self.check(TokenType.RBRACKET):
                self.consume(TokenType.RBRACKET, "Expected ']'")
                return ArrayLiteral([])
            first = self.expression()
            if self.match(TokenType.COLON):
                pairs = []
                second = self.expression()
                pairs.append((first, second))
                while self.match(TokenType.COMMA):
                    if self.check(TokenType.RBRACKET):
                        break
                    k = self.expression()
                    self.consume(TokenType.COLON, "Expected ':' in dict literal")
                    v = self.expression()
                    pairs.append((k, v))
                self.consume(TokenType.RBRACKET, "Expected ']'")
                return DictLiteral(pairs)
            elements = [first]
            while self.match(TokenType.COMMA):
                if self.check(TokenType.RBRACKET):
                    break
                elements.append(self.expression())
            self.consume(TokenType.RBRACKET, "Expected ']'")
            return ArrayLiteral(elements)
        token = self.match(TokenType.FUNC)
        if token:
            return self.anonymous_function(token)
        if self.match(TokenType.NEW):
            return self.new_expr()
        if self.match(TokenType.SCHEDULE):
            return self.schedule_expr()
        self.error(f"Expected expression, got {self.current}")

    def new_expr(self) -> Expr:
        name = self.consume(TokenType.IDENTIFIER, "Expected class name").value
        self.consume(TokenType.LPAREN, "Expected '('")
        args = []
        if not self.check(TokenType.RPAREN):
            args.append(self.expression())
            while self.match(TokenType.COMMA):
                args.append(self.expression())
        self.consume(TokenType.RPAREN, "Expected ')'")
        return Call(Variable(name), args)

    def schedule_expr(self) -> Expr:
        if self.match(TokenType.DOT):
            method = self.consume(TokenType.IDENTIFIER, "Expected method").value
            self.consume(TokenType.LPAREN, "Expected '('")
            args = []
            if not self.check(TokenType.RPAREN):
                args.append(self.expression())
                while self.match(TokenType.COMMA):
                    args.append(self.expression())
            self.consume(TokenType.RPAREN, "Expected ')'")
            return Call(GetAttr(Variable("Schedule"), method), args)
        self.error("Expected 'Schedule.xxx'")
