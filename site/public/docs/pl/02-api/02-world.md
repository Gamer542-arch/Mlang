# World API — pełna dokumentacja

## Spis method

### Bloki — odczyt
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.GetBlock(x, y, z)` | `string` | ID bloku (np. "minecraft:stone") |
| `World.GetBlockState(x, y, z)` | `string` | ID + properties (np. "minecraft:stone[facing=north]") |
| `World.GetBlockData(x, y, z)` | `BlockData` | Obiekt BlockData |
| `World.IsAir(x, y, z)` | `bool` | Czy blok to powietrze |
| `World.IsSolid(x, y, z)` | `bool` | Czy blok jest pełny (solid) |
| `World.IsLiquid(x, y, z)` | `bool` | Czy blok to płyn |
| `World.IsReplaceable(x, y, z)` | `bool` | Czy blok można zastąpić |
| `World.IsOpaque(x, y, z)` | `bool` | Czy blok jest nieprzezroczysty |
| `World.IsFlammable(x, y, z)` | `bool` | Czy blok jest palny |
| `World.IsSignalSource(x, y, z)` | `bool` | Czy blok emituje redstone signal |
| `World.IsPowered(x, y, z)` | `bool` | Czy blok jest zasilany |
| `World.GetHardness(x, y, z)` | `float` | Twardość bloku |
| `World.GetBlastResistance(x, y, z)` | `float` | Odporność na wybuch |
| `World.GetLightEmission(x, y, z)` | `int` | Światło emitowane przez blok |
| `World.GetLightLevel(x, y, z)` | `int` | Poziom światła (0-15) |
| `World.GetBlockLight(x, y, z)` | `int` | Światło blokowe |
| `World.GetSkyLight(x, y, z)` | `int` | Światło nieba |
| `World.GetAmbientDarkness(x, y, z)` | `int` | Ciemność otoczenia |
| `World.GetBlockPosBelow(x, y, z)` | `BlockPos` | Blok poniżej |
| `World.GetBlockEntity(x, y, z)` | `BlockEntity` | Block entity (skrzynia, piec...) |
| `World.HasBlockEntity(x, y, z)` | `bool` | Czy blok ma block entity |
| `World.GetBlockTags(x, y, z)` | `List<string>` | Tagi bloku |
| `World.IsInTag(x, y, z, tag)` | `bool` | Czy blok ma tag (np. "#minecraft:logs") |

### Bloki — zapis
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.SetBlock(x, y, z, block)` | `bool` | Postaw blok |
| `World.SetBlock(x, y, z, block, flags)` | `bool` | Postaw blok z flagami (update, fizyka, render) |
| `World.SetBlockWithData(x, y, z, block, properties)` | `bool` | Postaw blok z property |
| `World.SetBlockState(x, y, z, state)` | `bool` | Postaw BlockState |
| `World.BreakBlock(x, y, z)` | `void` | Zniszcz blok (drop item) |
| `World.BreakBlock(x, y, z, drop)` | `void` | Zniszcz blok (drop = true/false) |
| `World.ReplaceBlock(x, y, z, block)` | `bool` | Zastąp blok (bez update) |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block)` | `int` | Wypełnij obszar blokiem (zwraca liczbę zmienionych) |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block, mode)` | `int` | Fill z trybem: "replace", "destroy", "hollow", "outline" |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block, mode, filter)` | `int` | Fill zastępujący tylko filter |
| `World.CloneBlocks(sx, sy, sz, ex, ey, ez, dx, dy, dz)` | `bool` | Skopiuj obszar |
| `World.CloneBlocks(sx, sy, sz, ex, ey, ez, dx, dy, dz, mode)` | `bool` | Clone z trybem: "force", "move", "normal" |
| `World.ReplaceBlocks(x1, y1, z1, x2, y2, z2, from, to)` | `int` | Zamień bloki |
| `World.ClearRegion(x1, y1, z1, x2, y2, z2)` | `int` | Wyczyść obszar (ustaw air) |
| `World.GetHighestBlockY(x, z)` | `int` | Najwyższy blok na X,Z |
| `World.GetHighestSolidBlockY(x, z)` | `int` | Najwyższy solid blok |
| `World.GetTopBlock(x, z)` | `string` | ID najwyższego bloku |
| `World.GetSurfaceY(x, z)` | `int` | Y powierzchni (trawy/piasku) |

### Bloki — redstone i mechanika
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.EmitRedstone(x, y, z, power)` | `void` | Emituj redstone signal |
| `World.ClearRedstone(x, y, z)` | `void` | Wyczyść redstone signal |
| `World.GetRedstonePower(x, y, z)` | `int` | Siła redstone (0-15) |
| `World.GetBestRedstonePower(x, y, z)` | `int` | Najlepszy redstone (z wszystkich stron) |
| `World.GetDirectRedstonePower(x, y, z)` | `int` | Bezpośredni redstone |
| `World.UpdateBlock(x, y, z)` | `void` | Wymuś update bloku |
| `World.UpdateNeighbors(x, y, z)` | `void` | Update sąsiadów |
| `World.UpdateComparators(x, y, z)` | `void` | Update comparatorów |

### Bloki — specjalne
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.SignSetText(x, y, z, lines[])` | `void` | Ustaw tekst na znaku (4 linie) |
| `World.SignGetText(x, y, z)` | `string[]` | Pobierz tekst ze znaku |
| `World.SignSetColor(x, y, z, color)` | `void` | Ustaw kolor znaku |
| `World.LecternGetBook(x, y, z)` | `ItemStack` | Książka z pulpitu |
| `World.LecternSetBook(x, y, z, book)` | `void` | Włóż książkę na pulpit |
| `World.CommandBlockSetCommand(x, y, z, cmd)` | `void` | Ustaw komendę w command blocku |
| `World.CommandBlockGetCommand(x, y, z)` | `string` | Pobierz komendę z command blocku |
| `World.CommandBlockSetMode(x, y, z, mode)` | `void` | Tryb: "impulse", "chain", "repeat" |
| `World.CommandBlockSetConditional(x, y, z, bool)` | `void` | Ustaw conditional mode |
| `World.CommandBlockSetAlwaysActive(x, y, z, bool)` | `void` | Always active |
| `World.CommandBlockExecute(x, y, z)` | `void` | Wykonaj command block |
| `World.SetSpawnerEntity(x, y, z, entity)` | `void` | Ustaw mob spawner |
| `World.GetSpawnerEntity(x, y, z)` | `string` | Pobierz typ spawnera |
| `World.SetSpawnerDelay(x, y, z, ticks)` | `void` | Ustaw delay spawnera |
| `World.SetSpawnerMinDelay(x, y, z, ticks)` | `void` | Min delay |
| `World.SetSpawnerMaxDelay(x, y, z, ticks)` | `void` | Max delay |
| `World.SetSpawnerSpawnRange(x, y, z, range)` | `void` | Zasięg spawnu |
| `World.SetSpawnerPlayerRange(x, y, z, range)` | `void` | Zasięg wykrywania gracza |
| `World.SetSpawnerMaxNearbyEntities(x, y, z, count)` | `void` | Max encji w okolicy |
| `World.SetSpawnerRequiredPlayerRange(x, y, z, range)` | `void` | Wymagany zasięg gracza |
| `World.JukeboxSetRecord(x, y, z, item)` | `void` | Włóż płytę do jukeboxa |
| `World.JukeboxGetRecord(x, y, z)` | `ItemStack` | Płyta z jukeboxa |
| `World.JukeboxPlay(x, y, z)` | `void` | Odtwórz jukebox |
| `World.JukeboxStop(x, y, z)` | `void` | Zatrzymaj jukebox |
| `World.JukeboxIsPlaying(x, y, z)` | `bool` | Czy jukebox gra |
| `World.BeehiveGetBeeCount(x, y, z)` | `int` | Liczba pszczół w ulu |
| `World.BeehiveSetBeeCount(x, y, z, count)` | `void` | Ustaw liczbę pszczół |
| `World.BeehiveGetHoneyLevel(x, y, z)` | `int` | Poziom miodu (0-5) |
| `World.BeehiveSetHoneyLevel(x, y, z, level)` | `void` | Ustaw poziom miodu |

### Encje — spawn i usuwanie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.Summon(entity, x, y, z)` | `Entity` | Spawn encji |
| `World.Summon(entity, x, y, z, nbt)` | `Entity` | Spawn z NBT |
| `World.Summon(entity, x, y, z, nbt, spawnEvent)` | `Entity` | Spawn z eventem |
| `World.SpawnMob(type, x, y, z)` | `Entity` | Spawn moba |
| `World.SpawnMob(type, x, y, z, count)` | `List<Entity>` | Spawn wiele mobów |
| `World.SpawnAnimal(type, x, y, z)` | `Entity` | Spawn zwierzęcia |
| `World.SpawnItem(item, x, y, z)` | `Entity` | Spawn item drop |
| `World.SpawnItem(item, x, y, z, count)` | `Entity` | Spawn item stack |
| `World.SpawnFallingBlock(block, x, y, z)` | `Entity` | Spawn spadający blok |
| `World.SpawnPrimedTNT(x, y, z, fuse)` | `Entity` | Spawn TNT |
| `World.SpawnFirework(x, y, z, item)` | `Entity` | Spawn fajerwerk |
| `World.SpawnAreaEffectCloud(x, y, z, effect)` | `Entity` | Spawn area effect cloud |
| `World.SpawnPainting(x, y, z, facing, motive)` | `Entity` | Spawn obraz |
| `World.SpawnItemFrame(x, y, z, facing)` | `Entity` | Spawn item frame |
| `World.SpawnArmorStand(x, y, z)` | `Entity` | Spawn armor stand |
| `World.SpawnTextDisplay(text, x, y, z)` | `Entity` | Spawn text display (1.19+) |
| `World.SpawnTextDisplay(text, x, y, z, opts)` | `Entity` | Spawn text z opcjami |
| `World.SpawnItemDisplay(item, x, y, z)` | `Entity` | Spawn item display |
| `World.SpawnBlockDisplay(block, x, y, z)` | `Entity` | Spawn block display |
| `World.Kill(entityId)` | `void` | Zabij encję po ID |
| `World.Kill(entity)` | `void` | Zabij encję |
| `World.KillAll(type)` | `int` | Zabij wszystkie encje danego typu |
| `World.KillAll(type, radius)` | `int` | Zabij w zasięgu |
| `World.Remove(entity)` | `void` | Usuń encję (bez drops) |
| `World.RemoveAll(type)` | `int` | Usuń wszystkie encje danego typu |

### Encje — odczyt i wyszukiwanie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.GetEntityById(id)` | `Entity` | Pobierz encję po ID |
| `World.GetEntityByUUID(uuid)` | `Entity` | Pobierz encję po UUID |
| `World.GetEntities()` | `List<Entity>` | Wszystkie encje w świecie |
| `World.GetEntitiesOfType(type)` | `List<Entity>` | Encje danego typu |
| `World.GetNearbyEntities(x, y, z, radius)` | `List<Entity>` | Encje w promieniu |
| `World.GetNearbyEntities(x, y, z, radius, type)` | `List<Entity>` | Encje danego typu w promieniu |
| `World.GetNearbyPlayers(x, y, z, radius)` | `List<Player>` | Gracze w promieniu |
| `World.GetPlayers()` | `List<Player>` | Wszyscy gracze online |
| `World.GetPlayerByName(name)` | `Player` | Gracz po nicku |
| `World.GetPlayerByUUID(uuid)` | `Player` | Gracz po UUID |
| `World.GetEntityCount()` | `int` | Liczba encji |
| `World.GetEntityCount(type)` | `int` | Liczba encji danego typu |
| `World.GetChunkEntities(chunkX, chunkZ)` | `List<Entity>` | Encje w chunku |
| `World.IsChunkLoaded(x, z)` | `bool` | Czy chunk załadowany |
| `World.LoadChunk(x, z)` | `void` | Załaduj chunk |
| `World.UnloadChunk(x, z)` | `void` | Wyładuj chunk |
| `World.GetChunk(x, z)` | `Chunk` | Pobierz chunk |
| `World.IsAreaLoaded(x1, y1, z1, x2, y2, z2)` | `bool` | Czy obszar załadowany |

### Czas
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.Time` | `long` | Czas świata (ticki, 0-24000) |
| `World.SetTime(long)` | `void` | Ustaw czas |
| `World.SetTimeAdd(long)` | `void` | Dodaj do czasu |
| `World.GameTime` | `long` | Czas gry (łączny) |
| `World.DayTime` | `long` | Czas dnia |
| `World.WorldAge` | `long` | Wiek świata (ticki) |
| `World.IsDay` | `bool` | Czy dzień (czas 1000-13000) |
| `World.IsNight` | `bool` | Czy noc |
| `World.IsDawn` | `bool` | Czy świt |
| `World.IsDusk` | `bool` | Czy zmierzch |
| `World.GetMoonPhase()` | `int` | Faza księżyca (0-7) |
| `World.GetMoonSize()` | `float` | Wielkość księżyca |
| `World.GetStarBrightness()` | `float` | Jasność gwiazd (0.0-1.0) |
| `World.GetSunAngle()` | `float` | Kąt słońca |
| `World.GetSkyAngle()` | `float` | Kąt nieba |
| `World.GetSkyDarkness()` | `float` | Ciemność nieba |

### Pogoda
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.Weather` | `string` | Pogoda: "clear", "rain", "thunder" |
| `World.SetWeather(string)` | `void` | Ustaw pogodę |
| `World.SetWeather(string, duration)` | `void` | Ustaw pogodę z czasem trwania |
| `World.IsRaining` | `bool` | Czy pada deszcz |
| `World.IsThundering` | `bool` | Czy burza |
| `World.RainDuration` | `int` | Czas trwania deszczu (ticki) |
| `World.SetRainDuration(int)` | `void` | Ustaw czas deszczu |
| `World.ThunderDuration` | `int` | Czas trwania burzy |
| `World.SetThunderDuration(int)` | `void` | Ustaw czas burzy |
| `World.GetRainStrength()` | `float` | Siła deszczu (0.0-1.0) |
| `World.GetThunderStrength()` | `float` | Siła burzy (0.0-1.0) |
| `World.ClearWeather(int)` | `void` | Wyczyść pogodę na X ticków |

### Biomy i środowisko
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.GetBiome(x, y, z)` | `string` | ID biomu (np. "minecraft:plains") |
| `World.GetBiomeCategory(x, y, z)` | `string` | Kategoria biomu |
| `World.GetTemperature(x, y, z)` | `float` | Temperatura (0.0-2.0) |
| `World.GetHumidity(x, y, z)` | `float` | Wilgotność (0.0-1.0) |
| `World.GetDownfall(x, y, z)` | `float` | Opady (0.0-1.0) |
| `World.GetFoliageColor(x, y, z)` | `int` | Kolor liści (RGB) |
| `World.GetGrassColor(x, y, z)` | `int` | Kolor trawy (RGB) |
| `World.GetWaterColor(x, y, z)` | `int` | Kolor wody (RGB) |
| `World.GetSkyColor(x, y, z)` | `int` | Kolor nieba (RGB) |
| `World.GetFogColor(x, y, z)` | `int` | Kolor mgły (RGB) |
| `World.IsSlimeChunk(x, z)` | `bool` | Czy slime chunk |
| `World.IsVillage(x, y, z)` | `bool` | Czy w wiosce |
| `World.IsStructureAt(x, y, z, structure)` | `bool` | Czy struktura w pozycji |
| `World.LocateStructure(structure, x, y, z, radius)` | `BlockPos` | Znajdź najbliższą strukturę |
| `World.LocateBiome(biome, x, y, z, radius)` | `BlockPos` | Znajdź najbliższy biom |
| `World.GetStructures()` | `List<string>` | Lista struktur w świecie |

### Eksplozje i efekty
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.CreateExplosion(x, y, z, power, fire?)` | `void` | Stwórz eksplozję |
| `World.CreateExplosion(x, y, z, power, fire?, destroy?)` | `void` | Eksplozja z opcjami |
| `World.CreateExplosion(x, y, z, power, fire?, destroy?, source?)` | `void` | Eksplozja ze źródłem |
| `World.StrikeLightning(x, y, z)` | `Entity` | Uderzenie pioruna (z obrażeniami) |
| `World.StrikeLightningEffect(x, y, z)` | `void` | Efekt pioruna (bez obrażeń) |
| `World.StrikeLightningCustom(x, y, z, damage?, fire?)` | `Entity` | Piorun z opcjami |
| `World.SpawnParticle(particle, x, y, z)` | `void` | Cząsteczka w punkcie |
| `World.SpawnParticle(particle, x, y, z, count)` | `void` | Wiele cząsteczek |
| `World.SpawnParticle(particle, x, y, z, count, dx, dy, dz, speed)` | `void` | Cząsteczki z spreadem |
| `World.SpawnParticle(particle, x, y, z, count, dx, dy, dz, speed, force?)` | `void` | Force = widoczne z daleka |
| `World.SpawnParticleLine(p, x1, y1, z1, x2, y2, z2, density)` | `void` | Linia cząsteczek |
| `World.SpawnParticleCircle(p, cx, cy, cz, radius, count)` | `void` | Okrąg cząsteczek |
| `World.SpawnParticleSphere(p, cx, cy, cz, radius, count)` | `void` | Kula cząsteczek |
| `World.SpawnParticleHelix(p, cx, cy, cz, height, turns, count)` | `void` | Helisa cząsteczek |
| `World.SpawnParticleCube(p, x1, y1, z1, x2, y2, z2, density)` | `void` | Sześcian cząsteczek |
| `World.PlaySound(sound, x, y, z, volume, pitch)` | `void` | Odtwórz dźwięk |
| `World.PlaySound(sound, x, y, z, volume, pitch, seed)` | `void` | Dźwięk z seedem |

### Światło
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.GetComputedLight(x, y, z)` | `int` | Połączone światło (block+sky) |
| `World.GetMaxLightLevel()` | `int` | Maksymalny poziom światła |
| `World.GetBrightness(x, y, z)` | `float` | Jasność (0.0-1.0) |
| `World.GetDayLight()` | `int` | Światło dzienne |
| `World.GetMoonLight()` | `int` | Światło księżyca |
| `World.IsDarkEnoughToSpawn(x, y, z)` | `bool` | Czy wystarczająco ciemno do spawnowania mobów |

### Świat — właściwości
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.Dimension` | `string` | ID wymiaru: "minecraft:overworld", "minecraft:the_nether", "minecraft:the_end" |
| `World.WorldType` | `string` | Typ świata: "default", "flat", "large_biomes", "amplified", "single_biome_surface" |
| `World.Seed` | `long` | Seed świata |
| `World.SeaLevel` | `int` | Poziom morza (zwykle 63) |
| `World.MaxBuildHeight` | `int` | Maksymalna wysokość budowania |
| `World.MinBuildHeight` | `int` | Minimalna wysokość budowania |
| `World.LogicalHeight` | `int` | Wysokość logiczna |
| `World.GetHorizonHeight()` | `int` | Wysokość horyzontu |
| `World.IsSurfaceWorld` | `bool` | Czy świat powierzchniowy |
| `World.HasSkyLight` | `bool` | Czy ma światło nieba |
| `World.HasCeiling` | `bool` | Czy ma sufit (nether) |
| `World.IsUltrawarm` | `bool` | Czy ultragorący (nether) |
| `World.HasRaids` | `bool` | Czy rajdy możliwe |
| `World.IsNatural` | `bool` | Czy naturalny wymiar |
| `World.CoordinateScale` | `double` | Skala koordynatów (nether = 8) |
| `World.PiglinSafe` | `bool` | Czy pigliny bezpieczne |
| `World.BedWorks` | `bool` | Czy łóżko działa |
| `World.RespawnAnchorWorks` | `bool` | Czy respawn anchor działa |
| `World.HasSpawnPoint` | `bool` | Czy ma punkt spawnu |
| `World.InfiniteBurn` | `bool` | Czy nieskończone palenie (nether) |
| `World.FixedTime` | `long` | Czy czas stały (jeśli ustawiony) |
| `World.GetSpawnPosition()` | `BlockPos` | Pozycja spawnu świata |
| `World.SetSpawnPosition(x, y, z)` | `void` | Ustaw spawn świata |
| `World.GetWorldBorder()` | `WorldBorder` | Granica świata |
| `World.SetWorldBorder(centerX, centerZ, size)` | `void` | Ustaw granicę |
| `World.SetWorldBorder(centerX, centerZ, size, damage, warning)` | `void` | Granica z opcjami |
| `World.GetDifficulty()` | `string` | Trudność: "peaceful", "easy", "normal", "hard" |
| `World.SetDifficulty(string)` | `void` | Ustaw trudność |
| `World.IsHardcore` | `bool` | Czy tryb hardcore |
| `World.SetHardcore(bool)` | `void` | Ustaw hardcore |
| `World.IsDebugWorld` | `bool` | Czy debug world |
| `World.IsFlatWorld` | `bool` | Czy superflat |
| `World.GetWorldFolder()` | `string` | Ścieżka folderu świata |

### GameRules
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.GetGameRule(rule)` | `object` | Pobierz gamerule (string/int/bool) |
| `World.SetGameRule(rule, value)` | `void` | Ustaw gamerule |
| `World.GetGameRules()` | `Dict<string, object>` | Wszystkie gamerule'y |
| `World.ResetGameRule(rule)` | `void` | Reset gamerule |
| `World.DoDaylightCycle` | `bool` | Get/set doDaylightCycle |
| `World.DoWeatherCycle` | `bool` | Get/set doWeatherCycle |
| `World.DoMobSpawning` | `bool` | Get/set doMobSpawning |
| `World.DoMobLoot` | `bool` | Mob loot |
| `World.DoTileDrops` | `bool` | Tile drops |
| `World.DoFireTick` | `bool` | Fire tick |
| `World.DoImmediateRespawn` | `bool` | Immediate respawn |
| `World.KeepInventory` | `bool` | Keep inventory |
| `World.MobGriefing` | `bool` | Mob griefing |
| `World.NaturalRegeneration` | `bool` | Natural regeneration |
| `World.RandomTickSpeed` | `int` | Random tick speed |
| `World.CommandBlockOutput` | `bool` | Command block output |
| `World.ShowDeathMessages` | `bool` | Death messages |
| `World.SpawnRadius` | `int` | Spawn radius |
| `World.MaxEntityCramming` | `int` | Max entity cramming |

### Scoreboard
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.CreateObjective(name, criteria, displayName)` | `void` | Stwórz objective |
| `World.RemoveObjective(name)` | `void` | Usuń objective |
| `World.GetObjective(name)` | `Objective` | Pobierz objective |
| `World.GetObjectives()` | `List<Objective>` | Lista objective'ów |
| `World.SetScore(player, objective, score)` | `void` | Ustaw score gracza |
| `World.GetScore(player, objective)` | `int` | Pobierz score gracza |
| `World.ResetScore(player, objective)` | `void` | Reset score |
| `World.ResetAllScores(player)` | `void` | Reset wszystkich score gracza |
| `World.DisplaySidebar(objective)` | `void` | Pokaż sidebar |
| `World.DisplayBelowName(objective)` | `void` | Pokaż pod nickiem |
| `World.DisplayPlayerList(objective)` | `void` | Pokaż na liście graczy |
| `World.ClearDisplay(slot)` | `void` | Wyczyść display slot |
| `World.CreateTeam(name)` | `void` | Stwórz team |
| `World.RemoveTeam(name)` | `void` | Usuń team |
| `World.GetTeam(name)` | `Team` | Pobierz team |
| `World.GetTeams()` | `List<Team>` | Lista teamów |
| `World.AddPlayerToTeam(player, team)` | `void` | Dodaj gracza do teamu |
| `World.RemovePlayerFromTeam(player)` | `void` | Usuń gracza z teamu |
| `World.GetPlayerTeam(player)` | `Team` | Team gracza |
| `World.SetTeamProperty(team, prop, value)` | `void` | Ustaw property teamu |

### BossBar
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.CreateBossBar(id, title, color, style)` | `BossBar` | Stwórz bossbara |
| `World.RemoveBossBar(id)` | `void` | Usuń bossbara |
| `World.GetBossBar(id)` | `BossBar` | Pobierz bossbara |
| `World.AddBossBarPlayer(id, player)` | `void` | Dodaj gracza do bossbara |
| `World.RemoveBossBarPlayer(id, player)` | `void` | Usuń gracza z bossbara |

### Komendy
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.RunCommand(command)` | `string` | Wykonaj komendę (zwraca output) |
| `World.RunCommandAs(player, command)` | `string` | Wykonaj komendę jako gracz |
| `World.RunCommandAs(entity, command)` | `string` | Wykonaj komendę jako encja |
| `World.RunCommandSilent(command)` | `void` | Wykonaj komendę cicho |
| `World.DispatchCommand(command)` | `int` | Dispatch command (return code) |

### Raids i struktury
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.GetRaids()` | `List<Raid>` | Lista aktywnych rajdów |
| `World.GetRaidAt(x, y, z)` | `Raid` | Rajd w pozycji |
| `World.StartRaid(x, y, z)` | `Raid` | Rozpocznij raj |
| `World.StopRaid(x, y, z)` | `void` | Zatrzymaj raj |
| `World.GetPoiPositions(poiType, x, y, z, radius)` | `List<BlockPos>` | POI w zasięgu |
| `World.GetChunkGenerator()` | `ChunkGenerator` | Generator chunka |
| `World.GetStructureManager()` | `StructureManager` | Manager struktur |

### Drop item
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.DropItem(item, x, y, z)` | `Entity` | Drop item w pozycji |
| `World.DropItem(item, x, y, z, count)` | `Entity` | Drop stack |
| `World.DropItemNaturally(item, x, y, z)` | `Entity` | Drop naturalny (losowy spread) |
| `World.DropExperience(x, y, z, amount)` | `void` | Drop exp |
| `World.DropExperienceOrb(x, y, z, value)` | `Entity` | Drop orb exp |

### Informacje
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.GetWorldName()` | `string` | Nazwa świata |
| `World.GetServer()` | `object` | Serwer Minecraft |
| `World.GetPlayersCount()` | `int` | Liczba graczy online |
| `World.GetMaxPlayers()` | `int` | Maksymalna liczba graczy |
| `World.IsEmpty()` | `bool` | Czy świat pusty (bez graczy) |
| `World.Save()` | `void` | Zapisz świat |
| `World.SaveChunk(x, z)` | `void` | Zapisz chunk |
| `World.SaveAll()` | `void` | Zapisz wszystko |
| `World.AutoSave` | `bool` | Auto-save włączony/wyłączony |
| `World.SetAutoSave(bool)` | `void` | Ustaw auto-save |

---

## Przykłady

### Budowanie
```glang
#version 1.0
#name "Builder Demo"

// Dom z powietrza
World.FillBlocks(0, 63, 0, 10, 63, 10, "minecraft:stone")       // podłoga
World.FillBlocks(0, 64, 0, 0, 68, 10, "minecraft:stone")        // ściana X
World.FillBlocks(10, 64, 0, 10, 68, 10, "minecraft:stone")      // ściana X+
World.FillBlocks(0, 64, 0, 10, 68, 0, "minecraft:stone")        // ściana Z
World.FillBlocks(0, 64, 10, 10, 68, 10, "minecraft:stone")      // ściana Z+
World.FillBlocks(0, 69, 0, 10, 69, 10, "minecraft:stone")       // dach
World.FillBlocks(1, 65, 0, 2, 66, 0, "minecraft:air")           // drzwi

// Oświetlenie
World.SetBlock(5, 64, 5, "minecraft:glowstone")

// Informacja
Chat.Send("§aDom zbudowany!")
```
