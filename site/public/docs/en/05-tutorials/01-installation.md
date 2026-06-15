# Installing MLang

## Requirements
- Python 3.10+
- Minecraft 1.21.8 (Fabric)
- Fabric Loader 0.16.0+

## Mod installation

1. Download `mlang-mod-1.0.0.jar` from the build
2. Drop it into the Minecraft `mods/` folder
3. Configure port/token in `config/mlang.json`

## Python package installation

```bash
cd mlang
pip install -e .
```

## Running

1. Start Minecraft with the mod
2. In Python:
```python
import asyncio
from mlang.bridge import BridgeClient

async def main():
    bridge = BridgeClient(port=27678, token="mlang-secret-key")
    await bridge.connect()
    health = await bridge.player_get_health()
    print(f"HP: {health}")
    await bridge.disconnect()

asyncio.run(main())
```

Or via CLI:
```bash
python -m mlang script.glang
python -m mlang --repl  # interactive mode
```
