# GLanguage Syntax

GLanguage verwendet eine C#-ähnliche Syntax, aber einfacher.

## Struktur

```glang
#version 1.0
#name "Mein Skript"
#author "DeinName"
#key F6

// Code...
```

---

## Variablen

```glang
// Typinferenz
var x = 10
var name = "Steve"
var alive = true

// Explizite Typen
int hp = 20
float speed = 1.5
double pi = 3.14159
string nick = "Player1"
bool flying = false

// Konstanten
const int MAX_HP = 20
const string VERSION = "1.0"

// Null
var nothing = null
```

---

## Funktionen

```glang
public void Greet(string name) {
    print("Hallo " + name)
}

public int Add(int a, int b) {
    return a + b
}

// Lambda
var square = (int x) => x * x
```

---

## Klassen

```glang
public class PlayerData {
    public string Name
    private int health = 20

    public PlayerData(string name) {
        this.Name = name
    }

    public void Heal(int amount) {
        health = Math.Min(health + amount, 20)
    }
}
```

---

## Bedingungen

```glang
if (Player.Health < 5) {
    Chat.Send("§cWenig HP!")
} else if (Player.Health < 10) {
    Chat.Send("§eVorsicht!")
} else {
    Chat.Send("§aGut!")
}

// Ternary
string status = Player.IsAlive ? "lebt" : "tot"
```

---

## Schleifen

```glang
// For
for (int i = 0; i < 10; i++) {
    World.SetBlock(i, 64, 0, "minecraft:stone")
}

// Foreach
foreach (string name in playerList) {
    Chat.Send("Spieler: " + name)
}

// While
while (Player.Health > 0) {
    Player.Heal(1)
}
```

---

## Arrays & Sammlungen

```glang
int[] numbers = [1, 2, 3, 4, 5]
string[] names = ["Steve", "Alex", "Notch"]

List<string> players = new List<string>()
players.Add("Steve")

Dictionary<string, int> scores = new Dictionary<string, int>()
scores["Steve"] = 100
```

---

## Operatoren

| Operator | Beschreibung |
|----------|-------------|
| `+ - * / %` | Arithmetisch |
| `**` | Potenz |
| `== != < > <= >=` | Vergleich |
| `&& \|\| !` | Logisch |
| `??` | Null-Coalescing |
| `is` | Typ-Prüfung |
| `as` | Typ-Umwandlung |
