# GL.Event — system eventów

## Tworzenie eventów

```glang
var events = new EventEmitter()

// Nasłuchiwanie
events.On("playerJoin", (data) => {
    print("Gracz dołączył: " + data.name)
})

// Jednorazowe nasłuchiwanie
events.Once("playerDeath", (data) => {
    print("Gracz umarł: " + data.name + " od " + data.cause)
})

// Emitowanie
events.Emit("playerJoin", {"name": "Steve"})
events.Emit("playerDeath", {"name": "Alex", "cause": "zombie"})
```

## Metody EventEmitter

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `emitter.On(event, callback)` | `void` | Nasłuchuj eventu |
| `emitter.Once(event, callback)` | `void` | Nasłuchuj jednorazowo |
| `emitter.Off(event)` | `void` | Usuń wszystkie callbacki |
| `emitter.Off(event, callback)` | `void` | Usuń konkretny callback |
| `emitter.Emit(event, data)` | `void` | Wyślij event |
| `emitter.EmitAsync(event, data)` | `Task` | Wyślij asynchronicznie |
| `emitter.Listeners(event)` | `int` | Ilość nasłuchujących |
| `emitter.EventNames()` | `List<string>` | Lista eventów |
| `emitter.RemoveAllListeners()` | `void` | Usuń wszystkie |
| `emitter.OnAny(callback)` | `void` | Nasłuchuj wszystkie eventy |

## Eventy Minecraft

Mod bridge wysyła eventy do interpretera:
```glang
events.On("playerJoin", (data) => {
    Chat.Send("§a+" + data.player + " dołączył!")
})

events.On("playerDeath", (data) => {
    Chat.Send("§c" + data.player + " umarł od " + data.cause)
})
```
