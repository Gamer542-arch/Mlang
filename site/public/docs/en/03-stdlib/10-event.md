# GL.Event — event system

## Creating events

```glang
var events = new EventEmitter()

// Listening
events.On("playerJoin", (data) => {
    print("Player joined: " + data.name)
})

// One-time listening
events.Once("playerDeath", (data) => {
    print("Player died: " + data.name + " from " + data.cause)
})

// Emitting
events.Emit("playerJoin", {"name": "Steve"})
events.Emit("playerDeath", {"name": "Alex", "cause": "zombie"})
```

## EventEmitter Methods

| Method | Returns | Description |
|--------|--------|------|
| `emitter.On(event, callback)` | `void` | Listen for event |
| `emitter.Once(event, callback)` | `void` | Listen once |
| `emitter.Off(event)` | `void` | Remove all callbacks |
| `emitter.Off(event, callback)` | `void` | Remove specific callback |
| `emitter.Emit(event, data)` | `void` | Emit event |
| `emitter.EmitAsync(event, data)` | `Task` | Emit asynchronously |
| `emitter.Listeners(event)` | `int` | Number of listeners |
| `emitter.EventNames()` | `List<string>` | List of events |
| `emitter.RemoveAllListeners()` | `void` | Remove all |
| `emitter.OnAny(callback)` | `void` | Listen for all events |

## Minecraft Events

The mod bridge sends events to the interpreter:
```glang
events.On("playerJoin", (data) => {
    Chat.Send("§a+" + data.player + " joined!")
})

events.On("playerDeath", (data) => {
    Chat.Send("§c" + data.player + " died from " + data.cause)
})
```
