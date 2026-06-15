"""Interactive REPL for MLang."""

import sys
from typing import Optional

from .lang.lexer import Lexer
from .lang.parser import Parser
from .lang.interpreter import Interpreter


class REPL:
    """Read-Eval-Print Loop for GLanguage."""

    def __init__(self):
        self.interpreter = Interpreter()
        self.history: list[str] = []

    def run(self):
        print("MLang v1.0.0 - Interactive REPL")
        print("Type 'exit' or Ctrl+C to quit")
        print("Type 'help' for commands")
        print()

        while True:
            try:
                line = input("GL> ")
                if not line.strip():
                    continue

                if line.strip() == "exit":
                    break
                if line.strip() == "help":
                    self._show_help()
                    continue
                if line.strip().startswith("!"):
                    self._handle_command(line.strip()[1:])
                    continue

                self.history.append(line)
                self._execute_line(line)

            except KeyboardInterrupt:
                print()
                break
            except EOFError:
                print()
                break
            except Exception as e:
                print(f"Error: {e}")

    def _execute_line(self, source: str):
        try:
            lexer = Lexer(source, "<repl>")
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            result = self.interpreter.interpret(ast)
            if result is not None:
                print(f"= {result}")
        except Exception as e:
            print(f"Error: {e}")

    def _show_help(self):
        print("MLang REPL Commands:")
        print("  exit          Exit REPL")
        print("  help          Show this help")
        print("  !clear        Clear screen")
        print("  !history      Show command history")
        print("  !vars         Show global variables")
        print("  !reset        Reset interpreter")
        print()
        print("Language examples:")
        print("  var x = 10")
        print('  print("Hello World!")')
        print("  if (x > 5) { print('yes') }")
        print("  for (int i = 0; i < 5; i++) { print(i) }")

    def _handle_command(self, cmd: str):
        parts = cmd.strip().split()
        if not parts:
            return
        command = parts[0]

        if command == "clear":
            print("\033[2J\033[H", end="")
        elif command == "history":
            for i, line in enumerate(self.history):
                print(f"{i:4}: {line}")
        elif command == "vars":
            for name, val in self.interpreter.globals.variables.items():
                print(f"  {name} = {val!r}")
        elif command == "reset":
            self.interpreter = Interpreter()
            print("Interpreter reset")
        else:
            print(f"Unknown command: !{command}")
