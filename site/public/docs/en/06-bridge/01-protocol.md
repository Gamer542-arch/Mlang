# Bridge Protocol — JSON-RPC 2.0 WebSocket

## Connection

The mod opens a WebSocket server at `ws://localhost:27678`. The client (Python) connects and authenticates.

```
Client ──► Server (mod):  ws://localhost:27678
         ──► auth with token
         ◄── result: true
         ──► player.getHealth
         ◄── result: 20.0
```

## Authorization

First message after establishing connection:

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

Token configurable in `config/mlang.json`. Default: `"mlang-secret-key"`.

## Message format

### Request
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "player.getHealth",
    "params": {}
}
```

### Response
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": 20.0
}
```

### Error
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "error": { "code": -1, "message": "Player not found" }
}
```

## API Endpoints

### Player
| Method | Params | Returns |
|--------|--------|---------|
| `player.getHealth` | `{}` | `float` |
| `player.setHealth` | `{"health": 20.0}` | `bool` |
| `player.getPosition` | `{}` | `{x, y, z, yaw, pitch}` |
| `player.teleport` | `{"x": 100, "y": 64, "z": 0}` | `bool` |
| `player.setGameMode` | `{"gamemode": "creative"}` | `bool` |
| `player.giveItem` | `{"item": "minecraft:diamond"}` | `bool` |
| `player.sendMessage` | `{"message": "&aHello!"}` | `bool` |
| `player.kill` | `{}` | `bool` |

### World
| Method | Params | Returns |
|--------|--------|---------|
| `world.getBlock` | `{"x": 0, "y": 64, "z": 0}` | `string` |
| `world.setBlock` | `{"x": 0, "y": 64, "z": 0, "block": "minecraft:stone"}` | `bool` |
| `world.getTime` | `{}` | `long` |
| `world.setTime` | `{"time": 6000}` | `bool` |
| `world.runCommand` | `{"command": "/say hello"}` | `string` |

### Chat
| Method | Params | Returns |
|--------|--------|---------|
| `chat.send` | `{"message": "Hello!"}` | `bool` |
| `chat.broadcast` | `{"message": "Broadcast!"}` | `bool` |
| `chat.runCommand` | `{"command": "/say hello"}` | `string` |

### GUI
| Method | Params | Returns |
|--------|--------|---------|
| `gui.show` | `{"widget": {...}}` | `bool` |
| `gui.setTheme` | `{"theme": "neon"}` | `bool` |
| `gui.notification` | `{"text": "Hello!", "duration": 60}` | `bool` |
