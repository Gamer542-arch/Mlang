# Item API — pełna dokumentacja

## ItemStack

### Tworzenie
```glang
// Podstawowe
var item = new ItemStack("minecraft:diamond_sword")
var item = new ItemStack("minecraft:diamond_sword", count: 1)
var item = new ItemStack("minecraft:diamond_sword", count: 1, damage: 0)
var item = new ItemStack("minecraft:diamond_sword", nbt: "{...}")
```

### Właściwości podstawowe
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.Id` | `string` | ID przedmiotu |
| `item.Count` | `int` | Ilość w stacku |
| `item.SetCount(int)` | `void` | Ustaw ilość |
| `item.MaxCount` | `int` | Maksymalna ilość w stacku |
| `item.Damage` | `int` | Obrażenia/nakarcie |
| `item.SetDamage(int)` | `void` | Ustaw nakarcie |
| `item.MaxDamage` | `int` | Maksymalne nakarcie |
| `item.IsDamaged` | `bool` | Czy uszkodzony |
| `item.IsDamageable` | `bool` | Czy może być uszkodzony |
| `item.IsEmpty` | `bool` | Czy pusty (air) |
| `item.HasTag` | `bool` | Czy ma tagi NBT |
| `item.GetTag()` | `NBTCompound` | Tagi NBT |

### Nazwa i lore
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.SetName(string)` | `ItemStack` | Ustaw nazwę (wspiera kolory) |
| `item.GetName()` | `string` | Pobierz nazwę |
| `item.GetDisplayName()` | `string` | Wyświetlana nazwa (z formatowaniem) |
| `item.AddLore(string)` | `ItemStack` | Dodaj linię lore |
| `item.SetLore(string[])` | `ItemStack` | Ustaw całe lore |
| `item.GetLore()` | `string[]` | Pobierz lore |
| `item.ClearLore()` | `void` | Wyczyść lore |

### Enchantmenty
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.AddEnchant(enchant, level)` | `ItemStack` | Dodaj enchant |
| `item.RemoveEnchant(enchant)` | `void` | Usuń enchant |
| `item.HasEnchant(enchant)` | `bool` | Czy ma enchant |
| `item.GetEnchantLevel(enchant)` | `int` | Poziom enchantu |
| `item.GetEnchantments()` | `Dict<string, int>` | Wszystkie enchanty |
| `item.ClearEnchantments()` | `void` | Wyczyść enchanty |
| `item.CanEnchantWith(enchant)` | `bool` | Czy można enchantować |

### Atrybuty
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.AddAttribute(attribute, name, amount, operation)` | `ItemStack` | Dodaj atrybut |
| `item.RemoveAttribute(name)` | `void` | Usuń atrybut |
| `item.GetAttributes()` | `List<Attribute>` | Lista atrybutów |
| `item.ClearAttributes()` | `void` | Wyczyść atrybuty |

### NBT
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.GetNBT()` | `string` | NBT jako string |
| `item.SetNBT(string)` | `void` | Ustaw NBT |
| `item.MergeNBT(string)` | `void` | Scal NBT |
| `item.SetNBTPath(path, value)` | `void` | Ustaw wartość w ścieżce NBT |
| `item.GetNBTPath(path)` | `object` | Pobierz wartość ze ścieżki |

### Flagi
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.SetUnbreakable(bool)` | `ItemStack` | Ustaw niezniszczalność |
| `item.IsUnbreakable` | `bool` | Czy niezniszczalny |
| `item.HideFlags(bool)` | `ItemStack` | Ukryj flagi (enchanty, atrybuty itp.) |
| `item.SetCustomModelData(int)` | `ItemStack` | Ustaw custom model data |
| `item.GetCustomModelData()` | `int` | Custom model data |
| `item.SetRepairCost(int)` | `void` | Koszt naprawy |
| `item.GetRepairCost()` | `int` | Koszt naprawy |

### Sprawdzanie typu
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.IsOf(type)` | `bool` | Czy jest danego typu |
| `item.IsFood` | `bool` | Czy jedzenie |
| `item.IsTool` | `bool` | Czy narzędzie |
| `item.IsArmor` | `bool` | Czy armor |
| `item.IsWeapon` | `bool` | Czy broń |
| `item.IsBlock` | `bool` | Czy blok |
| `item.IsPotion` | `bool` | Czy potion |
| `item.IsEdible` | `bool` | Czy zjadliwy |
| `item.IsEnchantable` | `bool` | Czy można enchantować |
| `item.IsEnchanted` | `bool` | Czy enchantowany |
| `item.IsFireResistant` | `bool` | Czy odporny na ogień |
| `item.IsStackable` | `bool` | Czy stackowalny |
| `item.IsDurable` | `bool` | Czy ma trwałość |

### Porównanie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.IsSimilar(other)` | `bool` | Czy taki sam typ (ignoruje count) |
| `item.Equals(other)` | `bool` | Czy identyczny (w tym count) |
| `item.Matches(other)` | `bool` | Czy match (sprawdza też tagi) |
| `item.GetHashCode()` | `int` | Hash code |
| `item.ToString()` | `string` | String reprezentacja |

### Kopiowanie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `item.Clone()` | `ItemStack` | Klonuj przedmiot |
| `item.Copy()` | `ItemStack` | Kopiuj przedmiot |
| `item.Split(count)` | `ItemStack` | Podziel stack (zwraca nowy) |

---

## Enchanty

### Lista enchantów
| ID | Opis |
|----|------|
| `"minecraft:sharpness"` | Ostrość |
| `"minecraft:smite"` | Pogromca nieumarłych |
| `"minecraft:bane_of_arthropods"` | Pogromca stawonogów |
| `"minecraft:knockback"` | Odrzut |
| `"minecraft:fire_aspect"` | Zaklęty ogień |
| `"minecraft:looting"` | Grabienie |
| `"minecraft:sweeping"` | Zamiatanie |
| `"minecraft:efficiency"` | Wydajność |
| `"minecraft:fortune"` | Szczęście |
| `"minecraft:silk_touch"` | Jedwabny dotyk |
| `"minecraft:unbreaking"` | Niezniszczalność |
| `"minecraft:mending"` | Naprawa |
| `"minecraft:protection"` | Ochrona |
| `"minecraft:fire_protection"` | Ochrona przed ogniem |
| `"minecraft:feather_falling"` | Ochrona przed upadkiem |
| `"minecraft:blast_protection"` | Ochrona przed wybuchem |
| `"minecraft:projectile_protection"` | Ochrona przed pociskami |
| `"minecraft:respiration"` | Oddychanie |
| `"minecraft:aqua_affinity"` | Wodna afiniczność |
| `"minecraft:depth_strider"` | Wodny spacer |
| `"minecraft:soul_speed"` | Prędkość dusz |
| `"minecraft:swift_sneak"` | Szybkie skradanie |
| `"minecraft:power"` | Siła (łuk) |
| `"minecraft:punch"` | Odporność (łuk) |
| `"minecraft:flame"` | Płomień (łuk) |
| `"minecraft:infinity"` | Nieskończoność (łuk) |
| `"minecraft:lure"` | Wabik (wędka) |
| `"minecraft:luck_of_the_sea"` | Szczęście morza |
| `"minecraft:channeling"` | Kanałowanie (trójząb) |
| `"minecraft:impaling"` | Przebicie (trójząb) |
| `"minecraft:loyalty"` | Lojalność (trójząb) |
| `"minecraft:riptide"` | Riptide (trójząb) |
| `"minecraft:multishot"` | Wielostrzał (kusza) |
| `"minecraft:quick_charge"` | Szybkie ładowanie |
| `"minecraft:piercing"` | Przeszycie |

---

## Atrybuty

### Lista atrybutów
| ID | Opis |
|----|------|
| `"minecraft:generic.max_health"` | Maksymalne HP |
| `"minecraft:generic.follow_range"` | Zasięg follow |
| `"minecraft:generic.knockback_resistance"` | Odporność na odrzut |
| `"minecraft:generic.movement_speed"` | Prędkość ruchu |
| `"minecraft:generic.flying_speed"` | Prędkość latania |
| `"minecraft:generic.attack_damage"` | Obrażenia ataku |
| `"minecraft:generic.attack_speed"` | Szybkość ataku |
| `"minecraft:generic.armor"` | Punktów ochrony |
| `"minecraft:generic.armor_toughness"` | Wytrzymałość ochrony |
| `"minecraft:generic.luck"` | Szczęście |
| `"minecraft:generic.horse.jump_strength"` | Siła skoku konia |
| `"minecraft:generic.scale"` | Skala encji |
| `"minecraft:generic.step_height"` | Wysokość kroku |
| `"minecraft:player.block_interaction_range"` | Zasięg interakcji |
| `"minecraft:player.entity_interaction_range"` | Zasięg interakcji z encją |

### Operacje atrybutów
| Operacja | Wartość | Opis |
|----------|---------|------|
| `0` | ADD_NUMBER | Dodaje wartość do bazy |
| `1` | MULTIPLY_BASE | Mnoży bazę o procent |
| `2` | MULTIPLY_TOTAL | Mnoży całkowitą wartość |

---

## Przykłady

```glang
// Stwórz miecz
var sword = new ItemStack("minecraft:diamond_sword")
    .SetName("§6§lMiecz Gwiezdny §r§c[Legenda]")
    .AddLore("§7Miecz wykuty z gwiazd")
    .AddLore("§7Zadaje §c500§7 obrażeń")
    .AddEnchant("sharpness", 10)
    .AddEnchant("unbreaking", 5)
    .AddEnchant("mending", 1)
    .AddEnchant("fire_aspect", 3)
    .SetUnbreakable(true)
    .HideFlags(true)
    .SetCustomModelData(1001)

// Atrybuty
sword.AddAttribute("generic.attack_damage", "AD", 50.0, 0)

// Daj graczowi
Player.Give(sword)

// Stwórz specjalne jabłko
var apple = new ItemStack("minecraft:golden_apple")
    .SetName("§6§lJabłko Nieśmiertelności")
    .AddLore("§aDaje REGEN V na 30s")
    .AddLore("§aDaje ABSORPTION IV na 2min")
    .SetNBT("{HideFlags:1}")
```
