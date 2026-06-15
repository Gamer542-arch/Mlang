# Erstes Skript

Erstelle `hello.glang`:

```glang
#version 1.0
#name "Hello World"
#key F6

var name = "Steve"
var hp = 20

print("Hallo " + name + "!")
print("Du hast " + hp + " HP")

if (hp > 10) {
    print("Du bist gesund!")
} else {
    print("Du bist verletzt!")
}
```

Ausführen:
```bash
python -m mlang hello.glang
```

## Mit Minecraft verbinden

```python
import asyncio
from mlang.bridge import BridgeClient

async def example():
    bridge = BridgeClient()
    await bridge.connect()
    
    name = await bridge.player_get_name()
    health = await bridge.player_get_health()
    print(f"Spieler: {name}, HP: {health}")
    
    await bridge.player_teleport(0, 64, 0)
    await bridge.chat_send("§aTeleportation erfolgreich!")
    
    await bridge.disconnect()

asyncio.run(example())
```
