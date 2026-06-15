# Tests for MLang interpreter

from mlang.lang.lexer import Lexer
from mlang.lang.parser import Parser
from mlang.lang.interpreter import Interpreter

def run(source):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interp = Interpreter()
    return interp.interpret(ast)

def test_interpreter_print():
    # Just ensure no crash
    run("print('hello')")
    print("test_interpreter_print PASSED")

def test_interpreter_variables():
    run("""
        var x = 10
        var y = 20
        var z = x + y
    """)
    print("test_interpreter_variables PASSED")

def test_interpreter_if():
    run("""
        var x = 10
        if (x > 5) {
            print('yes')
        }
    """)
    print("test_interpreter_if PASSED")

def test_interpreter_while():
    run("""
        var i = 0
        while (i < 5) {
            i = i + 1
        }
    """)
    print("test_interpreter_while PASSED")

def test_interpreter_for():
    run("""
        for (var i = 0; i < 5; i = i + 1) {
            print(i)
        }
    """)
    print("test_interpreter_for PASSED")

def test_interpreter_functions():
    run("""
        func add(a, b) {
            return a + b
        }
        var result = add(10, 20)
    """)
    print("test_interpreter_functions PASSED")

def test_interpreter_foreach():
    run("""
        var items = [1, 2, 3]
        foreach (item in items) {
            print(item)
        }
    """)
    print("test_interpreter_foreach PASSED")

def test_interpreter_lists():
    run("""
        var items = [1, 2, 3]
        var first = items[0]
        print(first)
    """)
    print("test_interpreter_lists PASSED")

def test_interpreter_dicts():
    # Dict literal syntax: var d = ["key": val]
    result = run("""
        var d = ["key1": 1, "key2": 2]
    """)
    print("test_interpreter_dicts PASSED")

if __name__ == "__main__":
    test_interpreter_print()
    test_interpreter_variables()
    test_interpreter_if()
    test_interpreter_while()
    test_interpreter_for()
    test_interpreter_functions()
    test_interpreter_foreach()
    test_interpreter_lists()
    test_interpreter_dicts()
    print("All interpreter tests passed!")
