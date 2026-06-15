from typing import Any, Optional


class Environment:
    """Variable scope/environment for the interpreter."""

    def __init__(self, parent: Optional["Environment"] = None):
        self.parent = parent
        self.variables: dict[str, Any] = {}
        self.constants: set[str] = set()
        self.children: list[Environment] = []

    def define(self, name: str, value: Any, is_const: bool = False):
        self.variables[name] = value
        if is_const:
            self.constants.add(name)

    def assign(self, name: str, value: Any):
        if name in self.constants:
            raise RuntimeError(f"Cannot assign to constant '{name}'")
        if name in self.variables:
            self.variables[name] = value
            return
        if self.parent is not None:
            self.parent.assign(name, value)
            return
        raise RuntimeError(f"Undefined variable '{name}'")

    def get(self, name: str) -> Any:
        if name in self.variables:
            return self.variables[name]
        if self.parent is not None:
            return self.parent.get(name)
        raise RuntimeError(f"Undefined variable '{name}'")

    def has(self, name: str) -> bool:
        if name in self.variables:
            return True
        if self.parent is not None:
            return self.parent.has(name)
        return False

    def assign_at(self, depth: int, name: str, value: Any):
        env = self._ancestor(depth)
        if name in env.constants:
            raise RuntimeError(f"Cannot assign to constant '{name}'")
        env.variables[name] = value

    def get_at(self, depth: int, name: str) -> Any:
        return self._ancestor(depth).variables.get(name)

    def _ancestor(self, depth: int) -> "Environment":
        env = self
        for _ in range(depth):
            env = env.parent
        return env

    def __repr__(self):
        return f"Environment(vars={dict(self.variables)}, consts={self.constants})"
