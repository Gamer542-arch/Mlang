# Bridge Protocol — JSON-RPC 2.0 WebSocket

## Połączenie

Mod otwiera serwer WebSocket na `ws://localhost:27678`. Klient (Python) łączy się i autoryzuje.

```
Klient ──► Serwer (mod):  ws://localhost:27678
         ──► auth z tokenem
         ◄── result: true
         ──► player.getHealth
         ◄── result: 20.0
         ──► world.setBlock(100, 64, -200, "minecraft:stone")
         ◄── result: true
```

## Autoryzacja

Pierwsza wiadomość po nawiązaniu połączenia:

```json
→ {
    "jsonrpc": "2.0",
    "id": 0,
    "method": "auth",
    "params": {
        "token": "mlang-secret-key"
    }
}

← {
    "jsonrpc": "2.0",
    "id": 0,
    "result": true
}
```

Token konfigurowalny w `config/mlang.json` moda. Domyślnie: `"mlang-secret-key"`.

Jeśli token nieprawidłowy:
```json
← {
    "jsonrpc": "2.0",
    "id": 0,
    "error": {
        "code": -32001,
        "message": "Invalid auth token"
    }
}
```

## Format wiadomości

### Żądanie (Request)
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "player.getHealth",
    "params": {}
}
```

### Odpowiedź (Response)
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": 20.0
}
```

### Błąd (Error)
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "error": {
        "code": -1,
        "message": "Player not found"
    }
}
```

### Event (jednokierunkowy, bez ID)
```json
{
    "jsonrpc": "2.0",
    "method": "event",
    "params": {
        "type": "playerDeath",
        "data": {
            "player": "Steve",
            "cause": "zombie"
        }
    }
}
```

## Kody błędów

| Kod | Opis |
|-----|------|
| `-32700` | Parse error — nieprawidłowy JSON |
| `-32600` | Invalid request — brak jsonrpc/method |
| `-32601` | Method not found — nieznana metoda |
| `-32602` | Invalid params — złe parametry |
| `-32603` | Internal error — błąd wewnętrzny |
| `-32000` | Not authenticated — brak auth |
| `-32001` | Invalid token — zły token |
| `-32099` | Execution error — błąd wykonania (np. gracz offline) |

## Endpointy API

### Player
| Method | Params | Returns |
|--------|--------|---------|
| `player.getHealth` | `{}` | `float` |
| `player.setHealth` | `{"health": 20.0}` | `bool` |
| `player.getMaxHealth` | `{}` | `float` |
| `player.setMaxHealth` | `{"maxHealth": 40.0}` | `bool` |
| `player.getPosition` | `{}` | `{"x": double, "y": double, "z": double, "yaw": float, "pitch": float}` |
| `player.teleport` | `{"x": double, "y": double, "z": double, "yaw?": float, "pitch?": float}` | `bool` |
| `player.getVelocity` | `{}` | `{"x": double, "y": double, "z": double}` |
| `player.setVelocity` | `{"x": double, "y": double, "z": double}` | `bool` |
| `player.getGameMode` | `{}` | `string` |
| `player.setGameMode` | `{"gamemode": "creative"}` | `bool` |
| `player.getFoodLevel` | `{}` | `int` |
| `player.setFoodLevel` | `{"level": 20}` | `bool` |
| `player.getSaturation` | `{}` | `float` |
| `player.setSaturation` | `{"saturation": 5.0}` | `bool` |
| `player.getExperience` | `{}` | `int` |
| `player.setExperience` | `{"xp": 500}` | `bool` |
| `player.getLevel` | `{}` | `int` |
| `player.setLevel` | `{"level": 50}` | `bool` |
| `player.giveExperience` | `{"amount": 100}` | `bool` |
| `player.giveItem` | `{"item": "minecraft:diamond", "count?": 64}` | `bool` |
| `player.getMainHandItem` | `{}` | `ItemStack` |
| `player.setMainHandItem` | `{"item": "minecraft:diamond_sword"}` | `bool` |
| `player.sendMessage` | `{"message": "§aHello!"}` | `bool` |
| `player.showTitle` | `{"title": "§6Witaj", "subtitle?": "", "fadeIn?": 10, "stay?": 70, "fadeOut?": 20}` | `bool` |
| `player.getEffects` | `{}` | `[{"type": "speed", "duration": 200, "amplifier": 1}]` |
| `player.addEffect` | `{"type": "speed", "duration": 200, "amplifier": 2}` | `bool` |
| `player.removeEffect` | `{"type": "speed"}` | `bool` |
| `player.clearEffects` | `{}` | `bool` |
| `player.getInventory` | `{}` | `[ItemStack...]` |
| `player.clearInventory` | `{}` | `bool` |
| `player.getSelectedSlot` | `{}` | `int` |
| `player.setSelectedSlot` | `{"slot": 0}` | `bool` |
| `player.jump` | `{}` | `bool` |
| `player.setSprint` | `{"sprint": true}` | `bool` |
| `player.setSneak` | `{"sneak": true}` | `bool` |
| `player.setFly` | `{"fly": true}` | `bool` |
| `player.kill` | `{}` | `bool` |
| `player.getName` | `{}` | `string` |
| `player.getUUID` | `{}` | `string` |
| `player.getDimension` | `{}` | `string` |
| `player.isAlive` | `{}` | `bool` |
| `player.isFlying` | `{}` | `bool` |
| `player.isSneaking` | `{}` | `bool` |
| `player.isSprinting` | `{}` | `bool` |
| `player.isOnGround` | `{}` | `bool` |
| `player.isInWater` | `{}` | `bool` |
| `player.isOnFire` | `{}` | `bool` |
| `player.isBlocking` | `{}` | `bool` |
| `player.getNBT` | `{}` | `string` |
| `player.setNBT` | `{"nbt": "{...}"}` | `bool` |

### World
| Method | Params | Returns |
|--------|--------|---------|
| `world.getBlock` | `{"x": int, "y": int, "z": int}` | `string` |
| `world.setBlock` | `{"x": int, "y": int, "z": int, "block": "minecraft:stone"}` | `bool` |
| `world.breakBlock` | `{"x": int, "y": int, "z": int}` | `bool` |
| `world.getBiome` | `{"x": int, "y": int, "z": int}` | `string` |
| `world.getTime` | `{}` | `long` |
| `world.setTime` | `{"time": 6000}` | `bool` |
| `world.getWeather` | `{}` | `string` |
| `world.setWeather` | `{"weather": "clear"}` | `bool` |
| `world.getDifficulty` | `{}` | `string` |
| `world.setDifficulty` | `{"difficulty": "peaceful"}` | `bool` |
| `world.getDimension` | `{}` | `string` |
| `world.getGameRule` | `{"rule": "keepInventory"}` | `object` |
| `world.setGameRule` | `{"rule": "keepInventory", "value": "true"}` | `bool` |
| `world.runCommand` | `{"command": "/say hello"}` | `string` |
| `world.getNearbyEntities` | `{"x": double, "y": double, "z": double, "radius": 5.0}` | `[Entity...]` |
| `world.getPlayers` | `{}` | `[Player...]` |
| `world.summon` | `{"entity": "minecraft:zombie", "x": double, "y": double, "z": double}` | `Entity` |
| `world.fillBlocks` | `{"x1": int, "y1": int, "z1": int, "x2": int, "y2": int, "z2": int, "block": "minecraft:air"}` | `int` |
| `world.createExplosion` | `{"x": double, "y": double, "z": double, "power": 4.0}` | `bool` |
| `world.strikeLightning` | `{"x": double, "y": double, "z": double}` | `bool` |
| `world.spawnParticle` | `{"particle": "minecraft:flame", "x": double, "y": double, "z": double, "count": 10}` | `bool` |
| `world.playSound` | `{"sound": "minecraft:entity.player.levelup", "x": double, "y": double, "z": double, "volume": 1.0, "pitch": 1.0}` | `bool` |

### Entity
| Method | Params | Returns |
|--------|--------|---------|
| `entity.getHealth` | `{"id": int}` | `float` |
| `entity.setHealth` | `{"id": int, "health": 20.0}` | `bool` |
| `entity.getPosition` | `{"id": int}` | `{"x": double, "y": double, "z": double}` |
| `entity.teleport` | `{"id": int, "x": double, "y": double, "z": double}` | `bool` |
| `entity.kill` | `{"id": int}` | `bool` |
| `entity.remove` | `{"id": int}` | `bool` |
| `entity.getNBT` | `{"id": int}` | `string` |
| `entity.setNBT` | `{"id": int, "nbt": "{...}"}` | `bool` |
| `entity.setCustomName` | `{"id": int, "name": "§6Elite Zombie"}` | `bool` |
| `entity.setGlowing` | `{"id": int, "glowing": true}` | `bool` |
| `entity.setInvisible` | `{"id": int, "invisible": true}` | `bool` |
| `entity.setInvulnerable` | `{"id": int, "invulnerable": true}` | `bool` |
| `entity.addEffect` | `{"id": int, "type": "speed", "duration": 200, "amplifier": 2}` | `bool` |
| `entity.removeEffect` | `{"id": int, "type": "speed"}` | `bool` |
| `entity.getType` | `{"id": int}` | `string` |
| `entity.isAlive` | `{"id": int}` | `bool` |

### Chat
| Method | Params | Returns |
|--------|--------|---------|
| `chat.send` | `{"message": "§aHello world!"}` | `bool` |
| `chat.broadcast` | `{"message": "§6Server broadcast!"}` | `bool` |
| `chat.runCommand` | `{"command": "/say hello"}` | `string` |

### Sound
| Method | Params | Returns |
|--------|--------|---------|
| `sound.play` | `{"sound": "minecraft:entity.player.levelup", "volume?": 1.0, "pitch?": 1.0}` | `bool` |
| `sound.playAt` | `{"sound": "minecraft:block.anvil.land", "x": double, "y": double, "z": double, "volume?": 1.0, "pitch?": 1.0}` | `bool` |
| `sound.stopAll` | `{}` | `bool` |

### Particle
| Method | Params | Returns |
|--------|--------|---------|
| `particle.spawn` | `{"particle": "minecraft:flame", "x": double, "y": double, "z": double, "count?": 1, "dx?": 0.0, "dy?": 0.0, "dz?": 0.0, "speed?": 0.0}` | `bool` |

### Inventory
| Method | Params | Returns |
|--------|--------|---------|
| `inventory.getItems` | `{}` | `[ItemStack...]` |
| `inventory.giveItem` | `{"item": "minecraft:diamond", "count?": 1}` | `bool` |
| `inventory.removeItem` | `{"item": "minecraft:diamond", "count?": 1}` | `bool` |
| `inventory.clear` | `{}` | `bool` |
| `inventory.hasItem` | `{"item": "minecraft:diamond"}` | `bool` |

### System
| Method | Params | Returns |
|--------|--------|---------|
| `system.ping` | `{}` | `"pong"` |
| `system.getModVersion` | `{}` | `string` |
| `system.getMcVersion` | `{}` | `string` |
| `system.getPlayers` | `{}` | `[{"name": "Steve", "uuid": "...", "ping": 20}]` |
| `system.getServerTick` | `{}` | `int` |
| `system.getUptime` | `{}` | `long` |

---

## Eventy (Mod → Python)

Mod może wysyłać eventy do Pythona.

```json
{
    "jsonrpc": "2.0",
    "method": "event",
    "params": {
        "type": "playerJoin",
        "data": {
            "player": "Steve",
            "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        }
    }
}
```

### Lista eventów
| Typ | Data | Opis |
|-----|------|------|
| `playerJoin` | `{"player", "uuid"}` | Gracz dołączył |
| `playerLeave` | `{"player", "uuid"}` | Gracz wyszedł |
| `playerDeath` | `{"player", "cause", "x", "y", "z"}` | Gracz umarł |
| `playerRespawn` | `{"player"}` | Gracz się odrodził |
| `playerMove` | `{"player", "from": {x,y,z}, "to": {x,y,z}}` | Gracz zmienił pozycję |
| `chatMessage` | `{"player", "message", "type"}` | Wiadomość na czacie |
| `blockBreak` | `{"player", "block", "x", "y", "z"}` | Blok zniszczony |
| `blockPlace` | `{"player", "block", "x", "y", "z"}` | Blok postawiony |
| `entityDeath` | `{"entity", "type", "killer", "x", "y", "z"}` | Encja umarła |
| `serverTick` | `{"tick"}` | Tick serwera (co 20 ticków) |
| `worldLoad` | `{"world", "dimension"}` | Świat załadowany |
| `worldSave` | `{"world"}` | Świat zapisany |

---

## Przykład sesji

```
→ CONNECT ws://localhost:27678

→ {"jsonrpc": "2.0", "id": 0, "method": "auth", "params": {"token": "mlang-secret-key"}}
← {"jsonrpc": "2.0", "id": 0, "result": true}

→ {"jsonrpc": "2.0", "id": 1, "method": "player.getPosition", "params": {}}
← {"jsonrpc": "2.0", "id": 1, "result": {"x": 100.5, "y": 64.0, "z": -200.3, "yaw": 45.0, "pitch": 30.0}}

→ {"jsonrpc": "2.0", "id": 2, "method": "player.teleport", "params": {"x": 0, "y": 64, "z": 0}}
← {"jsonrpc": "2.0", "id": 2, "result": true}

→ {"jsonrpc": "2.0", "id": 3, "method": "world.setBlock", "params": {"x": 0, "y": 64, "z": 0, "block": "minecraft:diamond_block"}}
← {"jsonrpc": "2.0", "id": 3, "result": true}

→ {"jsonrpc": "2.0", "id": 4, "method": "world.runCommand", "params": {"command": "/say Hello from MLang!"}}
← {"jsonrpc": "2.0", "id": 4, "result": "Done"}

← {"jsonrpc": "2.0", "method": "event", "params": {"type": "playerDeath", "data": {"player": "Notch", "cause": "fall"}}}

→ DISCONNECT
```
