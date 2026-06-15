# Klient Python

## Instalacja

```bash
cd mlang
pip install -e .
```

## Użycie

### Klient Bridge

```python
import asyncio
from mlang.bridge import BridgeClient

async def main():
    bridge = BridgeClient(port=27678, token="mlang-secret-key")
    await bridge.connect()

    # API gracza
    hp = await bridge.player_get_health()
    pos = await bridge.player_get_position()
    print(f"Health: {hp}, Position: {pos}")

    # API świata
    await bridge.world_set_block(100, 64, -200, "minecraft:diamond_block")
    await bridge.world_set_time(6000)

    # Czat
    await bridge.chat_send("§aHello from Python!")

    # Zdarzenia
    bridge.on("playerJoin", lambda data: print(f"{data['player']} joined!"))

    await bridge.disconnect()

asyncio.run(main())
```

### CLI

```bash
# Uruchom plik .glang
python -m mlang script.glang

# Interaktywne REPL
python -m mlang --repl

# Ewaluacja inline
python -m mlang -e "print('Hello World!')"
```

### Komendy GUI

```python
from mlang.gui import serialize_gui_state, Window, Button

win = Window("My Panel", width=400, height=300)
btn = Button("Click!", on_click=lambda: print("clicked"))
win.add(btn)

# Wyślij do gry
state = serialize_gui_state([], [win])
await bridge.gui_send_state(state)
```
