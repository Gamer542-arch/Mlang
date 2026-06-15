# Player API — vollständige Dokumentation

## Methodenübersicht

### Position und Bewegung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.X` | `double` | X-Koordinate |
| `Player.Y` | `double` | Y-Koordinate |
| `Player.Z` | `double` | Z-Koordinate |
| `Player.Yaw` | `float` | Horizontaler Winkel (Y-Rotation) |
| `Player.Pitch` | `float` | Vertikaler Winkel (X-Rotation) |
| `Player.TeleportTo(x, y, z)` | `bool` | Teleportiere zu Koordinaten |
| `Player.TeleportTo(x, y, z, yaw, pitch)` | `bool` | Teleportiere mit Rotation |
| `Player.TeleportTo(player)` | `bool` | Teleportiere zu anderem Spieler |
| `Player.TeleportTo(entity)` | `bool` | Teleportiere zu Entität |
| `Player.SetPosition(x, y, z)` | `void` | Setze Position (ohne Lerp) |
| `Player.SetRotation(yaw, pitch)` | `void` | Setze Rotation |
| `Player.LookAt(x, y, z)` | `void` | Blick auf Punkt richten |
| `Player.LookAt(entity)` | `void` | Blick auf Entität richten |
| `Player.GetBlockPos()` | `BlockPos` | Position als Block (int) |
| `Player.GetChunkPos()` | `ChunkPos` | Chunk-Position |
| `Player.DistanceTo(x, y, z)` | `double` | Distanz zum Punkt |
| `Player.DistanceTo(entity)` | `double` | Distanz zur Entität |
| `Player.DistanceToSqr(x, y, z)` | `double` | Distanz² zum Punkt |
| `Player.IsInRange(x, y, z, radius)` | `bool` | Ist Spieler in Reichweite |

### Bewegung und Steuerung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.Velocity` | `Vector3` | Aktuelle Geschwindigkeit |
| `Player.SetVelocity(vx, vy, vz)` | `void` | Setze Geschwindigkeit |
| `Player.AddVelocity(vx, vy, vz)` | `void` | Füge Geschwindigkeit hinzu |
| `Player.Knockback(strength, x, z)` | `void` | Rückstoß |
| `Player.Jump()` | `void` | Erzwinge Sprung |
| `Player.SetJumping(bool)` | `void` | Setze Sprungzustand |
| `Player.IsJumping` | `bool` | Springt der Spieler |
| `Player.Sprint(bool)` | `void` | Sprint ein/aus |
| `Player.IsSprinting` | `bool` | Sprintet der Spieler |
| `Player.Sneak(bool)` | `void` | Schleichen ein/aus |
| `Player.IsSneaking` | `bool` | Schleicht der Spieler |
| `Player.Fly(bool)` | `void` | Fliegen ein/aus |
| `Player.IsFlying` | `bool` | Fliegt der Spieler |
| `Player.SetFlySpeed(float)` | `void` | Fluggeschwindigkeit (0.0-1.0) |
| `Player.SetWalkSpeed(float)` | `void` | Laufgeschwindigkeit (0.0-1.0) |
| `Player.Swim(bool)` | `void` | Schwimmen ein/aus |
| `Player.IsSwimming` | `bool` | Schwimmt der Spieler |
| `Player.SetGliding(bool)` | `void` | Gleitflug ein/aus (Elytra) |
| `Player.IsGliding` | `bool` | Gleitet der Spieler |
| `Player.SetFallFlying(bool)` | `void` | Fallflug ein/aus |
| `Player.IsFallFlying` | `bool` | Im Fallflug |
| `Player.SetSprinting(bool)` | `void` | Sprint |
| `Player.SwingHand(hand?)` | `void` | Hand schwingen (main/off) |
| `Player.Attack()` | `void` | Angriff (Linksklick) |
| `Player.Interact()` | `void` | Interaktion (Rechtsklick) |
| `Player.PickBlock()` | `void` | Block aufnehmen (Mittelklick) |
| `Player.DropItem(dropAll?)` | `void` | Gegenstand fallen lassen |
| `Player.UseItem()` | `void` | Gegenstand benutzen |

### Gesundheit und Hunger
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.Health` | `float` | Aktuelles HP |
| `Player.MaxHealth` | `float` | Maximales HP |
| `Player.SetHealth(float)` | `void` | Setze HP |
| `Player.SetMaxHealth(float)` | `void` | Setze max HP |
| `Player.Heal(amount)` | `void` | Heile um Betrag |
| `Player.Damage(amount)` | `void` | Füge Schaden zu |
| `Player.Damage(amount, source)` | `void` | Füge Schaden zu (Typ) |
| `Player.Kill()` | `void` | Töte Spieler |
| `Player.IsAlive` | `bool` | Lebt der Spieler |
| `Player.IsDead` | `bool` | Ist der Spieler tot |
| `Player.DeathTime` | `int` | Zeit seit Tod (Ticks) |
| `Player.FoodLevel` | `int` | Hungerlevel (0-20) |
| `Player.SetFoodLevel(int)` | `void` | Setze Hunger |
| `Player.Saturation` | `float` | Sättigung (0.0-5.0) |
| `Player.SetSaturation(float)` | `void` | Setze Sättigung |
| `Player.Exhaustion` | `float` | Erschöpfung (0.0-4.0) |
| `Player.SetExhaustion(float)` | `void` | Setze Erschöpfung |
| `Player.AirSupply` | `int` | Luftvorrat (0-300) |
| `Player.SetAirSupply(int)` | `void` | Setze Luftvorrat |
| `Player.MaxAir` | `int` | Maximaler Luftvorrat |
| `Player.FireTicks` | `int` | Feuer-Ticks (-20 für Dauer, 0 = nein) |
| `Player.SetFireTicks(int)` | `void` | Setze Feuer-Ticks |
| `Player.FireImmuneTicks` | `int` | Feuerimmunitäts-Ticks |
| `Player.SetFireImmuneTicks(int)` | `void` | Setze Feuerimmunität |
| `Player.FrozenTicks` | `int` | Gefrier-Ticks |
| `Player.SetFrozenTicks(int)` | `void` | Setze Gefrieren |
| `Player.IsOnFire` | `bool` | Brennt der Spieler |
| `Player.IsOnGround` | `bool` | Auf dem Boden |
| `Player.IsInWater` | `bool` | Im Wasser |
| `Player.IsInLava` | `bool` | In Lava |
| `Player.IsUnderwater` | `bool` | Unter Wasser |
| `Player.IsWet` | `bool` | Nass (Wasser/Regen) |
| `Player.IsInRain` | `bool` | Im Regen |
| `Player.IsInBubbleColumn` | `bool` | In Blasensäule |
| `Player.IsInsideWall` | `bool` | In Wand |
| `Player.FallDistance` | `float` | Fallhöhe |
| `Player.SetFallDistance(float)` | `void` | Setze/zurücksetzen Fallhöhe |
| `Player.Absorption` | `float` | Absorption (goldene Herzen) |
| `Player.SetAbsorption(float)` | `void` | Setze Absorption |
| `Player.StingerCount` | `int` | Stachelanzahl (Bienen) |
| `Player.SetStingerCount(int)` | `void` | Setze Stachel |
| `Player.ArrowCount` | `int` | Anzahl Pfeile im Körper |
| `Player.SetArrowCount(int)` | `void` | Setze Pfeile |

### Spielmodus und Berechtigungen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.GameMode` | `string` | Spielmodus: "survival", "creative", "adventure", "spectator" |
| `Player.SetGameMode(string)` | `void` | Ändere Spielmodus |
| `Player.IsCreative` | `bool` | Ist Kreativmodus |
| `Player.IsSpectator` | `bool` | Ist Zuschauermodus |
| `Player.IsAdventure` | `bool` | Ist Abenteuermodus |
| `Player.IsSurvival` | `bool` | Ist Überlebensmodus |
| `Player.IsOp` | `bool` | Ist Server-Operator |
| `Player.SetOp(bool)` | `void` | OP geben/entziehen |
| `Player.AllowFlight` | `bool` | Darf fliegen |
| `Player.SetAllowFlight(bool)` | `void` | Fliegen erlauben |
| `Player.FlyingSpeed` | `float` | Fluggeschwindigkeit |
| `Player.SetFlyingSpeed(float)` | `void` | Setze Fluggeschwindigkeit |
| `Player.WalkSpeed` | `float` | Laufgeschwindigkeit |
| `Player.SetWalkSpeed(float)` | `void` | Setze Laufgeschwindigkeit |
| `Player.ViewDistance` | `int` | Sichtweite |
| `Player.SetViewDistance(int)` | `void` | Setze Sichtweite |
| `Player.CanFly` | `bool` | Kann fliegen |
| `Player.CanSee(entity)` | `bool` | Kann Entität sehen |
| `Player.HasLineOfSight(x, y, z)` | `bool` | Hat Sichtlinie |

### Inventar und Gegenstände
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.MainHandItem` | `ItemStack` | Gegenstand in Haupthand |
| `Player.OffHandItem` | `ItemStack` | Gegenstand in Zweithand |
| `Player.SetMainHandItem(item)` | `void` | Setze Gegenstand in Haupthand |
| `Player.SetOffHandItem(item)` | `void` | Setze Gegenstand in Zweithand |
| `Player.ArmorHelmet` | `ItemStack` | Helm |
| `Player.ArmorChest` | `ItemStack` | Brustpanzer |
| `Player.ArmorLegs` | `ItemStack` | Hose |
| `Player.ArmorBoots` | `ItemStack` | Stiefel |
| `Player.SetArmorHelmet(item)` | `void` | Setze Helm |
| `Player.SetArmorChest(item)` | `void` | Setze Brustpanzer |
| `Player.SetArmorLegs(item)` | `void` | Setze Hose |
| `Player.SetArmorBoots(item)` | `void` | Setze Stiefel |
| `Player.SetArmor(items[])` | `void` | Setze gesamte Rüstung |
| `Player.GiveItem(item, count?)` | `void` | Gib Gegenstand an Spieler |
| `Player.GiveItem(ItemStack)` | `void` | Gib Item-Stack |
| `Player.RemoveItem(item, count?)` | `void` | Entferne Gegenstand aus Inventar |
| `Player.ClearInventory()` | `void` | Leere Inventar |
| `Player.HasItem(item)` | `bool` | Hat Gegenstand (ID) |
| `Player.HasItem(ItemStack)` | `bool` | Hat Item-Stack |
| `Player.ItemCount(item)` | `int` | Anzahl des Gegenstands im Inventar |
| `Player.GetItemInSlot(slot)` | `ItemStack` | Item in Slot (0-40) |
| `Player.SetItemInSlot(slot, item)` | `void` | Setze Item in Slot |
| `Player.GetSelectedSlot()` | `int` | Ausgewählter Hotbar-Slot (0-8) |
| `Player.SetSelectedSlot(int)` | `void` | Wähle Hotbar-Slot |
| `Player.GetInventory()` | `Inventory` | Referenz zur Inventory API |
| `Player.GetEnderChest()` | `Inventory` | Enderkiste des Spielers |
| `Player.OpenInventory(inv)` | `void` | Öffne Inventar-Oberfläche |
| `Player.CloseScreen()` | `void` | Schließe geöffneten Bildschirm |
| `Player.IsScreenOpen` | `bool` | Ist ein Bildschirm geöffnet |
| `Player.DropItemStack()` | `void` | Ganzen Stack fallen lassen |
| `Player.DropSelectedItem()` | `void` | Ausgewähltes Item fallen lassen |

### Erfahrung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.Experience` | `int` | Gesamt-XP |
| `Player.Level` | `int` | Erfahrungsstufe |
| `Player.ExperienceBar` | `float` | XP-Leiste (0.0-1.0) |
| `Player.SetExperience(int)` | `void` | Setze Gesamt-XP |
| `Player.SetLevel(int)` | `void` | Setze Stufe |
| `Player.GiveExperience(int)` | `void` | Gib XP |
| `Player.GiveExperienceLevels(int)` | `void` | Gib Stufen |
| `Player.GetXpNeededForNextLevel()` | `int` | XP für nächste Stufe |
| `Player.GetXpProgress()` | `float` | Fortschritt zur nächsten Stufe (0.0-1.0) |
| `Player.GetTotalExperience()` | `int` | Gesamt-XP in Zahlen |

### Statuseffekte
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.AddEffect(effect, duration, amplifier)` | `void` | Füge Effekt hinzu |
| `Player.AddEffect(effect, duration, amplifier, particles?, icon?)` | `void` | Füge Effekt mit Optionen hinzu |
| `Player.RemoveEffect(effect)` | `void` | Entferne Effekt |
| `Player.ClearEffects()` | `void` | Entferne alle Effekte |
| `Player.HasEffect(effect)` | `bool` | Hat Effekt |
| `Player.GetEffect(effect)` | `Effect` | Hole Effekt |
| `Player.GetEffects()` | `List<Effect>` | Liste aller Effekte |
| `Player.IsAffectedByEffects` | `bool` | Unter Einfluss eines Effekts |

### Bildschirm und Anzeige
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.ShowTitle(title)` | `void` | Zeige Titel (großer Text) |
| `Player.ShowTitle(title, subtitle, fadeIn, stay, fadeOut)` | `void` | Titel mit Optionen |
| `Player.ShowSubtitle(subtitle)` | `void` | Untertitel |
| `Player.ShowActionBar(text)` | `void` | Text über HP-Leiste |
| `Player.SendMessage(text)` | `void` | Private Chat-Nachricht |
| `Player.SendMessage(text, position)` | `void` | Nachricht an Position: chat, action_bar, system |
| `Player.SendHotbarMessage(text)` | `void` | Schnelle Hotbar-Nachricht |
| `Player.ResetTitle()` | `void` | Titel zurücksetzen |
| `Player.ClearTitle()` | `void` | Titel löschen |
| `Player.SetTitleTimes(fadeIn, stay, fadeOut)` | `void` | Setze Titel-Zeiten |
| `Player.SetSubtitle(subtitle)` | `void` | Setze Untertitel (vor show) |
| `Player.ShowBossBar(bar)` | `void` | Zeige Bossleiste |
| `Player.HideBossBar()` | `void` | Verstecke Bossleiste |

### Klänge
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.PlaySound(sound)` | `void` | Spiele Klang ab |
| `Player.PlaySound(sound, volume, pitch)` | `void` | Klang mit Lautstärke |
| `Player.PlaySound(sound, volume, pitch, x, y, z)` | `void` | Klang an Position |
| `Player.StopSound(sound)` | `void` | Stoppe Klang |
| `Player.StopAllSounds()` | `void` | Stoppe alle Klänge |

### Kamera und Ansicht
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.SetCameraEntity(entity)` | `void` | Setze Kamera auf Entität |
| `Player.SetCameraEntity(player)` | `void` | Setze Kamera auf Spieler |
| `Player.ResetCamera()` | `void` | Stelle normale Kamera wieder her |
| `Player.SetRenderDistance(int)` | `void` | Renderdistanz |
| `Player.SetFovMultiplier(float)` | `void` | FOV-Multiplikator |

### Statistiken und Erfolge
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.GetStatistic(type, key)` | `int` | Hole Statistik |
| `Player.SetStatistic(type, key, value)` | `void` | Setze Statistik |
| `Player.ResetStatistic(type, key)` | `void` | Setze Statistik zurück |
| `Player.GetAdvancementProgress(adv)` | `string` | Fortschritt des Erfolgs |
| `Player.GrantAdvancement(adv)` | `void` | Schalte Erfolg frei |
| `Player.RevokeAdvancement(adv)` | `void` | Entziehe Erfolg |
| `Player.HasAdvancement(adv)` | `bool` | Hat Erfolg |

### Umgebungsinteraktion
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.OpenChest(x, y, z)` | `Inventory` | Öffne Kiste |
| `Player.OpenWorkbench()` | `void` | Öffne Werkbank |
| `Player.OpenFurnace(x, y, z)` | `void` | Öffne Ofen |
| `Player.OpenEnchantingTable(x, y, z)` | `void` | Öffne Zaubertisch |
| `Player.OpenAnvil(x, y, z)` | `void` | Öffne Amboss |
| `Player.OpenGrindstone(x, y, z)` | `void` | Öffne Schleifstein |
| `Player.OpenCartographyTable(x, y, z)` | `void` | Öffne Kartografietisch |
| `Player.OpenLoom(x, y, z)` | `void` | Öffne Webstuhl |
| `Player.OpenStonecutter(x, y, z)` | `void` | Öffne Steinsäge |
| `Player.OpenSmithingTable(x, y, z)` | `void` | Öffne Schmiedetisch |
| `Player.OpenBrewingStand(x, y, z)` | `void` | Öffne Braustand |
| `Player.OpenHopper(x, y, z)` | `void` | Öffne Trichter |
| `Player.OpenBarrel(x, y, z)` | `void` | Öffne Fass |
| `Player.OpenShulkerBox(x, y, z)` | `void` | Öffne Shulkerkiste |
| `Player.BreakBlock(x, y, z)` | `void` | Zerstöre Block (wie Klick) |
| `Player.InteractBlock(x, y, z)` | `void` | Interagiere mit Block |
| `Player.InteractEntity(entity)` | `void` | Interagiere mit Entität |
| `Player.AttackEntity(entity)` | `void` | Greife Entität an |
| `Player.Sleep(x, y, z)` | `bool` | Lege dich schlafen |
| `Player.WakeUp()` | `void` | Aufwachen |
| `Player.IsSleeping` | `bool` | Schläft der Spieler |
| `Player.SleepTimer` | `int` | Schlaf-Timer (Ticks) |
| `Player.Respawn()` | `void` | Spieler respawnen |

### Reiten und Fahrzeuge
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.StartRiding(entity)` | `bool` | Auf Entität aufsitzen |
| `Player.StopRiding()` | `void` | Absitzen |
| `Player.IsRiding` | `bool` | Reitet der Spieler auf etwas |
| `Player.Vehicle` | `Entity` | Fahrzeug, auf dem der Spieler reitet |
| `Player.GetPassengers()` | `List<Entity>` | Passagierliste (wenn jemand auf dem Spieler reitet) |
| `Player.HasControllingPassenger` | `bool` | Steuert jemand den Spieler |
| `Player.GetControllingPassenger()` | `Entity` | Wer steuert den Spieler |
| `Player.Dismount()` | `void` | Vom Fahrzeug absteigen |
| `Player.Mount(entity)` | `void` | Auf Entität aufsitzen |
| `Player.SetYaw(float)` | `void` | Setze horizontalen Winkel |
| `Player.SetPitch(float)` | `void` | Setze vertikalen Winkel |

### Angriffe und Kampf
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.GetAttackCooldown()` | `float` | Angriffs-Cooldown (0.0-1.0) |
| `Player.ResetAttackCooldown()` | `void` | Cooldown zurücksetzen |
| `Player.GetLastAttackTime()` | `int` | Tick des letzten Angriffs |
| `Player.IsBlocking` | `bool` | Blockt der Spieler (Schild) |
| `Player.IsClimbing` | `bool` | Klettert der Spieler |
| `Player.GetLastHurtByEntity()` | `Entity` | Letzte Entität, die verletzt hat |
| `Player.GetLastHurtByPlayer()` | `Player` | Letzter Spieler, der verletzt hat |
| `Player.GetLastHurtEntity()` | `Entity` | Letzte verletzte Entität |
| `Player.GetLastDamageSource()` | `string` | Letzte Schadensquelle |
| `Player.GetLastDamageAmount()` | `float` | Letzte Schadensmenge |
| `Player.InvulnerableTime` | `int` | Unverwundbarkeits-Ticks nach Angriff |
| `Player.SetInvulnerableTime(int)` | `void` | Setze Unverwundbarkeits-Ticks |

### Spielerinformationen
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.Name` | `string` | Spielername |
| `Player.UUID` | `string` | Spieler-UUID (mit Bindestrichen) |
| `Player.UUIDShort` | `string` | UUID ohne Bindestriche |
| `Player.DisplayName` | `string` | Anzeigename (mit Farben) |
| `Player.SetDisplayName(string)` | `void` | Setze Anzeigenamen |
| `Player.PlayerListName` | `string` | Name in Spielerliste |
| `Player.SetPlayerListName(string)` | `void` | Setze Namen in Spielerliste |
| `Player.GetPlayerList()` | `List<Player>` | Liste aller Online-Spieler |
| `Player.GetWorld()` | `World` | Welt, in der sich der Spieler befindet |
| `Player.Dimension` | `string` | Dimension: "overworld", "nether", "end" |
| `Player.GetSpawnPosition()` | `BlockPos` | Spawn-Position |
| `Player.SetSpawnPosition(x, y, z)` | `void` | Setze Spawn-Position |
| `Player.SetSpawnPosition(x, y, z, force)` | `void` | Setze Spawn (force=true überschreibt) |
| `Player.Ping` | `int` | Spieler-Ping (ms) |
| `Player.Locale` | `string` | Spielersprache (z.B. "de_DE") |
| `Player.SkinUrl` | `string` | Skin-URL des Spielers |
| `Player.CapeUrl` | `string` | Umhang-URL (falls vorhanden) |
| `Player.ModelType` | `string` | Modelltyp: "default" / "slim" |
| `Player.MainArm` | `string` | Haupthand: "right" / "left" |
| `Player.SetMainArm(string)` | `void` | Setze Haupthand |
| `Player.ClientBrand` | `string` | Client des Spielers (z.B. "vanilla", "fabric") |
| `Player.ServerBrand` | `string` | Server-Marke |
| `Player.ChunkX` | `int` | Chunk X des Spielers |
| `Player.ChunkZ` | `int` | Chunk Z des Spielers |
| `Player.ChunkY` | `int` | Chunk Y des Spielers |
| `Player.GetScore()` | `int` | Spielerpunktzahl (Score) |
| `Player.SetScore(int)` | `void` | Setze Punktzahl |

### NBT
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.GetNBT()` | `string` | Hole Spieler-NBT als String |
| `Player.SetNBT(string)` | `void` | Setze gesamtes Spieler-NBT |
| `Player.MergeNBT(string)` | `void` | NBT zusammenführen (Felder hinzufügen/ändern) |
| `Player.GetPersistentData()` | `NBTCompound` | Persistente Daten (Mod-Daten) |
| `Player.SetPersistentData(key, value)` | `void` | Persistente Daten speichern |
| `Player.GetPersistentData(key)` | `object` | Persistente Daten lesen |

### Scoreboard und Teams
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.GetScoreboardObjective(objective)` | `int` | Punktzahl in Objective |
| `Player.SetScoreboardObjective(objective, score)` | `void` | Setze Punktzahl in Objective |
| `Player.GetTeam()` | `string` | Teamname des Spielers |
| `Player.SetTeam(team)` | `void` | Zu Team hinzufügen |
| `Player.RemoveFromTeam()` | `void` | Aus Team entfernen |
| `Player.GetTeamColor()` | `string` | Teamfarbe (hex) |

### Pakete senden
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.SendPacket(packet)` | `void` | Sende Paket an Spieler |
| `Player.SendBlockUpdate(x, y, z)` | `void` | Sende Block-Update |
| `Player.SendLightUpdate(x, y, z)` | `void` | Sende Licht-Update |
| `Player.SendSignText(x, y, z, lines[])` | `void` | Sende Text auf Schild |

### Sonstiges
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.GetRiptideTicks()` | `int` | Riptide-Ticks (Dreizack) |
| `Player.SetRiptideTicks(int)` | `void` | Setze Riptide-Ticks |
| `Player.GetPortalCooldown()` | `int` | Portal-Cooldown |
| `Player.SetPortalCooldown(int)` | `void` | Setze Portal-Cooldown |
| `Player.GetPortalWaitTime()` | `int` | Wartezeit im Portal |
| `Player.IsUsingItem` | `bool` | Benutzt der Spieler einen Gegenstand |
| `Player.GetUsingItem()` | `ItemStack` | Gegenstand, den er benutzt |
| `Player.GetActiveItem()` | `ItemStack` | Aktiver Gegenstand |
| `Player.GetActiveItemUseTime()` | `int` | Nutzungsdauer des Gegenstands |
| `Player.BedPosition` | `BlockPos` | Bettposition |
| `Player.HasBed` | `bool` | Hat ein gesetztes Bett |
| `Player.GetChunkCoordIntPair()` | `string` | Spieler-Chunks als String |

---

## Beispiele

### Vollständige Spielerkontrolle
```glang
#version 1.0
#name "Player Control Demo"
#key F6

// Teleportation und Bewegung
Player.TeleportTo(100, 64, -200)
Player.SetWalkSpeed(0.5f)
Player.SetFlySpeed(0.3f)
Player.Fly(true)

// Gesundheit
Player.SetMaxHealth(40)
Player.SetHealth(40)
Player.AddEffect("regeneration", 200, 2)
Player.AddEffect("speed", 600, 1)

// Inventar
Player.GiveItem("minecraft:diamond_sword", 1)
Player.GiveItem("minecraft:elytra", 1)
Player.SetArmor(
    "minecraft:diamond_helmet",
    "minecraft:diamond_chestplate",
    "minecraft:diamond_leggings",
    "minecraft:diamond_boots"
)

// Anzeige
Player.ShowTitle("§6Hallo!", "§7MLang Demo", 10, 70, 20)
Player.SendMessage("§aSteuerung funktioniert!")

// Status prüfen
if (Player.IsFlying) {
    Chat.Send("Flug aktiv!")
}

// Erfahrung
Player.SetLevel(50)
Player.GiveExperience(1000)
```
