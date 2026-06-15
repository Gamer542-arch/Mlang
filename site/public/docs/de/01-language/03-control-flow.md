# Kontrollfluss

## if/else
```glang
if (condition) {
    // Code
} else if (other) {
    // Code
} else {
    // Code
}
```

## switch
```glang
switch (value) {
    case 1:
        print("one")
        break
    case 2:
        print("two")
        break
    default:
        print("other")
        break
}
```

## match (Musterabgleich)
```glang
match (value) {
    when > 10 => print("groß")
    when > 5  => print("mittel")
    when > 0  => print("klein")
    else      => print("null oder negativ")
}
```

## Schleifen
```glang
// for (Zählschleife)
for (var i = 0; i < 10; i = i + 1) {
    print(i)
}

// foreach (für jedes Element)
foreach (item in list) {
    print(item)
}

// foreach mit Index
foreach (int i, item in list.Enumerate()) {
    print(i + ": " + item)
}

// while (kopfgesteuerte Schleife)
while (condition) {
    // Code
}

// do-while (fußgesteuerte Schleife)
do {
    // Code
} while (condition)

// range (Bereichsschleife)
for (int i in Range(0, 10)) {
    print(i)
}
```

## Break / Continue
```glang
for (var i = 0; i < 100; i = i + 1) {
    if (i == 50) break
    if (i % 2 == 0) continue
    print(i)
}
```

## Ternärer Operator
```glang
var status = Player.Health > 10 ? "sicher" : "Gefahr"
```

## Null-Coalescing
```glang
var name = Player.Name ?? "Unbekannt"
```
