# Pierwszy skrypt w MLang

Stwórz plik `hello.glang`:

```glang
#version 1.0
#name "Hello World"
#key F6

var name = "Steve"
var hp = 20

print("Hello " + name + "!")
print("Masz " + hp + " HP")

if (hp > 10) {
    print("Jesteś zdrowy!")
} else {
    print("Jesteś ranny!")
}
```

Uruchom:
```bash
python -m mlang hello.glang
```

## Łączenie z Minecraftem

Aby skrypt sterował grą, użyj bridge clienta:

```python
import asyncio
from mlang.bridge import BridgeClient

async def example():
    bridge = BridgeClient()
    await bridge.connect()
    
    name = await bridge.player_get_name()
    hp = await bridge.player_get_health()
    print(f"Gracz: {name}, HP: {hp}")
    
    await bridge.player_teleport(0, 64, 0)
    await bridge.chat_send("§aTeleportacja udana!")
    
    await bridge.player_set_gamemode("creative")
    
    await bridge.disconnect()

asyncio.run(example())
```
