# NBT API

## Parsing

```glang
var nbt = NBT.Parse('{Health:20.0f,CustomName:"\\"Steve\\""}')
var nbt = NBT.Parse('{Items:[{id:"minecraft:stone",Count:64b}]}')
```

## Creating

```glang
var tag = new NBTCompound()
tag.SetFloat("Health", 20.0)
tag.SetString("CustomName", "My Mob")
tag.SetInt("Age", 0)
tag.SetBool("Invisible", true)
tag.SetDouble("Speed", 1.5)
tag.SetIntArray("Pos", [0, 64, 0])
tag.SetStringList("Lore", ["Line 1", "Line 2"])
```

## NBTCompound Methods

| Method | Returns | Description |
|--------|--------|------|
| `tag.SetString(key, value)` | `void` | Set string |
| `tag.SetInt(key, value)` | `void` | Set int |
| `tag.SetFloat(key, value)` | `void` | Set float |
| `tag.SetDouble(key, value)` | `void` | Set double |
| `tag.SetLong(key, value)` | `void` | Set long |
| `tag.SetBool(key, value)` | `void` | Set bool |
| `tag.SetByte(key, value)` | `void` | Set byte |
| `tag.SetShort(key, value)` | `void` | Set short |
| `tag.SetIntArray(key, value[])` | `void` | Set int array |
| `tag.SetByteArray(key, value[])` | `void` | Set byte array |
| `tag.SetLongArray(key, value[])` | `void` | Set long array |
| `tag.SetStringList(key, value[])` | `void` | Set string list |
| `tag.GetString(key)` | `string` | Get string |
| `tag.GetInt(key)` | `int` | Get int |
| `tag.GetFloat(key)` | `float` | Get float |
| `tag.GetDouble(key)` | `double` | Get double |
| `tag.GetBool(key)` | `bool` | Get bool |
| `tag.Get(key)` | `object` | Get any type |
| `tag.Has(key)` | `bool` | Whether has key |
| `tag.Remove(key)` | `void` | Remove key |
| `tag.Keys()` | `List<string>` | List of keys |
| `tag.Size()` | `int` | Number of keys |
| `tag.IsEmpty()` | `bool` | Whether empty |
| `tag.Clear()` | `void` | Clear |
| `tag.Merge(other)` | `void` | Merge with another NBT |
| `tag.Clone()` | `NBTCompound` | Copy |
| `tag.ToString()` | `string` | SNBT format |
| `tag.ToPrettyString()` | `string` | Formatted SNBT |

## Usage with entities

```glang
// Get entity NBT
var nbt = entity.GetNBT()
entity.SetNBT('{CustomName:"\\"Steve\\""}')
entity.MergeNBT('{CustomNameVisible:1b}')

// Get player NBT
var playerNbt = Player.GetNBT()
Player.MergeNBT('{flying:1b}')
```
