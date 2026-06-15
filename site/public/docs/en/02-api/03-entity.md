# Entity API — full documentation

## Method Reference

### Basic properties
| Method | Returns | Description |
|--------|--------|------|
| `Entity.Id` | `int` | Entity ID |
| `Entity.UUID` | `string` | Entity UUID |
| `Entity.Type` | `string` | Entity type (e.g. "minecraft:zombie") |
| `Entity.Name` | `string` | Entity name |
| `Entity.DisplayName` | `string` | Display name (supports colors) |
| `Entity.SetDisplayName(string)` | `void` | Set display name |
| `Entity.CustomName` | `string` | Custom name (if set) |
| `Entity.SetCustomName(string)` | `void` | Set custom name |
| `Entity.IsCustomNameVisible` | `bool` | Whether custom name is visible |
| `Entity.SetCustomNameVisible(bool)` | `void` | Show/hide custom name |
| `Entity.AlwaysRenderNameTag` | `bool` | Whether to always render name tag |
| `Entity.SetAlwaysRenderNameTag(bool)` | `void` | Set always render name tag |
| `Entity.Tags` | `List<string>` | Entity tags (scoreboard) |
| `Entity.AddTag(string)` | `void` | Add tag |
| `Entity.RemoveTag(string)` | `void` | Remove tag |
| `Entity.HasTag(string)` | `bool` | Whether has tag |
| `Entity.Score` | `int` | Entity score |
| `Entity.SetScore(int)` | `void` | Set score |

### Position and movement
| Method | Returns | Description |
|--------|--------|------|
| `Entity.X` | `double` | X position |
| `Entity.Y` | `double` | Y position |
| `Entity.Z` | `double` | Z position |
| `Entity.Yaw` | `float` | Horizontal angle |
| `Entity.Pitch` | `float` | Vertical angle |
| `Entity.HeadYaw` | `float` | Head angle |
| `Entity.BodyYaw` | `float` | Body angle |
| `Entity.SetPosition(x, y, z)` | `void` | Set position |
| `Entity.SetRotation(yaw, pitch)` | `void` | Set rotation |
| `Entity.SetHeadYaw(float)` | `void` | Set head angle |
| `Entity.SetBodyYaw(float)` | `void` | Set body angle |
| `Entity.Teleport(x, y, z)` | `void` | Teleport entity |
| `Entity.Teleport(x, y, z, yaw, pitch)` | `void` | Teleport with rotation |
| `Entity.TeleportTo(entity)` | `void` | Teleport to entity |
| `Entity.TeleportTo(player)` | `void` | Teleport to player |
| `Entity.Velocity` | `Vector3` | Current velocity |
| `Entity.SetVelocity(vx, vy, vz)` | `void` | Set velocity |
| `Entity.AddVelocity(vx, vy, vz)` | `void` | Add velocity |
| `Entity.Knockback(strength, x, z)` | `void` | Knockback |
| `Entity.Move(vx, vy, vz)` | `void` | Move relatively |
| `Entity.MoveTo(x, y, z)` | `void` | Move to position |
| `Entity.PrevX` | `double` | Previous X position |
| `Entity.PrevY` | `double` | Previous Y position |
| `Entity.PrevZ` | `double` | Previous Z position |
| `Entity.DistanceTo(x, y, z)` | `double` | Distance to a point |
| `Entity.DistanceTo(entity)` | `double` | Distance to entity |
| `Entity.DistanceToSqr(x, y, z)` | `double` | Distance² |
| `Entity.GetBlockPos()` | `BlockPos` | Block position |
| `Entity.GetChunkPos()` | `ChunkPos` | Chunk position |
| `Entity.GetLookDirection()` | `Vector3` | Look direction |
| `Entity.GetLookVector()` | `Vector3` | Look vector |
| `Entity.LookAt(x, y, z)` | `void` | Look toward a point |
| `Entity.LookAt(entity)` | `void` | Look toward an entity |
| `Entity.GetEyePosition()` | `Vector3` | Eye position |
| `Entity.GetEyeHeight()` | `float` | Eye height |
| `Entity.GetBoundingBox()` | `AABB` | Bounding box |

### State
| Method | Returns | Description |
|--------|--------|------|
| `Entity.IsAlive` | `bool` | Whether entity is alive |
| `Entity.IsDead` | `bool` | Whether entity is dead |
| `Entity.IsRemoved` | `bool` | Whether entity is removed |
| `Entity.IsOnGround` | `bool` | Whether on the ground |
| `Entity.IsInWater` | `bool` | Whether in water |
| `Entity.IsInLava` | `bool` | Whether in lava |
| `Entity.IsUnderwater` | `bool` | Whether underwater |
| `Entity.IsWet` | `bool` | Whether wet |
| `Entity.IsInRain` | `bool` | Whether in rain |
| `Entity.IsInBubbleColumn` | `bool` | Whether in a bubble column |
| `Entity.IsInsideWall` | `bool` | Whether inside a wall |
| `Entity.IsOnFire` | `bool` | Whether burning |
| `Entity.IsInvisible` | `bool` | Whether invisible |
| `Entity.IsGlowing` | `bool` | Whether glowing |
| `Entity.IsSilent` | `bool` | Whether silent |
| `Entity.IsNoGravity` | `bool` | Whether no gravity |
| `Entity.IsPushable` | `bool` | Whether pushable |
| `Entity.IsInvulnerable` | `bool` | Whether invulnerable |
| `Entity.IsCollidable` | `bool` | Whether collidable |
| `Entity.IsAttackable` | `bool` | Whether attackable |
| `Entity.IsSleeping` | `bool` | Whether sleeping |
| `Entity.IsClimbing` | `bool` | Whether climbing |
| `Entity.IsBlocking` | `bool` | Whether blocking (shield) |
| `Entity.IsRiptide` | `bool` | Whether riptide (trident) |
| `Entity.IsSpinAttacking` | `bool` | Whether spin attacking |
| `Entity.FireTicks` | `int` | Ticks on fire |
| `Entity.SetFireTicks(int)` | `void` | Set fire ticks |
| `Entity.FrozenTicks` | `int` | Frozen ticks |
| `Entity.SetFrozenTicks(int)` | `void` | Set frozen |
| `Entity.AirSupply` | `int` | Air level |
| `Entity.SetAirSupply(int)` | `void` | Set air |
| `Entity.MaxAir` | `int` | Maximum air |
| `Entity.FallDistance` | `float` | Fall distance |
| `Entity.SetFallDistance(float)` | `void` | Set fall distance |

### Invisibility and visual effects
| Method | Returns | Description |
|--------|--------|------|
| `Entity.SetInvisible(bool)` | `void` | Set invisibility |
| `Entity.SetGlowing(bool)` | `void` | Set glowing |
| `Entity.SetSilent(bool)` | `void` | Set silence |
| `Entity.SetNoGravity(bool)` | `void` | Set no gravity |
| `Entity.SetInvulnerable(bool)` | `void` | Set invulnerability |
| `Entity.SetFireImmune(bool)` | `void` | Set fire immunity |
| `Entity.SetPushable(bool)` | `void` | Set pushability |
| `Entity.SetCollidable(bool)` | `void` | Set collidability |
| `Entity.SetGravity(bool)` | `void` | Enable/disable gravity |
| `Entity.SetPortalCooldown(int)` | `void` | Set portal cooldown |
| `Entity.GetPortalCooldown()` | `int` | Portal cooldown |
| `Entity.HasPortalCooldown` | `bool` | Whether has portal cooldown |

### Health and damage
| Method | Returns | Description |
|--------|--------|------|
| `Entity.Health` | `float` | Current HP |
| `Entity.MaxHealth` | `float` | Maximum HP |
| `Entity.SetHealth(float)` | `void` | Set HP |
| `Entity.SetMaxHealth(float)` | `void` | Set max HP |
| `Entity.Heal(amount)` | `void` | Heal |
| `Entity.Damage(amount)` | `bool` | Deal damage |
| `Entity.Damage(amount, source)` | `bool` | Deal damage (type) |
| `Entity.Kill()` | `void` | Kill |
| `Entity.Remove()` | `void` | Remove (without drops) |
| `Entity.Discard()` | `void` | Discard from world |
| `Entity.Absorption` | `float` | Absorption |
| `Entity.SetAbsorption(float)` | `void` | Set absorption |
| `Entity.ArmorValue` | `int` | Armor value (protection points) |
| `Entity.ArmorCoverPercentage` | `float` | Armor coverage percentage |
| `Entity.KnockbackResistance` | `float` | Knockback resistance |
| `Entity.GetLastDamageSource()` | `string` | Last damage source |
| `Entity.GetLastDamageAmount()` | `float` | Last damage amount |
| `Entity.InvulnerableTime` | `int` | Invulnerability ticks |
| `Entity.SetInvulnerableTime(int)` | `void` | Set invulnerability ticks |
| `Entity.Hurt(damage)` | `bool` | Hurt |
| `Entity.Hurt(damage, source)` | `bool` | Hurt with source |

### Attributes
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetAttribute(name)` | `double` | Attribute value |
| `Entity.SetAttribute(name, value)` | `void` | Set attribute |
| `Entity.GetAttributeBase(name)` | `double` | Base attribute value |
| `Entity.GetAttributeDefault(name)` | `double` | Default value |
| `Entity.HasAttribute(name)` | `bool` | Whether has attribute |
| `Entity.GetAttributes()` | `Dict<string, double>` | All attributes |
| `Entity.ResetAttribute(name)` | `void` | Reset attribute |

### Effects
| Method | Returns | Description |
|--------|--------|------|
| `Entity.HasEffect(type)` | `bool` | Whether has effect |
| `Entity.GetEffect(type)` | `Effect` | Get effect |
| `Entity.GetEffects()` | `List<Effect>` | List of effects |
| `Entity.AddEffect(type, duration, amplifier)` | `bool` | Add effect |
| `Entity.AddEffect(type, duration, amplifier, particles, icon)` | `bool` | Add effect with options |
| `Entity.AddEffect(effect)` | `bool` | Add effect (object) |
| `Entity.RemoveEffect(type)` | `bool` | Remove effect |
| `Entity.ClearEffects()` | `void` | Clear effects |
| `Entity.IsAffectedByEffects` | `bool` | Whether affected by effects |

### AI movement
| Method | Returns | Description |
|--------|--------|------|
| `Entity.Jump()` | `void` | Force jump |
| `Entity.SetJumping(bool)` | `void` | Set jumping |
| `Entity.IsJumping` | `bool` | Whether jumping |
| `Entity.SetSprinting(bool)` | `void` | Set sprinting |
| `Entity.IsSprinting` | `bool` | Whether sprinting |
| `Entity.SetSneaking(bool)` | `void` | Set sneaking |
| `Entity.IsSneaking` | `bool` | Whether sneaking |
| `Entity.SetSwimming(bool)` | `void` | Set swimming |
| `Entity.IsSwimming` | `bool` | Whether swimming |
| `Entity.SetGliding(bool)` | `void` | Set gliding |
| `Entity.IsGliding` | `bool` | Whether gliding |
| `Entity.SetFallFlying(bool)` | `void` | Set fall flying |
| `Entity.IsFallFlying` | `bool` | Whether fall flying |
| `Entity.SetFlying(bool)` | `void` | Set flying |
| `Entity.IsFlying` | `bool` | Whether flying |
| `Entity.SetNoAi(bool)` | `void` | Disable AI |
| `Entity.HasNoAi` | `bool` | Whether AI is disabled |
| `Entity.SetAi(bool)` | `void` | Enable/disable AI |
| `Entity.IsAiDisabled` | `bool` | Whether AI is disabled |
| `Entity.SetPersistenceRequired(bool)` | `void` | Set persistence (won't despawn) |
| `Entity.IsPersistent` | `bool` | Whether persistent |

### Riding and vehicles
| Method | Returns | Description |
|--------|--------|------|
| `Entity.StartRiding(entity)` | `bool` | Ride an entity |
| `Entity.StopRiding()` | `void` | Dismount |
| `Entity.IsRiding` | `bool` | Whether riding something |
| `Entity.Vehicle` | `Entity` | Vehicle |
| `Entity.GetPassengers()` | `List<Entity>` | List of passengers |
| `Entity.AddPassenger(entity)` | `void` | Add passenger |
| `Entity.RemovePassenger(entity)` | `void` | Remove passenger |
| `Entity.ClearPassengers()` | `void` | Remove all passengers |
| `Entity.HasControllingPassenger` | `bool` | Whether has a controlling passenger |
| `Entity.GetControllingPassenger()` | `Entity` | Passenger who controls |
| `Entity.IsVehicle` | `bool` | Whether is a vehicle |

### Leash
| Method | Returns | Description |
|--------|--------|------|
| `Entity.IsLeashed` | `bool` | Whether leashed |
| `Entity.GetLeashHolder()` | `Entity` | Who holds the leash |
| `Entity.SetLeashHolder(entity)` | `bool` | Leash to entity |
| `Entity.SetLeashHolder(player)` | `bool` | Leash to player |
| `Entity.Unleash()` | `void` | Unleash |
| `Entity.SetLeashed(bool)` | `void` | Set leashed |
| `Entity.Leash()` | `bool` | Attach leash |
| `Entity.DropLeash()` | `void` | Drop leash |

### Equipment
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetMainHandItem()` | `ItemStack` | Item in main hand |
| `Entity.SetMainHandItem(item)` | `void` | Set item in main hand |
| `Entity.GetOffHandItem()` | `ItemStack` | Item in off hand |
| `Entity.SetOffHandItem(item)` | `void` | Set item in off hand |
| `Entity.GetHelmet()` | `ItemStack` | Helmet |
| `Entity.SetHelmet(item)` | `void` | Set helmet |
| `Entity.GetChestplate()` | `ItemStack` | Chestplate |
| `Entity.SetChestplate(item)` | `void` | Set chestplate |
| `Entity.GetLeggings()` | `ItemStack` | Leggings |
| `Entity.SetLeggings(item)` | `void` | Set leggings |
| `Entity.GetBoots()` | `ItemStack` | Boots |
| `Entity.SetBoots(item)` | `void` | Set boots |
| `Entity.GetEquipment(slot)` | `ItemStack` | Item in slot (0=hand, 1-4=armor, 5=off) |
| `Entity.SetEquipment(slot, item)` | `void` | Set item in slot |
| `Entity.GetAllEquipment()` | `List<ItemStack>` | All equipment |
| `Entity.GetArmorContents()` | `ItemStack[]` | Armor slot contents |
| `Entity.SetArmorContents(items[])` | `void` | Set armor |
| `Entity.GetDropChance(slot)` | `float` | Slot drop chance |
| `Entity.SetDropChance(slot, chance)` | `void` | Set drop chance |
| `Entity.GetHandDropChances()` | `float[]` | Hand drop chances |
| `Entity.GetArmorDropChances()` | `float[]` | Armor drop chances |
| `Entity.CanPickUpLoot` | `bool` | Whether can pick up loot |
| `Entity.SetCanPickUpLoot(bool)` | `void` | Set loot pickup |
| `Entity.ShouldDropEquipment` | `bool` | Whether to drop equipment |
| `Entity.SetShouldDropEquipment(bool)` | `void` | Set drop equipment |
| `Entity.ShouldDropLoot` | `bool` | Whether to drop loot |
| `Entity.SetShouldDropLoot(bool)` | `void` | Set drop loot |

### NBT
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetNBT()` | `string` | Get NBT as string |
| `Entity.SetNBT(string)` | `void` | Set entire NBT |
| `Entity.MergeNBT(string)` | `void` | Merge NBT |
| `Entity.HasNBT(key)` | `bool` | Whether has NBT key |
| `Entity.GetNBTCompound()` | `NBTCompound` | NBT as object |
| `Entity.SetNBTTag(key, value)` | `void` | Set NBT tag |
| `Entity.GetNBTTag(key)` | `object` | Get NBT tag |

### World and dimension
| Method | Returns | Description |
|--------|--------|------|
| `Entity.Dimension` | `string` | Entity dimension |
| `Entity.SetDimension(string)` | `void` | Change dimension |
| `Entity.GetWorld()` | `World` | Entity's world |
| `Entity.ChunkX` | `int` | Chunk X |
| `Entity.ChunkZ` | `int` | Chunk Z |

### Interaction
| Method | Returns | Description |
|--------|--------|------|
| `Entity.Interact(entity)` | `bool` | Interact with entity |
| `Entity.Interact(player)` | `bool` | Interact with player |
| `Entity.InteractAt(entity, pos)` | `bool` | Interact at position |
| `Entity.Attack()` | `void` | Attack |
| `Entity.SwingMainHand()` | `void` | Swing main hand |
| `Entity.SwingOffHand()` | `void` | Swing off hand |
| `Entity.UseItem()` | `void` | Use item |
| `Entity.BreakItem()` | `void` | Break held item |
| `Entity.DropItem()` | `void` | Drop item |

### Sounds
| Method | Returns | Description |
|--------|--------|------|
| `Entity.PlaySound(sound)` | `void` | Play sound |
| `Entity.PlaySound(sound, volume, pitch)` | `void` | Sound with parameters |
| `Entity.GetHurtSound()` | `string` | Hurt sound |
| `Entity.GetDeathSound()` | `string` | Death sound |
| `Entity.GetStepSound()` | `string` | Step sound |
| `Entity.GetFallSound()` | `string` | Fall sound |
| `Entity.GetSwimSound()` | `string` | Swim sound |
| `Entity.GetSplashSound()` | `string` | Splash sound |

### Age and development
| Method | Returns | Description |
|--------|--------|------|
| `Entity.Age` | `int` | Entity age (ticks) |
| `Entity.SetAge(int)` | `void` | Set age |
| `Entity.IsBaby` | `bool` | Whether baby |
| `Entity.SetBaby(bool)` | `void` | Set baby |
| `Entity.GetScale()` | `float` | Entity scale |
| `Entity.GetBreed()` | `bool` | Whether can breed |
| `Entity.CanBreed` | `bool` | Whether can breed |
| `Entity.SetBreed(bool)` | `void` | Set breeding ability |
| `Entity.IsInLove` | `bool` | Whether in love mode |
| `Entity.SetInLove(bool)` | `void` | Set love mode |
| `Entity.GetLoveCause()` | `string` | Who caused love mode |
| `Entity.GetAgeTimer()` | `int` | Age timer |
| `Entity.SetAgeTimer(int)` | `void` | Set age timer |

### Taming
| Method | Returns | Description |
|--------|--------|------|
| `Entity.IsTamed` | `bool` | Whether tamed |
| `Entity.SetTamed(bool)` | `void` | Set tamed |
| `Entity.GetOwner()` | `string` | Owner name |
| `Entity.GetOwnerUUID()` | `string` | Owner UUID |
| `Entity.SetOwnerUUID(string)` | `void` | Set owner (UUID) |
| `Entity.SetOwner(player)` | `void` | Set player as owner |
| `Entity.SetOwnerName(string)` | `void` | Set owner name |
| `Entity.IsSitting` | `bool` | Whether sitting |
| `Entity.SetSitting(bool)` | `void` | Set sitting |
| `Entity.IsTameable` | `bool` | Whether tameable |

### Mobs — targeting
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetTarget()` | `Entity` | Current target |
| `Entity.SetTarget(entity)` | `void` | Set target |
| `Entity.ClearTarget()` | `void` | Clear target |
| `Entity.GetLastHurtByMob()` | `Entity` | Last mob that hurt it |
| `Entity.SetLastHurtByMob(entity)` | `void` | Set last that hurt it |
| `Entity.GetLastHurtByPlayer()` | `Player` | Last player that hurt it |
| `Entity.GetLastHurtMob()` | `Entity` | Last mob hurt by it |
| `Entity.SetLastHurtMob(entity)` | `void` | Set last hurt by it |
| `Entity.GetAngerTime()` | `int` | Anger time |
| `Entity.SetAngerTime(int)` | `void` | Set anger time |
| `Entity.GetAngryAt()` | `string` | UUID of who it's angry at |
| `Entity.SetAngryAt(uuid)` | `void` | Set who it's angry at |
| `Entity.Revenge()` | `void` | Revenge on last attacker |

### Navigation / Pathfinding
| Method | Returns | Description |
|--------|--------|------|
| `Entity.NavigateTo(x, y, z)` | `bool` | Navigate to point |
| `Entity.NavigateTo(entity)` | `bool` | Navigate to entity |
| `Entity.NavigateTo(player)` | `bool` | Navigate to player |
| `Entity.StopNavigation()` | `void` | Stop navigation |
| `Entity.HasPath` | `bool` | Whether has a path |
| `Entity.GetPath()` | `Path` | Path |
| `Entity.SetPath(path)` | `void` | Set path |
| `Entity.GetNavigation()` | `Navigation` | Navigation object |
| `Entity.IsNavigating` | `bool` | Whether navigating |
| `Entity.GetSpeed()` | `float` | Movement speed |
| `Entity.SetSpeed(float)` | `void` | Set speed |
| `Entity.Follow(entity, speed)` | `bool` | Follow entity |
| `Entity.Follow(player, speed)` | `bool` | Follow player |
| `Entity.Wander()` | `void` | Random walking |
| `Entity.MoveTo(x, y, z, speed)` | `bool` | Move to point |

### Mobs — specific
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetVillagerProfession()` | `string` | Villager profession |
| `Entity.SetVillagerProfession(string)` | `void` | Set profession |
| `Entity.GetVillagerLevel()` | `int` | Villager level |
| `Entity.SetVillagerLevel(int)` | `void` | Set level |
| `Entity.GetVillagerXP()` | `int` | Villager XP |
| `Entity.SetVillagerXP(int)` | `void` | Set XP |
| `Entity.IsVillagerSleeping` | `bool` | Whether villager is sleeping |
| `Entity.IsZombieVillager` | `bool` | Whether zombie villager |
| `Entity.CureZombieVillager()` | `void` | Cure zombie villager |
| `Entity.GetCatType()` | `int` | Cat type (0-9) |
| `Entity.SetCatType(int)` | `void` | Set cat type |
| `Entity.GetFoxType()` | `string` | Fox type: "red", "snow" |
| `Entity.SetFoxType(string)` | `void` | Set fox type |
| `Entity.GetMooshroomType()` | `string` | Mooshroom type: "red", "brown" |
| `Entity.SetMooshroomType(string)` | `void` | Set mooshroom type |
| `Entity.GetParrotVariant()` | `int` | Parrot variant (0-3) |
| `Entity.SetParrotVariant(int)` | `void` | Set variant |
| `Entity.GetRabbitType()` | `int` | Rabbit type (0-5) |
| `Entity.SetRabbitType(int)` | `void` | Set type |
| `Entity.GetHorseColor()` | `string` | Horse color |
| `Entity.SetHorseColor(string)` | `void` | Set color |
| `Entity.GetHorseMarkings()` | `string` | Horse markings |
| `Entity.SetHorseMarkings(string)` | `void` | Set markings |
| `Entity.GetHorseArmor()` | `ItemStack` | Horse armor |
| `Entity.SetHorseArmor(item)` | `void` | Set horse armor |
| `Entity.IsHorseSaddled` | `bool` | Whether horse is saddled |
| `Entity.SetHorseSaddled(bool)` | `void` | Set saddle |
| `Entity.GetLlamaStrength()` | `int` | Llama strength (1-5) |
| `Entity.SetLlamaStrength(int)` | `void` | Set strength |
| `Entity.GetLlamaColor()` | `int` | Llama color |
| `Entity.SetLlamaColor(int)` | `void` | Set color |
| `Entity.GetSheepColor()` | `string` | Sheep color (dye color) |
| `Entity.SetSheepColor(string)` | `void` | Set color |
| `Entity.IsSheepSheared` | `bool` | Whether sheep is sheared |
| `Entity.SetSheepSheared(bool)` | `void` | Shear |
| `Entity.GetGoatHorns()` | `int` | Goat horn count |
| `Entity.SetGoatHorns(int)` | `void` | Set horns |
| `Entity.IsScreamingGoat` | `bool` | Whether screaming goat |
| `Entity.SetScreamingGoat(bool)` | `void` | Set screaming goat |
| `Entity.GetPandaGenes()` | `Dict` | Panda genes (main/hidden) |
| `Entity.SetPandaGene(gene, value)` | `void` | Set panda gene |
| `Entity.GetBeeHivePos()` | `BlockPos` | Bee hive position |
| `Entity.SetBeeHivePos(x, y, z)` | `void` | Set hive position |
| `Entity.GetBeeHasNectar` | `bool` | Whether bee has nectar |
| `Entity.GetBeeHasStung` | `bool` | Whether bee has stung |
| `Entity.GetAxolotlVariant()` | `int` | Axolotl variant (0-4) |
| `Entity.SetAxolotlVariant(int)` | `void` | Set variant |
| `Entity.GetFrogVariant()` | `string` | Frog variant: "temperate", "warm", "cold" |
| `Entity.SetFrogVariant(string)` | `void` | Set variant |
| `Entity.GetCamelDashing` | `bool` | Whether camel is dashing |
| `Entity.SetCamelDashing(bool)` | `void` | Set camel dashing |
| `Entity.GetSnailageState()` | `string` | Snail state |
| `Entity.GetWardenAnger()` | `int` | Warden anger |
| `Entity.SetWardenAnger(int)` | `void` | Set anger |

### Slimes and Magma Cubes
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetSlimeSize()` | `int` | Slime size |
| `Entity.SetSlimeSize(int)` | `void` | Set size |

### Creeper
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetCreeperFuse()` | `int` | Fuse time (ticks) |
| `Entity.SetCreeperFuse(int)` | `void` | Set fuse time |
| `Entity.GetCreeperExplosionRadius()` | `int` | Explosion radius |
| `Entity.SetCreeperExplosionRadius(int)` | `void` | Set radius |
| `Entity.IsCreeperCharged` | `bool` | Whether charged (lightning) |
| `Entity.SetCreeperCharged(bool)` | `void` | Set charged |
| `Entity.IgniteCreeper()` | `void` | Ignite creeper |

### Enderman
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetEndermanHeldBlock()` | `string` | Held block |
| `Entity.SetEndermanHeldBlock(block)` | `void` | Set held block |
| `Entity.IsEndermanScreaming` | `bool` | Whether screaming |
| `Entity.SetEndermanScreaming(bool)` | `void` | Set screaming |

### Phantom
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetPhantomSize()` | `int` | Phantom size |
| `Entity.SetPhantomSize(int)` | `void` | Set size |

### Shulker
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetShulkerColor()` | `string` | Shulker color |
| `Entity.SetShulkerColor(string)` | `void` | Set color |
| `Entity.GetShulkerAttachedFace()` | `string` | Face it is attached to |
| `Entity.GetShulkerPeekAmount()` | `int` | How open it is |

### Area Effect Cloud
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetAoeRadius()` | `float` | Cloud radius |
| `Entity.SetAoeRadius(float)` | `void` | Set radius |
| `Entity.GetAoeColor()` | `int` | Cloud color (RGB) |
| `Entity.SetAoeColor(int)` | `void` | Set color |
| `Entity.GetAoeDuration()` | `int` | Duration |
| `Entity.SetAoeDuration(int)` | `void` | Set duration |
| `Entity.GetAoeWaitTime()` | `int` | Time since creation |
| `Entity.GetAoeParticle()` | `string` | Cloud particle |
| `Entity.SetAoeParticle(string)` | `void` | Set particle |

### Item Frame
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetItemFrameItem()` | `ItemStack` | Item in frame |
| `Entity.SetItemFrameItem(item)` | `void` | Set item in frame |
| `Entity.GetItemFrameRotation()` | `int` | Rotation (0-7) |
| `Entity.SetItemFrameRotation(int)` | `void` | Set rotation |
| `Entity.IsItemFrameFixed` | `bool` | Whether frame is fixed |
| `Entity.SetItemFrameFixed(bool)` | `void` | Set fixed frame |
| `Entity.IsItemFrameVisible` | `bool` | Whether frame is visible |
| `Entity.SetItemFrameVisible(bool)` | `void` | Set visibility |
| `Entity.IsItemFrameMap` | `bool` | Whether map in frame |

### Armor Stand
| Method | Returns | Description |
|--------|--------|------|
| `Entity.IsArmorStandSmall` | `bool` | Whether small armor stand |
| `Entity.SetArmorStandSmall(bool)` | `void` | Set small |
| `Entity.IsArmorStandMarker` | `bool` | Whether marker (invisible, hitbox) |
| `Entity.SetArmorStandMarker(bool)` | `void` | Set marker |
| `Entity.IsArmorStandShowArms` | `bool` | Whether to show arms |
| `Entity.SetArmorStandShowArms(bool)` | `void` | Set arms |
| `Entity.IsArmorStandNoBasePlate` | `bool` | Whether without base plate |
| `Entity.SetArmorStandNoBasePlate(bool)` | `void` | Set base plate |
| `Entity.IsArmorStandNoGravity` | `bool` | Whether without gravity |
| `Entity.SetArmorStandNoGravity(bool)` | `void` | Set gravity |
| `Entity.IsArmorStandNoClip` | `bool` | Whether noclip |
| `Entity.SetArmorStandNoClip(bool)` | `void` | Set noclip |
| `Entity.SetArmorStandPose(part, x, y, z)` | `void` | Set pose (head, body, leftArm, rightArm, leftLeg, rightLeg) |
| `Entity.GetArmorStandPose(part)` | `Vector3` | Get pose |
| `Entity.SetArmorStandHeadPose(x, y, z)` | `void` | Head position |
| `Entity.SetArmorStandBodyPose(x, y, z)` | `void` | Body position |
| `Entity.SetArmorStandLeftArmPose(x, y, z)` | `void` | Left arm |
| `Entity.SetArmorStandRightArmPose(x, y, z)` | `void` | Right arm |
| `Entity.SetArmorStandLeftLegPose(x, y, z)` | `void` | Left leg |
| `Entity.SetArmorStandRightLegPose(x, y, z)` | `void` | Right leg |

### Text Display (1.19+)
| Method | Returns | Description |
|--------|--------|------|
| `Entity.SetTextDisplayText(text)` | `void` | Set display text |
| `Entity.GetTextDisplayText()` | `string` | Get text |
| `Entity.SetTextDisplayBackgroundColor(int)` | `void` | Background color (ARGB) |
| `Entity.GetTextDisplayBackgroundColor()` | `int` | Get background color |
| `Entity.SetTextDisplayTextOpacity(byte)` | `void` | Text opacity |
| `Entity.SetTextDisplayLineWidth(int)` | `void` | Line width |
| `Entity.SetTextDisplayAlignment(string)` | `void` | Alignment: "center", "left", "right" |
| `Entity.SetTextDisplayBillboard(string)` | `void` | Billboard: "fixed", "vertical", "horizontal", "center" |
| `Entity.SetTextDisplayScale(float)` | `void` | Text scale |
| `Entity.SetTextDisplayShadow(bool)` | `void` | Text shadow |
| `Entity.SetTextDisplaySeeThrough(bool)` | `void` | Visible through blocks |
| `Entity.SetTextDisplayDefaultBackground(bool)` | `void` | Default background |

### Display Entity (common)
| Method | Returns | Description |
|--------|--------|------|
| `Entity.SetDisplayTranslation(transformation)` | `void` | Set transformation |
| `Entity.SetDisplayScale(x, y, z)` | `void` | Set scale |
| `Entity.SetDisplayTranslation(x, y, z)` | `void` | Set translation |
| `Entity.SetDisplayLeftRotation(x, y, z)` | `void` | Left rotation |
| `Entity.SetDisplayRightRotation(x, y, z)` | `void` | Right rotation |
| `Entity.SetDisplayBillboard(string)` | `void` | Billboard mode |
| `Entity.SetDisplayBrightness(block, sky)` | `void` | Brightness |
| `Entity.SetDisplayViewRange(float)` | `void` | View range |
| `Entity.SetDisplayShadowRadius(float)` | `void` | Shadow radius |
| `Entity.SetDisplayShadowStrength(float)` | `void` | Shadow strength |
| `Entity.SetDisplayGlowColorOverride(int)` | `void` | Glow color |
| `Entity.SetDisplayStartInterpolation(int)` | `void` | Interpolation start |
| `Entity.SetDisplayInterpolationDuration(int)` | `void` | Interpolation duration |
| `Entity.SetDisplayTeleportDuration(int)` | `void` | Teleport duration |

### Misc
| Method | Returns | Description |
|--------|--------|------|
| `Entity.GetTicksLived()` | `int` | Lifetime ticks |
| `Entity.GetPose()` | `string` | Pose: "standing", "fall_flying", "sleeping", "swimming", "spin_attack", "sneaking", "long_jumping", "dying", "croaking", "using_tongue", "sitting", "sniffing", "digging" |
| `Entity.SetPose(string)` | `void` | Set pose |
| `Entity.GetRemovalReason()` | `string` | Removal reason |
| `Entity.SetRemovalReason(string)` | `void` | Set removal reason |
| `Entity.ShouldBeSaved` | `bool` | Whether should be saved |
| `Entity.SetShouldBeSaved(bool)` | `void` | Set saving |
| `Entity.GetEntityCategory()` | `string` | Category: "monster", "creature", "ambient", "water_creature", "water_ambient", "misc" |
| `Entity.GetClassification()` | `string` | Classification |
| `Entity.GetMobType()` | `string` | Mob type |
| `Entity.GetCreatureAttribute()` | `string` | Creature attribute: "undead", "arthropod", "undefined", "water", "illager" |
| `Entity.GetExperienceReward()` | `int` | XP for killing |
| `Entity.SetExperienceReward(int)` | `void` | Set XP |
| `Entity.GetEnchantmentSeed()` | `int` | Enchantment seed |
| `Entity.CopyDataFrom(entity)` | `void` | Copy data from entity |
| `Entity.SendMessage(message)` | `void` | Send message (if can receive) |

---

## Examples

### Modifying mobs
```glang
// Spawn zombie with equipment
var zombie = World.Summon("minecraft:zombie", 100, 64, -200)
zombie.SetCustomName("§6Elite Zombie")
zombie.SetCustomNameVisible(true)
zombie.SetHealth(40)
zombie.SetMaxHealth(40)
zombie.SetMainHandItem(ItemStack("minecraft:diamond_sword").AddEnchant("sharpness", 5))
zombie.SetHelmet(ItemStack("minecraft:diamond_helmet"))
zombie.SetChestplate(ItemStack("minecraft:diamond_chestplate"))
zombie.SetBoots(ItemStack("minecraft:diamond_boots"))
zombie.AddEffect("speed", 999999, 1)
zombie.AddEffect("strength", 999999, 2)
zombie.SetInvulnerable(true)
zombie.SetPersistent(true)
zombie.SetDropChance(0, 0.0f)   // main hand does not drop
zombie.SetDropChance(1, 0.0f)   // boots do not drop

// Set target to player
zombie.SetTarget(Player)
```

### Armor stand pose
```glang
var stand = World.SpawnArmorStand(100, 64, -200)
stand.SetArmorStandShowArms(true)
stand.SetArmorStandSmall(false)
stand.SetArmorStandMarker(false)
stand.SetArmorStandHeadPose(30, 0, 0)     // head slightly down
stand.SetArmorStandRightArmPose(-45, 0, 0) // arm extended

// Equip
stand.SetHelmet(ItemStack("minecraft:carved_pumpkin"))
stand.SetChestplate(ItemStack("minecraft:leather_chestplate"))
```
