# Player API — pełna dokumentacja

## Spis method

### Pozycja i ruch
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.X` | `double` | Koordynat X |
| `Player.Y` | `double` | Koordynat Y |
| `Player.Z` | `double` | Koordynat Z |
| `Player.Yaw` | `float` | Kąt poziomy (rotacja Y) |
| `Player.Pitch` | `float` | Kąt pionowy (rotacja X) |
| `Player.TeleportTo(x, y, z)` | `bool` | Teleportacja na koordynaty |
| `Player.TeleportTo(x, y, z, yaw, pitch)` | `bool` | Teleportacja z rotacją |
| `Player.TeleportTo(player)` | `bool` | Teleportacja do innego gracza |
| `Player.TeleportTo(entity)` | `bool` | Teleportacja do encji |
| `Player.SetPosition(x, y, z)` | `void` | Ustaw pozycję (bez lerp) |
| `Player.SetRotation(yaw, pitch)` | `void` | Ustaw rotację |
| `Player.LookAt(x, y, z)` | `void` | Obróć wzrok na punkt |
| `Player.LookAt(entity)` | `void` | Obróć wzrok na encję |
| `Player.GetBlockPos()` | `BlockPos` | Pozycja jako blok (int) |
| `Player.GetChunkPos()` | `ChunkPos` | Pozycja chunka |
| `Player.DistanceTo(x, y, z)` | `double` | Dystans do punktu |
| `Player.DistanceTo(entity)` | `double` | Dystans do encji |
| `Player.DistanceToSqr(x, y, z)` | `double` | Dystans² do punktu |
| `Player.IsInRange(x, y, z, radius)` | `bool` | Czy gracz w zasięgu |

### Ruch i sterowanie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.Velocity` | `Vector3` | Aktualna prędkość |
| `Player.SetVelocity(vx, vy, vz)` | `void` | Ustaw prędkość |
| `Player.AddVelocity(vx, vy, vz)` | `void` | Dodaj prędkość |
| `Player.Knockback(strength, x, z)` | `void` | Odrzut |
| `Player.Jump()` | `void` | Wymuś skok |
| `Player.SetJumping(bool)` | `void` | Ustaw stan skoku |
| `Player.IsJumping` | `bool` | Czy gracz skacze |
| `Player.Sprint(bool)` | `void` | Włącz/wyłącz sprint |
| `Player.IsSprinting` | `bool` | Czy gracz sprintuje |
| `Player.Sneak(bool)` | `void` | Włącz/wyłącz skradanie |
| `Player.IsSneaking` | `bool` | Czy gracz się skrada |
| `Player.Fly(bool)` | `void` | Włącz/wyłącz latanie |
| `Player.IsFlying` | `bool` | Czy gracz lata |
| `Player.SetFlySpeed(float)` | `void` | Prędkość latania (0.0-1.0) |
| `Player.SetWalkSpeed(float)` | `void` | Prędkość chodzenia (0.0-1.0) |
| `Player.Swim(bool)` | `void` | Włącz/wyłącz pływanie |
| `Player.IsSwimming` | `bool` | Czy gracz płynie |
| `Player.SetGliding(bool)` | `void` | Włącz/wyłącz szybownie (elytra) |
| `Player.IsGliding` | `bool` | Czy gracz szybuje |
| `Player.SetFallFlying(bool)` | `void` | Włącz/wyłącz lot spadkowy |
| `Player.IsFallFlying` | `bool` | Czy gracz w locie spadkowym |
| `Player.SetSprinting(bool)` | `void` | Sprint |
| `Player.SwingHand(hand?)` | `void` | Machnięcie ręką (main/off) |
| `Player.Attack()` | `void` | Atak (lewy klik) |
| `Player.Interact()` | `void` | Interakcja (prawy klik) |
| `Player.PickBlock()` | `void` | Pick block (środkowy klik) |
| `Player.DropItem(dropAll?)` | `void` | Upuść przedmiot |
| `Player.UseItem()` | `void` | Użyj przedmiotu |

### Zdrowie i głód
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.Health` | `float` | Aktualne HP |
| `Player.MaxHealth` | `float` | Maksymalne HP |
| `Player.SetHealth(float)` | `void` | Ustaw HP |
| `Player.SetMaxHealth(float)` | `void` | Ustaw max HP |
| `Player.Heal(amount)` | `void` | Ulecz o amount |
| `Player.Damage(amount)` | `void` | Zadaj obrażenia |
| `Player.Damage(amount, source)` | `void` | Zadaj obrażenia (typ) |
| `Player.Kill()` | `void` | Zabij gracza |
| `Player.IsAlive` | `bool` | Czy gracz żyje |
| `Player.IsDead` | `bool` | Czy gracz martwy |
| `Player.DeathTime` | `int` | Czas od śmierci (ticki) |
| `Player.FoodLevel` | `int` | Poziom głodu (0-20) |
| `Player.SetFoodLevel(int)` | `void` | Ustaw głód |
| `Player.Saturation` | `float` | Saturacja (0.0-5.0) |
| `Player.SetSaturation(float)` | `void` | Ustaw saturację |
| `Player.Exhaustion` | `float` | Wyczerpanie (0.0-4.0) |
| `Player.SetExhaustion(float)` | `void` | Ustaw wyczerpanie |
| `Player.AirSupply` | `int` | Poziom powietrza (0-300) |
| `Player.SetAirSupply(int)` | `void` | Ustaw powietrze |
| `Player.MaxAir` | `int` | Maksymalne powietrze |
| `Player.FireTicks` | `int` | Ticki w ogniu (-20 to tyle, 0 = nie) |
| `Player.SetFireTicks(int)` | `void` | Ustaw ticki w ogniu |
| `Player.FireImmuneTicks` | `int` | Ticki odporności na ogień |
| `Player.SetFireImmuneTicks(int)` | `void` | Ustaw odporność na ogień |
| `Player.FrozenTicks` | `int` | Ticki zamrożenia |
| `Player.SetFrozenTicks(int)` | `void` | Ustaw zamrożenie |
| `Player.IsOnFire` | `bool` | Czy gracz płonie |
| `Player.IsOnGround` | `bool` | Czy gracz na ziemi |
| `Player.IsInWater` | `bool` | Czy gracz w wodzie |
| `Player.IsInLava` | `bool` | Czy gracz w lawie |
| `Player.IsUnderwater` | `bool` | Czy gracz pod wodą |
| `Player.IsWet` | `bool` | Czy gracz mokry (woda/deszcz) |
| `Player.IsInRain` | `bool` | Czy gracz na deszczu |
| `Player.IsInBubbleColumn` | `bool` | Czy w kolumnie bąbelkowej |
| `Player.IsInsideWall` | `bool` | Czy gracz w ścianie |
| `Player.FallDistance` | `float` | Dystans upadku |
| `Player.SetFallDistance(float)` | `void` | Resetuj/zmień dystans upadku |
| `Player.Absorption` | `float` | Absorpcja (złote serca) |
| `Player.SetAbsorption(float)` | `void` | Ustaw absorpcję |
| `Player.StingerCount` | `int` | Liczba żądeł (pszczoły) |
| `Player.SetStingerCount(int)` | `void` | Ustaw żądła |
| `Player.ArrowCount` | `int` | Liczba strzał w ciele |
| `Player.SetArrowCount(int)` | `void` | Ustaw strzały |

### Tryb gry i uprawnienia
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.GameMode` | `string` | Tryb gry: "survival", "creative", "adventure", "spectator" |
| `Player.SetGameMode(string)` | `void` | Zmień tryb gry |
| `Player.IsCreative` | `bool` | Czy tryb kreatywny |
| `Player.IsSpectator` | `bool` | Czy tryb spectator |
| `Player.IsAdventure` | `bool` | Czy tryb adventure |
| `Player.IsSurvival` | `bool` | Czy tryb survival |
| `Player.IsOp` | `bool` | Czy operator serwera |
| `Player.SetOp(bool)` | `void` | Nadaj/odbierz OP |
| `Player.AllowFlight` | `bool` | Czy może latać |
| `Player.SetAllowFlight(bool)` | `void` | Zezwól na latanie |
| `Player.FlyingSpeed` | `float` | Prędkość latania |
| `Player.SetFlyingSpeed(float)` | `void` | Ustaw prędkość latania |
| `Player.WalkSpeed` | `float` | Prędkość chodzenia |
| `Player.SetWalkSpeed(float)` | `void` | Ustaw prędkość chodzenia |
| `Player.ViewDistance` | `int` | Dystans widzenia |
| `Player.SetViewDistance(int)` | `void` | Ustaw dystans widzenia |
| `Player.CanFly` | `bool` | Czy może latać |
| `Player.CanSee(entity)` | `bool` | Czy widzi encję |
| `Player.HasLineOfSight(x, y, z)` | `bool` | Czy ma linię widzenia |

### Ekwipunek i przedmioty
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.MainHandItem` | `ItemStack` | Przedmiot w głównej ręce |
| `Player.OffHandItem` | `ItemStack` | Przedmiot w drugiej ręce |
| `Player.SetMainHandItem(item)` | `void` | Ustaw przedmiot w głównej ręce |
| `Player.SetOffHandItem(item)` | `void` | Ustaw przedmiot w drugiej ręce |
| `Player.ArmorHelmet` | `ItemStack` | Hełm |
| `Player.ArmorChest` | `ItemStack` | Napierśnik |
| `Player.ArmorLegs` | `ItemStack` | Spodnie |
| `Player.ArmorBoots` | `ItemStack` | Buty |
| `Player.SetArmorHelmet(item)` | `void` | Ustaw hełm |
| `Player.SetArmorChest(item)` | `void` | Ustaw napierśnik |
| `Player.SetArmorLegs(item)` | `void` | Ustaw spodnie |
| `Player.SetArmorBoots(item)` | `void` | Ustaw buty |
| `Player.SetArmor(items[])` | `void` | Ustaw cały armor |
| `Player.GiveItem(item, count?)` | `void` | Daj przedmiot graczowi |
| `Player.GiveItem(ItemStack)` | `void` | Daj item stack |
| `Player.RemoveItem(item, count?)` | `void` | Usuń przedmiot z ekwipunku |
| `Player.ClearInventory()` | `void` | Wyczyść ekwipunek |
| `Player.HasItem(item)` | `bool` | Czy ma przedmiot (id) |
| `Player.HasItem(ItemStack)` | `bool` | Czy ma item stack |
| `Player.ItemCount(item)` | `int` | Ilość przedmiotu w ekwipunku |
| `Player.GetItemInSlot(slot)` | `ItemStack` | Item w slocie (0-40) |
| `Player.SetItemInSlot(slot, item)` | `void` | Ustaw item w slocie |
| `Player.GetSelectedSlot()` | `int` | Wybrany slot hotbara (0-8) |
| `Player.SetSelectedSlot(int)` | `void` | Wybierz slot hotbara |
| `Player.GetInventory()` | `Inventory` | Referencja do Inventory API |
| `Player.GetEnderChest()` | `Inventory` | Ender chest gracza |
| `Player.OpenInventory(inv)` | `void` | Otwórz interfejs inventory |
| `Player.CloseScreen()` | `void` | Zamknij otwarty ekran |
| `Player.IsScreenOpen` | `bool` | Czy otwarty jakiś ekran |
| `Player.DropItemStack()` | `void` | Upuść cały stack |
| `Player.DropSelectedItem()` | `void` | Upuść wybrany item |

### Doświadczenie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.Experience` | `int` | Całkowity XP |
| `Player.Level` | `int` | Poziom doświadczenia |
| `Player.ExperienceBar` | `float` | Pasek XP (0.0-1.0) |
| `Player.SetExperience(int)` | `void` | Ustaw całkowity XP |
| `Player.SetLevel(int)` | `void` | Ustaw poziom |
| `Player.GiveExperience(int)` | `void` | Dodaj XP |
| `Player.GiveExperienceLevels(int)` | `void` | Dodaj poziomy |
| `Player.GetXpNeededForNextLevel()` | `int` | XP potrzebny do next level |
| `Player.GetXpProgress()` | `float` | Postęp do next levelu (0.0-1.0) |
| `Player.GetTotalExperience()` | `int` | Całkowity XP w liczbach |

### Efekty statusu
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.AddEffect(effect, duration, amplifier)` | `void` | Dodaj efekt |
| `Player.AddEffect(effect, duration, amplifier, particles?, icon?)` | `void` | Dodaj efekt z opcjami |
| `Player.RemoveEffect(effect)` | `void` | Usuń efekt |
| `Player.ClearEffects()` | `void` | Wyczyść wszystkie efekty |
| `Player.HasEffect(effect)` | `bool` | Czy ma efekt |
| `Player.GetEffect(effect)` | `Effect` | Pobierz efekt |
| `Player.GetEffects()` | `List<Effect>` | Lista wszystkich efektów |
| `Player.IsAffectedByEffects` | `bool` | Czy pod wpływem jakiegoś efektu |

### Ekran i wyświetlanie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.ShowTitle(title)` | `void` | Pokaż tytuł (duży tekst) |
| `Player.ShowTitle(title, subtitle, fadeIn, stay, fadeOut)` | `void` | Tytuł z opcjami |
| `Player.ShowSubtitle(subtitle)` | `void` | Podtytuł |
| `Player.ShowActionBar(text)` | `void` | Tekst nad paskiem HP |
| `Player.SendMessage(text)` | `void` | Prywatna wiadomość na czacie |
| `Player.SendMessage(text, position)` | `void` | Wiadomość w pozycji: chat, action_bar, system |
| `Player.SendHotbarMessage(text)` | `void` | Szybka wiadomość w hotbarze |
| `Player.ResetTitle()` | `void` | Reset tytułu |
| `Player.ClearTitle()` | `void` | Wyczyść tytuł |
| `Player.SetTitleTimes(fadeIn, stay, fadeOut)` | `void` | Ustaw czasy tytułu |
| `Player.SetSubtitle(subtitle)` | `void` | Ustaw podtytuł (przed show) |
| `Player.ShowBossBar(bar)` | `void` | Pokaż bossbara |
| `Player.HideBossBar()` | `void` | Ukryj bossbara |

### Dźwięki
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.PlaySound(sound)` | `void` | Odtwórz dźwięk |
| `Player.PlaySound(sound, volume, pitch)` | `void` | Dźwięk z głośnością |
| `Player.PlaySound(sound, volume, pitch, x, y, z)` | `void` | Dźwięk w pozycji |
| `Player.StopSound(sound)` | `void` | Zatrzymaj dźwięk |
| `Player.StopAllSounds()` | `void` | Zatrzymaj wszystkie dźwięki |

### Kamera i widok
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.SetCameraEntity(entity)` | `void` | Ustaw kamerę na encję |
| `Player.SetCameraEntity(player)` | `void` | Ustaw kamerę na gracza |
| `Player.ResetCamera()` | `void` | Przywróć normalną kamerę |
| `Player.SetRenderDistance(int)` | `void` | Dystans renderowania |
| `Player.SetFovMultiplier(float)` | `void` | Mnożnik FOV |

### Statystyki i osiągnięcia
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.GetStatistic(type, key)` | `int` | Pobierz statystykę |
| `Player.SetStatistic(type, key, value)` | `void` | Ustaw statystykę |
| `Player.ResetStatistic(type, key)` | `void` | Reset statystyki |
| `Player.GetAdvancementProgress(adv)` | `string` | Postęp achievementu |
| `Player.GrantAdvancement(adv)` | `void` | Odblokuj achievement |
| `Player.RevokeAdvancement(adv)` | `void` | Cofnij achievement |
| `Player.HasAdvancement(adv)` | `bool` | Czy ma achievement |

### Interakcja z otoczeniem
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.OpenChest(x, y, z)` | `Inventory` | Otwórz skrzynię |
| `Player.OpenWorkbench()` | `void` | Otwórz crafting table |
| `Player.OpenFurnace(x, y, z)` | `void` | Otwórz piec |
| `Player.OpenEnchantingTable(x, y, z)` | `void` | Otwórz enchant Table |
| `Player.OpenAnvil(x, y, z)` | `void` | Otwórz kowadło |
| `Player.OpenGrindstone(x, y, z)` | `void` | Otwórz grindstone |
| `Player.OpenCartographyTable(x, y, z)` | `void` | Otwórz cartography |
| `Player.OpenLoom(x, y, z)` | `void` | Otwórz krosno |
| `Player.OpenStonecutter(x, y, z)` | `void` | Otwórz stonecutter |
| `Player.OpenSmithingTable(x, y, z)` | `void` | Otwórz smithing table |
| `Player.OpenBrewingStand(x, y, z)` | `void` | Otwórz brewing stand |
| `Player.OpenHopper(x, y, z)` | `void` | Otwórz lej |
| `Player.OpenBarrel(x, y, z)` | `void` | Otwórz beczkę |
| `Player.OpenShulkerBox(x, y, z)` | `void` | Otwórz shulker box |
| `Player.BreakBlock(x, y, z)` | `void` | Zniszcz blok (jak klik) |
| `Player.InteractBlock(x, y, z)` | `void` | Interakcja z blokiem |
| `Player.InteractEntity(entity)` | `void` | Interakcja z encją |
| `Player.AttackEntity(entity)` | `void` | Atak na encję |
| `Player.Sleep(x, y, z)` | `bool` | Połóż się spać |
| `Player.WakeUp()` | `void` | Obudź się |
| `Player.IsSleeping` | `bool` | Czy gracz śpi |
| `Player.SleepTimer` | `int` | Timer snu (ticki) |
| `Player.Respawn()` | `void` | Respawn gracza |

### Jazda i pojazdy
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.StartRiding(entity)` | `bool` | Wsiadź na encję |
| `Player.StopRiding()` | `void` | Zsiadź |
| `Player.IsRiding` | `bool` | Czy gracz na czymś jedzie |
| `Player.Vehicle` | `Entity` | Pojazd na którym gracz jedzie |
| `Player.GetPassengers()` | `List<Entity>` | Lista pasażerów (gdy jedzie ktoś na graczu) |
| `Player.HasControllingPassenger` | `bool` | Czy ktoś steruje graczem |
| `Player.GetControllingPassenger()` | `Entity` | Kto steruje graczem |
| `Player.Dismount()` | `void` | Zsiadź z pojazdu |
| `Player.Mount(entity)` | `void` | Wsiadź na encję |
| `Player.SetYaw(float)` | `void` | Ustaw kąt poziomy |
| `Player.SetPitch(float)` | `void` | Ustaw kąt pionowy |

### Ataki i walka
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.GetAttackCooldown()` | `float` | Cooldown ataku (0.0-1.0) |
| `Player.ResetAttackCooldown()` | `void` | Reset cooldownu |
| `Player.GetLastAttackTime()` | `int` | Tick ostatniego ataku |
| `Player.IsBlocking` | `bool` | Czy gracz blokuje (tarcza) |
| `Player.IsClimbing` | `bool` | Czy gracz się wspina |
| `Player.GetLastHurtByEntity()` | `Entity` | Ostatnia encja która zraniła |
| `Player.GetLastHurtByPlayer()` | `Player` | Ostatni gracz który zranił |
| `Player.GetLastHurtEntity()` | `Entity` | Ostatnia zraniona encja |
| `Player.GetLastDamageSource()` | `string` | Ostatnie źródło obrażeń |
| `Player.GetLastDamageAmount()` | `float` | Ostatnia ilość obrażeń |
| `Player.InvulnerableTime` | `int` | Ticki niewrażliwości po ataku |
| `Player.SetInvulnerableTime(int)` | `void` | Ustaw ticki niewrażliwości |

### Informacje o graczu
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.Name` | `string` | Nick gracza |
| `Player.UUID` | `string` | UUID gracza (z myślnikami) |
| `Player.UUIDShort` | `string` | UUID bez myślników |
| `Player.DisplayName` | `string` | Wyświetlana nazwa (z kolorami) |
| `Player.SetDisplayName(string)` | `void` | Ustaw wyświetlaną nazwę |
| `Player.PlayerListName` | `string` | Nazwa na liście graczy |
| `Player.SetPlayerListName(string)` | `void` | Ustaw nazwę na liście graczy |
| `Player.GetPlayerList()` | `List<Player>` | Lista wszystkich graczy online |
| `Player.GetWorld()` | `World` | Świat w którym jest gracz |
| `Player.Dimension` | `string` | Wymiar: "overworld", "nether", "end" |
| `Player.GetSpawnPosition()` | `BlockPos` | Pozycja spawnu |
| `Player.SetSpawnPosition(x, y, z)` | `void` | Ustaw pozycję spawnu |
| `Player.SetSpawnPosition(x, y, z, force)` | `void` | Ustaw spawn (force=true nadpisuje) |
| `Player.Ping` | `int` | Ping gracza (ms) |
| `Player.Locale` | `string` | Język gracza (np. "pl_PL") |
| `Player.SkinUrl` | `string` | URL skina gracza |
| `Player.CapeUrl` | `string` | URL capy (jeśli ma) |
| `Player.ModelType` | `string` | Typ modelu: "default" / "slim" |
| `Player.MainArm` | `string` | Główna ręka: "right" / "left" |
| `Player.SetMainArm(string)` | `void` | Ustaw główną rękę |
| `Player.ClientBrand` | `string` | Klient gracza (np. "vanilla", "fabric") |
| `Player.ServerBrand` | `string` | Marka serwera |
| `Player.ChunkX` | `int` | Chunki X gracza |
| `Player.ChunkZ` | `int` | Chunki Z gracza |
| `Player.ChunkY` | `int` | Chunki Y gracza |
| `Player.GetScore()` | `int` | Wynik gracza (score) |
| `Player.SetScore(int)` | `void` | Ustaw wynik |

### NBT
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.GetNBT()` | `string` | Pobierz NBT gracza jako string |
| `Player.SetNBT(string)` | `void` | Ustaw całe NBT gracza |
| `Player.MergeNBT(string)` | `void` | Scal NBT (dodaj/zmień pola) |
| `Player.GetPersistentData()` | `NBTCompound` | Persistent data (mod data) |
| `Player.SetPersistentData(key, value)` | `void` | Zapisz persistent data |
| `Player.GetPersistentData(key)` | `object` | Odczytaj persistent data |

### Scoreboard i teamy
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.GetScoreboardObjective(objective)` | `int` | Wynik w objective |
| `Player.SetScoreboardObjective(objective, score)` | `void` | Ustaw wynik w objective |
| `Player.GetTeam()` | `string` | Nazwa teamu gracza |
| `Player.SetTeam(team)` | `void` | Dodaj do teamu |
| `Player.RemoveFromTeam()` | `void` | Usuń z teamu |
| `Player.GetTeamColor()` | `string` | Kolor teamu (hex) |

### Wysyłanie pakietów
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.SendPacket(packet)` | `void` | Wyślij pakiet do gracza |
| `Player.SendBlockUpdate(x, y, z)` | `void` | Wyślij update bloku |
| `Player.SendLightUpdate(x, y, z)` | `void` | Wyślij update światła |
| `Player.SendSignText(x, y, z, lines[])` | `void` | Wyślij tekst na znaku |

### Misc
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.GetRiptideTicks()` | `int` | Ticki riptide (trójząb) |
| `Player.SetRiptideTicks(int)` | `void` | Ustaw ticki riptide |
| `Player.GetPortalCooldown()` | `int` | Cooldown portalu |
| `Player.SetPortalCooldown(int)` | `void` | Ustaw cooldown portalu |
| `Player.GetPortalWaitTime()` | `int` | Czas oczekiwania w portalu |
| `Player.IsUsingItem` | `bool` | Czy gracz używa przedmiotu |
| `Player.GetUsingItem()` | `ItemStack` | Przedmiot którego używa |
| `Player.GetActiveItem()` | `ItemStack` | Aktywny przedmiot |
| `Player.GetActiveItemUseTime()` | `int` | Czas używania przedmiotu |
| `Player.BedPosition` | `BlockPos` | Pozycja łóżka |
| `Player.HasBed` | `bool` | Czy ma ustawione łóżko |
| `Player.GetChunkCoordIntPair()` | `string` | Chunki gracza jako string |

---

## Przykłady

### Pełna kontrola gracza
```glang
#version 1.0
#name "Player Control Demo"
#key F6

// Teleportacja i ruch
Player.TeleportTo(100, 64, -200)
Player.SetWalkSpeed(0.5f)
Player.SetFlySpeed(0.3f)
Player.Fly(true)

// Zdrowie
Player.SetMaxHealth(40)
Player.SetHealth(40)
Player.AddEffect("regeneration", 200, 2)
Player.AddEffect("speed", 600, 1)

// Ekwipunek
Player.GiveItem("minecraft:diamond_sword", 1)
Player.GiveItem("minecraft:elytra", 1)
Player.SetArmor(
    "minecraft:diamond_helmet",
    "minecraft:diamond_chestplate",
    "minecraft:diamond_leggings",
    "minecraft:diamond_boots"
)

// Wyświetlanie
Player.ShowTitle("§6Witaj!", "§7Demo MLang", 10, 70, 20)
Player.SendMessage("§aSterowanie działa!")

// Sprawdzanie stanu
if (Player.IsFlying) {
    Chat.Send("Lata aktywny!")
}

// Doświadczenie
Player.SetLevel(50)
Player.GiveExperience(1000)
```
