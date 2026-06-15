from mlang.lang.lexer import Lexer
from mlang.lang.tokens import TokenType

def test_lexer_basic():
    source = "var x = 10\nprint('hello')"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.VAR
    assert tokens[1].type == TokenType.IDENTIFIER
    assert tokens[1].value == "x"
    assert tokens[2].type == TokenType.ASSIGN
    assert tokens[3].type == TokenType.NUMBER_INT
    assert tokens[3].value == 10
    print("test_lexer_basic PASSED")

def test_lexer_strings():
    source = 'var s = "hello"'
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    assert tokens[3].type == TokenType.STRING
    assert tokens[3].value == "hello"
    print("test_lexer_strings PASSED")

def test_lexer_comments():
    source = "var x = 1 // this is a comment\nvar y = 2"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    # tokens: VAR, IDENTIFIER(x), ASSIGN, NUMBER_INT(1), NEWLINE, VAR, IDENTIFIER(y), ASSIGN, NUMBER_INT(2), EOF
    var_tokens = [t for t in tokens if t.type == TokenType.VAR]
    assert len(var_tokens) == 2
    print("test_lexer_comments PASSED")

if __name__ == "__main__":
    test_lexer_basic()
    test_lexer_strings()
    test_lexer_comments()
    print("All lexer tests passed!")
