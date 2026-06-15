# First MLang script

Create a `hello.glang` file:

```glang
#version 1.0
#name "Hello World"
#key F6

var name = "Steve"
var hp = 20

print("Hello " + name + "!")
print("You have " + hp + " HP")

if (hp > 10) {
    print("You are healthy!")
} else {
    print("You are wounded!")
}
```

Run:
```bash
python -m mlang hello.glang
```

## Connecting to Minecraft

To make the script control the game, use the bridge client:

```python
import asyncio
from mlang.bridge import BridgeClient

async def example():
    bridge = BridgeClient()
    await bridge.connect()
    
    name = await bridge.player_get_name()
    hp = await bridge.player_get_health()
    print(f"Player: {name}, HP: {hp}")
    
    await bridge.player_teleport(0, 64, 0)
    await bridge.chat_send("§aTeleport successful!")
    
    await bridge.disconnect()

asyncio.run(example())
```
