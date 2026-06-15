# Protokół Bridge — JSON-RPC 2.0 WebSocket

## Połączenie

Mod otwiera serwer WebSocket na `ws://localhost:27678`. Klient (Python) łączy się i autoryzuje.

```
Klient ──► Serwer (mod):  ws://localhost:27678
         ──► auth z tokenem
         ◄── result: true
         ──► player.getHealth
         ◄── result: 20.0
```

## Autoryzacja

Pierwsza wiadomość po nawiązaniu połączenia:

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

Token konfigurowalny w `config/mlang.json`. Domyślnie: `"mlang-secret-key"`.

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
    "error": { "code": -1, "message": "Player not found" }
}
```

## Endpointy API

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
