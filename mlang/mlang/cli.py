"""CLI entry point for MLang."""

import argparse
import asyncio
import sys

from .lang.lexer import Lexer
from .lang.parser import Parser
from .lang.interpreter import Interpreter
from .repl import REPL


def run_file(filepath: str):
    """Run a .GLang file."""
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    lexer = Lexer(source, filepath)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.interpret(ast)


def run_repl():
    """Start interactive REPL."""
    repl = REPL()
    repl.run()


def run_source(source: str, filename: str = "<stdin>"):
    """Run GLanguage source code."""
    lexer = Lexer(source, filename)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    return interpreter.interpret(ast)


def tokenize_file(filepath: str):
    """Tokenize a file (debug)."""
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    lexer = Lexer(source, filepath)
    tokens = lexer.tokenize()
    for tok in tokens:
        print(tok)


def parse_file(filepath: str):
    """Parse a file and print AST (debug)."""
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    lexer = Lexer(source, filepath)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    for stmt in ast:
        print(stmt)


def main():
    parser = argparse.ArgumentParser(
        description="MLang - Minecraft Scripting Language",
        usage="mlang [options] [file.glang]"
    )
    parser.add_argument("file", nargs="?", help=".GLang file to execute")
    parser.add_argument("--repl", "-i", action="store_true", help="Start REPL after execution")
    parser.add_argument("--tokens", action="store_true", help="Tokenize file (debug)")
    parser.add_argument("--ast", action="store_true", help="Parse and show AST (debug)")
    parser.add_argument("--eval", "-e", help="Evaluate inline code")

    args = parser.parse_args()

    if args.file:
        if args.tokens:
            tokenize_file(args.file)
        elif args.ast:
            parse_file(args.file)
        else:
            run_file(args.file)
            if args.repl:
                run_repl()
    elif args.eval:
        run_source(args.eval)
    else:
        run_repl()


if __name__ == "__main__":
    main()
