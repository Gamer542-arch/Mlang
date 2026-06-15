# Item API — full documentation

## ItemStack

### Creating
```glang
// Basic
var item = new ItemStack("minecraft:diamond_sword")
var item = new ItemStack("minecraft:diamond_sword", count: 1)
var item = new ItemStack("minecraft:diamond_sword", count: 1, damage: 0)
var item = new ItemStack("minecraft:diamond_sword", nbt: "{...}")
```

### Basic properties
| Method | Returns | Description |
|--------|--------|------|
| `item.Id` | `string` | Item ID |
| `item.Count` | `int` | Stack size |
| `item.SetCount(int)` | `void` | Set size |
| `item.MaxCount` | `int` | Maximum stack size |
| `item.Damage` | `int` | Damage/durability |
| `item.SetDamage(int)` | `void` | Set durability |
| `item.MaxDamage` | `int` | Maximum durability |
| `item.IsDamaged` | `bool` | Whether damaged |
| `item.IsDamageable` | `bool` | Whether damageable |
| `item.IsEmpty` | `bool` | Whether empty (air) |
| `item.HasTag` | `bool` | Whether has NBT tags |
| `item.GetTag()` | `NBTCompound` | NBT tags |

### Name and lore
| Method | Returns | Description |
|--------|--------|------|
| `item.SetName(string)` | `ItemStack` | Set name (supports colors) |
| `item.GetName()` | `string` | Get name |
| `item.GetDisplayName()` | `string` | Display name (with formatting) |
| `item.AddLore(string)` | `ItemStack` | Add lore line |
| `item.SetLore(string[])` | `ItemStack` | Set entire lore |
| `item.GetLore()` | `string[]` | Get lore |
| `item.ClearLore()` | `void` | Clear lore |

### Enchantments
| Method | Returns | Description |
|--------|--------|------|
| `item.AddEnchant(enchant, level)` | `ItemStack` | Add enchantment |
| `item.RemoveEnchant(enchant)` | `void` | Remove enchantment |
| `item.HasEnchant(enchant)` | `bool` | Whether has enchantment |
| `item.GetEnchantLevel(enchant)` | `int` | Enchantment level |
| `item.GetEnchantments()` | `Dict<string, int>` | All enchantments |
| `item.ClearEnchantments()` | `void` | Clear enchantments |
| `item.CanEnchantWith(enchant)` | `bool` | Whether can be enchanted with |

### Attributes
| Method | Returns | Description |
|--------|--------|------|
| `item.AddAttribute(attribute, name, amount, operation)` | `ItemStack` | Add attribute |
| `item.RemoveAttribute(name)` | `void` | Remove attribute |
| `item.GetAttributes()` | `List<Attribute>` | List of attributes |
| `item.ClearAttributes()` | `void` | Clear attributes |

### NBT
| Method | Returns | Description |
|--------|--------|------|
| `item.GetNBT()` | `string` | NBT as string |
| `item.SetNBT(string)` | `void` | Set NBT |
| `item.MergeNBT(string)` | `void` | Merge NBT |
| `item.SetNBTPath(path, value)` | `void` | Set value at NBT path |
| `item.GetNBTPath(path)` | `object` | Get value from path |

### Flags
| Method | Returns | Description |
|--------|--------|------|
| `item.SetUnbreakable(bool)` | `ItemStack` | Set unbreakable |
| `item.IsUnbreakable` | `bool` | Whether unbreakable |
| `item.HideFlags(bool)` | `ItemStack` | Hide flags (enchantments, attributes etc.) |
| `item.SetCustomModelData(int)` | `ItemStack` | Set custom model data |
| `item.GetCustomModelData()` | `int` | Custom model data |
| `item.SetRepairCost(int)` | `void` | Repair cost |
| `item.GetRepairCost()` | `int` | Repair cost |

### Type checking
| Method | Returns | Description |
|--------|--------|------|
| `item.IsOf(type)` | `bool` | Whether is of the given type |
| `item.IsFood` | `bool` | Whether food |
| `item.IsTool` | `bool` | Whether tool |
| `item.IsArmor` | `bool` | Whether armor |
| `item.IsWeapon` | `bool` | Whether weapon |
| `item.IsBlock` | `bool` | Whether block |
| `item.IsPotion` | `bool` | Whether potion |
| `item.IsEdible` | `bool` | Whether edible |
| `item.IsEnchantable` | `bool` | Whether enchantable |
| `item.IsEnchanted` | `bool` | Whether enchanted |
| `item.IsFireResistant` | `bool` | Whether fire resistant |
| `item.IsStackable` | `bool` | Whether stackable |
| `item.IsDurable` | `bool` | Whether has durability |

### Comparison
| Method | Returns | Description |
|--------|--------|------|
| `item.IsSimilar(other)` | `bool` | Whether same type (ignores count) |
| `item.Equals(other)` | `bool` | Whether identical (including count) |
| `item.Matches(other)` | `bool` | Whether matches (also checks tags) |
| `item.GetHashCode()` | `int` | Hash code |
| `item.ToString()` | `string` | String representation |

### Copying
| Method | Returns | Description |
|--------|--------|------|
| `item.Clone()` | `ItemStack` | Clone item |
| `item.Copy()` | `ItemStack` | Copy item |
| `item.Split(count)` | `ItemStack` | Split stack (returns new) |

---

## Enchantments

### Enchantment list
| ID | Description |
|----|------|
| `"minecraft:sharpness"` | Sharpness |
| `"minecraft:smite"` | Smite |
| `"minecraft:bane_of_arthropods"` | Bane of Arthropods |
| `"minecraft:knockback"` | Knockback |
| `"minecraft:fire_aspect"` | Fire Aspect |
| `"minecraft:looting"` | Looting |
| `"minecraft:sweeping"` | Sweeping Edge |
| `"minecraft:efficiency"` | Efficiency |
| `"minecraft:fortune"` | Fortune |
| `"minecraft:silk_touch"` | Silk Touch |
| `"minecraft:unbreaking"` | Unbreaking |
| `"minecraft:mending"` | Mending |
| `"minecraft:protection"` | Protection |
| `"minecraft:fire_protection"` | Fire Protection |
| `"minecraft:feather_falling"` | Feather Falling |
| `"minecraft:blast_protection"` | Blast Protection |
| `"minecraft:projectile_protection"` | Projectile Protection |
| `"minecraft:respiration"` | Respiration |
| `"minecraft:aqua_affinity"` | Aqua Affinity |
| `"minecraft:depth_strider"` | Depth Strider |
| `"minecraft:soul_speed"` | Soul Speed |
| `"minecraft:swift_sneak"` | Swift Sneak |
| `"minecraft:power"` | Power (bow) |
| `"minecraft:punch"` | Punch (bow) |
| `"minecraft:flame"` | Flame (bow) |
| `"minecraft:infinity"` | Infinity (bow) |
| `"minecraft:lure"` | Lure (fishing rod) |
| `"minecraft:luck_of_the_sea"` | Luck of the Sea |
| `"minecraft:channeling"` | Channeling (trident) |
| `"minecraft:impaling"` | Impaling (trident) |
| `"minecraft:loyalty"` | Loyalty (trident) |
| `"minecraft:riptide"` | Riptide (trident) |
| `"minecraft:multishot"` | Multishot (crossbow) |
| `"minecraft:quick_charge"` | Quick Charge |
| `"minecraft:piercing"` | Piercing |

---

## Attributes

### Attribute list
| ID | Description |
|----|------|
| `"minecraft:generic.max_health"` | Maximum HP |
| `"minecraft:generic.follow_range"` | Follow range |
| `"minecraft:generic.knockback_resistance"` | Knockback resistance |
| `"minecraft:generic.movement_speed"` | Movement speed |
| `"minecraft:generic.flying_speed"` | Flying speed |
| `"minecraft:generic.attack_damage"` | Attack damage |
| `"minecraft:generic.attack_speed"` | Attack speed |
| `"minecraft:generic.armor"` | Armor points |
| `"minecraft:generic.armor_toughness"` | Armor toughness |
| `"minecraft:generic.luck"` | Luck |
| `"minecraft:generic.horse.jump_strength"` | Horse jump strength |
| `"minecraft:generic.scale"` | Entity scale |
| `"minecraft:generic.step_height"` | Step height |
| `"minecraft:player.block_interaction_range"` | Block interaction range |
| `"minecraft:player.entity_interaction_range"` | Entity interaction range |

### Attribute operations
| Operation | Value | Description |
|-----------|-------|------|
| `0` | ADD_NUMBER | Adds value to base |
| `1` | MULTIPLY_BASE | Multiplies base by percentage |
| `2` | MULTIPLY_TOTAL | Multiplies total value |

---

## Examples

```glang
// Create a sword
var sword = new ItemStack("minecraft:diamond_sword")
    .SetName("§6§lStar Sword §r§c[Legend]")
    .AddLore("§7A sword forged from stars")
    .AddLore("§7Deals §c500§7 damage")
    .AddEnchant("sharpness", 10)
    .AddEnchant("unbreaking", 5)
    .AddEnchant("mending", 1)
    .AddEnchant("fire_aspect", 3)
    .SetUnbreakable(true)
    .HideFlags(true)
    .SetCustomModelData(1001)

// Attributes
sword.AddAttribute("generic.attack_damage", "AD", 50.0, 0)

// Give to player
Player.Give(sword)

// Create a special apple
var apple = new ItemStack("minecraft:golden_apple")
    .SetName("§6§lApple of Immortality")
    .AddLore("§aGives REGEN V for 30s")
    .AddLore("§aGives ABSORPTION IV for 2min")
    .SetNBT("{HideFlags:1}")
```
