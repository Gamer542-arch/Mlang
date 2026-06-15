# NBT API — tagi NBT

## Parsowanie

```glang
var nbt = NBT.Parse('{Health:20.0f,CustomName:"\\"Steve\\""}')
var nbt = NBT.Parse('{Items:[{id:"minecraft:stone",Count:64b}]}')
```

## Tworzenie

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

## Metody NBTCompound

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `tag.SetString(key, value)` | `void` | Ustaw string |
| `tag.SetInt(key, value)` | `void` | Ustaw int |
| `tag.SetFloat(key, value)` | `void` | Ustaw float |
| `tag.SetDouble(key, value)` | `void` | Ustaw double |
| `tag.SetLong(key, value)` | `void` | Ustaw long |
| `tag.SetBool(key, value)` | `void` | Ustaw bool |
| `tag.SetByte(key, value)` | `void` | Ustaw byte |
| `tag.SetShort(key, value)` | `void` | Ustaw short |
| `tag.SetIntArray(key, value[])` | `void` | Ustaw int array |
| `tag.SetByteArray(key, value[])` | `void` | Ustaw byte array |
| `tag.SetLongArray(key, value[])` | `void` | Ustaw long array |
| `tag.SetStringList(key, value[])` | `void` | Ustaw list stringów |
| `tag.GetString(key)` | `string` | Pobierz string |
| `tag.GetInt(key)` | `int` | Pobierz int |
| `tag.GetFloat(key)` | `float` | Pobierz float |
| `tag.GetDouble(key)` | `double` | Pobierz double |
| `tag.GetBool(key)` | `bool` | Pobierz bool |
| `tag.Get(key)` | `object` | Pobierz dowolny typ |
| `tag.Has(key)` | `bool` | Czy ma klucz |
| `tag.Remove(key)` | `void` | Usuń klucz |
| `tag.Keys()` | `List<string>` | Lista kluczy |
| `tag.Size()` | `int` | Ilość kluczy |
| `tag.IsEmpty()` | `bool` | Czy pusty |
| `tag.Clear()` | `void` | Wyczyść |
| `tag.Merge(other)` | `void` | Scal z innym NBT |
| `tag.Clone()` | `NBTCompound` | Kopiuj |
| `tag.ToString()` | `string` | SNBT format |
| `tag.ToPrettyString()` | `string` | Sformatowany SNBT |

## Użycie z encjami

```glang
// Pobierz NBT encji
var nbt = entity.GetNBT()
entity.SetNBT('{CustomName:"\\"Steve\\""}')
entity.MergeNBT('{CustomNameVisible:1b}')

// Pobierz NBT gracza
var playerNbt = Player.GetNBT()
Player.MergeNBT('{flying:1b}')
```
