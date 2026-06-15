# Tests for MLang parser

from mlang.lang.lexer import Lexer
from mlang.lang.parser import Parser

def test_parser_variable():
    source = "var x = 10"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    assert len(ast) == 1
    assert ast[0].name == "x"
    print("test_parser_variable PASSED")

def test_parser_if():
    source = "if (x > 5) { print('yes') }"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    assert len(ast) == 1
    print("test_parser_if PASSED")

def test_parser_function():
    source = "func add(a, b) { return a + b }"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    assert len(ast) == 1
    assert ast[0].name == "add"
    print("test_parser_function PASSED")

def test_parser_class():
    source = "class PlayerData { var name var health }"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    assert len(ast) == 1
    assert ast[0].name == "PlayerData"
    print("test_parser_class PASSED")

if __name__ == "__main__":
    test_parser_variable()
    test_parser_if()
    test_parser_function()
    test_parser_class()
    print("All parser tests passed!")
