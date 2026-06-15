# Składnia GLanguage

## Struktura pliku

```glang
#version 1.0
#name "Nazwa skryptu"
#author "Autor"
#key F6
#import "utils.glang"

// kod...
```

### Dyrektywy
| Dyrektywa | Opis |
|-----------|------|
| `#version` | Wersja języka |
| `#name` | Nazwa skryptu (widoczna w edytorze) |
| `#author` | Autor |
| `#key` | Klawisz do uruchomienia (F5-F8) |
| `#import` | Import innego pliku .glang |
| `#description` | Opis skryptu |

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
char letter = 'A'
byte b = 255

// Stałe
const int MAX_HP = 20
const string VERSION = "1.0"

// Null
var nothing = null
object obj = null

// Wielokrotna deklaracja
var a = 1, b = 2, c = 3
```

---

## Funkcje

```glang
// Podstawowa
public void Greet(string name) {
    print("Hej " + name)
}

// Z wartością zwracaną
public int Add(int a, int b) {
    return a + b
}

// Wartości domyślne
public void TeleportPlayer(double x, double y = 64.0, double z = 0.0) {
    Player.TeleportTo(x, y, z)
}

// Lambda
var square = (int x) => x * x
var greet = (string name) => "Hej " + name

// Funkcja anonimowa
var callback = func(int val) {
    print("Wartość: " + val)
}

// Variadic params
public void Log(params string[] messages) {
    foreach (string msg in messages) {
        print(msg)
    }
}

// Static
public static int Multiply(int a, int b) {
    return a * b
}

// Private - tylko wewnątrz klasy/pliku
private void Helper() {
    // ...
}

// Overload (przeciążanie)
public void Print(int value) { print("int: " + value) }
public void Print(string value) { print("str: " + value) }
public void Print(int a, int b) { print("sum: " + (a + b)) }
```

---

## Klasy

```glang
public class PlayerData {
    public string Name
    private int health = 20
    protected const int MAX_SPEED = 10

    public PlayerData(string name) {
        this.Name = name
    }

    public int Health {
        get { return health }
        set { health = Math.Clamp(value, 0, 20) }
    }

    public void Heal(int amount) {
        health = Math.Min(health + amount, 20)
    }

    public override string ToString() {
        return "Player(" + Name + ", " + health + "HP)"
    }
}
```

### Dziedziczenie i interfejsy

```glang
public interface IEntity {
    void Spawn(double x, double y, double z)
    void Remove()
}

public abstract class BaseEntity : IEntity {
    public double X, Y, Z
    public string Type

    public abstract void Update()

    public void Spawn(double x, double y, double z) {
        this.X = x; this.Y = y; this.Z = z
        World.Summon(Type, x, y, z)
    }

    public void Remove() {
        World.KillEntity(this)
    }
}

public class CustomZombie : BaseEntity {
    public float Health = 20.0f

    public CustomZombie() {
        this.Type = "minecraft:zombie"
    }

    public override void Update() {
        if (Health <= 0) Remove()
    }
}
```

### Polimorfizm
```glang
IEntity e = new CustomZombie()
e.Spawn(100, 64, -200)

// Type checking
if (e is CustomZombie) {
    Chat.Send("To jest zombie!")
}

// Pattern matching
match (e) {
    case CustomZombie z => z.Health = 30
    case BaseEntity b   => b.Update()
    else                => print("Nieznana encja")
}
```

---

## Operatory

### Arytmetyczne
| Operator | Opis |
|----------|------|
| `+` | Dodawanie / konkatenacja |
| `-` | Odejmowanie |
| `*` | Mnożenie |
| `/` | Dzielenie (float) |
| `//` | Dzielenie całkowite |
| `%` | Modulo |
| `**` | Potęga |

### Porównania
| Operator | Opis |
|----------|------|
| `==` | Równe |
| `!=` | Nierówne |
| `<` | Mniejsze |
| `>` | Większe |
| `<=` | Mniejsze lub równe |
| `>=` | Większe lub równe |

### Logiczne
| Operator | Opis |
|----------|------|
| `&&` | AND |
| `\|\|` | OR |
| `!` | NOT |

### Bitowe
| Operator | Opis |
|----------|------|
| `&` | Bitwise AND |
| `\|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Shift left |
| `>>` | Shift right |

### Przypisania
| Operator | Opis |
|----------|------|
| `=` | Przypisanie |
| `+=` | Dodaj i przypisz |
| `-=` | Odejmij i przypisz |
| `*=` | Mnożenie i przypisz |
| `/=` | Dzielenie i przypisz |
| `%=` | Modulo i przypisz |

### Inne
| Operator | Opis |
|----------|------|
| `??` | Null coalescing |
| `?.` | Optional chaining (null-safe) |
| `is` | Type check |
| `as` | Type cast |
| `=>` | Lambda / arrow |
| `..` | Range (w pętlach) |

---

## Warunki

```glang
// If
if (Player.Health < 5) {
    Chat.Send("Mało HP!")
}

// If-else
if (Player.Health > 10) {
    Chat.Send("Dobrze")
} else {
    Chat.Send("Słabo")
}

// Else if
if (Player.Health < 5) {
    Chat.Send("Krytyczne!")
} else if (Player.Health < 10) {
    Chat.Send("Uważaj!")
} else {
    Chat.Send("W porządku")
}

// Ternary
string status = Player.IsAlive ? "żyje" : "martwy"

// Null coalescing
string nick = Player.Name ?? "Nieznany"

// Switch
switch (Player.GameMode) {
    case "survival":
        Chat.Send("Tryb przetrwania")
        break
    case "creative":
        Chat.Send("Tryb kreatywny")
        break
    default:
        Chat.Send("Inny tryb")
        break
}

// Match (pattern matching)
match (Player.Health) {
    when > 15  => Chat.Send("Dobrze")
    when > 5   => Chat.Send("Średnio")
    when > 0   => Chat.Send("Źle")
    else       => Chat.Send("Martwy")
}
```

---

## Pętle

```glang
// For
for (int i = 0; i < 10; i++) {
    World.SetBlock(i, 64, 0, "minecraft:stone")
}

// For (range)
for (int i in 0..10) {
    print(i)
}

// Foreach
foreach (string name in playerList) {
    Chat.Send("Gracz: " + name)
}

// Foreach z indeksem
foreach (int i, string name in names.Enumerate()) {
    print(i + ": " + name)
}

// While
while (Player.Health > 0) {
    Player.Heal(1)
    if (Player.Health >= 20) break
}

// Do-while
do {
    Player.Jump()
} while (!Player.IsOnGround)

// Break / Continue
for (int i = 0; i < 100; i++) {
    if (i == 50) break
    if (i % 2 == 0) continue
    print(i)
}
```

---

## Tablice i kolekcje

```glang
// Tablice
int[] numbers = [1, 2, 3, 4, 5]
string[] names = ["Steve", "Alex", "Notch"]
int first = numbers[0]
numbers[1] = 10
int len = numbers.Length

// List
List<string> players = new List<string>()
players.Add("Steve")
players.Remove("Steve")
players.Contains("Alex")
int count = players.Count
players.RemoveAt(0)
players.Clear()

// Dictionary
Dictionary<string, int> scores = new Dictionary<string, int>()
scores["Steve"] = 100
scores["Alex"] = 200
int steveScore = scores["Steve"]
scores.Remove("Alex")
scores.ContainsKey("Steve")
scores.Keys()   // List<string>
scores.Values() // List<int>

// Set
Set<string> unique = new Set<string>()
unique.Add("a")
unique.Add("a")  // ignorowane
unique.Contains("a")
unique.Remove("a")
int size = unique.Count

// Inicjalizacja skrócona
var list = List["Steve", "Alex", "Notch"]
var dict = Dict["key1": 1, "key2": 2]
var set  = Set["a", "b", "c"]
```

---

## Generyki

```glang
// Klasa generyczna
public class Stack<T> {
    private List<T> items = new List<T>()

    public void Push(T item) {
        items.Add(item)
    }

    public T Pop() {
        T last = items[items.Count - 1]
        items.RemoveAt(items.Count - 1)
        return last
    }

    public T Peek() {
        return items[items.Count - 1]
    }

    public bool IsEmpty {
        get { return items.Count == 0 }
    }
}

// Użycie
var stack = new Stack<string>()
stack.Push("a")
stack.Push("b")
string top = stack.Pop()  // "b"

// Metoda generyczna
public T Identity<T>(T value) {
    return value
}

var result = Identity<int>(42)
```

---

## Obsługa błędów

```glang
// Try-catch
try {
    Player.TeleportTo(999999, 0, 0)
} catch (GException e) {
    Chat.Send("Błąd: " + e.Message)
    Log.Error(e.StackTrace)
} catch (Exception e) {
    Chat.Send("Nieznany błąd: " + e)
} finally {
    Chat.Send("Gotowe")
}

// Throw
void CheckHP(int hp) {
    if (hp <= 0) {
        throw new GException("HP nie może być 0!")
    }
}

// Własny wyjątek
public class MyException : GException {
    public MyException(string msg) : base(msg) {}
}
```

---

## Async/Await

```glang
// Asynchroniczna funkcja
public async Task<string> FetchData(string url) {
    string result = await Http.Get(url)
    return result
}

// Opóźnienie
public async void DelayedTeleport(double x, double y, double z, int ticks) {
    await Wait.Ticks(ticks)
    Player.TeleportTo(x, y, z)
}

// Schedule cykliczny
Schedule.Every(20, () => {
    Chat.Send("Minęła sekunda!")
})

// Schedule jednorazowy
Schedule.After(100, () => {
    Chat.Send("5 sekund minęło")
})

// Schedule warunkowy
Schedule.When(() => Player.Health < 5, () => {
    Chat.Send("§cMało HP!")
})
```

---

## Komentarze

```glang
// Komentarz jednolinijkowy

/*
   Komentarz
   blokowy
*/

/// Dokumentacja (doc comment)
/// @param name Imię gracza
/// @return Przywitanie
public string Greet(string name) {
    return "Cześć " + name
}
```

---

## Konwersje typów

```glang
// Casting
int x = (int) 3.99     // = 3
double d = (double) 5  // = 5.0
string s = (string) 42 // = "42"

// Metody konwersji
int i = "42".ToInt()
double db = "3.14".ToDouble()
bool b = "true".ToBool()
string str = 42.ToString()
char[] chars = "hello".ToChars()
float f = "1.5".ToFloat()
long big = "999999".ToLong()

// Nullable
int? maybe = null
int val = maybe ?? 0

// Type checking
if (x is int) { }
if (obj is string s) {
    print(s) // s jest string
}
```
