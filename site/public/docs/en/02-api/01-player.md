# Player API — full documentation

## Method Reference

### Position and movement
| Method | Returns | Description |
|--------|--------|------|
| `Player.X` | `double` | X coordinate |
| `Player.Y` | `double` | Y coordinate |
| `Player.Z` | `double` | Z coordinate |
| `Player.Yaw` | `float` | Horizontal angle (Y rotation) |
| `Player.Pitch` | `float` | Vertical angle (X rotation) |
| `Player.TeleportTo(x, y, z)` | `bool` | Teleport to coordinates |
| `Player.TeleportTo(x, y, z, yaw, pitch)` | `bool` | Teleport with rotation |
| `Player.TeleportTo(player)` | `bool` | Teleport to another player |
| `Player.TeleportTo(entity)` | `bool` | Teleport to entity |
| `Player.SetPosition(x, y, z)` | `void` | Set position (without lerp) |
| `Player.SetRotation(yaw, pitch)` | `void` | Set rotation |
| `Player.LookAt(x, y, z)` | `void` | Look at a point |
| `Player.LookAt(entity)` | `void` | Look at an entity |
| `Player.GetBlockPos()` | `BlockPos` | Position as block (int) |
| `Player.GetChunkPos()` | `ChunkPos` | Chunk position |
| `Player.DistanceTo(x, y, z)` | `double` | Distance to a point |
| `Player.DistanceTo(entity)` | `double` | Distance to an entity |
| `Player.DistanceToSqr(x, y, z)` | `double` | Distance² to a point |
| `Player.IsInRange(x, y, z, radius)` | `bool` | Whether the player is in range |

### Movement and controls
| Method | Returns | Description |
|--------|--------|------|
| `Player.Velocity` | `Vector3` | Current velocity |
| `Player.SetVelocity(vx, vy, vz)` | `void` | Set velocity |
| `Player.AddVelocity(vx, vy, vz)` | `void` | Add velocity |
| `Player.Knockback(strength, x, z)` | `void` | Knockback |
| `Player.Jump()` | `void` | Force jump |
| `Player.SetJumping(bool)` | `void` | Set jumping state |
| `Player.IsJumping` | `bool` | Whether the player is jumping |
| `Player.Sprint(bool)` | `void` | Enable/disable sprinting |
| `Player.IsSprinting` | `bool` | Whether the player is sprinting |
| `Player.Sneak(bool)` | `void` | Enable/disable sneaking |
| `Player.IsSneaking` | `bool` | Whether the player is sneaking |
| `Player.Fly(bool)` | `void` | Enable/disable flying |
| `Player.IsFlying` | `bool` | Whether the player is flying |
| `Player.SetFlySpeed(float)` | `void` | Flying speed (0.0-1.0) |
| `Player.SetWalkSpeed(float)` | `void` | Walking speed (0.0-1.0) |
| `Player.Swim(bool)` | `void` | Enable/disable swimming |
| `Player.IsSwimming` | `bool` | Whether the player is swimming |
| `Player.SetGliding(bool)` | `void` | Enable/disable gliding (elytra) |
| `Player.IsGliding` | `bool` | Whether the player is gliding |
| `Player.SetFallFlying(bool)` | `void` | Enable/disable fall flying |
| `Player.IsFallFlying` | `bool` | Whether the player is fall flying |
| `Player.SetSprinting(bool)` | `void` | Sprint |
| `Player.SwingHand(hand?)` | `void` | Swing hand (main/off) |
| `Player.Attack()` | `void` | Attack (left click) |
| `Player.Interact()` | `void` | Interact (right click) |
| `Player.PickBlock()` | `void` | Pick block (middle click) |
| `Player.DropItem(dropAll?)` | `void` | Drop item |
| `Player.UseItem()` | `void` | Use item |

### Health and hunger
| Method | Returns | Description |
|--------|--------|------|
| `Player.Health` | `float` | Current HP |
| `Player.MaxHealth` | `float` | Maximum HP |
| `Player.SetHealth(float)` | `void` | Set HP |
| `Player.SetMaxHealth(float)` | `void` | Set max HP |
| `Player.Heal(amount)` | `void` | Heal by amount |
| `Player.Damage(amount)` | `void` | Deal damage |
| `Player.Damage(amount, source)` | `void` | Deal damage (type) |
| `Player.Kill()` | `void` | Kill the player |
| `Player.IsAlive` | `bool` | Whether the player is alive |
| `Player.IsDead` | `bool` | Whether the player is dead |
| `Player.DeathTime` | `int` | Time since death (ticks) |
| `Player.FoodLevel` | `int` | Hunger level (0-20) |
| `Player.SetFoodLevel(int)` | `void` | Set hunger |
| `Player.Saturation` | `float` | Saturation (0.0-5.0) |
| `Player.SetSaturation(float)` | `void` | Set saturation |
| `Player.Exhaustion` | `float` | Exhaustion (0.0-4.0) |
| `Player.SetExhaustion(float)` | `void` | Set exhaustion |
| `Player.AirSupply` | `int` | Air level (0-300) |
| `Player.SetAirSupply(int)` | `void` | Set air |
| `Player.MaxAir` | `int` | Maximum air |
| `Player.FireTicks` | `int` | Ticks on fire (-20 = not on fire, 0 = on fire) |
| `Player.SetFireTicks(int)` | `void` | Set fire ticks |
| `Player.FireImmuneTicks` | `int` | Fire immunity ticks |
| `Player.SetFireImmuneTicks(int)` | `void` | Set fire immunity |
| `Player.FrozenTicks` | `int` | Frozen ticks |
| `Player.SetFrozenTicks(int)` | `void` | Set frozen |
| `Player.IsOnFire` | `bool` | Whether the player is burning |
| `Player.IsOnGround` | `bool` | Whether the player is on the ground |
| `Player.IsInWater` | `bool` | Whether the player is in water |
| `Player.IsInLava` | `bool` | Whether the player is in lava |
| `Player.IsUnderwater` | `bool` | Whether the player is underwater |
| `Player.IsWet` | `bool` | Whether the player is wet (water/rain) |
| `Player.IsInRain` | `bool` | Whether the player is in rain |
| `Player.IsInBubbleColumn` | `bool` | Whether in a bubble column |
| `Player.IsInsideWall` | `bool` | Whether the player is inside a wall |
| `Player.FallDistance` | `float` | Fall distance |
| `Player.SetFallDistance(float)` | `void` | Reset/change fall distance |
| `Player.Absorption` | `float` | Absorption (golden hearts) |
| `Player.SetAbsorption(float)` | `void` | Set absorption |
| `Player.StingerCount` | `int` | Number of stingers (bees) |
| `Player.SetStingerCount(int)` | `void` | Set stingers |
| `Player.ArrowCount` | `int` | Number of arrows in body |
| `Player.SetArrowCount(int)` | `void` | Set arrows |

### Game mode and permissions
| Method | Returns | Description |
|--------|--------|------|
| `Player.GameMode` | `string` | Game mode: "survival", "creative", "adventure", "spectator" |
| `Player.SetGameMode(string)` | `void` | Change game mode |
| `Player.IsCreative` | `bool` | Whether creative mode |
| `Player.IsSpectator` | `bool` | Whether spectator mode |
| `Player.IsAdventure` | `bool` | Whether adventure mode |
| `Player.IsSurvival` | `bool` | Whether survival mode |
| `Player.IsOp` | `bool` | Whether server operator |
| `Player.SetOp(bool)` | `void` | Grant/revoke OP |
| `Player.AllowFlight` | `bool` | Whether flight is allowed |
| `Player.SetAllowFlight(bool)` | `void` | Allow flight |
| `Player.FlyingSpeed` | `float` | Flying speed |
| `Player.SetFlyingSpeed(float)` | `void` | Set flying speed |
| `Player.WalkSpeed` | `float` | Walking speed |
| `Player.SetWalkSpeed(float)` | `void` | Set walking speed |
| `Player.ViewDistance` | `int` | View distance |
| `Player.SetViewDistance(int)` | `void` | Set view distance |
| `Player.CanFly` | `bool` | Whether the player can fly |
| `Player.CanSee(entity)` | `bool` | Whether the player can see the entity |
| `Player.HasLineOfSight(x, y, z)` | `bool` | Whether the player has line of sight |

### Inventory and items
| Method | Returns | Description |
|--------|--------|------|
| `Player.MainHandItem` | `ItemStack` | Item in main hand |
| `Player.OffHandItem` | `ItemStack` | Item in off hand |
| `Player.SetMainHandItem(item)` | `void` | Set item in main hand |
| `Player.SetOffHandItem(item)` | `void` | Set item in off hand |
| `Player.ArmorHelmet` | `ItemStack` | Helmet |
| `Player.ArmorChest` | `ItemStack` | Chestplate |
| `Player.ArmorLegs` | `ItemStack` | Leggings |
| `Player.ArmorBoots` | `ItemStack` | Boots |
| `Player.SetArmorHelmet(item)` | `void` | Set helmet |
| `Player.SetArmorChest(item)` | `void` | Set chestplate |
| `Player.SetArmorLegs(item)` | `void` | Set leggings |
| `Player.SetArmorBoots(item)` | `void` | Set boots |
| `Player.SetArmor(items[])` | `void` | Set full armor |
| `Player.GiveItem(item, count?)` | `void` | Give item to player |
| `Player.GiveItem(ItemStack)` | `void` | Give item stack |
| `Player.RemoveItem(item, count?)` | `void` | Remove item from inventory |
| `Player.ClearInventory()` | `void` | Clear inventory |
| `Player.HasItem(item)` | `bool` | Whether has item (id) |
| `Player.HasItem(ItemStack)` | `bool` | Whether has item stack |
| `Player.ItemCount(item)` | `int` | Item count in inventory |
| `Player.GetItemInSlot(slot)` | `ItemStack` | Item in slot (0-40) |
| `Player.SetItemInSlot(slot, item)` | `void` | Set item in slot |
| `Player.GetSelectedSlot()` | `int` | Selected hotbar slot (0-8) |
| `Player.SetSelectedSlot(int)` | `void` | Select hotbar slot |
| `Player.GetInventory()` | `Inventory` | Reference to Inventory API |
| `Player.GetEnderChest()` | `Inventory` | Player's ender chest |
| `Player.OpenInventory(inv)` | `void` | Open inventory GUI |
| `Player.CloseScreen()` | `void` | Close open screen |
| `Player.IsScreenOpen` | `bool` | Whether any screen is open |
| `Player.DropItemStack()` | `void` | Drop entire stack |
| `Player.DropSelectedItem()` | `void` | Drop selected item |

### Experience
| Method | Returns | Description |
|--------|--------|------|
| `Player.Experience` | `int` | Total XP |
| `Player.Level` | `int` | Experience level |
| `Player.ExperienceBar` | `float` | XP bar (0.0-1.0) |
| `Player.SetExperience(int)` | `void` | Set total XP |
| `Player.SetLevel(int)` | `void` | Set level |
| `Player.GiveExperience(int)` | `void` | Add XP |
| `Player.GiveExperienceLevels(int)` | `void` | Add levels |
| `Player.GetXpNeededForNextLevel()` | `int` | XP needed for next level |
| `Player.GetXpProgress()` | `float` | Progress to next level (0.0-1.0) |
| `Player.GetTotalExperience()` | `int` | Total XP as a number |

### Status effects
| Method | Returns | Description |
|--------|--------|------|
| `Player.AddEffect(effect, duration, amplifier)` | `void` | Add effect |
| `Player.AddEffect(effect, duration, amplifier, particles?, icon?)` | `void` | Add effect with options |
| `Player.RemoveEffect(effect)` | `void` | Remove effect |
| `Player.ClearEffects()` | `void` | Clear all effects |
| `Player.HasEffect(effect)` | `bool` | Whether has effect |
| `Player.GetEffect(effect)` | `Effect` | Get effect |
| `Player.GetEffects()` | `List<Effect>` | List of all effects |
| `Player.IsAffectedByEffects` | `bool` | Whether affected by any effect |

### Screen and display
| Method | Returns | Description |
|--------|--------|------|
| `Player.ShowTitle(title)` | `void` | Show title (large text) |
| `Player.ShowTitle(title, subtitle, fadeIn, stay, fadeOut)` | `void` | Title with options |
| `Player.ShowSubtitle(subtitle)` | `void` | Subtitle |
| `Player.ShowActionBar(text)` | `void` | Text above the HP bar |
| `Player.SendMessage(text)` | `void` | Private chat message |
| `Player.SendMessage(text, position)` | `void` | Message at position: chat, action_bar, system |
| `Player.SendHotbarMessage(text)` | `void` | Quick message in hotbar |
| `Player.ResetTitle()` | `void` | Reset title |
| `Player.ClearTitle()` | `void` | Clear title |
| `Player.SetTitleTimes(fadeIn, stay, fadeOut)` | `void` | Set title timings |
| `Player.SetSubtitle(subtitle)` | `void` | Set subtitle (before show) |
| `Player.ShowBossBar(bar)` | `void` | Show boss bar |
| `Player.HideBossBar()` | `void` | Hide boss bar |

### Sounds
| Method | Returns | Description |
|--------|--------|------|
| `Player.PlaySound(sound)` | `void` | Play sound |
| `Player.PlaySound(sound, volume, pitch)` | `void` | Sound with volume |
| `Player.PlaySound(sound, volume, pitch, x, y, z)` | `void` | Sound at position |
| `Player.StopSound(sound)` | `void` | Stop sound |
| `Player.StopAllSounds()` | `void` | Stop all sounds |

### Camera and view
| Method | Returns | Description |
|--------|--------|------|
| `Player.SetCameraEntity(entity)` | `void` | Set camera on an entity |
| `Player.SetCameraEntity(player)` | `void` | Set camera on a player |
| `Player.ResetCamera()` | `void` | Restore normal camera |
| `Player.SetRenderDistance(int)` | `void` | Render distance |
| `Player.SetFovMultiplier(float)` | `void` | FOV multiplier |

### Statistics and advancements
| Method | Returns | Description |
|--------|--------|------|
| `Player.GetStatistic(type, key)` | `int` | Get statistic |
| `Player.SetStatistic(type, key, value)` | `void` | Set statistic |
| `Player.ResetStatistic(type, key)` | `void` | Reset statistic |
| `Player.GetAdvancementProgress(adv)` | `string` | Advancement progress |
| `Player.GrantAdvancement(adv)` | `void` | Grant advancement |
| `Player.RevokeAdvancement(adv)` | `void` | Revoke advancement |
| `Player.HasAdvancement(adv)` | `bool` | Whether has advancement |

### World interaction
| Method | Returns | Description |
|--------|--------|------|
| `Player.OpenChest(x, y, z)` | `Inventory` | Open chest |
| `Player.OpenWorkbench()` | `void` | Open crafting table |
| `Player.OpenFurnace(x, y, z)` | `void` | Open furnace |
| `Player.OpenEnchantingTable(x, y, z)` | `void` | Open enchantment table |
| `Player.OpenAnvil(x, y, z)` | `void` | Open anvil |
| `Player.OpenGrindstone(x, y, z)` | `void` | Open grindstone |
| `Player.OpenCartographyTable(x, y, z)` | `void` | Open cartography table |
| `Player.OpenLoom(x, y, z)` | `void` | Open loom |
| `Player.OpenStonecutter(x, y, z)` | `void` | Open stonecutter |
| `Player.OpenSmithingTable(x, y, z)` | `void` | Open smithing table |
| `Player.OpenBrewingStand(x, y, z)` | `void` | Open brewing stand |
| `Player.OpenHopper(x, y, z)` | `void` | Open hopper |
| `Player.OpenBarrel(x, y, z)` | `void` | Open barrel |
| `Player.OpenShulkerBox(x, y, z)` | `void` | Open shulker box |
| `Player.BreakBlock(x, y, z)` | `void` | Break block (as click) |
| `Player.InteractBlock(x, y, z)` | `void` | Interact with block |
| `Player.InteractEntity(entity)` | `void` | Interact with entity |
| `Player.AttackEntity(entity)` | `void` | Attack entity |
| `Player.Sleep(x, y, z)` | `bool` | Go to sleep |
| `Player.WakeUp()` | `void` | Wake up |
| `Player.IsSleeping` | `bool` | Whether the player is sleeping |
| `Player.SleepTimer` | `int` | Sleep timer (ticks) |
| `Player.Respawn()` | `void` | Respawn the player |

### Riding and vehicles
| Method | Returns | Description |
|--------|--------|------|
| `Player.StartRiding(entity)` | `bool` | Ride an entity |
| `Player.StopRiding()` | `void` | Dismount |
| `Player.IsRiding` | `bool` | Whether the player is riding something |
| `Player.Vehicle` | `Entity` | Vehicle the player is riding |
| `Player.GetPassengers()` | `List<Entity>` | List of passengers (when someone is riding the player) |
| `Player.HasControllingPassenger` | `bool` | Whether someone is controlling the player |
| `Player.GetControllingPassenger()` | `Entity` | Who is controlling the player |
| `Player.Dismount()` | `void` | Dismount from vehicle |
| `Player.Mount(entity)` | `void` | Mount an entity |
| `Player.SetYaw(float)` | `void` | Set horizontal angle |
| `Player.SetPitch(float)` | `void` | Set vertical angle |

### Attacks and combat
| Method | Returns | Description |
|--------|--------|------|
| `Player.GetAttackCooldown()` | `float` | Attack cooldown (0.0-1.0) |
| `Player.ResetAttackCooldown()` | `void` | Reset cooldown |
| `Player.GetLastAttackTime()` | `int` | Tick of last attack |
| `Player.IsBlocking` | `bool` | Whether the player is blocking (shield) |
| `Player.IsClimbing` | `bool` | Whether the player is climbing |
| `Player.GetLastHurtByEntity()` | `Entity` | Last entity that hurt the player |
| `Player.GetLastHurtByPlayer()` | `Player` | Last player that hurt the player |
| `Player.GetLastHurtEntity()` | `Entity` | Last entity hurt by the player |
| `Player.GetLastDamageSource()` | `string` | Last damage source |
| `Player.GetLastDamageAmount()` | `float` | Last damage amount |
| `Player.InvulnerableTime` | `int` | Invulnerability ticks after attack |
| `Player.SetInvulnerableTime(int)` | `void` | Set invulnerability ticks |

### Player information
| Method | Returns | Description |
|--------|--------|------|
| `Player.Name` | `string` | Player nickname |
| `Player.UUID` | `string` | Player UUID (with hyphens) |
| `Player.UUIDShort` | `string` | UUID without hyphens |
| `Player.DisplayName` | `string` | Display name (with colors) |
| `Player.SetDisplayName(string)` | `void` | Set display name |
| `Player.PlayerListName` | `string` | Name on player list |
| `Player.SetPlayerListName(string)` | `void` | Set name on player list |
| `Player.GetPlayerList()` | `List<Player>` | List of all online players |
| `Player.GetWorld()` | `World` | World the player is in |
| `Player.Dimension` | `string` | Dimension: "overworld", "nether", "end" |
| `Player.GetSpawnPosition()` | `BlockPos` | Spawn position |
| `Player.SetSpawnPosition(x, y, z)` | `void` | Set spawn position |
| `Player.SetSpawnPosition(x, y, z, force)` | `void` | Set spawn (force=true overrides) |
| `Player.Ping` | `int` | Player ping (ms) |
| `Player.Locale` | `string` | Player language (e.g. "pl_PL") |
| `Player.SkinUrl` | `string` | Player skin URL |
| `Player.CapeUrl` | `string` | Cape URL (if present) |
| `Player.ModelType` | `string` | Model type: "default" / "slim" |
| `Player.MainArm` | `string` | Main arm: "right" / "left" |
| `Player.SetMainArm(string)` | `void` | Set main arm |
| `Player.ClientBrand` | `string` | Player client (e.g. "vanilla", "fabric") |
| `Player.ServerBrand` | `string` | Server brand |
| `Player.ChunkX` | `int` | Player chunk X |
| `Player.ChunkZ` | `int` | Player chunk Z |
| `Player.ChunkY` | `int` | Player chunk Y |
| `Player.GetScore()` | `int` | Player score |
| `Player.SetScore(int)` | `void` | Set score |

### NBT
| Method | Returns | Description |
|--------|--------|------|
| `Player.GetNBT()` | `string` | Get player NBT as string |
| `Player.SetNBT(string)` | `void` | Set entire player NBT |
| `Player.MergeNBT(string)` | `void` | Merge NBT (add/modify fields) |
| `Player.GetPersistentData()` | `NBTCompound` | Persistent data (mod data) |
| `Player.SetPersistentData(key, value)` | `void` | Save persistent data |
| `Player.GetPersistentData(key)` | `object` | Read persistent data |

### Scoreboard and teams
| Method | Returns | Description |
|--------|--------|------|
| `Player.GetScoreboardObjective(objective)` | `int` | Score in objective |
| `Player.SetScoreboardObjective(objective, score)` | `void` | Set score in objective |
| `Player.GetTeam()` | `string` | Player's team name |
| `Player.SetTeam(team)` | `void` | Add to team |
| `Player.RemoveFromTeam()` | `void` | Remove from team |
| `Player.GetTeamColor()` | `string` | Team color (hex) |

### Sending packets
| Method | Returns | Description |
|--------|--------|------|
| `Player.SendPacket(packet)` | `void` | Send packet to player |
| `Player.SendBlockUpdate(x, y, z)` | `void` | Send block update |
| `Player.SendLightUpdate(x, y, z)` | `void` | Send light update |
| `Player.SendSignText(x, y, z, lines[])` | `void` | Send sign text |

### Misc
| Method | Returns | Description |
|--------|--------|------|
| `Player.GetRiptideTicks()` | `int` | Riptide ticks (trident) |
| `Player.SetRiptideTicks(int)` | `void` | Set riptide ticks |
| `Player.GetPortalCooldown()` | `int` | Portal cooldown |
| `Player.SetPortalCooldown(int)` | `void` | Set portal cooldown |
| `Player.GetPortalWaitTime()` | `int` | Time waiting in portal |
| `Player.IsUsingItem` | `bool` | Whether the player is using an item |
| `Player.GetUsingItem()` | `ItemStack` | Item being used |
| `Player.GetActiveItem()` | `ItemStack` | Active item |
| `Player.GetActiveItemUseTime()` | `int` | Item use time |
| `Player.BedPosition` | `BlockPos` | Bed position |
| `Player.HasBed` | `bool` | Whether has a bed set |
| `Player.GetChunkCoordIntPair()` | `string` | Player chunk as string |

---

## Examples

### Full player control
```glang
#version 1.0
#name "Player Control Demo"
#key F6

// Teleportation and movement
Player.TeleportTo(100, 64, -200)
Player.SetWalkSpeed(0.5f)
Player.SetFlySpeed(0.3f)
Player.Fly(true)

// Health
Player.SetMaxHealth(40)
Player.SetHealth(40)
Player.AddEffect("regeneration", 200, 2)
Player.AddEffect("speed", 600, 1)

// Inventory
Player.GiveItem("minecraft:diamond_sword", 1)
Player.GiveItem("minecraft:elytra", 1)
Player.SetArmor(
    "minecraft:diamond_helmet",
    "minecraft:diamond_chestplate",
    "minecraft:diamond_leggings",
    "minecraft:diamond_boots"
)

// Display
Player.ShowTitle("§6Hello!", "§7MLang Demo", 10, 70, 20)
Player.SendMessage("§aControls working!")

// State check
if (Player.IsFlying) {
    Chat.Send("Flight active!")
}

// Experience
Player.SetLevel(50)
Player.GiveExperience(1000)
```
