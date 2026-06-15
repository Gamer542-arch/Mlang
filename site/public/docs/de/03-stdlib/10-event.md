# GL.Event — Eventsystem

## Events erstellen

```glang
var events = new EventEmitter()

// Lauschen
events.On("playerJoin", (data) => {
    print("Spieler beigetreten: " + data.name)
})

// Einmaliges Lauschen
events.Once("playerDeath", (data) => {
    print("Spieler gestorben: " + data.name + " durch " + data.cause)
})

// Emittieren
events.Emit("playerJoin", {"name": "Steve"})
events.Emit("playerDeath", {"name": "Alex", "cause": "zombie"})
```

## EventEmitter-Methoden

| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `emitter.On(event, callback)` | `void` | Auf Event lauschen |
| `emitter.Once(event, callback)` | `void` | Einmalig lauschen |
| `emitter.Off(event)` | `void` | Alle Callbacks entfernen |
| `emitter.Off(event, callback)` | `void` | Bestimmten Callback entfernen |
| `emitter.Emit(event, data)` | `void` | Event senden |
| `emitter.EmitAsync(event, data)` | `Task` | Asynchron senden |
| `emitter.Listeners(event)` | `int` | Anzahl der Lauscher |
| `emitter.EventNames()` | `List<string>` | Event-Liste |
| `emitter.RemoveAllListeners()` | `void` | Alle entfernen |
| `emitter.OnAny(callback)` | `void` | Auf alle Events lauschen |

## Minecraft-Events

Die Mod-Bridge sendet Events an den Interpreter:
```glang
events.On("playerJoin", (data) => {
    Chat.Send("§a+" + data.player + " ist beigetreten!")
})

events.On("playerDeath", (data) => {
    Chat.Send("§c" + data.player + " gestorben durch " + data.cause)
})
```
