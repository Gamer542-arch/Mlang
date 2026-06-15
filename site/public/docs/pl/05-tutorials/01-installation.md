# Instalacja MLang

## Wymagania
- Python 3.10+
- Minecraft 1.21.8 (Fabric)
- Fabric Loader 0.16.0+

## Instalacja moda

1. Pobierz `mlang-mod-1.0.0.jar` z buildu
2. Wrzuć do `mods/` folderu Minecrafta
3. Skonfiguruj port/token w `config/mlang.json`

## Instalacja Python package

```bash
cd mlang
pip install -e .
```

## Uruchomienie

1. Odpal Minecraft z modem
2. W Pythonie:
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

Lub przez CLI:
```bash
python -m mlang script.glang
python -m mlang --repl  # tryb interaktywny
```
