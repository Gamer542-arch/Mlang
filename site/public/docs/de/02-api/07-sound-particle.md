# Sound- und Partikel-API

## Sound-API

| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Sound.Play(sound)` | `void` | Sound abspielen (für Absender) |
| `Sound.Play(sound, volume, pitch)` | `void` | Sound mit Parametern |
| `Sound.Play(sound, x, y, z)` | `void` | An Weltposition abspielen |
| `Sound.Play(sound, x, y, z, volume, pitch)` | `void` | Sound an Position |
| `Sound.PlayTo(player, sound)` | `void` | Sound für bestimmten Spieler |
| `Sound.PlayTo(player, sound, volume, pitch)` | `void` | Sound für Spieler mit Parametern |
| `Sound.StopAll()` | `void` | Alle Sounds stoppen |
| `Sound.Stop(sound)` | `void` | Bestimmten Sound stoppen |
| `Sound.StopCategory(category)` | `void` | Kategorie stoppen (master, music, record, weather, blocks, hostile, neutral, players, ambient, voice) |
| `Sound.SetVolume(category, volume)` | `void` | Lautstärke der Kategorie setzen |

### Vordefinierte Sounds
| Methode | Beschreibung |
|--------|------|
| `Sound.PlayLevelUp()` | Level-Up-Sound |
| `Sound.PlayPickup()` | Gegenstand aufheben |
| `Sound.PlayExplosion()` | Explosion |
| `Sound.PlayClick()` | Klick |
| `Sound.PlayDing()` | Ding (Erfolg) |
| `Sound.PlayError()` | Fehler |
| `Sound.PlaySuccess()` | Erfolg |
| `Sound.PlayOrb()` | Erfahrungskugel |
| `Sound.PlayAnvil()` | Amboss |
| `Sound.PlayEnderDragonDeath()` | Drachentod |
| `Sound.PlayWitherSpawn()` | Wither-Spawn |
| `Sound.PlayThunder()` | Donner |
| `Sound.PlayFirework()` | Feuerwerk |
| `Sound.PlayPortal()` | Portal |
| `Sound.PlayBeacon()` | Leuchtfeuer |
| `Sound.PlayNote(inst, note)` | Noten-Sound (Instrument: 0=harp, 1=bd, 2=snare, 3=hat, 4=bass) |

---

## Partikel-API

| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Particle.Spawn(particle, x, y, z)` | `void` | Partikel an Punkt |
| `Particle.Spawn(particle, x, y, z, count)` | `void` | Partikel (Anzahl) |
| `Particle.Spawn(particle, x, y, z, count, spread, speed)` | `void` | Partikel mit Streuung (dx,dy,dz = spread) |
| `Particle.Spawn(particle, x, y, z, count, dx, dy, dz, speed)` | `void` | Volle Streuungskontrolle |
| `Particle.Spawn(particle, x, y, z, count, dx, dy, dz, speed, force)` | `void` | Force = aus der Ferne rendern |
| `Particle.SpawnLine(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Partikellinie |
| `Particle.SpawnCircle(particle, cx, cy, cz, radius, count)` | `void` | Partikelkreis |
| `Particle.SpawnCircle(particle, cx, cy, cz, radius, count, axis)` | `void` | Kreis auf Achse (x/y/z) |
| `Particle.SpawnSphere(particle, cx, cy, cz, radius, count)` | `void` | Partikelkugel |
| `Particle.SpawnHelix(particle, cx, cy, cz, height, turns, count)` | `void` | Spirale/Helix |
| `Particle.SpawnCube(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Gefüllter Würfel |
| `Particle.SpawnCubeOutline(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Würfelkanten |
| `Particle.SpawnCylinder(particle, cx, cy, cz, radius, height, count)` | `void` | Zylinder |
| `Particle.SpawnCone(particle, cx, cy, cz, radius, height, count)` | `void` | Kegel |
| `Particle.SpawnTornado(particle, cx, cy, cz, radius, height, count)` | `void` | Partikeltornado |
| `Particle.SpawnHeart(particle, cx, cy, cz, count)` | `void` | Herzform |

### Partikeltypen
| ID | Beschreibung |
|----|------|
| `"minecraft:flame"` | Flamme |
| `"minecraft:smoke"` | Rauch |
| `"minecraft:large_smoke"` | Großer Rauch |
| `"minecraft:cloud"` | Wolke |
| `"minecraft:crit"` | Kritischer Treffer |
| `"minecraft:enchant"` | Verzauberung |
| `"minecraft:end_rod"` | Endstab-Partikel |
| `"minecraft:heart"` | Herz |
| `"minecraft:anger"` | Wut (Diener) |
| `"minecraft:damage_indicator"` | Schadensanzeige |
| `"minecraft:dragon_breath"` | Drachenatem |
| `"minecraft:dripping_lava"` | Tropfende Lava |
| `"minecraft:dripping_water"` | Tropfendes Wasser |
| `"minecraft:dust"` | Staub (farbig RGB) |
| `"minecraft:effect"` | Effekt (farbig RGB) |
| `"minecraft:elder_guardian"` | Großer Wächter |
| `"minecraft:electric_spark"` | Elektrischer Funke |
| `"minecraft:enchant"` | Verzauberungs-Glyphe |
| `"minecraft:end_rod"` | Endstab |
| `"minecraft:entity_effect"` | Entitätseffekt (farbig) |
| `"minecraft:explosion"` | Explosion |
| `"minecraft:falling_dust"` | Fallender Staub |
| `"minecraft:firework"` | Feuerwerk |
| `"minecraft:fishing"` | Angeln |
| `"minecraft:glow"` | Leuchttintenfisch-Tinte |
| `"minecraft:glow_squid_ink"` | Leuchttintenfisch-Tinte |
| `"minecraft:happy_villager"` | Glücklicher Dorfbewohner |
| `"minecraft:instant_effect"` | Soforteffekt |
| `"minecraft:item"` | Gegenstandssplitter |
| `"minecraft:item_slime"` | Schleim |
| `"minecraft:item_snowball"` | Schneeball |
| `"minecraft:large_smoke"` | Großer Rauch |
| `"minecraft:lava"` | Lava |
| `"minecraft:mycelium"` | Myzel |
| `"minecraft:note"` | Note |
| `"minecraft:poof"` | Puff |
| `"minecraft:portal"` | Portal |
| `"minecraft:rain"` | Regen |
| `"minecraft:sculk_charge"` | Sculk-Ladung |
| `"minecraft:sculk_soul"` | Sculk-Seele |
| `"minecraft:shriek"` | Sculk-Schrei |
| `"minecraft:sneeze"` | Panda-Nieser |
| `"minecraft:snowflake"` | Schneeflocke |
| `"minecraft:sonic_boom"` | Schallwelle (Warden) |
| `"minecraft:soul"` | Seelenfeuer-Flamme |
| `"minecraft:soul_fire_flame"` | Seelenfeuer |
| `"minecraft:spit"` | Lama-Spucke |
| `"minecraft:splash"` | Spritzer |
| `"minecraft:squid_ink"` | Tintenfischtinte |
| `"minecraft:sweep_attack"` | Schwungangriff |
| `"minecraft:totem_of_undying"` | Totem |
| `"minecraft:underwater"` | Unterwasser |
| `"minecraft:witch"` | Hexe |
| `"minecraft:wax_off"` | Wax off |
| `"minecraft:wax_on"` | Wax on |
| `"minecraft:white_ash"` | Weiße Asche |
| `"minecraft:witch"` | Hexe |

### Partikel mit Farbe (RGB)
| Methode | Beschreibung |
|--------|------|
| `Particle.SpawnDust(x, y, z, r, g, b, size)` | Farbiger Staub |
| `Particle.SpawnDust(x, y, z, r, g, b, size, count, spread)` | Farbiger Staub mit Anzahl |
| `Particle.SpawnEffect(x, y, z, r, g, b)` | Farbiger Effekt |
| `Particle.SpawnEntityEffect(x, y, z, r, g, b)` | Farbiger Entitätseffekt |

---

## Beispiele

```glang
// Sounds
Sound.Play("minecraft:entity.player.levelup")
Sound.Play("minecraft:block.anvil.land", 1.0f, 0.5f)
Sound.Play("minecraft:entity.generic.explode", Player.X, Player.Y, Player.Z)
Sound.PlayTo(Player, "minecraft:entity.experience_orb.pickup")
Sound.PlayLevelUp()
Sound.PlayClick()

// Partikel — Grundlagen
Particle.Spawn("minecraft:flame", 100, 64, -200)
Particle.Spawn("minecraft:flame", 100, 64, -200, 20, 0.5f, 0.1f)
Particle.Spawn("minecraft:heart", Player.X, Player.Y + 2, Player.Z, 10, 1.0f, 0.05f)

// Farbiger Staub
Particle.SpawnDust(Player.X, Player.Y, Player.Z, 255, 0, 0, 2.0f, 10, 0.5f)

// Erweiterte Formen
Particle.SpawnCircle("minecraft:flame", Player.X, Player.Y, Player.Z, 2.0f, 30)
Particle.SpawnSphere("minecraft:enchant", Player.X, Player.Y, Player.Z, 3.0f, 50)
Particle.SpawnHelix("minecraft:end_rod", Player.X, Player.Y, Player.Z, 4.0f, 3, 40)
Particle.SpawnTornado("minecraft:cloud", Player.X, Player.Y, Player.Z, 2.0f, 5.0f, 30)
Particle.SpawnHeart("minecraft:heart", Player.X, Player.Y + 3, Player.Z, 15)

// Linie vom Spieler zum Punkt
Particle.SpawnLine("minecraft:flame",
    Player.X, Player.Y, Player.Z,
    200, 64, 0, 5
)

// Kombo: Sound + Partikel
Player.TeleportTo(0, 64, 0)
Sound.Play("minecraft:entity.enderman.teleport")
Particle.Spawn("minecraft:portal", 0, 64, 0, 30, 0.5f, 0.5f)
```
