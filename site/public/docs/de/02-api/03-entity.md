# Entity API — vollständige Dokumentation

## Methodenübersicht

### Grundlegende Eigenschaften
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.Id` | `int` | Entitäts-ID |
| `Entity.UUID` | `string` | Entitäts-UUID |
| `Entity.Type` | `string` | Entitätstyp (z.B. "minecraft:zombie") |
| `Entity.Name` | `string` | Name der Entität |
| `Entity.DisplayName` | `string` | Anzeigename (unterstützt Farben) |
| `Entity.SetDisplayName(string)` | `void` | Setze Anzeigenamen |
| `Entity.CustomName` | `string` | Eigener Name (falls gesetzt) |
| `Entity.SetCustomName(string)` | `void` | Setze eigenen Namen |
| `Entity.IsCustomNameVisible` | `bool` | Ist eigener Name sichtbar |
| `Entity.SetCustomNameVisible(bool)` | `void` | Eigenen Namen zeigen/verstecken |
| `Entity.AlwaysRenderNameTag` | `bool` | Namensschild immer rendern |
| `Entity.SetAlwaysRenderNameTag(bool)` | `void` | Immer-Namensschild-Rendern setzen |
| `Entity.Tags` | `List<string>` | Entitäts-Tags (Scoreboard) |
| `Entity.AddTag(string)` | `void` | Tag hinzufügen |
| `Entity.RemoveTag(string)` | `void` | Tag entfernen |
| `Entity.HasTag(string)` | `bool` | Hat Tag |
| `Entity.Score` | `int` | Entitäts-Punktzahl |
| `Entity.SetScore(int)` | `void` | Punktzahl setzen |

### Position und Bewegung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.X` | `double` | X-Position |
| `Entity.Y` | `double` | Y-Position |
| `Entity.Z` | `double` | Z-Position |
| `Entity.Yaw` | `float` | Horizontaler Winkel |
| `Entity.Pitch` | `float` | Vertikaler Winkel |
| `Entity.HeadYaw` | `float` | Kopfwinkel |
| `Entity.BodyYaw` | `float` | Körperwinkel |
| `Entity.SetPosition(x, y, z)` | `void` | Position setzen |
| `Entity.SetRotation(yaw, pitch)` | `void` | Rotation setzen |
| `Entity.SetHeadYaw(float)` | `void` | Kopfwinkel setzen |
| `Entity.SetBodyYaw(float)` | `void` | Körperwinkel setzen |
| `Entity.Teleport(x, y, z)` | `void` | Entität teleportieren |
| `Entity.Teleport(x, y, z, yaw, pitch)` | `void` | Teleport mit Rotation |
| `Entity.TeleportTo(entity)` | `void` | Zu Entität teleportieren |
| `Entity.TeleportTo(player)` | `void` | Zu Spieler teleportieren |
| `Entity.Velocity` | `Vector3` | Aktuelle Geschwindigkeit |
| `Entity.SetVelocity(vx, vy, vz)` | `void` | Geschwindigkeit setzen |
| `Entity.AddVelocity(vx, vy, vz)` | `void` | Geschwindigkeit hinzufügen |
| `Entity.Knockback(strength, x, z)` | `void` | Rückstoß |
| `Entity.Move(vx, vy, vz)` | `void` | Relativ verschieben |
| `Entity.MoveTo(x, y, z)` | `void` | Zu Position verschieben |
| `Entity.PrevX` | `double` | Vorherige X-Position |
| `Entity.PrevY` | `double` | Vorherige Y-Position |
| `Entity.PrevZ` | `double` | Vorherige Z-Position |
| `Entity.DistanceTo(x, y, z)` | `double` | Distanz zum Punkt |
| `Entity.DistanceTo(entity)` | `double` | Distanz zur Entität |
| `Entity.DistanceToSqr(x, y, z)` | `double` | Distanz² |
| `Entity.GetBlockPos()` | `BlockPos` | Blockposition |
| `Entity.GetChunkPos()` | `ChunkPos` | Chunk-Position |
| `Entity.GetLookDirection()` | `Vector3` | Blickrichtung |
| `Entity.GetLookVector()` | `Vector3` | Blickvektor |
| `Entity.LookAt(x, y, z)` | `void` | In Richtung Punkt drehen |
| `Entity.LookAt(entity)` | `void` | In Richtung Entität drehen |
| `Entity.GetEyePosition()` | `Vector3` | Augenposition |
| `Entity.GetEyeHeight()` | `float` | Augenhöhe |
| `Entity.GetBoundingBox()` | `AABB` | Bounding Box |

### Zustand
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.IsAlive` | `bool` | Lebt die Entität |
| `Entity.IsDead` | `bool` | Ist die Entität tot |
| `Entity.IsRemoved` | `bool` | Ist die Entität entfernt |
| `Entity.IsOnGround` | `bool` | Auf dem Boden |
| `Entity.IsInWater` | `bool` | Im Wasser |
| `Entity.IsInLava` | `bool` | In Lava |
| `Entity.IsUnderwater` | `bool` | Unter Wasser |
| `Entity.IsWet` | `bool` | Nass |
| `Entity.IsInRain` | `bool` | Im Regen |
| `Entity.IsInBubbleColumn` | `bool` | In Blasensäule |
| `Entity.IsInsideWall` | `bool` | In Wand |
| `Entity.IsOnFire` | `bool` | Brennt |
| `Entity.IsInvisible` | `bool` | Unsichtbar |
| `Entity.IsGlowing` | `bool` | Leuchtet |
| `Entity.IsSilent` | `bool` | Lautlos |
| `Entity.IsNoGravity` | `bool` | Ohne Schwerkraft |
| `Entity.IsPushable` | `bool` | Schiebbar |
| `Entity.IsInvulnerable` | `bool` | Unverwundbar |
| `Entity.IsCollidable` | `bool` | Kollidierbar |
| `Entity.IsAttackable` | `bool` | Angreifbar |
| `Entity.IsSleeping` | `bool` | Schläft |
| `Entity.IsClimbing` | `bool` | Klettert |
| `Entity.IsBlocking` | `bool` | Blockt (Schild) |
| `Entity.IsRiptide` | `bool` | Riptide (Dreizack) |
| `Entity.IsSpinAttacking` | `bool` | Dreh-Angriff |
| `Entity.FireTicks` | `int` | Feuer-Ticks |
| `Entity.SetFireTicks(int)` | `void` | Feuer-Ticks setzen |
| `Entity.FrozenTicks` | `int` | Gefrier-Ticks |
| `Entity.SetFrozenTicks(int)` | `void` | Gefrieren setzen |
| `Entity.AirSupply` | `int` | Luftvorrat |
| `Entity.SetAirSupply(int)` | `void` | Luft setzen |
| `Entity.MaxAir` | `int` | Maximaler Luftvorrat |
| `Entity.FallDistance` | `float` | Fallhöhe |
| `Entity.SetFallDistance(float)` | `void` | Fallhöhe setzen |

### Unsichtbarkeit und visuelle Effekte
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.SetInvisible(bool)` | `void` | Unsichtbarkeit setzen |
| `Entity.SetGlowing(bool)` | `void` | Leuchten setzen |
| `Entity.SetSilent(bool)` | `void` | Lautlos setzen |
| `Entity.SetNoGravity(bool)` | `void` | Schwerelosigkeit setzen |
| `Entity.SetInvulnerable(bool)` | `void` | Unverwundbarkeit setzen |
| `Entity.SetFireImmune(bool)` | `void` | Feuerimmunität setzen |
| `Entity.SetPushable(bool)` | `void` | Schiebbarkeit setzen |
| `Entity.SetCollidable(bool)` | `void` | Kollidierbarkeit setzen |
| `Entity.SetGravity(bool)` | `void` | Schwerkraft ein/aus |
| `Entity.SetPortalCooldown(int)` | `void` | Portal-Cooldown setzen |
| `Entity.GetPortalCooldown()` | `int` | Portal-Cooldown |
| `Entity.HasPortalCooldown` | `bool` | Hat Portal-Cooldown |

### Gesundheit und Schaden
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.Health` | `float` | Aktuelles HP |
| `Entity.MaxHealth` | `float` | Maximales HP |
| `Entity.SetHealth(float)` | `void` | HP setzen |
| `Entity.SetMaxHealth(float)` | `void` | Max HP setzen |
| `Entity.Heal(amount)` | `void` | Heilen |
| `Entity.Damage(amount)` | `bool` | Schaden zufügen |
| `Entity.Damage(amount, source)` | `bool` | Schaden zufügen (Typ) |
| `Entity.Kill()` | `void` | Töten |
| `Entity.Remove()` | `void` | Entfernen (ohne Drops) |
| `Entity.Discard()` | `void` | Aus Welt entfernen |
| `Entity.Absorption` | `float` | Absorption |
| `Entity.SetAbsorption(float)` | `void` | Absorption setzen |
| `Entity.ArmorValue` | `int` | Rüstungswert (Schutzpunkte) |
| `Entity.ArmorCoverPercentage` | `float` | Rüstungsabdeckung in Prozent |
| `Entity.KnockbackResistance` | `float` | Rückstoßwiderstand |
| `Entity.GetLastDamageSource()` | `string` | Letzte Schadensquelle |
| `Entity.GetLastDamageAmount()` | `float` | Letzte Schadensmenge |
| `Entity.InvulnerableTime` | `int` | Unverwundbarkeits-Ticks |
| `Entity.SetInvulnerableTime(int)` | `void` | Unverwundbarkeits-Ticks setzen |
| `Entity.Hurt(damage)` | `bool` | Verletzung |
| `Entity.Hurt(damage, source)` | `bool` | Verletzung mit Quelle |

### Attribute
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetAttribute(name)` | `double` | Attributwert |
| `Entity.SetAttribute(name, value)` | `void` | Attribut setzen |
| `Entity.GetAttributeBase(name)` | `double` | Basis-Attributwert |
| `Entity.GetAttributeDefault(name)` | `double` | Standardwert |
| `Entity.HasAttribute(name)` | `bool` | Hat Attribut |
| `Entity.GetAttributes()` | `Dict<string, double>` | Alle Attribute |
| `Entity.ResetAttribute(name)` | `void` | Attribut zurücksetzen |

### Effekte
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.HasEffect(type)` | `bool` | Hat Effekt |
| `Entity.GetEffect(type)` | `Effect` | Effekt abrufen |
| `Entity.GetEffects()` | `List<Effect>` | Effektliste |
| `Entity.AddEffect(type, duration, amplifier)` | `bool` | Effekt hinzufügen |
| `Entity.AddEffect(type, duration, amplifier, particles, icon)` | `bool` | Effekt mit Optionen hinzufügen |
| `Entity.AddEffect(effect)` | `bool` | Effekt hinzufügen (Objekt) |
| `Entity.RemoveEffect(type)` | `bool` | Effekt entfernen |
| `Entity.ClearEffects()` | `void` | Effekte löschen |
| `Entity.IsAffectedByEffects` | `bool` | Unter Wirkung von Effekten |

### KI-Bewegung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.Jump()` | `void` | Sprung erzwingen |
| `Entity.SetJumping(bool)` | `void` | Springen setzen |
| `Entity.IsJumping` | `bool` | Springt |
| `Entity.SetSprinting(bool)` | `void` | Sprint setzen |
| `Entity.IsSprinting` | `bool` | Sprintet |
| `Entity.SetSneaking(bool)` | `void` | Schleichen setzen |
| `Entity.IsSneaking` | `bool` | Schleicht |
| `Entity.SetSwimming(bool)` | `void` | Schwimmen setzen |
| `Entity.IsSwimming` | `bool` | Schwimmt |
| `Entity.SetGliding(bool)` | `void` | Gleiten setzen |
| `Entity.IsGliding` | `bool` | Gleitet |
| `Entity.SetFallFlying(bool)` | `void` | Fallflug setzen |
| `Entity.IsFallFlying` | `bool` | Im Fallflug |
| `Entity.SetFlying(bool)` | `void` | Fliegen setzen |
| `Entity.IsFlying` | `bool` | Fliegt |
| `Entity.SetNoAi(bool)` | `void` | KI ausschalten |
| `Entity.HasNoAi` | `bool` | Ist KI ausgeschaltet |
| `Entity.SetAi(bool)` | `void` | KI ein/aus |
| `Entity.IsAiDisabled` | `bool` | Ist KI deaktiviert |
| `Entity.SetPersistenceRequired(bool)` | `void` | Persistenz setzen (despawnt nicht) |
| `Entity.IsPersistent` | `bool` | Ist persistent |

### Reiten und Fahrzeuge
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.StartRiding(entity)` | `bool` | Auf Entität aufsitzen |
| `Entity.StopRiding()` | `void` | Absitzen |
| `Entity.IsRiding` | `bool` | Reitet auf etwas |
| `Entity.Vehicle` | `Entity` | Fahrzeug |
| `Entity.GetPassengers()` | `List<Entity>` | Passagierliste |
| `Entity.AddPassenger(entity)` | `void` | Passagier hinzufügen |
| `Entity.RemovePassenger(entity)` | `void` | Passagier entfernen |
| `Entity.ClearPassengers()` | `void` | Alle Passagiere entfernen |
| `Entity.HasControllingPassenger` | `bool` | Hat kontrollierenden Passagier |
| `Entity.GetControllingPassenger()` | `Entity` | Passagier, der kontrolliert |
| `Entity.IsVehicle` | `bool` | Ist Fahrzeug |

### Leine
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.IsLeashed` | `bool` | An der Leine |
| `Entity.GetLeashHolder()` | `Entity` | Wer hält die Leine |
| `Entity.SetLeashHolder(entity)` | `bool` | Leine an Entität befestigen |
| `Entity.SetLeashHolder(player)` | `bool` | Leine an Spieler befestigen |
| `Entity.Unleash()` | `void` | Leine lösen |
| `Entity.SetLeashed(bool)` | `void` | Leine setzen |
| `Entity.Leash()` | `bool` | Leine anbringen |
| `Entity.DropLeash()` | `void` | Leine fallen lassen |

### Ausrüstung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetMainHandItem()` | `ItemStack` | Gegenstand in Haupthand |
| `Entity.SetMainHandItem(item)` | `void` | Gegenstand in Haupthand setzen |
| `Entity.GetOffHandItem()` | `ItemStack` | Gegenstand in Zweithand |
| `Entity.SetOffHandItem(item)` | `void` | Gegenstand in Zweithand setzen |
| `Entity.GetHelmet()` | `ItemStack` | Helm |
| `Entity.SetHelmet(item)` | `void` | Helm setzen |
| `Entity.GetChestplate()` | `ItemStack` | Brustpanzer |
| `Entity.SetChestplate(item)` | `void` | Brustpanzer setzen |
| `Entity.GetLeggings()` | `ItemStack` | Hose |
| `Entity.SetLeggings(item)` | `void` | Hose setzen |
| `Entity.GetBoots()` | `ItemStack` | Stiefel |
| `Entity.SetBoots(item)` | `void` | Stiefel setzen |
| `Entity.GetEquipment(slot)` | `ItemStack` | Gegenstand in Slot (0=Hand, 1-4=Rüstung, 5=Zweithand) |
| `Entity.SetEquipment(slot, item)` | `void` | Gegenstand in Slot setzen |
| `Entity.GetAllEquipment()` | `List<ItemStack>` | Alle Gegenstände |
| `Entity.GetArmorContents()` | `ItemStack[]` | Inhalt der Rüstungsslots |
| `Entity.SetArmorContents(items[])` | `void` | Rüstung setzen |
| `Entity.GetDropChance(slot)` | `float` | Drop-Chance des Slots |
| `Entity.SetDropChance(slot, chance)` | `void` | Drop-Chance setzen |
| `Entity.GetHandDropChances()` | `float[]` | Drop-Chancen der Hände |
| `Entity.GetArmorDropChances()` | `float[]` | Drop-Chancen der Rüstung |
| `Entity.CanPickUpLoot` | `bool` | Kann Beute aufheben |
| `Entity.SetCanPickUpLoot(bool)` | `void` | Beute-Aufheben setzen |
| `Entity.ShouldDropEquipment` | `bool` | Soll Ausrüstung droppen |
| `Entity.SetShouldDropEquipment(bool)` | `void` | Ausrüstungs-Drop setzen |
| `Entity.ShouldDropLoot` | `bool` | Soll Beute droppen |
| `Entity.SetShouldDropLoot(bool)` | `void` | Beute-Drop setzen |

### NBT
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetNBT()` | `string` | NBT als String abrufen |
| `Entity.SetNBT(string)` | `void` | Gesamtes NBT setzen |
| `Entity.MergeNBT(string)` | `void` | NBT zusammenführen |
| `Entity.HasNBT(key)` | `bool` | Hat NBT-Schlüssel |
| `Entity.GetNBTCompound()` | `NBTCompound` | NBT als Objekt |
| `Entity.SetNBTTag(key, value)` | `void` | NBT-Tag setzen |
| `Entity.GetNBTTag(key)` | `object` | NBT-Tag abrufen |

### Welt und Dimension
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.Dimension` | `string` | Dimension der Entität |
| `Entity.SetDimension(string)` | `void` | Dimension ändern |
| `Entity.GetWorld()` | `World` | Welt der Entität |
| `Entity.ChunkX` | `int` | Chunk X |
| `Entity.ChunkZ` | `int` | Chunk Z |

### Interaktion
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.Interact(entity)` | `bool` | Mit Entität interagieren |
| `Entity.Interact(player)` | `bool` | Mit Spieler interagieren |
| `Entity.InteractAt(entity, pos)` | `bool` | An Punkt interagieren |
| `Entity.Attack()` | `void` | Angreifen |
| `Entity.SwingMainHand()` | `void` | Haupthand schwingen |
| `Entity.SwingOffHand()` | `void` | Zweithand schwingen |
| `Entity.UseItem()` | `void` | Gegenstand benutzen |
| `Entity.BreakItem()` | `void` | Gehaltenen Gegenstand zerstören |
| `Entity.DropItem()` | `void` | Gegenstand fallen lassen |

### Klänge
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.PlaySound(sound)` | `void` | Klang abspielen |
| `Entity.PlaySound(sound, volume, pitch)` | `void` | Klang mit Parametern |
| `Entity.GetHurtSound()` | `string` | Verletzungsklang |
| `Entity.GetDeathSound()` | `string` | Todesklang |
| `Entity.GetStepSound()` | `string` | Schrittklang |
| `Entity.GetFallSound()` | `string` | Fallklang |
| `Entity.GetSwimSound()` | `string` | Schwimmklang |
| `Entity.GetSplashSound()` | `string` | Platschklang |

### Alter und Entwicklung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.Age` | `int` | Alter der Entität (Ticks) |
| `Entity.SetAge(int)` | `void` | Alter setzen |
| `Entity.IsBaby` | `bool` | Ist Baby |
| `Entity.SetBaby(bool)` | `void` | Baby setzen |
| `Entity.GetScale()` | `float` | Skalierung der Entität |
| `Entity.GetBreed()` | `bool` | Kann sich vermehren |
| `Entity.CanBreed` | `bool` | Kann sich vermehren |
| `Entity.SetBreed(bool)` | `void` | Vermehrungsfähigkeit setzen |
| `Entity.IsInLove` | `bool` | Im Liebesmodus |
| `Entity.SetInLove(bool)` | `void` | Liebesmodus setzen |
| `Entity.GetLoveCause()` | `string` | Wer hat Liebesmodus ausgelöst |
| `Entity.GetAgeTimer()` | `int` | Alters-Timer |
| `Entity.SetAgeTimer(int)` | `void` | Alters-Timer setzen |

### Zähmung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.IsTamed` | `bool` | Gezähmt |
| `Entity.SetTamed(bool)` | `void` | Zähmung setzen |
| `Entity.GetOwner()` | `string` | Besitzername |
| `Entity.GetOwnerUUID()` | `string` | Besitzer-UUID |
| `Entity.SetOwnerUUID(string)` | `void` | Besitzer setzen (UUID) |
| `Entity.SetOwner(player)` | `void` | Spieler als Besitzer setzen |
| `Entity.SetOwnerName(string)` | `void` | Besitzernamen setzen |
| `Entity.IsSitting` | `bool` | Sitzt |
| `Entity.SetSitting(bool)` | `void` | Sitzen setzen |
| `Entity.IsTameable` | `bool` | Zähmbar |

### Mobs — Zielerfassung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetTarget()` | `Entity` | Aktuelles Ziel |
| `Entity.SetTarget(entity)` | `void` | Ziel setzen |
| `Entity.ClearTarget()` | `void` | Ziel löschen |
| `Entity.GetLastHurtByMob()` | `Entity` | Letzter Mob, der verletzt hat |
| `Entity.SetLastHurtByMob(entity)` | `void` | Letzten Verletzer setzen |
| `Entity.GetLastHurtByPlayer()` | `Player` | Letzter Spieler, der verletzt hat |
| `Entity.GetLastHurtMob()` | `Entity` | Letzter verletzter Mob |
| `Entity.SetLastHurtMob(entity)` | `void` | Letzten Verletzten setzen |
| `Entity.GetAngerTime()` | `int` | Wut-Zeit |
| `Entity.SetAngerTime(int)` | `void` | Wut-Zeit setzen |
| `Entity.GetAngryAt()` | `string` | UUID auf wen wütend |
| `Entity.SetAngryAt(uuid)` | `void` | Wütend auf setzen |
| `Entity.Revenge()` | `void` | Rache am letzten Angreifer |

### Navigation / Wegfindung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.NavigateTo(x, y, z)` | `bool` | Zu Punkt navigieren |
| `Entity.NavigateTo(entity)` | `bool` | Zu Entität navigieren |
| `Entity.NavigateTo(player)` | `bool` | Zu Spieler navigieren |
| `Entity.StopNavigation()` | `void` | Navigation stoppen |
| `Entity.HasPath` | `bool` | Hat Pfad |
| `Entity.GetPath()` | `Path` | Pfad |
| `Entity.SetPath(path)` | `void` | Pfad setzen |
| `Entity.GetNavigation()` | `Navigation` | Navigationsobjekt |
| `Entity.IsNavigating` | `bool` | Navigiert |
| `Entity.GetSpeed()` | `float` | Bewegungsgeschwindigkeit |
| `Entity.SetSpeed(float)` | `void` | Geschwindigkeit setzen |
| `Entity.Follow(entity, speed)` | `bool` | Entität folgen |
| `Entity.Follow(player, speed)` | `bool` | Spieler folgen |
| `Entity.Wander()` | `void` | Zufälliges Umherlaufen |
| `Entity.MoveTo(x, y, z, speed)` | `bool` | Zu Punkt gehen |

### Mobs — Spezifisch
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetVillagerProfession()` | `string` | Beruf des Dorfbewohners |
| `Entity.SetVillagerProfession(string)` | `void` | Beruf setzen |
| `Entity.GetVillagerLevel()` | `int` | Stufe des Dorfbewohners |
| `Entity.SetVillagerLevel(int)` | `void` | Stufe setzen |
| `Entity.GetVillagerXP()` | `int` | XP des Dorfbewohners |
| `Entity.SetVillagerXP(int)` | `void` | XP setzen |
| `Entity.IsVillagerSleeping` | `bool` | Schläft der Dorfbewohner |
| `Entity.IsZombieVillager` | `bool` | Ist Zombie-Dorfbewohner |
| `Entity.CureZombieVillager()` | `void` | Zombie-Dorfbewohner heilen |
| `Entity.GetCatType()` | `int` | Katzentyp (0-9) |
| `Entity.SetCatType(int)` | `void` | Katzentyp setzen |
| `Entity.GetFoxType()` | `string` | Fuchstyp: "red", "snow" |
| `Entity.SetFoxType(string)` | `void` | Fuchstyp setzen |
| `Entity.GetMooshroomType()` | `string` | Mooshroom-Typ: "red", "brown" |
| `Entity.SetMooshroomType(string)` | `void` | Mooshroom-Typ setzen |
| `Entity.GetParrotVariant()` | `int` | Papageien-Variante (0-3) |
| `Entity.SetParrotVariant(int)` | `void` | Variante setzen |
| `Entity.GetRabbitType()` | `int` | Hasentyp (0-5) |
| `Entity.SetRabbitType(int)` | `void` | Typ setzen |
| `Entity.GetHorseColor()` | `string` | Pferdefarbe |
| `Entity.SetHorseColor(string)` | `void` | Farbe setzen |
| `Entity.GetHorseMarkings()` | `string` | Pferdeabzeichen |
| `Entity.SetHorseMarkings(string)` | `void` | Abzeichen setzen |
| `Entity.GetHorseArmor()` | `ItemStack` | Pferderüstung |
| `Entity.SetHorseArmor(item)` | `void` | Pferderüstung setzen |
| `Entity.IsHorseSaddled` | `bool` | Hat Pferd Sattel |
| `Entity.SetHorseSaddled(bool)` | `void` | Sattel setzen |
| `Entity.GetLlamaStrength()` | `int` | Lamastärke (1-5) |
| `Entity.SetLlamaStrength(int)` | `void` | Stärke setzen |
| `Entity.GetLlamaColor()` | `int` | Lamafarbe |
| `Entity.SetLlamaColor(int)` | `void` | Farbe setzen |
| `Entity.GetSheepColor()` | `string` | Schaffarbe (Farbstoff) |
| `Entity.SetSheepColor(string)` | `void` | Farbe setzen |
| `Entity.IsSheepSheared` | `bool` | Ist Schaf geschoren |
| `Entity.SetSheepSheared(bool)` | `void` | Scheren |
| `Entity.GetGoatHorns()` | `int` | Anzahl Ziegenhörner |
| `Entity.SetGoatHorns(int)` | `void` | Hörner setzen |
| `Entity.IsScreamingGoat` | `bool` | Ist schreiende Ziege |
| `Entity.SetScreamingGoat(bool)` | `void` | Schreiende Ziege setzen |
| `Entity.GetPandaGenes()` | `Dict` | Panda-Gene (main/hidden) |
| `Entity.SetPandaGene(gene, value)` | `void` | Panda-Gen setzen |
| `Entity.GetBeeHivePos()` | `BlockPos` | Bienenstock-Position |
| `Entity.SetBeeHivePos(x, y, z)` | `void` | Bienenstock-Position setzen |
| `Entity.GetBeeHasNectar` | `bool` | Hat Biene Nektar |
| `Entity.GetBeeHasStung` | `bool` | Hat Biene gestochen |
| `Entity.GetAxolotlVariant()` | `int` | Axolotl-Variante (0-4) |
| `Entity.SetAxolotlVariant(int)` | `void` | Variante setzen |
| `Entity.GetFrogVariant()` | `string` | Frosch-Variante: "temperate", "warm", "cold" |
| `Entity.SetFrogVariant(string)` | `void` | Variante setzen |
| `Entity.GetCamelDashing` | `bool` | Sprintet das Kamel |
| `Entity.SetCamelDashing(bool)` | `void` | Kamel-Sprint setzen |
| `Entity.GetSnailageState()` | `string` | Schneckenzustand |
| `Entity.GetWardenAnger()` | `int` | Warden-Wut |
| `Entity.SetWardenAnger(int)` | `void` | Wut setzen |

### Slimes und Magma Cubes
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetSlimeSize()` | `int` | Slime-Größe |
| `Entity.SetSlimeSize(int)` | `void` | Größe setzen |

### Creeper
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetCreeperFuse()` | `int` | Zündzeit (Ticks) |
| `Entity.SetCreeperFuse(int)` | `void` | Zündzeit setzen |
| `Entity.GetCreeperExplosionRadius()` | `int` | Explosionsradius |
| `Entity.SetCreeperExplosionRadius(int)` | `void` | Radius setzen |
| `Entity.IsCreeperCharged` | `bool` | Geladen (Blitz) |
| `Entity.SetCreeperCharged(bool)` | `void` | Ladung setzen |
| `Entity.IgniteCreeper()` | `void` | Creeper zünden |

### Enderman
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetEndermanHeldBlock()` | `string` | Gehaltener Block |
| `Entity.SetEndermanHeldBlock(block)` | `void` | Gehaltenen Block setzen |
| `Entity.IsEndermanScreaming` | `bool` | Schreit |
| `Entity.SetEndermanScreaming(bool)` | `void` | Schreien setzen |

### Phantom
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetPhantomSize()` | `int` | Phantom-Größe |
| `Entity.SetPhantomSize(int)` | `void` | Größe setzen |

### Shulker
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetShulkerColor()` | `string` | Shulker-Farbe |
| `Entity.SetShulkerColor(string)` | `void` | Farbe setzen |
| `Entity.GetShulkerAttachedFace()` | `string` | Angeheftete Seite |
| `Entity.GetShulkerPeekAmount()` | `int` | Öffnungsgrad |

### Wirkungsbereichswolke
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetAoeRadius()` | `float` | Wolkenradius |
| `Entity.SetAoeRadius(float)` | `void` | Radius setzen |
| `Entity.GetAoeColor()` | `int` | Wolkenfarbe (RGB) |
| `Entity.SetAoeColor(int)` | `void` | Farbe setzen |
| `Entity.GetAoeDuration()` | `int` | Dauer |
| `Entity.SetAoeDuration(int)` | `void` | Dauer setzen |
| `Entity.GetAoeWaitTime()` | `int` | Zeit seit Erstellung |
| `Entity.GetAoeParticle()` | `string` | Wolkenpartikel |
| `Entity.SetAoeParticle(string)` | `void` | Partikel setzen |

### Rahmen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetItemFrameItem()` | `ItemStack` | Gegenstand im Rahmen |
| `Entity.SetItemFrameItem(item)` | `void` | Gegenstand in Rahmen setzen |
| `Entity.GetItemFrameRotation()` | `int` | Rotation (0-7) |
| `Entity.SetItemFrameRotation(int)` | `void` | Rotation setzen |
| `Entity.IsItemFrameFixed` | `bool` | Ist Rahmen fixiert |
| `Entity.SetItemFrameFixed(bool)` | `void` | Fixierten Rahmen setzen |
| `Entity.IsItemFrameVisible` | `bool` | Ist Rahmen sichtbar |
| `Entity.SetItemFrameVisible(bool)` | `void` | Sichtbarkeit setzen |
| `Entity.IsItemFrameMap` | `bool` | Ist Karte im Rahmen |

### Rüstungsständer
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.IsArmorStandSmall` | `bool` | Ist kleiner Rüstungsständer |
| `Entity.SetArmorStandSmall(bool)` | `void` | Klein setzen |
| `Entity.IsArmorStandMarker` | `bool` | Ist Marker (unsichtbar, Hitbox) |
| `Entity.SetArmorStandMarker(bool)` | `void` | Marker setzen |
| `Entity.IsArmorStandShowArms` | `bool` | Arme zeigen |
| `Entity.SetArmorStandShowArms(bool)` | `void` | Arme setzen |
| `Entity.IsArmorStandNoBasePlate` | `bool` | Ohne Bodenplatte |
| `Entity.SetArmorStandNoBasePlate(bool)` | `void` | Bodenplatte setzen |
| `Entity.IsArmorStandNoGravity` | `bool` | Ohne Schwerkraft |
| `Entity.SetArmorStandNoGravity(bool)` | `void` | Schwerkraft setzen |
| `Entity.IsArmorStandNoClip` | `bool` | Noclip |
| `Entity.SetArmorStandNoClip(bool)` | `void` | Noclip setzen |
| `Entity.SetArmorStandPose(part, x, y, z)` | `void` | Pose setzen (head, body, leftArm, rightArm, leftLeg, rightLeg) |
| `Entity.GetArmorStandPose(part)` | `Vector3` | Pose abrufen |
| `Entity.SetArmorStandHeadPose(x, y, z)` | `void` | Kopfposition |
| `Entity.SetArmorStandBodyPose(x, y, z)` | `void` | Körperposition |
| `Entity.SetArmorStandLeftArmPose(x, y, z)` | `void` | Linker Arm |
| `Entity.SetArmorStandRightArmPose(x, y, z)` | `void` | Rechter Arm |
| `Entity.SetArmorStandLeftLegPose(x, y, z)` | `void` | Linkes Bein |
| `Entity.SetArmorStandRightLegPose(x, y, z)` | `void` | Rechtes Bein |

### Textanzeige (1.19+)
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.SetTextDisplayText(text)` | `void` | Anzeigetext setzen |
| `Entity.GetTextDisplayText()` | `string` | Text abrufen |
| `Entity.SetTextDisplayBackgroundColor(int)` | `void` | Hintergrundfarbe (ARGB) |
| `Entity.GetTextDisplayBackgroundColor()` | `int` | Hintergrundfarbe abrufen |
| `Entity.SetTextDisplayTextOpacity(byte)` | `void` | Texttransparenz |
| `Entity.SetTextDisplayLineWidth(int)` | `void` | Zeilenbreite |
| `Entity.SetTextDisplayAlignment(string)` | `void` | Ausrichtung: "center", "left", "right" |
| `Entity.SetTextDisplayBillboard(string)` | `void` | Billboard: "fixed", "vertical", "horizontal", "center" |
| `Entity.SetTextDisplayScale(float)` | `void` | Textskalierung |
| `Entity.SetTextDisplayShadow(bool)` | `void` | Textschatten |
| `Entity.SetTextDisplaySeeThrough(bool)` | `void` | Durch Blöcke sichtbar |
| `Entity.SetTextDisplayDefaultBackground(bool)` | `void` | Standardhintergrund |

### Display-Entität (gemeinsam)
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.SetDisplayTranslation(transformation)` | `void` | Transformation setzen |
| `Entity.SetDisplayScale(x, y, z)` | `void` | Skalierung setzen |
| `Entity.SetDisplayTranslation(x, y, z)` | `void` | Translation setzen |
| `Entity.SetDisplayLeftRotation(x, y, z)` | `void` | Linke Rotation |
| `Entity.SetDisplayRightRotation(x, y, z)` | `void` | Rechte Rotation |
| `Entity.SetDisplayBillboard(string)` | `void` | Billboard-Modus |
| `Entity.SetDisplayBrightness(block, sky)` | `void` | Helligkeit |
| `Entity.SetDisplayViewRange(float)` | `void` | Sichtweite |
| `Entity.SetDisplayShadowRadius(float)` | `void` | Schattenradius |
| `Entity.SetDisplayShadowStrength(float)` | `void` | Schattenstärke |
| `Entity.SetDisplayGlowColorOverride(int)` | `void` | Leuchtfarbe |
| `Entity.SetDisplayStartInterpolation(int)` | `void` | Interpolationsstart |
| `Entity.SetDisplayInterpolationDuration(int)` | `void` | Interpolationsdauer |
| `Entity.SetDisplayTeleportDuration(int)` | `void` | Teleportationsdauer |

### Sonstiges
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Entity.GetTicksLived()` | `int` | Gelebte Ticks |
| `Entity.GetPose()` | `string` | Pose: "standing", "fall_flying", "sleeping", "swimming", "spin_attack", "sneaking", "long_jumping", "dying", "croaking", "using_tongue", "sitting", "sniffing", "digging" |
| `Entity.SetPose(string)` | `void` | Pose setzen |
| `Entity.GetRemovalReason()` | `string` | Entfernungsgrund |
| `Entity.SetRemovalReason(string)` | `void` | Entfernungsgrund setzen |
| `Entity.ShouldBeSaved` | `bool` | Soll gespeichert werden |
| `Entity.SetShouldBeSaved(bool)` | `void` | Speicherung setzen |
| `Entity.GetEntityCategory()` | `string` | Kategorie: "monster", "creature", "ambient", "water_creature", "water_ambient", "misc" |
| `Entity.GetClassification()` | `string` | Klassifizierung |
| `Entity.GetMobType()` | `string` | Mob-Typ |
| `Entity.GetCreatureAttribute()` | `string` | Kreaturattribut: "undead", "arthropod", "undefined", "water", "illager" |
| `Entity.GetExperienceReward()` | `int` | XP fürs Töten |
| `Entity.SetExperienceReward(int)` | `void` | XP setzen |
| `Entity.GetEnchantmentSeed()` | `int` | Verzauberungs-Seed |
| `Entity.CopyDataFrom(entity)` | `void` | Daten von Entität kopieren |
| `Entity.SendMessage(message)` | `void` | Nachricht senden (falls empfangsbereit) |

---

## Beispiele

### Mob-Modifikation
```glang
// Zombie mit Ausrüstung spawnen
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
zombie.SetDropChance(0, 0.0f)   // Haupthand droppt nicht
zombie.SetDropChance(1, 0.0f)   // Stiefel droppen nicht

// Ziel auf Spieler setzen
zombie.SetTarget(Player)
```

### Rüstungsständer-Pose
```glang
var stand = World.SpawnArmorStand(100, 64, -200)
stand.SetArmorStandShowArms(true)
stand.SetArmorStandSmall(false)
stand.SetArmorStandMarker(false)
stand.SetArmorStandHeadPose(30, 0, 0)     // Kopf leicht nach unten
stand.SetArmorStandRightArmPose(-45, 0, 0) // Arm ausgestreckt

// Anziehen
stand.SetHelmet(ItemStack("minecraft:carved_pumpkin"))
stand.SetChestplate(ItemStack("minecraft:leather_chestplate"))
```
