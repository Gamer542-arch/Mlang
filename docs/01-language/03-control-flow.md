# Kontrola przepływu

## if/else
```glang
if (condition) {
    // code
} else if (other) {
    // code
} else {
    // code
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

## match (pattern matching)
```glang
match (value) {
    when > 10 => print("big")
    when > 5  => print("medium")
    when > 0  => print("small")
    else      => print("zero or negative")
}
```

## Pętle
```glang
// for
for (var i = 0; i < 10; i = i + 1) {
    print(i)
}

// foreach
foreach (item in list) {
    print(item)
}

// foreach with index
foreach (int i, item in list.Enumerate()) {
    print(i + ": " + item)
}

// while
while (condition) {
    // code
}

// do-while
do {
    // code
} while (condition)

// range
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

## Ternary
```glang
var status = Player.Health > 10 ? "safe" : "danger"
```

## Null coalescing
```glang
var name = Player.Name ?? "Unknown"
```
