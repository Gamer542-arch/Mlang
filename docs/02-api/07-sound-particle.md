# Sound API — pełna dokumentacja

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Sound.Play(sound)` | `void` | Odtwórz dźwięk (dla nadawcy) |
| `Sound.Play(sound, volume, pitch)` | `void` | Dźwięk z parametrami |
| `Sound.Play(sound, x, y, z)` | `void` | Odtwórz w pozycji świata |
| `Sound.Play(sound, x, y, z, volume, pitch)` | `void` | Dźwięk w pozycji |
| `Sound.PlayTo(player, sound)` | `void` | Dźwięk dla konkretnego gracza |
| `Sound.PlayTo(player, sound, volume, pitch)` | `void` | Dźwięk dla gracza z parametrami |
| `Sound.StopAll()` | `void` | Zatrzymaj wszystkie dźwięki |
| `Sound.Stop(sound)` | `void` | Zatrzymaj konkretny dźwięk |
| `Sound.StopCategory(category)` | `void` | Zatrzymaj kategorię (master, music, record, weather, blocks, hostile, neutral, players, ambient, voice) |
| `Sound.SetVolume(category, volume)` | `void` | Ustaw głośność kategorii |

### Predefiniowane dźwięki
| Metoda | Opis |
|--------|------|
| `Sound.PlayLevelUp()` | Dźwięk level up |
| `Sound.PlayPickup()` | Podniesienie przedmiotu |
| `Sound.PlayExplosion()` | Eksplozja |
| `Sound.PlayClick()` | Kliknięcie |
| `Sound.PlayDing()` | Ding (achievement) |
| `Sound.PlayError()` | Błąd |
| `Sound.PlaySuccess()` | Sukces |
| `Sound.PlayOrb()` | Experience orb |
| `Sound.PlayAnvil()` | Kowadło |
| `Sound.PlayEnderDragonDeath()` | Śmierć smoka |
| `Sound.PlayWitherSpawn()` | Spawn withera |
| `Sound.PlayThunder()` | Piorun |
| `Sound.PlayFirework()` | Fajerwerk |
| `Sound.PlayPortal()` | Portal |
| `Sound.PlayBeacon()` | Beacon |
| `Sound.PlayNote(inst, note)` | Dźwięk nota (instrument: 0=harp, 1=bd, 2=snare, 3=hat, 4=bass) |

---

# Particle API — pełna dokumentacja

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Particle.Spawn(particle, x, y, z)` | `void` | Cząsteczka w punkcie |
| `Particle.Spawn(particle, x, y, z, count)` | `void` | Cząsteczki (ilość) |
| `Particle.Spawn(particle, x, y, z, count, spread, speed)` | `void` | Cząsteczki ze spreadem (dx,dy,dz = spread) |
| `Particle.Spawn(particle, x, y, z, count, dx, dy, dz, speed)` | `void` | Pełna kontrola spreadu |
| `Particle.Spawn(particle, x, y, z, count, dx, dy, dz, speed, force)` | `void` | Force = renderuj z daleka |
| `Particle.SpawnLine(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Linia cząsteczek |
| `Particle.SpawnCircle(particle, cx, cy, cz, radius, count)` | `void` | Okrąg cząsteczek |
| `Particle.SpawnCircle(particle, cx, cy, cz, radius, count, axis)` | `void` | Okrąg na osi (x/y/z) |
| `Particle.SpawnSphere(particle, cx, cy, cz, radius, count)` | `void` | Kula cząsteczek |
| `Particle.SpawnHelix(particle, cx, cy, cz, height, turns, count)` | `void` | Spirala/helisa |
| `Particle.SpawnCube(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Sześcian wypełniony |
| `Particle.SpawnCubeOutline(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Krawędzie sześcianu |
| `Particle.SpawnCylinder(particle, cx, cy, cz, radius, height, count)` | `void` | Walec |
| `Particle.SpawnCone(particle, cx, cy, cz, radius, height, count)` | `void` | Stożek |
| `Particle.SpawnTornado(particle, cx, cy, cz, radius, height, count)` | `void` | Tornado cząsteczek |
| `Particle.SpawnHeart(particle, cx, cy, cz, count)` | `void` | Kształt serca |

### Typy particle
| ID | Opis |
|----|------|
| `"minecraft:flame"` | Płomień |
| `"minecraft:smoke"` | Dym |
| `"minecraft:large_smoke"` | Duży dym |
| `"minecraft:cloud"` | Chmura |
| `"minecraft:crit"` | Krytyczne uderzenie |
| `"minecraft:enchant"` | Enchant |
| `"minecraft:end_rod"` | End rod cząsteczka |
| `"minecraft:heart"` | Serce |
| `"minecraft:anger"` | Gniew (vindicator) |
| `"minecraft:damage_indicator"` | Wskaźnik obrażeń |
| `"minecraft:dragon_breath"` | Oddech smoka |
| `"minecraft:dripping_lava"` | Kapiąca lawa |
| `"minecraft:dripping_water"` | Kapiąca woda |
| `"minecraft:dust"` | Pył (kolorowy RGB) |
| `"minecraft:effect"` | Efekt (kolorowy RGB) |
| `"minecraft:elder_guardian"` | Elder guardian |
| `"minecraft:electric_spark"` | Iskra elektryczna |
| `"minecraft:enchant"` | Enchant glyph |
| `"minecraft:end_rod"` | End rod |
| `"minecraft:entity_effect"` | Efekt encji (kolorowy) |
| `"minecraft:explosion"` | Eksplozja |
| `"minecraft:falling_dust"` | Spadający pył |
| `"minecraft:firework"` | Fajerwerk |
| `"minecraft:fishing"` | Wędkowanie |
| `"minecraft:glow"` | Glow ink |
| `"minecraft:glow_squid_ink"` | Tusz świecącej kałamarnicy |
| `"minecraft:happy_villager"` | Szczęśliwy villager |
| `"minecraft:instant_effect"` | Natychmiastowy efekt |
| `"minecraft:item"` | Item crack |
| `"minecraft:item_slime"` | Slime |
| `"minecraft:item_snowball"` | Śnieżka |
| `"minecraft:large_smoke"` | Duży dym |
| `"minecraft:lava"` | Lawa |
| `"minecraft:mycelium"` | Mycelium |
| `"minecraft:note"` | Nutka |
| `"minecraft:poof"` | Puff |
| `"minecraft:portal"` | Portal |
| `"minecraft:rain"` | Deszcz |
| `"minecraft:sculk_charge"` | Sculk charge |
| `"minecraft:sculk_soul"` | Sculk soul |
| `"minecraft:shriek"` | Sculk shriek |
| `"minecraft:sneeze"` | Kichnięcie pandy |
| `"minecraft:snowflake"` | Płatek śniegu |
| `"minecraft:sonic_boom"` | Sonic boom (warden) |
| `"minecraft:soul"` | Soul fire flame |
| `"minecraft:soul_fire_flame"` | Soul fire |
| `"minecraft:spit"` | Plucie lamy |
| `"minecraft:splash"` | Plusk |
| `"minecraft:squid_ink"` | Tusz kałamarnicy |
| `"minecraft:sweep_attack"` | Zamiatanie |
| `"minecraft:totem_of_undying"` | Totem |
| `"minecraft:underwater"` | Podwodny |
| `"minecraft:witch"` | Czarownica |
| `"minecraft:wax_off"` | Wax off |
| `"minecraft:wax_on"` | Wax on |
| `"minecraft:white_ash"` | Biały popiół |
| `"minecraft:witch"` | Witch |

### Particle z kolorem (RGB)
| Metoda | Opis |
|--------|------|
| `Particle.SpawnDust(x, y, z, r, g, b, size)` | Kolorowy pył |
| `Particle.SpawnDust(x, y, z, r, g, b, size, count, spread)` | Kolorowy pył z ilością |
| `Particle.SpawnEffect(x, y, z, r, g, b)` | Kolorowy efekt |
| `Particle.SpawnEntityEffect(x, y, z, r, g, b)` | Kolorowy efekt encji |

---

## Przykłady

```glang
// Dźwięki
Sound.Play("minecraft:entity.player.levelup")
Sound.Play("minecraft:block.anvil.land", 1.0f, 0.5f)
Sound.Play("minecraft:entity.generic.explode", Player.X, Player.Y, Player.Z)
Sound.PlayTo(Player, "minecraft:entity.experience_orb.pickup")
Sound.PlayLevelUp()
Sound.PlayClick()

// Cząsteczki — podstawowe
Particle.Spawn("minecraft:flame", 100, 64, -200)
Particle.Spawn("minecraft:flame", 100, 64, -200, 20, 0.5f, 0.1f)
Particle.Spawn("minecraft:heart", Player.X, Player.Y + 2, Player.Z, 10, 1.0f, 0.05f)

// Kolorowy pył
Particle.SpawnDust(Player.X, Player.Y, Player.Z, 255, 0, 0, 2.0f, 10, 0.5f)

// Zaawansowane kształty
Particle.SpawnCircle("minecraft:flame", Player.X, Player.Y, Player.Z, 2.0f, 30)
Particle.SpawnSphere("minecraft:enchant", Player.X, Player.Y, Player.Z, 3.0f, 50)
Particle.SpawnHelix("minecraft:end_rod", Player.X, Player.Y, Player.Z, 4.0f, 3, 40)
Particle.SpawnTornado("minecraft:cloud", Player.X, Player.Y, Player.Z, 2.0f, 5.0f, 30)
Particle.SpawnHeart("minecraft:heart", Player.X, Player.Y + 3, Player.Z, 15)

// Linia od gracza do punktu
Particle.SpawnLine("minecraft:flame",
    Player.X, Player.Y, Player.Z,
    200, 64, 0, 5
)

// Kombo: dźwięk + particle
Player.TeleportTo(0, 64, 0)
Sound.Play("minecraft:entity.enderman.teleport")
Particle.Spawn("minecraft:portal", 0, 64, 0, 30, 0.5f, 0.5f)
```
