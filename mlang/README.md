# MLang — Minecraft Scripting Language

Custom programming language for controlling Minecraft. Write `.GLang` scripts, run them with a Python interpreter connected via WebSocket to the MLang Fabric mod bridge.

## Install

```bash
pip install mlang
```

Or from source:
```bash
git clone https://github.com/Gamer542-arch/MLang
cd mlang/mlang
pip install -e .
```

## Quick Start

### 1. Run a script
```bash
python -m mlang script.glang
```

### 2. Interactive REPL
```bash
python -m mlang
```

### 3. Connect to Minecraft
```python
import asyncio
from mlang.bridge import BridgeClient

async def main():
    bridge = BridgeClient()
    await bridge.connect()
    await bridge.player_teleport(0, 64, 0)
    await bridge.chat_send("&aHello from Python!")
    await bridge.disconnect()

asyncio.run(main())
```

## Features

- **GLanguage** — C#-like scripting language with full interpreter (lexer, parser, AST, tree-walk)
- **MC Bridge** — WebSocket JSON-RPC client for the MLang Fabric mod
- **GUI System** — 17 widget types, 7 themes (dark, neon, glass, future...), animations
- **CLI + REPL** — Run scripts or interactive development

## Requirements

- Python 3.10+
- Minecraft 1.21.8 with Fabric Loader and MLang Bridge mod
