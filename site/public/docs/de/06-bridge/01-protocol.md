# Bridge-Protokoll — JSON-RPC 2.0 WebSocket

## Verbindung

Der Mod öffnet einen WebSocket-Server auf `ws://localhost:27678`.

```
Client ──► Server (Mod): ws://localhost:27678
         ──► auth mit Token
         ◄── result: true
         ──► player.getHealth
         ◄── result: 20.0
```

## Authentifizierung

```json
→ {
    "jsonrpc": "2.0",
    "id": 0,
    "method": "auth",
    "params": { "token": "mlang-secret-key" }
}

← {
    "jsonrpc": "2.0",
    "id": 0,
    "result": true
}
```

## Endpoints

### Player
| Method | Params | Returns |
|--------|--------|---------|
| `player.getHealth` | `{}` | `float` |
| `player.setHealth` | `{"health": 20.0}` | `bool` |
| `player.getPosition` | `{}` | `{x, y, z, yaw, pitch}` |
| `player.teleport` | `{"x": 100, "y": 64, "z": 0}` | `bool` |
| `player.setGameMode` | `{"gamemode": "creative"}` | `bool` |
| `player.giveItem` | `{"item": "minecraft:diamond"}` | `bool` |
| `player.sendMessage` | `{"message": "&aHallo!"}` | `bool` |

### World
| Method | Params | Returns |
|--------|--------|---------|
| `world.getBlock` | `{"x": 0, "y": 64, "z": 0}` | `string` |
| `world.setBlock` | `{"x": 0, "y": 64, "z": 0, "block": "..."}` | `bool` |
| `world.getTime` | `{}` | `long` |
| `world.setTime` | `{"time": 6000}` | `bool` |
| `world.runCommand` | `{"command": "/say hallo"}` | `string` |

### GUI
| Method | Params | Returns |
|--------|--------|---------|
| `gui.show` | `{"widget": {...}}` | `bool` |
| `gui.setTheme` | `{"theme": "neon"}` | `bool` |
