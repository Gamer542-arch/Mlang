# World API — vollständige Dokumentation

## Methodenübersicht

### Blöcke — Lesen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.GetBlock(x, y, z)` | `string` | Block-ID (z.B. "minecraft:stone") |
| `World.GetBlockState(x, y, z)` | `string` | ID + Eigenschaften (z.B. "minecraft:stone[facing=north]") |
| `World.GetBlockData(x, y, z)` | `BlockData` | BlockData-Objekt |
| `World.IsAir(x, y, z)` | `bool` | Ist der Block Luft |
| `World.IsSolid(x, y, z)` | `bool` | Ist der Block massiv (solid) |
| `World.IsLiquid(x, y, z)` | `bool` | Ist der Block eine Flüssigkeit |
| `World.IsReplaceable(x, y, z)` | `bool` | Kann der Block ersetzt werden |
| `World.IsOpaque(x, y, z)` | `bool` | Ist der Block undurchsichtig |
| `World.IsFlammable(x, y, z)` | `bool` | Ist der Block brennbar |
| `World.IsSignalSource(x, y, z)` | `bool` | Sendet der Block ein Redstone-Signal |
| `World.IsPowered(x, y, z)` | `bool` | Ist der Block mit Strom versorgt |
| `World.GetHardness(x, y, z)` | `float` | Härte des Blocks |
| `World.GetBlastResistance(x, y, z)` | `float` | Explosionswiderstand |
| `World.GetLightEmission(x, y, z)` | `int` | Vom Block ausgestrahltes Licht |
| `World.GetLightLevel(x, y, z)` | `int` | Lichtstufe (0-15) |
| `World.GetBlockLight(x, y, z)` | `int` | Blocklicht |
| `World.GetSkyLight(x, y, z)` | `int` | Himmelslicht |
| `World.GetAmbientDarkness(x, y, z)` | `int` | Umgebungsdunkelheit |
| `World.GetBlockPosBelow(x, y, z)` | `BlockPos` | Block darunter |
| `World.GetBlockEntity(x, y, z)` | `BlockEntity` | Block-Entity (Kiste, Ofen...) |
| `World.HasBlockEntity(x, y, z)` | `bool` | Hat der Block eine Block-Entity |
| `World.GetBlockTags(x, y, z)` | `List<string>` | Tags des Blocks |
| `World.IsInTag(x, y, z, tag)` | `bool` | Hat der Block den Tag (z.B. "#minecraft:logs") |

### Blöcke — Schreiben
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.SetBlock(x, y, z, block)` | `bool` | Block setzen |
| `World.SetBlock(x, y, z, block, flags)` | `bool` | Block mit Flags setzen (update, Physik, render) |
| `World.SetBlockWithData(x, y, z, block, properties)` | `bool` | Block mit Eigenschaften setzen |
| `World.SetBlockState(x, y, z, state)` | `bool` | BlockState setzen |
| `World.BreakBlock(x, y, z)` | `void` | Block zerstören (Item droppen) |
| `World.BreakBlock(x, y, z, drop)` | `void` | Block zerstören (drop = true/false) |
| `World.ReplaceBlock(x, y, z, block)` | `bool` | Block ersetzen (ohne Update) |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block)` | `int` | Bereich mit Block füllen (gibt Anzahl der geänderten zurück) |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block, mode)` | `int` | Fill mit Modus: "replace", "destroy", "hollow", "outline" |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block, mode, filter)` | `int` | Fill, das nur Filter ersetzt |
| `World.CloneBlocks(sx, sy, sz, ex, ey, ez, dx, dy, dz)` | `bool` | Bereich kopieren |
| `World.CloneBlocks(sx, sy, sz, ex, ey, ez, dx, dy, dz, mode)` | `bool` | Clone mit Modus: "force", "move", "normal" |
| `World.ReplaceBlocks(x1, y1, z1, x2, y2, z2, from, to)` | `int` | Blöcke ersetzen |
| `World.ClearRegion(x1, y1, z1, x2, y2, z2)` | `int` | Bereich löschen (auf air setzen) |
| `World.GetHighestBlockY(x, z)` | `int` | Höchster Block auf X,Z |
| `World.GetHighestSolidBlockY(x, z)` | `int` | Höchster massiver Block |
| `World.GetTopBlock(x, z)` | `string` | ID des höchsten Blocks |
| `World.GetSurfaceY(x, z)` | `int` | Oberflächen-Y (Gras/Sand) |

### Blöcke — Redstone und Mechanik
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.EmitRedstone(x, y, z, power)` | `void` | Redstone-Signal ausgeben |
| `World.ClearRedstone(x, y, z)` | `void` | Redstone-Signal löschen |
| `World.GetRedstonePower(x, y, z)` | `int` | Redstone-Stärke (0-15) |
| `World.GetBestRedstonePower(x, y, z)` | `int` | Bestes Redstone (von allen Seiten) |
| `World.GetDirectRedstonePower(x, y, z)` | `int` | Direktes Redstone |
| `World.UpdateBlock(x, y, z)` | `void` | Block-Update erzwingen |
| `World.UpdateNeighbors(x, y, z)` | `void` | Nachbarn aktualisieren |
| `World.UpdateComparators(x, y, z)` | `void` | Komparatoren aktualisieren |

### Blöcke — Spezial
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.SignSetText(x, y, z, lines[])` | `void` | Text auf Schild setzen (4 Zeilen) |
| `World.SignGetText(x, y, z)` | `string[]` | Text vom Schild holen |
| `World.SignSetColor(x, y, z, color)` | `void` | Schildfarbe setzen |
| `World.LecternGetBook(x, y, z)` | `ItemStack` | Buch vom Lesepult |
| `World.LecternSetBook(x, y, z, book)` | `void` | Buch auf Lesepult legen |
| `World.CommandBlockSetCommand(x, y, z, cmd)` | `void` | Befehl im Befehlsblock setzen |
| `World.CommandBlockGetCommand(x, y, z)` | `string` | Befehl aus Befehlsblock holen |
| `World.CommandBlockSetMode(x, y, z, mode)` | `void` | Modus: "impulse", "chain", "repeat" |
| `World.CommandBlockSetConditional(x, y, z, bool)` | `void` | Bedingten Modus setzen |
| `World.CommandBlockSetAlwaysActive(x, y, z, bool)` | `void` | Always active |
| `World.CommandBlockExecute(x, y, z)` | `void` | Befehlsblock ausführen |
| `World.SetSpawnerEntity(x, y, z, entity)` | `void` | Mob-Spawner setzen |
| `World.GetSpawnerEntity(x, y, z)` | `string` | Spawner-Typ abrufen |
| `World.SetSpawnerDelay(x, y, z, ticks)` | `void` | Spawner-Verzögerung setzen |
| `World.SetSpawnerMinDelay(x, y, z, ticks)` | `void` | Min Verzögerung |
| `World.SetSpawnerMaxDelay(x, y, z, ticks)` | `void` | Max Verzögerung |
| `World.SetSpawnerSpawnRange(x, y, z, range)` | `void` | Spawn-Reichweite |
| `World.SetSpawnerPlayerRange(x, y, z, range)` | `void` | Spieler-Erkennungsreichweite |
| `World.SetSpawnerMaxNearbyEntities(x, y, z, count)` | `void` | Max Entitäten in der Nähe |
| `World.SetSpawnerRequiredPlayerRange(x, y, z, range)` | `void` | Erforderliche Spielerreichweite |
| `World.JukeboxSetRecord(x, y, z, item)` | `void` | Platte in Jukebox legen |
| `World.JukeboxGetRecord(x, y, z)` | `ItemStack` | Platte aus Jukebox |
| `World.JukeboxPlay(x, y, z)` | `void` | Jukebox abspielen |
| `World.JukeboxStop(x, y, z)` | `void` | Jukebox stoppen |
| `World.JukeboxIsPlaying(x, y, z)` | `bool` | Spielt die Jukebox |
| `World.BeehiveGetBeeCount(x, y, z)` | `int` | Anzahl Bienen im Stock |
| `World.BeehiveSetBeeCount(x, y, z, count)` | `void` | Bienenanzahl setzen |
| `World.BeehiveGetHoneyLevel(x, y, z)` | `int` | Honigstufe (0-5) |
| `World.BeehiveSetHoneyLevel(x, y, z, level)` | `void` | Honigstufe setzen |

### Entitäten — Spawn und Entfernen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.Summon(entity, x, y, z)` | `Entity` | Entität spawnen |
| `World.Summon(entity, x, y, z, nbt)` | `Entity` | Spawn mit NBT |
| `World.Summon(entity, x, y, z, nbt, spawnEvent)` | `Entity` | Spawn mit Event |
| `World.SpawnMob(type, x, y, z)` | `Entity` | Mob spawnen |
| `World.SpawnMob(type, x, y, z, count)` | `List<Entity>` | Mehrere Mobs spawnen |
| `World.SpawnAnimal(type, x, y, z)` | `Entity` | Tier spawnen |
| `World.SpawnItem(item, x, y, z)` | `Entity` | Item-Drop spawnen |
| `World.SpawnItem(item, x, y, z, count)` | `Entity` | Item-Stack spawnen |
| `World.SpawnFallingBlock(block, x, y, z)` | `Entity` | Fallenden Block spawnen |
| `World.SpawnPrimedTNT(x, y, z, fuse)` | `Entity` | TNT spawnen |
| `World.SpawnFirework(x, y, z, item)` | `Entity` | Feuerwerk spawnen |
| `World.SpawnAreaEffectCloud(x, y, z, effect)` | `Entity` | Wirkungsbereichswolke spawnen |
| `World.SpawnPainting(x, y, z, facing, motive)` | `Entity` | Gemälde spawnen |
| `World.SpawnItemFrame(x, y, z, facing)` | `Entity` | Rahmen spawnen |
| `World.SpawnArmorStand(x, y, z)` | `Entity` | Rüstungsständer spawnen |
| `World.SpawnTextDisplay(text, x, y, z)` | `Entity` | Textanzeige spawnen (1.19+) |
| `World.SpawnTextDisplay(text, x, y, z, opts)` | `Entity` | Text mit Optionen spawnen |
| `World.SpawnItemDisplay(item, x, y, z)` | `Entity` | Item-Anzeige spawnen |
| `World.SpawnBlockDisplay(block, x, y, z)` | `Entity` | Block-Anzeige spawnen |
| `World.Kill(entityId)` | `void` | Entität nach ID töten |
| `World.Kill(entity)` | `void` | Entität töten |
| `World.KillAll(type)` | `int` | Alle Entitäten eines Typs töten |
| `World.KillAll(type, radius)` | `int` | In Reichweite töten |
| `World.Remove(entity)` | `void` | Entität entfernen (ohne Drops) |
| `World.RemoveAll(type)` | `int` | Alle Entitäten eines Typs entfernen |

### Entitäten — Lesen und Suchen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.GetEntityById(id)` | `Entity` | Entität nach ID abrufen |
| `World.GetEntityByUUID(uuid)` | `Entity` | Entität nach UUID abrufen |
| `World.GetEntities()` | `List<Entity>` | Alle Entitäten in der Welt |
| `World.GetEntitiesOfType(type)` | `List<Entity>` | Entitäten eines Typs |
| `World.GetNearbyEntities(x, y, z, radius)` | `List<Entity>` | Entitäten im Umkreis |
| `World.GetNearbyEntities(x, y, z, radius, type)` | `List<Entity>` | Entitäten eines Typs im Umkreis |
| `World.GetNearbyPlayers(x, y, z, radius)` | `List<Player>` | Spieler im Umkreis |
| `World.GetPlayers()` | `List<Player>` | Alle Online-Spieler |
| `World.GetPlayerByName(name)` | `Player` | Spieler nach Name |
| `World.GetPlayerByUUID(uuid)` | `Player` | Spieler nach UUID |
| `World.GetEntityCount()` | `int` | Anzahl Entitäten |
| `World.GetEntityCount(type)` | `int` | Anzahl Entitäten eines Typs |
| `World.GetChunkEntities(chunkX, chunkZ)` | `List<Entity>` | Entitäten im Chunk |
| `World.IsChunkLoaded(x, z)` | `bool` | Ist Chunk geladen |
| `World.LoadChunk(x, z)` | `void` | Chunk laden |
| `World.UnloadChunk(x, z)` | `void` | Chunk entladen |
| `World.GetChunk(x, z)` | `Chunk` | Chunk abrufen |
| `World.IsAreaLoaded(x1, y1, z1, x2, y2, z2)` | `bool` | Ist Bereich geladen |

### Zeit
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.Time` | `long` | Weltzeit (Ticks, 0-24000) |
| `World.SetTime(long)` | `void` | Zeit setzen |
| `World.SetTimeAdd(long)` | `void` | Zur Zeit addieren |
| `World.GameTime` | `long` | Spielzeit (gesamt) |
| `World.DayTime` | `long` | Tageszeit |
| `World.WorldAge` | `long` | Weltalter (Ticks) |
| `World.IsDay` | `bool` | Ist es Tag (Zeit 1000-13000) |
| `World.IsNight` | `bool` | Ist es Nacht |
| `World.IsDawn` | `bool` | Ist Morgendämmerung |
| `World.IsDusk` | `bool` | Ist Abenddämmerung |
| `World.GetMoonPhase()` | `int` | Mondphase (0-7) |
| `World.GetMoonSize()` | `float` | Mondgröße |
| `World.GetStarBrightness()` | `float` | Sternenhelligkeit (0.0-1.0) |
| `World.GetSunAngle()` | `float` | Sonnenwinkel |
| `World.GetSkyAngle()` | `float` | Himmelswinkel |
| `World.GetSkyDarkness()` | `float` | Himmelsdunkelheit |

### Wetter
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.Weather` | `string` | Wetter: "clear", "rain", "thunder" |
| `World.SetWeather(string)` | `void` | Wetter setzen |
| `World.SetWeather(string, duration)` | `void` | Wetter mit Dauer setzen |
| `World.IsRaining` | `bool` | Regnet es |
| `World.IsThundering` | `bool` | Gewittert es |
| `World.RainDuration` | `int` | Regendauer (Ticks) |
| `World.SetRainDuration(int)` | `void` | Regendauer setzen |
| `World.ThunderDuration` | `int` | Gewitterdauer |
| `World.SetThunderDuration(int)` | `void` | Gewitterdauer setzen |
| `World.GetRainStrength()` | `float` | Regenstärke (0.0-1.0) |
| `World.GetThunderStrength()` | `float` | Gewitterstärke (0.0-1.0) |
| `World.ClearWeather(int)` | `void` | Wetter für X Ticks klären |

### Biome und Umgebung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.GetBiome(x, y, z)` | `string` | Biom-ID (z.B. "minecraft:plains") |
| `World.GetBiomeCategory(x, y, z)` | `string` | Biom-Kategorie |
| `World.GetTemperature(x, y, z)` | `float` | Temperatur (0.0-2.0) |
| `World.GetHumidity(x, y, z)` | `float` | Luftfeuchtigkeit (0.0-1.0) |
| `World.GetDownfall(x, y, z)` | `float` | Niederschlag (0.0-1.0) |
| `World.GetFoliageColor(x, y, z)` | `int` | Laubfarbe (RGB) |
| `World.GetGrassColor(x, y, z)` | `int` | Grasfarbe (RGB) |
| `World.GetWaterColor(x, y, z)` | `int` | Wasserfarbe (RGB) |
| `World.GetSkyColor(x, y, z)` | `int` | Himmelsfarbe (RGB) |
| `World.GetFogColor(x, y, z)` | `int` | Nebelfarbe (RGB) |
| `World.IsSlimeChunk(x, z)` | `bool` | Ist Slime-Chunk |
| `World.IsVillage(x, y, z)` | `bool` | In einem Dorf |
| `World.IsStructureAt(x, y, z, structure)` | `bool` | Struktur an Position |
| `World.LocateStructure(structure, x, y, z, radius)` | `BlockPos` | Nächste Struktur finden |
| `World.LocateBiome(biome, x, y, z, radius)` | `BlockPos` | Nächstes Biom finden |
| `World.GetStructures()` | `List<string>` | Strukturliste in der Welt |

### Explosionen und Effekte
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.CreateExplosion(x, y, z, power, fire?)` | `void` | Explosion erzeugen |
| `World.CreateExplosion(x, y, z, power, fire?, destroy?)` | `void` | Explosion mit Optionen |
| `World.CreateExplosion(x, y, z, power, fire?, destroy?, source?)` | `void` | Explosion mit Quelle |
| `World.StrikeLightning(x, y, z)` | `Entity` | Blitzeinschlag (mit Schaden) |
| `World.StrikeLightningEffect(x, y, z)` | `void` | Blitzeffekt (ohne Schaden) |
| `World.StrikeLightningCustom(x, y, z, damage?, fire?)` | `Entity` | Blitz mit Optionen |
| `World.SpawnParticle(particle, x, y, z)` | `void` | Partikel an Punkt |
| `World.SpawnParticle(particle, x, y, z, count)` | `void` | Mehrere Partikel |
| `World.SpawnParticle(particle, x, y, z, count, dx, dy, dz, speed)` | `void` | Partikel mit Streuung |
| `World.SpawnParticle(particle, x, y, z, count, dx, dy, dz, speed, force?)` | `void` | Force = aus der Ferne sichtbar |
| `World.SpawnParticleLine(p, x1, y1, z1, x2, y2, z2, density)` | `void` | Partikellinie |
| `World.SpawnParticleCircle(p, cx, cy, cz, radius, count)` | `void` | Partikelkreis |
| `World.SpawnParticleSphere(p, cx, cy, cz, radius, count)` | `void` | Partikelkugel |
| `World.SpawnParticleHelix(p, cx, cy, cz, height, turns, count)` | `void` | Partikelhelix |
| `World.SpawnParticleCube(p, x1, y1, z1, x2, y2, z2, density)` | `void` | Partikelwürfel |
| `World.PlaySound(sound, x, y, z, volume, pitch)` | `void` | Klang abspielen |
| `World.PlaySound(sound, x, y, z, volume, pitch, seed)` | `void` | Klang mit Seed |

### Licht
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.GetComputedLight(x, y, z)` | `int` | Kombiniertes Licht (Block+Himmel) |
| `World.GetMaxLightLevel()` | `int` | Maximale Lichtstufe |
| `World.GetBrightness(x, y, z)` | `float` | Helligkeit (0.0-1.0) |
| `World.GetDayLight()` | `int` | Tageslicht |
| `World.GetMoonLight()` | `int` | Mondlicht |
| `World.IsDarkEnoughToSpawn(x, y, z)` | `bool` | Dunkel genug zum Mobs spawnen |

### Welt — Eigenschaften
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.Dimension` | `string` | Dimensions-ID: "minecraft:overworld", "minecraft:the_nether", "minecraft:the_end" |
| `World.WorldType` | `string` | Welttyp: "default", "flat", "large_biomes", "amplified", "single_biome_surface" |
| `World.Seed` | `long` | Welt-Seed |
| `World.SeaLevel` | `int` | Meeresspiegel (normalerweise 63) |
| `World.MaxBuildHeight` | `int` | Maximale Bauhöhe |
| `World.MinBuildHeight` | `int` | Minimale Bauhöhe |
| `World.LogicalHeight` | `int` | Logische Höhe |
| `World.GetHorizonHeight()` | `int` | Horizonthöhe |
| `World.IsSurfaceWorld` | `bool` | Ist Oberflächenwelt |
| `World.HasSkyLight` | `bool` | Hat Himmelslicht |
| `World.HasCeiling` | `bool` | Hat Decke (Nether) |
| `World.IsUltrawarm` | `bool` | Ist ultraheiß (Nether) |
| `World.HasRaids` | `bool` | Sind Raids möglich |
| `World.IsNatural` | `bool` | Ist natürliche Dimension |
| `World.CoordinateScale` | `double` | Koordinatenskala (Nether = 8) |
| `World.PiglinSafe` | `bool` | Sind Piglins sicher |
| `World.BedWorks` | `bool` | Funktioniert Bett |
| `World.RespawnAnchorWorks` | `bool` | Funktioniert Respawn-Anker |
| `World.HasSpawnPoint` | `bool` | Hat Spawn-Punkt |
| `World.InfiniteBurn` | `bool` | Unendliches Brennen (Nether) |
| `World.FixedTime` | `long` | Feste Zeit (falls gesetzt) |
| `World.GetSpawnPosition()` | `BlockPos` | Welt-Spawn-Position |
| `World.SetSpawnPosition(x, y, z)` | `void` | Welt-Spawn setzen |
| `World.GetWorldBorder()` | `WorldBorder` | Weltgrenze |
| `World.SetWorldBorder(centerX, centerZ, size)` | `void` | Grenze setzen |
| `World.SetWorldBorder(centerX, centerZ, size, damage, warning)` | `void` | Grenze mit Optionen |
| `World.GetDifficulty()` | `string` | Schwierigkeit: "peaceful", "easy", "normal", "hard" |
| `World.SetDifficulty(string)` | `void` | Schwierigkeit setzen |
| `World.IsHardcore` | `bool` | Ist Hardcore-Modus |
| `World.SetHardcore(bool)` | `void` | Hardcore setzen |
| `World.IsDebugWorld` | `bool` | Ist Debug-Welt |
| `World.IsFlatWorld` | `bool` | Ist Superflat |
| `World.GetWorldFolder()` | `string` | Weltordner-Pfad |

### GameRules
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.GetGameRule(rule)` | `object` | Gamerule abrufen (string/int/bool) |
| `World.SetGameRule(rule, value)` | `void` | Gamerule setzen |
| `World.GetGameRules()` | `Dict<string, object>` | Alle Gamerules |
| `World.ResetGameRule(rule)` | `void` | Gamerule zurücksetzen |
| `World.DoDaylightCycle` | `bool` | Get/set doDaylightCycle |
| `World.DoWeatherCycle` | `bool` | Get/set doWeatherCycle |
| `World.DoMobSpawning` | `bool` | Get/set doMobSpawning |
| `World.DoMobLoot` | `bool` | Mob-Beute |
| `World.DoTileDrops` | `bool` | Block-Drops |
| `World.DoFireTick` | `bool` | Feuer-Tick |
| `World.DoImmediateRespawn` | `bool` | Sofortiger Respawn |
| `World.KeepInventory` | `bool` | Inventar behalten |
| `World.MobGriefing` | `bool` | Mob-Griefing |
| `World.NaturalRegeneration` | `bool` | Natürliche Regeneration |
| `World.RandomTickSpeed` | `int` | Zufällige Tick-Geschwindigkeit |
| `World.CommandBlockOutput` | `bool` | Befehlsblock-Ausgabe |
| `World.ShowDeathMessages` | `bool` | Todesmeldungen |
| `World.SpawnRadius` | `int` | Spawn-Radius |
| `World.MaxEntityCramming` | `int` | Max Entity Cramming |

### Scoreboard
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.CreateObjective(name, criteria, displayName)` | `void` | Objective erstellen |
| `World.RemoveObjective(name)` | `void` | Objective entfernen |
| `World.GetObjective(name)` | `Objective` | Objective abrufen |
| `World.GetObjectives()` | `List<Objective>` | Liste der Objectives |
| `World.SetScore(player, objective, score)` | `void` | Spieler-Score setzen |
| `World.GetScore(player, objective)` | `int` | Spieler-Score abrufen |
| `World.ResetScore(player, objective)` | `void` | Score zurücksetzen |
| `World.ResetAllScores(player)` | `void` | Alle Spieler-Scores zurücksetzen |
| `World.DisplaySidebar(objective)` | `void` | Seitenleiste anzeigen |
| `World.DisplayBelowName(objective)` | `void` | Unter dem Namen anzeigen |
| `World.DisplayPlayerList(objective)` | `void` | In Spielerliste anzeigen |
| `World.ClearDisplay(slot)` | `void` | Anzeige-Slot löschen |
| `World.CreateTeam(name)` | `void` | Team erstellen |
| `World.RemoveTeam(name)` | `void` | Team entfernen |
| `World.GetTeam(name)` | `Team` | Team abrufen |
| `World.GetTeams()` | `List<Team>` | Teamliste |
| `World.AddPlayerToTeam(player, team)` | `void` | Spieler zu Team hinzufügen |
| `World.RemovePlayerFromTeam(player)` | `void` | Spieler aus Team entfernen |
| `World.GetPlayerTeam(player)` | `Team` | Spieler-Team |
| `World.SetTeamProperty(team, prop, value)` | `void` | Team-Eigenschaft setzen |

### BossBar
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.CreateBossBar(id, title, color, style)` | `BossBar` | Bossleiste erstellen |
| `World.RemoveBossBar(id)` | `void` | Bossleiste entfernen |
| `World.GetBossBar(id)` | `BossBar` | Bossleiste abrufen |
| `World.AddBossBarPlayer(id, player)` | `void` | Spieler zur Bossleiste hinzufügen |
| `World.RemoveBossBarPlayer(id, player)` | `void` | Spieler von Bossleiste entfernen |

### Befehle
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.RunCommand(command)` | `string` | Befehl ausführen (gibt Ausgabe zurück) |
| `World.RunCommandAs(player, command)` | `string` | Befehl als Spieler ausführen |
| `World.RunCommandAs(entity, command)` | `string` | Befehl als Entität ausführen |
| `World.RunCommandSilent(command)` | `void` | Befehl leise ausführen |
| `World.DispatchCommand(command)` | `int` | Befehl dispatchen (Return-Code) |

### Raids und Strukturen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.GetRaids()` | `List<Raid>` | Liste aktiver Raids |
| `World.GetRaidAt(x, y, z)` | `Raid` | Raid an Position |
| `World.StartRaid(x, y, z)` | `Raid` | Raid starten |
| `World.StopRaid(x, y, z)` | `void` | Raid stoppen |
| `World.GetPoiPositions(poiType, x, y, z, radius)` | `List<BlockPos>` | POI in Reichweite |
| `World.GetChunkGenerator()` | `ChunkGenerator` | Chunk-Generator |
| `World.GetStructureManager()` | `StructureManager` | Struktur-Manager |

### Item droppen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.DropItem(item, x, y, z)` | `Entity` | Item an Position droppen |
| `World.DropItem(item, x, y, z, count)` | `Entity` | Stack droppen |
| `World.DropItemNaturally(item, x, y, z)` | `Entity` | Natürliches Droppen (zufällige Streuung) |
| `World.DropExperience(x, y, z, amount)` | `void` | Erfahrung droppen |
| `World.DropExperienceOrb(x, y, z, value)` | `Entity` | Erfahrungskugel droppen |

### Informationen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.GetWorldName()` | `string` | Weltname |
| `World.GetServer()` | `object` | Minecraft-Server |
| `World.GetPlayersCount()` | `int` | Anzahl Online-Spieler |
| `World.GetMaxPlayers()` | `int` | Maximale Spieleranzahl |
| `World.IsEmpty()` | `bool` | Ist Welt leer (keine Spieler) |
| `World.Save()` | `void` | Welt speichern |
| `World.SaveChunk(x, z)` | `void` | Chunk speichern |
| `World.SaveAll()` | `void` | Alles speichern |
| `World.AutoSave` | `bool` | Auto-Save ein/aus |
| `World.SetAutoSave(bool)` | `void` | Auto-Save setzen |

---

## Beispiele

### Bauen
```glang
#version 1.0
#name "Builder Demo"

// Haus aus dem Nichts
World.FillBlocks(0, 63, 0, 10, 63, 10, "minecraft:stone")       // Boden
World.FillBlocks(0, 64, 0, 0, 68, 10, "minecraft:stone")        // Wand X
World.FillBlocks(10, 64, 0, 10, 68, 10, "minecraft:stone")      // Wand X+
World.FillBlocks(0, 64, 0, 10, 68, 0, "minecraft:stone")        // Wand Z
World.FillBlocks(0, 64, 10, 10, 68, 10, "minecraft:stone")      // Wand Z+
World.FillBlocks(0, 69, 0, 10, 69, 10, "minecraft:stone")       // Dach
World.FillBlocks(1, 65, 0, 2, 66, 0, "minecraft:air")           // Tür

// Beleuchtung
World.SetBlock(5, 64, 5, "minecraft:glowstone")

// Information
Chat.Send("§aHaus gebaut!")
```
