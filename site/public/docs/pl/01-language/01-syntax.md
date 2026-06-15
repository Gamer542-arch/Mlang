# Składnia GLanguage

GLanguage wygląda jak C#, ale jest prostszy. Bez generyków, refleksji i skomplikowanych wzorców.

## Struktura pliku

```glang
#version 1.0
#name "Nazwa skryptu"
#author "Autor"
#key F6
#import "utils.glang"

// kod...
```

---

## Zmienne

```glang
// Inferencja typu
var x = 10
var name = "Steve"
var alive = true

// Typy jawne
int hp = 20
float speed = 1.5
double pi = 3.14159
string nick = "Player1"
bool flying = false

// Stałe
const int MAX_HP = 20
const string VERSION = "1.0"

// Null
var nothing = null
```

---

## Funkcje

```glang
public void Greet(string name) {
    print("Hej " + name)
}

public int Add(int a, int b) {
    return a + b
}

// Lambda
var square = (int x) => x * x
var greet = (string name) => "Hej " + name
```

---

## Klasy

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

## Dziedziczenie

```glang
public class CustomZombie : BaseEntity {
    public float Health = 20.0f

    public override void Update() {
        if (Health <= 0) Remove()
    }
}
```

---

## Warunki

```glang
if (Player.Health < 5) {
    Chat.Send("§cMało HP!")
} else if (Player.Health < 10) {
    Chat.Send("§eUważaj!")
} else {
    Chat.Send("§aDobrze")
}

// Ternary
string status = Player.IsAlive ? "żyje" : "martwy"

// Switch
switch (Player.GameMode) {
    case "survival": Chat.Send("Przetrwanie"); break
    case "creative": Chat.Send("Kreatywny"); break
    default: Chat.Send("Inny tryb"); break
}
```

---

## Pętle

```glang
// For
for (int i = 0; i < 10; i++) {
    World.SetBlock(i, 64, 0, "minecraft:stone")
}

// Foreach
foreach (string name in playerList) {
    Chat.Send("Gracz: " + name)
}

// While
while (Player.Health > 0) {
    Player.Heal(1)
}
```

---

## Tablice i kolekcje

```glang
// Tablice
int[] numbers = [1, 2, 3, 4, 5]
string[] names = ["Steve", "Alex", "Notch"]

// List
List<string> players = new List<string>()
players.Add("Steve")
players.Remove("Steve")

// Dictionary
Dictionary<string, int> scores = new Dictionary<string, int>()
scores["Steve"] = 100
scores["Alex"] = 200

// Set
Set<string> unique = new Set<string>()
unique.Add("a")
```

---

## Operatory

| Operator | Opis |
|----------|------|
| `+ - * / %` | Arytmetyczne |
| `**` | Potęga |
| `== != < > <= >=` | Porównania |
| `&& \|\| !` | Logiczne |
| `??` | Null coalescing |
| `is` | Sprawdzenie typu |
| `as` | Rzutowanie |
