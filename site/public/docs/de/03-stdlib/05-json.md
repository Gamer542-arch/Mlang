# GL.JSON — JSON-Parser

```glang
// Parsen
var json = JSON.Parse('{"name":"Steve","hp":20,"items":["diamond","stone"]}')
var name = json["name"]     // "Steve"
var hp = json["hp"]         // 20
var items = json["items"]   // ["diamond", "stone"]
var first = items[0]        // "diamond"

// Stringify
var str = JSON.Stringify(obj)
var pretty = JSON.Stringify(obj, true)  // pretty print
var indented = JSON.Stringify(obj, 2)   // 2 spaces indent

// Prüfen
var isValid = JSON.IsValid('{"a":1}')   // true
var isValid2 = JSON.IsValid("{bad}")    // false

// Minify (Leerzeichen entfernen)
var min = JSON.Minify('{ "a" : 1 }')   // {"a":1}
```
