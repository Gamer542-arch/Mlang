# NBT-API

## Parsen

```glang
var nbt = NBT.Parse('{Health:20.0f,CustomName:"\\"Steve\\""}')
var nbt = NBT.Parse('{Items:[{id:"minecraft:stone",Count:64b}]}')
```

## Erstellen

```glang
var tag = new NBTCompound()
tag.SetFloat("Health", 20.0)
tag.SetString("CustomName", "Mój Mob")
tag.SetInt("Age", 0)
tag.SetBool("Invisible", true)
tag.SetDouble("Speed", 1.5)
tag.SetIntArray("Pos", [0, 64, 0])
tag.SetStringList("Lore", ["Linia 1", "Linia 2"])
```

## Methoden von NBTCompound

| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `tag.SetString(key, value)` | `void` | String setzen |
| `tag.SetInt(key, value)` | `void` | Int setzen |
| `tag.SetFloat(key, value)` | `void` | Float setzen |
| `tag.SetDouble(key, value)` | `void` | Double setzen |
| `tag.SetLong(key, value)` | `void` | Long setzen |
| `tag.SetBool(key, value)` | `void` | Bool setzen |
| `tag.SetByte(key, value)` | `void` | Byte setzen |
| `tag.SetShort(key, value)` | `void` | Short setzen |
| `tag.SetIntArray(key, value[])` | `void` | Int-Array setzen |
| `tag.SetByteArray(key, value[])` | `void` | Byte-Array setzen |
| `tag.SetLongArray(key, value[])` | `void` | Long-Array setzen |
| `tag.SetStringList(key, value[])` | `void` | String-Liste setzen |
| `tag.GetString(key)` | `string` | String abrufen |
| `tag.GetInt(key)` | `int` | Int abrufen |
| `tag.GetFloat(key)` | `float` | Float abrufen |
| `tag.GetDouble(key)` | `double` | Double abrufen |
| `tag.GetBool(key)` | `bool` | Bool abrufen |
| `tag.Get(key)` | `object` | Beliebigen Typ abrufen |
| `tag.Has(key)` | `bool` | Hat Schlüssel |
| `tag.Remove(key)` | `void` | Schlüssel entfernen |
| `tag.Keys()` | `List<string>` | Liste der Schlüssel |
| `tag.Size()` | `int` | Anzahl der Schlüssel |
| `tag.IsEmpty()` | `bool` | Ist leer |
| `tag.Clear()` | `void` | Leeren |
| `tag.Merge(other)` | `void` | Mit anderem NBT zusammenführen |
| `tag.Clone()` | `NBTCompound` | Kopieren |
| `tag.ToString()` | `string` | SNBT-Format |
| `tag.ToPrettyString()` | `string` | Formatiertes SNBT |

## Verwendung mit Entitäten

```glang
// NBT der Entität abrufen
var nbt = entity.GetNBT()
entity.SetNBT('{CustomName:"\\"Steve\\""}')
entity.MergeNBT('{CustomNameVisible:1b}')

// NBT des Spielers abrufen
var playerNbt = Player.GetNBT()
Player.MergeNBT('{flying:1b}')
```
