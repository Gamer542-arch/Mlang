# Sammlungen

## List
```glang
var list = new List<string>()
list.Add("a")
list.Add("b")
list.Remove("a")
list.Contains("b")  // true
list.Count          // 2
list.Clear()

// Initialisierung
var items = List["a", "b", "c"]
```

## Dictionary
```glang
var dict = new Dictionary<string, int>()
dict["key1"] = 100
dict["key2"] = 200
var val = dict["key1"]
dict.Remove("key1")
dict.ContainsKey("key2")  // true

// Initialisierung
var scores = Dict["Steve": 100, "Alex": 200]
```

## Set
```glang
var set = new Set<string>()
set.Add("a")
set.Add("a")  // ignoriert (Duplikat)
set.Contains("a")  // true
set.Remove("a")
set.Count

// Initialisierung
var tags = Set["stone", "wood", "dirt"]
```

## Iteration
```glang
foreach (item in list) { }
foreach (key, val in dict) { }
foreach (item in set) { }
```
