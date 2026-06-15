# Item API — vollständige Dokumentation

## ItemStack

### Erstellung
```glang
// Grundlegend
var item = new ItemStack("minecraft:diamond_sword")
var item = new ItemStack("minecraft:diamond_sword", count: 1)
var item = new ItemStack("minecraft:diamond_sword", count: 1, damage: 0)
var item = new ItemStack("minecraft:diamond_sword", nbt: "{...}")
```

### Grundlegende Eigenschaften
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.Id` | `string` | Gegenstands-ID |
| `item.Count` | `int` | Anzahl im Stack |
| `item.SetCount(int)` | `void` | Anzahl setzen |
| `item.MaxCount` | `int` | Maximale Anzahl im Stack |
| `item.Damage` | `int` | Schaden/Haltbarkeit |
| `item.SetDamage(int)` | `void` | Haltbarkeit setzen |
| `item.MaxDamage` | `int` | Maximale Haltbarkeit |
| `item.IsDamaged` | `bool` | Ist beschädigt |
| `item.IsDamageable` | `bool` | Kann beschädigt werden |
| `item.IsEmpty` | `bool` | Ist leer (air) |
| `item.HasTag` | `bool` | Hat NBT-Tags |
| `item.GetTag()` | `NBTCompound` | NBT-Tags |

### Name und Lore
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.SetName(string)` | `ItemStack` | Name setzen (unterstützt Farben) |
| `item.GetName()` | `string` | Namen abrufen |
| `item.GetDisplayName()` | `string` | Anzeigename (mit Formatierung) |
| `item.AddLore(string)` | `ItemStack` | Lore-Zeile hinzufügen |
| `item.SetLore(string[])` | `ItemStack` | Gesamtes Lore setzen |
| `item.GetLore()` | `string[]` | Lore abrufen |
| `item.ClearLore()` | `void` | Lore löschen |

### Verzauberungen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.AddEnchant(enchant, level)` | `ItemStack` | Verzauberung hinzufügen |
| `item.RemoveEnchant(enchant)` | `void` | Verzauberung entfernen |
| `item.HasEnchant(enchant)` | `bool` | Hat Verzauberung |
| `item.GetEnchantLevel(enchant)` | `int` | Verzauberungsstufe |
| `item.GetEnchantments()` | `Dict<string, int>` | Alle Verzauberungen |
| `item.ClearEnchantments()` | `void` | Verzauberungen löschen |
| `item.CanEnchantWith(enchant)` | `bool` | Kann verzaubert werden |

### Attribute
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.AddAttribute(attribute, name, amount, operation)` | `ItemStack` | Attribut hinzufügen |
| `item.RemoveAttribute(name)` | `void` | Attribut entfernen |
| `item.GetAttributes()` | `List<Attribute>` | Attributliste |
| `item.ClearAttributes()` | `void` | Attribute löschen |

### NBT
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.GetNBT()` | `string` | NBT als String |
| `item.SetNBT(string)` | `void` | NBT setzen |
| `item.MergeNBT(string)` | `void` | NBT zusammenführen |
| `item.SetNBTPath(path, value)` | `void` | Wert im NBT-Pfad setzen |
| `item.GetNBTPath(path)` | `object` | Wert aus Pfad abrufen |

### Flags
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.SetUnbreakable(bool)` | `ItemStack` | Unzerstörbarkeit setzen |
| `item.IsUnbreakable` | `bool` | Ist unzerstörbar |
| `item.HideFlags(bool)` | `ItemStack` | Flags verstecken (Verzauberungen, Attribute usw.) |
| `item.SetCustomModelData(int)` | `ItemStack` | Custom Model Data setzen |
| `item.GetCustomModelData()` | `int` | Custom Model Data |
| `item.SetRepairCost(int)` | `void` | Reparaturkosten |
| `item.GetRepairCost()` | `int` | Reparaturkosten |

### Typprüfung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.IsOf(type)` | `bool` | Ist vom Typ |
| `item.IsFood` | `bool` | Ist Essen |
| `item.IsTool` | `bool` | Ist Werkzeug |
| `item.IsArmor` | `bool` | Ist Rüstung |
| `item.IsWeapon` | `bool` | Ist Waffe |
| `item.IsBlock` | `bool` | Ist Block |
| `item.IsPotion` | `bool` | Ist Trank |
| `item.IsEdible` | `bool` | Ist essbar |
| `item.IsEnchantable` | `bool` | Ist verzauberbar |
| `item.IsEnchanted` | `bool` | Ist verzaubert |
| `item.IsFireResistant` | `bool` | Ist feuerfest |
| `item.IsStackable` | `bool` | Ist stapelbar |
| `item.IsDurable` | `bool` | Hat Haltbarkeit |

### Vergleich
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.IsSimilar(other)` | `bool` | Gleicher Typ (ignoriert Anzahl) |
| `item.Equals(other)` | `bool` | Ist identisch (inkl. Anzahl) |
| `item.Matches(other)` | `bool` | Übereinstimmung (prüft auch Tags) |
| `item.GetHashCode()` | `int` | Hash-Code |
| `item.ToString()` | `string` | String-Darstellung |

### Kopieren
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `item.Clone()` | `ItemStack` | Gegenstand klonen |
| `item.Copy()` | `ItemStack` | Gegenstand kopieren |
| `item.Split(count)` | `ItemStack` | Stack teilen (gibt neuen zurück) |

---

## Verzauberungen

### Verzauberungsliste
| ID | Beschreibung |
|----|------|
| `"minecraft:sharpness"` | Schärfe |
| `"minecraft:smite"` | Heimsuchung |
| `"minecraft:bane_of_arthropods"` | Nemesis der Gliederfüßer |
| `"minecraft:knockback"` | Rückstoß |
| `"minecraft:fire_aspect"` | Verbrennung |
| `"minecraft:looting"` | Plünderung |
| `"minecraft:sweeping"` | Schwungkraft |
| `"minecraft:efficiency"` | Effizienz |
| `"minecraft:fortune"` | Glück |
| `"minecraft:silk_touch"` | Behutsamkeit |
| `"minecraft:unbreaking"` | Haltbarkeit |
| `"minecraft:mending"` | Reparatur |
| `"minecraft:protection"` | Schutz |
| `"minecraft:fire_protection"` | Feuerschutz |
| `"minecraft:feather_falling"` | Federfall |
| `"minecraft:blast_protection"` | Explosionsschutz |
| `"minecraft:projectile_protection"` | Schusssicher |
| `"minecraft:respiration"` | Atmung |
| `"minecraft:aqua_affinity"` | Wasseraffinität |
| `"minecraft:depth_strider"` | Wasserläufer |
| `"minecraft:soul_speed"` | Seelenläufer |
| `"minecraft:swift_sneak"` | Huschen |
| `"minecraft:power"` | Stärke (Bogen) |
| `"minecraft:punch"` | Schlag (Bogen) |
| `"minecraft:flame"` | Flamme (Bogen) |
| `"minecraft:infinity"` | Unendlichkeit (Bogen) |
| `"minecraft:lure"` | Köder (Angel) |
| `"minecraft:luck_of_the_sea"` | Glück des Meeres |
| `"minecraft:channeling"` | Entladung (Dreizack) |
| `"minecraft:impaling"` | Harpune (Dreizack) |
| `"minecraft:loyalty"` | Treue (Dreizack) |
| `"minecraft:riptide"` | Sog (Dreizack) |
| `"minecraft:multishot"` | Mehrfachschuss (Armbrust) |
| `"minecraft:quick_charge"` | Schnellladen |
| `"minecraft:piercing"` | Durchschuss |

---

## Attribute

### Attributliste
| ID | Beschreibung |
|----|------|
| `"minecraft:generic.max_health"` | Maximales HP |
| `"minecraft:generic.follow_range"` | Folgereichweite |
| `"minecraft:generic.knockback_resistance"` | Rückstoßwiderstand |
| `"minecraft:generic.movement_speed"` | Bewegungsgeschwindigkeit |
| `"minecraft:generic.flying_speed"` | Fluggeschwindigkeit |
| `"minecraft:generic.attack_damage"` | Angriffsschaden |
| `"minecraft:generic.attack_speed"` | Angriffsgeschwindigkeit |
| `"minecraft:generic.armor"` | Rüstungspunkte |
| `"minecraft:generic.armor_toughness"` | Rüstungshärte |
| `"minecraft:generic.luck"` | Glück |
| `"minecraft:generic.horse.jump_strength"` | Sprungstärke des Pferdes |
| `"minecraft:generic.scale"` | Entitätsskalierung |
| `"minecraft:generic.step_height"` | Schritthöhe |
| `"minecraft:player.block_interaction_range"` | Interaktionsreichweite |
| `"minecraft:player.entity_interaction_range"` | Entitätsinteraktionsreichweite |

### Attributoperationen
| Operation | Wert | Beschreibung |
|----------|---------|------|
| `0` | ADD_NUMBER | Addiert Wert zur Basis |
| `1` | MULTIPLY_BASE | Multipliziert Basis um Prozent |
| `2` | MULTIPLY_TOTAL | Multipliziert Gesamtwert |

---

## Beispiele

```glang
// Schwert erstellen
var sword = new ItemStack("minecraft:diamond_sword")
    .SetName("§6§lSternenschwert §r§c[Legende]")
    .AddLore("§7Ein aus Sternen geschmiedetes Schwert")
    .AddLore("§7Verursacht §c500§7 Schaden")
    .AddEnchant("sharpness", 10)
    .AddEnchant("unbreaking", 5)
    .AddEnchant("mending", 1)
    .AddEnchant("fire_aspect", 3)
    .SetUnbreakable(true)
    .HideFlags(true)
    .SetCustomModelData(1001)

// Attribute
sword.AddAttribute("generic.attack_damage", "AD", 50.0, 0)

// Spieler geben
Player.Give(sword)

// Speziellen Apfel erstellen
var apple = new ItemStack("minecraft:golden_apple")
    .SetName("§6§lApfel der Unsterblichkeit")
    .AddLore("§aGibt REGEN V für 30s")
    .AddLore("§aGibt ABSORPTION IV für 2min")
    .SetNBT("{HideFlags:1}")
```
