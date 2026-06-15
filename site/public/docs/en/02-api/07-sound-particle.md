# Sound and Particle API

## Sound API

| Method | Returns | Description |
|--------|--------|------|
| `Sound.Play(sound)` | `void` | Play sound (for sender) |
| `Sound.Play(sound, volume, pitch)` | `void` | Sound with parameters |
| `Sound.Play(sound, x, y, z)` | `void` | Play at world position |
| `Sound.Play(sound, x, y, z, volume, pitch)` | `void` | Sound at position |
| `Sound.PlayTo(player, sound)` | `void` | Sound for specific player |
| `Sound.PlayTo(player, sound, volume, pitch)` | `void` | Sound for player with parameters |
| `Sound.StopAll()` | `void` | Stop all sounds |
| `Sound.Stop(sound)` | `void` | Stop specific sound |
| `Sound.StopCategory(category)` | `void` | Stop category (master, music, record, weather, blocks, hostile, neutral, players, ambient, voice) |
| `Sound.SetVolume(category, volume)` | `void` | Set category volume |

### Predefined sounds
| Method | Description |
|--------|------|
| `Sound.PlayLevelUp()` | Level up sound |
| `Sound.PlayPickup()` | Item pickup |
| `Sound.PlayExplosion()` | Explosion |
| `Sound.PlayClick()` | Click |
| `Sound.PlayDing()` | Ding (achievement) |
| `Sound.PlayError()` | Error |
| `Sound.PlaySuccess()` | Success |
| `Sound.PlayOrb()` | Experience orb |
| `Sound.PlayAnvil()` | Anvil |
| `Sound.PlayEnderDragonDeath()` | Ender dragon death |
| `Sound.PlayWitherSpawn()` | Wither spawn |
| `Sound.PlayThunder()` | Thunder |
| `Sound.PlayFirework()` | Firework |
| `Sound.PlayPortal()` | Portal |
| `Sound.PlayBeacon()` | Beacon |
| `Sound.PlayNote(inst, note)` | Note sound (instrument: 0=harp, 1=bd, 2=snare, 3=hat, 4=bass) |

---

## Particle API

| Method | Returns | Description |
|--------|--------|------|
| `Particle.Spawn(particle, x, y, z)` | `void` | Particle at point |
| `Particle.Spawn(particle, x, y, z, count)` | `void` | Particles (count) |
| `Particle.Spawn(particle, x, y, z, count, spread, speed)` | `void` | Particles with spread (dx,dy,dz = spread) |
| `Particle.Spawn(particle, x, y, z, count, dx, dy, dz, speed)` | `void` | Full spread control |
| `Particle.Spawn(particle, x, y, z, count, dx, dy, dz, speed, force)` | `void` | Force = render from afar |
| `Particle.SpawnLine(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Particle line |
| `Particle.SpawnCircle(particle, cx, cy, cz, radius, count)` | `void` | Particle circle |
| `Particle.SpawnCircle(particle, cx, cy, cz, radius, count, axis)` | `void` | Circle on axis (x/y/z) |
| `Particle.SpawnSphere(particle, cx, cy, cz, radius, count)` | `void` | Particle sphere |
| `Particle.SpawnHelix(particle, cx, cy, cz, height, turns, count)` | `void` | Spiral/helix |
| `Particle.SpawnCube(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Filled cube |
| `Particle.SpawnCubeOutline(particle, x1, y1, z1, x2, y2, z2, density)` | `void` | Cube edges |
| `Particle.SpawnCylinder(particle, cx, cy, cz, radius, height, count)` | `void` | Cylinder |
| `Particle.SpawnCone(particle, cx, cy, cz, radius, height, count)` | `void` | Cone |
| `Particle.SpawnTornado(particle, cx, cy, cz, radius, height, count)` | `void` | Particle tornado |
| `Particle.SpawnHeart(particle, cx, cy, cz, count)` | `void` | Heart shape |

### Particle types
| ID | Description |
|----|------|
| `"minecraft:flame"` | Flame |
| `"minecraft:smoke"` | Smoke |
| `"minecraft:large_smoke"` | Large smoke |
| `"minecraft:cloud"` | Cloud |
| `"minecraft:crit"` | Critical hit |
| `"minecraft:enchant"` | Enchant |
| `"minecraft:end_rod"` | End rod particle |
| `"minecraft:heart"` | Heart |
| `"minecraft:anger"` | Anger (vindicator) |
| `"minecraft:damage_indicator"` | Damage indicator |
| `"minecraft:dragon_breath"` | Dragon breath |
| `"minecraft:dripping_lava"` | Dripping lava |
| `"minecraft:dripping_water"` | Dripping water |
| `"minecraft:dust"` | Dust (colored RGB) |
| `"minecraft:effect"` | Effect (colored RGB) |
| `"minecraft:elder_guardian"` | Elder guardian |
| `"minecraft:electric_spark"` | Electric spark |
| `"minecraft:enchant"` | Enchant glyph |
| `"minecraft:end_rod"` | End rod |
| `"minecraft:entity_effect"` | Entity effect (colored) |
| `"minecraft:explosion"` | Explosion |
| `"minecraft:falling_dust"` | Falling dust |
| `"minecraft:firework"` | Firework |
| `"minecraft:fishing"` | Fishing |
| `"minecraft:glow"` | Glow ink |
| `"minecraft:glow_squid_ink"` | Glow squid ink |
| `"minecraft:happy_villager"` | Happy villager |
| `"minecraft:instant_effect"` | Instant effect |
| `"minecraft:item"` | Item crack |
| `"minecraft:item_slime"` | Slime |
| `"minecraft:item_snowball"` | Snowball |
| `"minecraft:large_smoke"` | Large smoke |
| `"minecraft:lava"` | Lava |
| `"minecraft:mycelium"` | Mycelium |
| `"minecraft:note"` | Note |
| `"minecraft:poof"` | Puff |
| `"minecraft:portal"` | Portal |
| `"minecraft:rain"` | Rain |
| `"minecraft:sculk_charge"` | Sculk charge |
| `"minecraft:sculk_soul"` | Sculk soul |
| `"minecraft:shriek"` | Sculk shriek |
| `"minecraft:sneeze"` | Panda sneeze |
| `"minecraft:snowflake"` | Snowflake |
| `"minecraft:sonic_boom"` | Sonic boom (warden) |
| `"minecraft:soul"` | Soul fire flame |
| `"minecraft:soul_fire_flame"` | Soul fire |
| `"minecraft:spit"` | Llama spit |
| `"minecraft:splash"` | Splash |
| `"minecraft:squid_ink"` | Squid ink |
| `"minecraft:sweep_attack"` | Sweeping |
| `"minecraft:totem_of_undying"` | Totem |
| `"minecraft:underwater"` | Underwater |
| `"minecraft:witch"` | Witch |
| `"minecraft:wax_off"` | Wax off |
| `"minecraft:wax_on"` | Wax on |
| `"minecraft:white_ash"` | White ash |
| `"minecraft:witch"` | Witch |

### Colored particles (RGB)
| Method | Description |
|--------|------|
| `Particle.SpawnDust(x, y, z, r, g, b, size)` | Colored dust |
| `Particle.SpawnDust(x, y, z, r, g, b, size, count, spread)` | Colored dust with count |
| `Particle.SpawnEffect(x, y, z, r, g, b)` | Colored effect |
| `Particle.SpawnEntityEffect(x, y, z, r, g, b)` | Colored entity effect |

---

## Examples

```glang
// Sounds
Sound.Play("minecraft:entity.player.levelup")
Sound.Play("minecraft:block.anvil.land", 1.0f, 0.5f)
Sound.Play("minecraft:entity.generic.explode", Player.X, Player.Y, Player.Z)
Sound.PlayTo(Player, "minecraft:entity.experience_orb.pickup")
Sound.PlayLevelUp()
Sound.PlayClick()

// Particles — basic
Particle.Spawn("minecraft:flame", 100, 64, -200)
Particle.Spawn("minecraft:flame", 100, 64, -200, 20, 0.5f, 0.1f)
Particle.Spawn("minecraft:heart", Player.X, Player.Y + 2, Player.Z, 10, 1.0f, 0.05f)

// Colored dust
Particle.SpawnDust(Player.X, Player.Y, Player.Z, 255, 0, 0, 2.0f, 10, 0.5f)

// Advanced shapes
Particle.SpawnCircle("minecraft:flame", Player.X, Player.Y, Player.Z, 2.0f, 30)
Particle.SpawnSphere("minecraft:enchant", Player.X, Player.Y, Player.Z, 3.0f, 50)
Particle.SpawnHelix("minecraft:end_rod", Player.X, Player.Y, Player.Z, 4.0f, 3, 40)
Particle.SpawnTornado("minecraft:cloud", Player.X, Player.Y, Player.Z, 2.0f, 5.0f, 30)
Particle.SpawnHeart("minecraft:heart", Player.X, Player.Y + 3, Player.Z, 15)

// Line from player to point
Particle.SpawnLine("minecraft:flame",
    Player.X, Player.Y, Player.Z,
    200, 64, 0, 5
)

// Combo: sound + particle
Player.TeleportTo(0, 64, 0)
Sound.Play("minecraft:entity.enderman.teleport")
Particle.Spawn("minecraft:portal", 0, 64, 0, 30, 0.5f, 0.5f)
```
