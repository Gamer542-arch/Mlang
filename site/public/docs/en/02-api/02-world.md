# World API — full documentation

## Method Reference

### Blocks — reading
| Method | Returns | Description |
|--------|--------|------|
| `World.GetBlock(x, y, z)` | `string` | Block ID (e.g. "minecraft:stone") |
| `World.GetBlockState(x, y, z)` | `string` | ID + properties (e.g. "minecraft:stone[facing=north]") |
| `World.GetBlockData(x, y, z)` | `BlockData` | BlockData object |
| `World.IsAir(x, y, z)` | `bool` | Whether the block is air |
| `World.IsSolid(x, y, z)` | `bool` | Whether the block is solid |
| `World.IsLiquid(x, y, z)` | `bool` | Whether the block is a liquid |
| `World.IsReplaceable(x, y, z)` | `bool` | Whether the block can be replaced |
| `World.IsOpaque(x, y, z)` | `bool` | Whether the block is opaque |
| `World.IsFlammable(x, y, z)` | `bool` | Whether the block is flammable |
| `World.IsSignalSource(x, y, z)` | `bool` | Whether the block emits a redstone signal |
| `World.IsPowered(x, y, z)` | `bool` | Whether the block is powered |
| `World.GetHardness(x, y, z)` | `float` | Block hardness |
| `World.GetBlastResistance(x, y, z)` | `float` | Blast resistance |
| `World.GetLightEmission(x, y, z)` | `int` | Light emitted by the block |
| `World.GetLightLevel(x, y, z)` | `int` | Light level (0-15) |
| `World.GetBlockLight(x, y, z)` | `int` | Block light |
| `World.GetSkyLight(x, y, z)` | `int` | Sky light |
| `World.GetAmbientDarkness(x, y, z)` | `int` | Ambient darkness |
| `World.GetBlockPosBelow(x, y, z)` | `BlockPos` | Block below |
| `World.GetBlockEntity(x, y, z)` | `BlockEntity` | Block entity (chest, furnace...) |
| `World.HasBlockEntity(x, y, z)` | `bool` | Whether the block has a block entity |
| `World.GetBlockTags(x, y, z)` | `List<string>` | Block tags |
| `World.IsInTag(x, y, z, tag)` | `bool` | Whether the block has a tag (e.g. "#minecraft:logs") |

### Blocks — writing
| Method | Returns | Description |
|--------|--------|------|
| `World.SetBlock(x, y, z, block)` | `bool` | Place a block |
| `World.SetBlock(x, y, z, block, flags)` | `bool` | Place a block with flags (update, physics, render) |
| `World.SetBlockWithData(x, y, z, block, properties)` | `bool` | Place a block with properties |
| `World.SetBlockState(x, y, z, state)` | `bool` | Place a BlockState |
| `World.BreakBlock(x, y, z)` | `void` | Break block (drop item) |
| `World.BreakBlock(x, y, z, drop)` | `void` | Break block (drop = true/false) |
| `World.ReplaceBlock(x, y, z, block)` | `bool` | Replace block (without update) |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block)` | `int` | Fill area with block (returns number changed) |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block, mode)` | `int` | Fill with mode: "replace", "destroy", "hollow", "outline" |
| `World.FillBlocks(x1, y1, z1, x2, y2, z2, block, mode, filter)` | `int` | Fill replacing only filter |
| `World.CloneBlocks(sx, sy, sz, ex, ey, ez, dx, dy, dz)` | `bool` | Clone area |
| `World.CloneBlocks(sx, sy, sz, ex, ey, ez, dx, dy, dz, mode)` | `bool` | Clone with mode: "force", "move", "normal" |
| `World.ReplaceBlocks(x1, y1, z1, x2, y2, z2, from, to)` | `int` | Replace blocks |
| `World.ClearRegion(x1, y1, z1, x2, y2, z2)` | `int` | Clear region (set to air) |
| `World.GetHighestBlockY(x, z)` | `int` | Highest block at X,Z |
| `World.GetHighestSolidBlockY(x, z)` | `int` | Highest solid block |
| `World.GetTopBlock(x, z)` | `string` | ID of the highest block |
| `World.GetSurfaceY(x, z)` | `int` | Surface Y (grass/sand) |

### Blocks — redstone and mechanics
| Method | Returns | Description |
|--------|--------|------|
| `World.EmitRedstone(x, y, z, power)` | `void` | Emit redstone signal |
| `World.ClearRedstone(x, y, z)` | `void` | Clear redstone signal |
| `World.GetRedstonePower(x, y, z)` | `int` | Redstone power (0-15) |
| `World.GetBestRedstonePower(x, y, z)` | `int` | Best redstone (from all sides) |
| `World.GetDirectRedstonePower(x, y, z)` | `int` | Direct redstone |
| `World.UpdateBlock(x, y, z)` | `void` | Force block update |
| `World.UpdateNeighbors(x, y, z)` | `void` | Update neighbors |
| `World.UpdateComparators(x, y, z)` | `void` | Update comparators |

### Blocks — special
| Method | Returns | Description |
|--------|--------|------|
| `World.SignSetText(x, y, z, lines[])` | `void` | Set sign text (4 lines) |
| `World.SignGetText(x, y, z)` | `string[]` | Get sign text |
| `World.SignSetColor(x, y, z, color)` | `void` | Set sign color |
| `World.LecternGetBook(x, y, z)` | `ItemStack` | Book from lectern |
| `World.LecternSetBook(x, y, z, book)` | `void` | Put book on lectern |
| `World.CommandBlockSetCommand(x, y, z, cmd)` | `void` | Set command in command block |
| `World.CommandBlockGetCommand(x, y, z)` | `string` | Get command from command block |
| `World.CommandBlockSetMode(x, y, z, mode)` | `void` | Mode: "impulse", "chain", "repeat" |
| `World.CommandBlockSetConditional(x, y, z, bool)` | `void` | Set conditional mode |
| `World.CommandBlockSetAlwaysActive(x, y, z, bool)` | `void` | Always active |
| `World.CommandBlockExecute(x, y, z)` | `void` | Execute command block |
| `World.SetSpawnerEntity(x, y, z, entity)` | `void` | Set mob spawner |
| `World.GetSpawnerEntity(x, y, z)` | `string` | Get spawner type |
| `World.SetSpawnerDelay(x, y, z, ticks)` | `void` | Set spawner delay |
| `World.SetSpawnerMinDelay(x, y, z, ticks)` | `void` | Min delay |
| `World.SetSpawnerMaxDelay(x, y, z, ticks)` | `void` | Max delay |
| `World.SetSpawnerSpawnRange(x, y, z, range)` | `void` | Spawn range |
| `World.SetSpawnerPlayerRange(x, y, z, range)` | `void` | Player detection range |
| `World.SetSpawnerMaxNearbyEntities(x, y, z, count)` | `void` | Max nearby entities |
| `World.SetSpawnerRequiredPlayerRange(x, y, z, range)` | `void` | Required player range |
| `World.JukeboxSetRecord(x, y, z, item)` | `void` | Put record in jukebox |
| `World.JukeboxGetRecord(x, y, z)` | `ItemStack` | Record from jukebox |
| `World.JukeboxPlay(x, y, z)` | `void` | Play jukebox |
| `World.JukeboxStop(x, y, z)` | `void` | Stop jukebox |
| `World.JukeboxIsPlaying(x, y, z)` | `bool` | Whether jukebox is playing |
| `World.BeehiveGetBeeCount(x, y, z)` | `int` | Number of bees in hive |
| `World.BeehiveSetBeeCount(x, y, z, count)` | `void` | Set bee count |
| `World.BeehiveGetHoneyLevel(x, y, z)` | `int` | Honey level (0-5) |
| `World.BeehiveSetHoneyLevel(x, y, z, level)` | `void` | Set honey level |

### Entities — spawning and removal
| Method | Returns | Description |
|--------|--------|------|
| `World.Summon(entity, x, y, z)` | `Entity` | Spawn entity |
| `World.Summon(entity, x, y, z, nbt)` | `Entity` | Spawn with NBT |
| `World.Summon(entity, x, y, z, nbt, spawnEvent)` | `Entity` | Spawn with event |
| `World.SpawnMob(type, x, y, z)` | `Entity` | Spawn a mob |
| `World.SpawnMob(type, x, y, z, count)` | `List<Entity>` | Spawn multiple mobs |
| `World.SpawnAnimal(type, x, y, z)` | `Entity` | Spawn an animal |
| `World.SpawnItem(item, x, y, z)` | `Entity` | Spawn item drop |
| `World.SpawnItem(item, x, y, z, count)` | `Entity` | Spawn item stack |
| `World.SpawnFallingBlock(block, x, y, z)` | `Entity` | Spawn falling block |
| `World.SpawnPrimedTNT(x, y, z, fuse)` | `Entity` | Spawn TNT |
| `World.SpawnFirework(x, y, z, item)` | `Entity` | Spawn firework |
| `World.SpawnAreaEffectCloud(x, y, z, effect)` | `Entity` | Spawn area effect cloud |
| `World.SpawnPainting(x, y, z, facing, motive)` | `Entity` | Spawn painting |
| `World.SpawnItemFrame(x, y, z, facing)` | `Entity` | Spawn item frame |
| `World.SpawnArmorStand(x, y, z)` | `Entity` | Spawn armor stand |
| `World.SpawnTextDisplay(text, x, y, z)` | `Entity` | Spawn text display (1.19+) |
| `World.SpawnTextDisplay(text, x, y, z, opts)` | `Entity` | Spawn text with options |
| `World.SpawnItemDisplay(item, x, y, z)` | `Entity` | Spawn item display |
| `World.SpawnBlockDisplay(block, x, y, z)` | `Entity` | Spawn block display |
| `World.Kill(entityId)` | `void` | Kill entity by ID |
| `World.Kill(entity)` | `void` | Kill entity |
| `World.KillAll(type)` | `int` | Kill all entities of type |
| `World.KillAll(type, radius)` | `int` | Kill in range |
| `World.Remove(entity)` | `void` | Remove entity (without drops) |
| `World.RemoveAll(type)` | `int` | Remove all entities of type |

### Entities — reading and searching
| Method | Returns | Description |
|--------|--------|------|
| `World.GetEntityById(id)` | `Entity` | Get entity by ID |
| `World.GetEntityByUUID(uuid)` | `Entity` | Get entity by UUID |
| `World.GetEntities()` | `List<Entity>` | All entities in the world |
| `World.GetEntitiesOfType(type)` | `List<Entity>` | Entities of a given type |
| `World.GetNearbyEntities(x, y, z, radius)` | `List<Entity>` | Entities within radius |
| `World.GetNearbyEntities(x, y, z, radius, type)` | `List<Entity>` | Entities of a given type within radius |
| `World.GetNearbyPlayers(x, y, z, radius)` | `List<Player>` | Players within radius |
| `World.GetPlayers()` | `List<Player>` | All online players |
| `World.GetPlayerByName(name)` | `Player` | Player by nickname |
| `World.GetPlayerByUUID(uuid)` | `Player` | Player by UUID |
| `World.GetEntityCount()` | `int` | Entity count |
| `World.GetEntityCount(type)` | `int` | Entity count of a given type |
| `World.GetChunkEntities(chunkX, chunkZ)` | `List<Entity>` | Entities in chunk |
| `World.IsChunkLoaded(x, z)` | `bool` | Whether chunk is loaded |
| `World.LoadChunk(x, z)` | `void` | Load chunk |
| `World.UnloadChunk(x, z)` | `void` | Unload chunk |
| `World.GetChunk(x, z)` | `Chunk` | Get chunk |
| `World.IsAreaLoaded(x1, y1, z1, x2, y2, z2)` | `bool` | Whether area is loaded |

### Time
| Method | Returns | Description |
|--------|--------|------|
| `World.Time` | `long` | World time (ticks, 0-24000) |
| `World.SetTime(long)` | `void` | Set time |
| `World.SetTimeAdd(long)` | `void` | Add to time |
| `World.GameTime` | `long` | Game time (total) |
| `World.DayTime` | `long` | Day time |
| `World.WorldAge` | `long` | World age (ticks) |
| `World.IsDay` | `bool` | Whether it is day (time 1000-13000) |
| `World.IsNight` | `bool` | Whether it is night |
| `World.IsDawn` | `bool` | Whether it is dawn |
| `World.IsDusk` | `bool` | Whether it is dusk |
| `World.GetMoonPhase()` | `int` | Moon phase (0-7) |
| `World.GetMoonSize()` | `float` | Moon size |
| `World.GetStarBrightness()` | `float` | Star brightness (0.0-1.0) |
| `World.GetSunAngle()` | `float` | Sun angle |
| `World.GetSkyAngle()` | `float` | Sky angle |
| `World.GetSkyDarkness()` | `float` | Sky darkness |

### Weather
| Method | Returns | Description |
|--------|--------|------|
| `World.Weather` | `string` | Weather: "clear", "rain", "thunder" |
| `World.SetWeather(string)` | `void` | Set weather |
| `World.SetWeather(string, duration)` | `void` | Set weather with duration |
| `World.IsRaining` | `bool` | Whether it is raining |
| `World.IsThundering` | `bool` | Whether it is thundering |
| `World.RainDuration` | `int` | Rain duration (ticks) |
| `World.SetRainDuration(int)` | `void` | Set rain duration |
| `World.ThunderDuration` | `int` | Thunder duration |
| `World.SetThunderDuration(int)` | `void` | Set thunder duration |
| `World.GetRainStrength()` | `float` | Rain strength (0.0-1.0) |
| `World.GetThunderStrength()` | `float` | Thunder strength (0.0-1.0) |
| `World.ClearWeather(int)` | `void` | Clear weather for X ticks |

### Biomes and environment
| Method | Returns | Description |
|--------|--------|------|
| `World.GetBiome(x, y, z)` | `string` | Biome ID (e.g. "minecraft:plains") |
| `World.GetBiomeCategory(x, y, z)` | `string` | Biome category |
| `World.GetTemperature(x, y, z)` | `float` | Temperature (0.0-2.0) |
| `World.GetHumidity(x, y, z)` | `float` | Humidity (0.0-1.0) |
| `World.GetDownfall(x, y, z)` | `float` | Downfall (0.0-1.0) |
| `World.GetFoliageColor(x, y, z)` | `int` | Foliage color (RGB) |
| `World.GetGrassColor(x, y, z)` | `int` | Grass color (RGB) |
| `World.GetWaterColor(x, y, z)` | `int` | Water color (RGB) |
| `World.GetSkyColor(x, y, z)` | `int` | Sky color (RGB) |
| `World.GetFogColor(x, y, z)` | `int` | Fog color (RGB) |
| `World.IsSlimeChunk(x, z)` | `bool` | Whether slime chunk |
| `World.IsVillage(x, y, z)` | `bool` | Whether in a village |
| `World.IsStructureAt(x, y, z, structure)` | `bool` | Whether structure at position |
| `World.LocateStructure(structure, x, y, z, radius)` | `BlockPos` | Find nearest structure |
| `World.LocateBiome(biome, x, y, z, radius)` | `BlockPos` | Find nearest biome |
| `World.GetStructures()` | `List<string>` | List of structures in the world |

### Explosions and effects
| Method | Returns | Description |
|--------|--------|------|
| `World.CreateExplosion(x, y, z, power, fire?)` | `void` | Create explosion |
| `World.CreateExplosion(x, y, z, power, fire?, destroy?)` | `void` | Explosion with options |
| `World.CreateExplosion(x, y, z, power, fire?, destroy?, source?)` | `void` | Explosion with source |
| `World.StrikeLightning(x, y, z)` | `Entity` | Lightning strike (with damage) |
| `World.StrikeLightningEffect(x, y, z)` | `void` | Lightning effect (without damage) |
| `World.StrikeLightningCustom(x, y, z, damage?, fire?)` | `Entity` | Lightning with options |
| `World.SpawnParticle(particle, x, y, z)` | `void` | Particle at a point |
| `World.SpawnParticle(particle, x, y, z, count)` | `void` | Multiple particles |
| `World.SpawnParticle(particle, x, y, z, count, dx, dy, dz, speed)` | `void` | Particles with spread |
| `World.SpawnParticle(particle, x, y, z, count, dx, dy, dz, speed, force?)` | `void` | Force = visible from afar |
| `World.SpawnParticleLine(p, x1, y1, z1, x2, y2, z2, density)` | `void` | Particle line |
| `World.SpawnParticleCircle(p, cx, cy, cz, radius, count)` | `void` | Particle circle |
| `World.SpawnParticleSphere(p, cx, cy, cz, radius, count)` | `void` | Particle sphere |
| `World.SpawnParticleHelix(p, cx, cy, cz, height, turns, count)` | `void` | Particle helix |
| `World.SpawnParticleCube(p, x1, y1, z1, x2, y2, z2, density)` | `void` | Particle cube |
| `World.PlaySound(sound, x, y, z, volume, pitch)` | `void` | Play sound |
| `World.PlaySound(sound, x, y, z, volume, pitch, seed)` | `void` | Sound with seed |

### Light
| Method | Returns | Description |
|--------|--------|------|
| `World.GetComputedLight(x, y, z)` | `int` | Combined light (block+sky) |
| `World.GetMaxLightLevel()` | `int` | Maximum light level |
| `World.GetBrightness(x, y, z)` | `float` | Brightness (0.0-1.0) |
| `World.GetDayLight()` | `int` | Daylight |
| `World.GetMoonLight()` | `int` | Moonlight |
| `World.IsDarkEnoughToSpawn(x, y, z)` | `bool` | Whether dark enough for mob spawning |

### World — properties
| Method | Returns | Description |
|--------|--------|------|
| `World.Dimension` | `string` | Dimension ID: "minecraft:overworld", "minecraft:the_nether", "minecraft:the_end" |
| `World.WorldType` | `string` | World type: "default", "flat", "large_biomes", "amplified", "single_biome_surface" |
| `World.Seed` | `long` | World seed |
| `World.SeaLevel` | `int` | Sea level (usually 63) |
| `World.MaxBuildHeight` | `int` | Maximum build height |
| `World.MinBuildHeight` | `int` | Minimum build height |
| `World.LogicalHeight` | `int` | Logical height |
| `World.GetHorizonHeight()` | `int` | Horizon height |
| `World.IsSurfaceWorld` | `bool` | Whether surface world |
| `World.HasSkyLight` | `bool` | Whether it has sky light |
| `World.HasCeiling` | `bool` | Whether it has a ceiling (nether) |
| `World.IsUltrawarm` | `bool` | Whether ultrawarm (nether) |
| `World.HasRaids` | `bool` | Whether raids possible |
| `World.IsNatural` | `bool` | Whether natural dimension |
| `World.CoordinateScale` | `double` | Coordinate scale (nether = 8) |
| `World.PiglinSafe` | `bool` | Whether piglins are safe |
| `World.BedWorks` | `bool` | Whether beds work |
| `World.RespawnAnchorWorks` | `bool` | Whether respawn anchors work |
| `World.HasSpawnPoint` | `bool` | Whether it has a spawn point |
| `World.InfiniteBurn` | `bool` | Whether infinite burning (nether) |
| `World.FixedTime` | `long` | Whether time is fixed (if set) |
| `World.GetSpawnPosition()` | `BlockPos` | World spawn position |
| `World.SetSpawnPosition(x, y, z)` | `void` | Set world spawn |
| `World.GetWorldBorder()` | `WorldBorder` | World border |
| `World.SetWorldBorder(centerX, centerZ, size)` | `void` | Set border |
| `World.SetWorldBorder(centerX, centerZ, size, damage, warning)` | `void` | Border with options |
| `World.GetDifficulty()` | `string` | Difficulty: "peaceful", "easy", "normal", "hard" |
| `World.SetDifficulty(string)` | `void` | Set difficulty |
| `World.IsHardcore` | `bool` | Whether hardcore mode |
| `World.SetHardcore(bool)` | `void` | Set hardcore |
| `World.IsDebugWorld` | `bool` | Whether debug world |
| `World.IsFlatWorld` | `bool` | Whether superflat |
| `World.GetWorldFolder()` | `string` | World folder path |

### GameRules
| Method | Returns | Description |
|--------|--------|------|
| `World.GetGameRule(rule)` | `object` | Get gamerule (string/int/bool) |
| `World.SetGameRule(rule, value)` | `void` | Set gamerule |
| `World.GetGameRules()` | `Dict<string, object>` | All gamerules |
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
| Method | Returns | Description |
|--------|--------|------|
| `World.CreateObjective(name, criteria, displayName)` | `void` | Create objective |
| `World.RemoveObjective(name)` | `void` | Remove objective |
| `World.GetObjective(name)` | `Objective` | Get objective |
| `World.GetObjectives()` | `List<Objective>` | List of objectives |
| `World.SetScore(player, objective, score)` | `void` | Set player score |
| `World.GetScore(player, objective)` | `int` | Get player score |
| `World.ResetScore(player, objective)` | `void` | Reset score |
| `World.ResetAllScores(player)` | `void` | Reset all player scores |
| `World.DisplaySidebar(objective)` | `void` | Show sidebar |
| `World.DisplayBelowName(objective)` | `void` | Show below name |
| `World.DisplayPlayerList(objective)` | `void` | Show on player list |
| `World.ClearDisplay(slot)` | `void` | Clear display slot |
| `World.CreateTeam(name)` | `void` | Create team |
| `World.RemoveTeam(name)` | `void` | Remove team |
| `World.GetTeam(name)` | `Team` | Get team |
| `World.GetTeams()` | `List<Team>` | List of teams |
| `World.AddPlayerToTeam(player, team)` | `void` | Add player to team |
| `World.RemovePlayerFromTeam(player)` | `void` | Remove player from team |
| `World.GetPlayerTeam(player)` | `Team` | Player's team |
| `World.SetTeamProperty(team, prop, value)` | `void` | Set team property |

### BossBar
| Method | Returns | Description |
|--------|--------|------|
| `World.CreateBossBar(id, title, color, style)` | `BossBar` | Create boss bar |
| `World.RemoveBossBar(id)` | `void` | Remove boss bar |
| `World.GetBossBar(id)` | `BossBar` | Get boss bar |
| `World.AddBossBarPlayer(id, player)` | `void` | Add player to boss bar |
| `World.RemoveBossBarPlayer(id, player)` | `void` | Remove player from boss bar |

### Commands
| Method | Returns | Description |
|--------|--------|------|
| `World.RunCommand(command)` | `string` | Execute command (returns output) |
| `World.RunCommandAs(player, command)` | `string` | Execute command as player |
| `World.RunCommandAs(entity, command)` | `string` | Execute command as entity |
| `World.RunCommandSilent(command)` | `void` | Execute command silently |
| `World.DispatchCommand(command)` | `int` | Dispatch command (return code) |

### Raids and structures
| Method | Returns | Description |
|--------|--------|------|
| `World.GetRaids()` | `List<Raid>` | List of active raids |
| `World.GetRaidAt(x, y, z)` | `Raid` | Raid at position |
| `World.StartRaid(x, y, z)` | `Raid` | Start raid |
| `World.StopRaid(x, y, z)` | `void` | Stop raid |
| `World.GetPoiPositions(poiType, x, y, z, radius)` | `List<BlockPos>` | POI within radius |
| `World.GetChunkGenerator()` | `ChunkGenerator` | Chunk generator |
| `World.GetStructureManager()` | `StructureManager` | Structure manager |

### Dropping items
| Method | Returns | Description |
|--------|--------|------|
| `World.DropItem(item, x, y, z)` | `Entity` | Drop item at position |
| `World.DropItem(item, x, y, z, count)` | `Entity` | Drop stack |
| `World.DropItemNaturally(item, x, y, z)` | `Entity` | Natural drop (random spread) |
| `World.DropExperience(x, y, z, amount)` | `void` | Drop exp |
| `World.DropExperienceOrb(x, y, z, value)` | `Entity` | Drop exp orb |

### Information
| Method | Returns | Description |
|--------|--------|------|
| `World.GetWorldName()` | `string` | World name |
| `World.GetServer()` | `object` | Minecraft server |
| `World.GetPlayersCount()` | `int` | Online player count |
| `World.GetMaxPlayers()` | `int` | Maximum player count |
| `World.IsEmpty()` | `bool` | Whether world is empty (no players) |
| `World.Save()` | `void` | Save world |
| `World.SaveChunk(x, z)` | `void` | Save chunk |
| `World.SaveAll()` | `void` | Save everything |
| `World.AutoSave` | `bool` | Auto-save enabled/disabled |
| `World.SetAutoSave(bool)` | `void` | Set auto-save |

---

## Examples

### Building
```glang
#version 1.0
#name "Builder Demo"

// House from scratch
World.FillBlocks(0, 63, 0, 10, 63, 10, "minecraft:stone")       // floor
World.FillBlocks(0, 64, 0, 0, 68, 10, "minecraft:stone")        // X wall
World.FillBlocks(10, 64, 0, 10, 68, 10, "minecraft:stone")      // X+ wall
World.FillBlocks(0, 64, 0, 10, 68, 0, "minecraft:stone")        // Z wall
World.FillBlocks(0, 64, 10, 10, 68, 10, "minecraft:stone")      // Z+ wall
World.FillBlocks(0, 69, 0, 10, 69, 10, "minecraft:stone")       // roof
World.FillBlocks(1, 65, 0, 2, 66, 0, "minecraft:air")           // door

// Lighting
World.SetBlock(5, 64, 5, "minecraft:glowstone")

// Info
Chat.Send("§aHouse built!")
```
