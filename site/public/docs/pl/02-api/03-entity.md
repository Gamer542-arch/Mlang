# Entity API — pełna dokumentacja

## Spis method

### Podstawowe właściwości
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.Id` | `int` | ID encji |
| `Entity.UUID` | `string` | UUID encji |
| `Entity.Type` | `string` | Typ encji (np. "minecraft:zombie") |
| `Entity.Name` | `string` | Nazwa encji |
| `Entity.DisplayName` | `string` | Wyświetlana nazwa (wspiera kolory) |
| `Entity.SetDisplayName(string)` | `void` | Ustaw wyświetlaną nazwę |
| `Entity.CustomName` | `string` | Custom name (jeśli ustawiony) |
| `Entity.SetCustomName(string)` | `void` | Ustaw custom name |
| `Entity.IsCustomNameVisible` | `bool` | Czy custom name widoczny |
| `Entity.SetCustomNameVisible(bool)` | `void` | Pokaż/ukryj custom name |
| `Entity.AlwaysRenderNameTag` | `bool` | Czy zawsze renderować name tag |
| `Entity.SetAlwaysRenderNameTag(bool)` | `void` | Ustaw zawsze renderowanie tagu |
| `Entity.Tags` | `List<string>` | Tagi encji (scoreboard) |
| `Entity.AddTag(string)` | `void` | Dodaj tag |
| `Entity.RemoveTag(string)` | `void` | Usuń tag |
| `Entity.HasTag(string)` | `bool` | Czy ma tag |
| `Entity.Score` | `int` | Wynik encji |
| `Entity.SetScore(int)` | `void` | Ustaw wynik |

### Pozycja i ruch
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.X` | `double` | Pozycja X |
| `Entity.Y` | `double` | Pozycja Y |
| `Entity.Z` | `double` | Pozycja Z |
| `Entity.Yaw` | `float` | Kąt poziomy |
| `Entity.Pitch` | `float` | Kąt pionowy |
| `Entity.HeadYaw` | `float` | Kąt głowy |
| `Entity.BodyYaw` | `float` | Kąt ciała |
| `Entity.SetPosition(x, y, z)` | `void` | Ustaw pozycję |
| `Entity.SetRotation(yaw, pitch)` | `void` | Ustaw rotację |
| `Entity.SetHeadYaw(float)` | `void` | Ustaw kąt głowy |
| `Entity.SetBodyYaw(float)` | `void` | Ustaw kąt ciała |
| `Entity.Teleport(x, y, z)` | `void` | Teleportuj encję |
| `Entity.Teleport(x, y, z, yaw, pitch)` | `void` | Teleportuj z rotacją |
| `Entity.TeleportTo(entity)` | `void` | Teleportuj do encji |
| `Entity.TeleportTo(player)` | `void` | Teleportuj do gracza |
| `Entity.Velocity` | `Vector3` | Aktualna prędkość |
| `Entity.SetVelocity(vx, vy, vz)` | `void` | Ustaw prędkość |
| `Entity.AddVelocity(vx, vy, vz)` | `void` | Dodaj prędkość |
| `Entity.Knockback(strength, x, z)` | `void` | Odrzut |
| `Entity.Move(vx, vy, vz)` | `void` | Przesuń relatywnie |
| `Entity.MoveTo(x, y, z)` | `void` | Przesuń do pozycji |
| `Entity.PrevX` | `double` | Poprzednia pozycja X |
| `Entity.PrevY` | `double` | Poprzednia pozycja Y |
| `Entity.PrevZ` | `double` | Poprzednia pozycja Z |
| `Entity.DistanceTo(x, y, z)` | `double` | Dystans do punktu |
| `Entity.DistanceTo(entity)` | `double` | Dystans do encji |
| `Entity.DistanceToSqr(x, y, z)` | `double` | Dystans² |
| `Entity.GetBlockPos()` | `BlockPos` | Pozycja bloku |
| `Entity.GetChunkPos()` | `ChunkPos` | Pozycja chunka |
| `Entity.GetLookDirection()` | `Vector3` | Kierunek patrzenia |
| `Entity.GetLookVector()` | `Vector3` | Wektor patrzenia |
| `Entity.LookAt(x, y, z)` | `void` | Obróć w kierunku punktu |
| `Entity.LookAt(entity)` | `void` | Obróć w kierunku encji |
| `Entity.GetEyePosition()` | `Vector3` | Pozycja oczu |
| `Entity.GetEyeHeight()` | `float` | Wysokość oczu |
| `Entity.GetBoundingBox()` | `AABB` | Bounding box |

### Stan
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.IsAlive` | `bool` | Czy encja żyje |
| `Entity.IsDead` | `bool` | Czy encja martwa |
| `Entity.IsRemoved` | `bool` | Czy encja usunięta |
| `Entity.IsOnGround` | `bool` | Czy na ziemi |
| `Entity.IsInWater` | `bool` | Czy w wodzie |
| `Entity.IsInLava` | `bool` | Czy w lawie |
| `Entity.IsUnderwater` | `bool` | Czy pod wodą |
| `Entity.IsWet` | `bool` | Czy mokra |
| `Entity.IsInRain` | `bool` | Czy na deszczu |
| `Entity.IsInBubbleColumn` | `bool` | Czy w kolumnie bąbelkowej |
| `Entity.IsInsideWall` | `bool` | Czy w ścianie |
| `Entity.IsOnFire` | `bool` | Czy płonie |
| `Entity.IsInvisible` | `bool` | Czy niewidzialna |
| `Entity.IsGlowing` | `bool` | Czy świeci |
| `Entity.IsSilent` | `bool` | Czy cicha |
| `Entity.IsNoGravity` | `bool` | Czy bez grawitacji |
| `Entity.IsPushable` | `bool` | Czy można pchać |
| `Entity.IsInvulnerable` | `bool` | Czy niezniszczalna |
| `Entity.IsCollidable` | `bool` | Czy można kolidować |
| `Entity.IsAttackable` | `bool` | Czy można zaatakować |
| `Entity.IsSleeping` | `bool` | Czy śpi |
| `Entity.IsClimbing` | `bool` | Czy się wspina |
| `Entity.IsBlocking` | `bool` | Czy blokuje (tarcza) |
| `Entity.IsRiptide` | `bool` | Czy riptide (trójząb) |
| `Entity.IsSpinAttacking` | `bool` | Czy spin attack |
| `Entity.FireTicks` | `int` | Ticki w ogniu |
| `Entity.SetFireTicks(int)` | `void` | Ustaw ticki w ogniu |
| `Entity.FrozenTicks` | `int` | Ticki zamrożenia |
| `Entity.SetFrozenTicks(int)` | `void` | Ustaw zamrożenie |
| `Entity.AirSupply` | `int` | Poziom powietrza |
| `Entity.SetAirSupply(int)` | `void` | Ustaw powietrze |
| `Entity.MaxAir` | `int` | Maksymalne powietrze |
| `Entity.FallDistance` | `float` | Dystans upadku |
| `Entity.SetFallDistance(float)` | `void` | Ustaw dystans upadku |

### Invisibility i efekty wizualne
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.SetInvisible(bool)` | `void` | Ustaw niewidzialność |
| `Entity.SetGlowing(bool)` | `void` | Ustaw świecenie |
| `Entity.SetSilent(bool)` | `void` | Ustaw ciszę |
| `Entity.SetNoGravity(bool)` | `void` | Ustaw brak grawitacji |
| `Entity.SetInvulnerable(bool)` | `void` | Ustaw nieśmiertelność |
| `Entity.SetFireImmune(bool)` | `void` | Ustaw odporność na ogień |
| `Entity.SetPushable(bool)` | `void` | Ustaw pushowalność |
| `Entity.SetCollidable(bool)` | `void` | Ustaw kolidowalność |
| `Entity.SetGravity(bool)` | `void` | Włącz/wyłącz grawitację |
| `Entity.SetPortalCooldown(int)` | `void` | Ustaw cooldown portalu |
| `Entity.GetPortalCooldown()` | `int` | Cooldown portalu |
| `Entity.HasPortalCooldown` | `bool` | Czy ma cooldown portalu |

### Zdrowie i obrażenia
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.Health` | `float` | Aktualne HP |
| `Entity.MaxHealth` | `float` | Maksymalne HP |
| `Entity.SetHealth(float)` | `void` | Ustaw HP |
| `Entity.SetMaxHealth(float)` | `void` | Ustaw max HP |
| `Entity.Heal(amount)` | `void` | Ulecz |
| `Entity.Damage(amount)` | `bool` | Zadaj obrażenia |
| `Entity.Damage(amount, source)` | `bool` | Zadaj obrażenia (typ) |
| `Entity.Kill()` | `void` | Zabij |
| `Entity.Remove()` | `void` | Usuń (bez drops) |
| `Entity.Discard()` | `void` | Usuń z świata |
| `Entity.Absorption` | `float` | Absorpcja |
| `Entity.SetAbsorption(float)` | `void` | Ustaw absorpcję |
| `Entity.ArmorValue` | `int` | Wartość armor (punkty ochrony) |
| `Entity.ArmorCoverPercentage` | `float` | Procent pokrycia armor |
| `Entity.KnockbackResistance` | `float` | Odporność na odrzut |
| `Entity.GetLastDamageSource()` | `string` | Ostatnie źródło obrażeń |
| `Entity.GetLastDamageAmount()` | `float` | Ostatnia ilość obrażeń |
| `Entity.InvulnerableTime` | `int` | Ticki niewrażliwości |
| `Entity.SetInvulnerableTime(int)` | `void` | Ustaw ticki niewrażliwości |
| `Entity.Hurt(damage)` | `bool` | Zranienie |
| `Entity.Hurt(damage, source)` | `bool` | Zranienie z źródłem |

### Atrybuty
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetAttribute(name)` | `double` | Wartość atrybutu |
| `Entity.SetAttribute(name, value)` | `void` | Ustaw atrybut |
| `Entity.GetAttributeBase(name)` | `double` | Bazowa wartość atrybutu |
| `Entity.GetAttributeDefault(name)` | `double` | Domyślna wartość |
| `Entity.HasAttribute(name)` | `bool` | Czy ma atrybut |
| `Entity.GetAttributes()` | `Dict<string, double>` | Wszystkie atrybuty |
| `Entity.ResetAttribute(name)` | `void` | Reset atrybutu |

### Efekty
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.HasEffect(type)` | `bool` | Czy ma efekt |
| `Entity.GetEffect(type)` | `Effect` | Pobierz efekt |
| `Entity.GetEffects()` | `List<Effect>` | Lista efektów |
| `Entity.AddEffect(type, duration, amplifier)` | `bool` | Dodaj efekt |
| `Entity.AddEffect(type, duration, amplifier, particles, icon)` | `bool` | Dodaj efekt z opcjami |
| `Entity.AddEffect(effect)` | `bool` | Dodaj efekt (obiekt) |
| `Entity.RemoveEffect(type)` | `bool` | Usuń efekt |
| `Entity.ClearEffects()` | `void` | Wyczyść efekty |
| `Entity.IsAffectedByEffects` | `bool` | Czy pod wpływem efektów |

### Ruch AI
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.Jump()` | `void` | Wymuś skok |
| `Entity.SetJumping(bool)` | `void` | Ustaw skakanie |
| `Entity.IsJumping` | `bool` | Czy skacze |
| `Entity.SetSprinting(bool)` | `void` | Ustaw sprint |
| `Entity.IsSprinting` | `bool` | Czy sprintuje |
| `Entity.SetSneaking(bool)` | `void` | Ustaw skradanie |
| `Entity.IsSneaking` | `bool` | Czy się skrada |
| `Entity.SetSwimming(bool)` | `void` | Ustaw pływanie |
| `Entity.IsSwimming` | `bool` | Czy płynie |
| `Entity.SetGliding(bool)` | `void` | Ustaw szybownie |
| `Entity.IsGliding` | `bool` | Czy szybuje |
| `Entity.SetFallFlying(bool)` | `void` | Ustaw lot spadkowy |
| `Entity.IsFallFlying` | `bool` | Czy w locie spadkowym |
| `Entity.SetFlying(bool)` | `void` | Ustaw latanie |
| `Entity.IsFlying` | `bool` | Czy lata |
| `Entity.SetNoAi(bool)` | `void` | Wyłącz AI |
| `Entity.HasNoAi` | `bool` | Czy AI wyłączone |
| `Entity.SetAi(bool)` | `void` | Włącz/wyłącz AI |
| `Entity.IsAiDisabled` | `bool` | Czy AI wyłączone |
| `Entity.SetPersistenceRequired(bool)` | `void` | Ustaw persistence (nie despawnuje) |
| `Entity.IsPersistent` | `bool` | Czy persistent |

### Jazda i pojazdy
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.StartRiding(entity)` | `bool` | Wsiadaj na encję |
| `Entity.StopRiding()` | `void` | Zsiadaj |
| `Entity.IsRiding` | `bool` | Czy na czymś jedzie |
| `Entity.Vehicle` | `Entity` | Pojazd |
| `Entity.GetPassengers()` | `List<Entity>` | Lista pasażerów |
| `Entity.AddPassenger(entity)` | `void` | Dodaj pasażera |
| `Entity.RemovePassenger(entity)` | `void` | Usuń pasażera |
| `Entity.ClearPassengers()` | `void` | Usuń wszystkich pasażerów |
| `Entity.HasControllingPassenger` | `bool` | Czy ma kontrolującego pasażera |
| `Entity.GetControllingPassenger()` | `Entity` | Pasażer który kontroluje |
| `Entity.IsVehicle` | `bool` | Czy jest pojazdem |

### Leash (smycz)
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.IsLeashed` | `bool` | Czy na smyczy |
| `Entity.GetLeashHolder()` | `Entity` | Kto trzyma smycz |
| `Entity.SetLeashHolder(entity)` | `bool` | Przypnij smycz do encji |
| `Entity.SetLeashHolder(player)` | `bool` | Przypnij smycz do gracza |
| `Entity.Unleash()` | `void` | Odepnij smycz |
| `Entity.SetLeashed(bool)` | `void` | Ustaw smycz |
| `Entity.Leash()` | `bool` | Zaczep smycz |
| `Entity.DropLeash()` | `void` | Upuść smycz |

### Equipment
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetMainHandItem()` | `ItemStack` | Przedmiot w głównej ręce |
| `Entity.SetMainHandItem(item)` | `void` | Ustaw przedmiot w głównej ręce |
| `Entity.GetOffHandItem()` | `ItemStack` | Przedmiot w drugiej ręce |
| `Entity.SetOffHandItem(item)` | `void` | Ustaw przedmiot w drugiej ręce |
| `Entity.GetHelmet()` | `ItemStack` | Hełm |
| `Entity.SetHelmet(item)` | `void` | Ustaw hełm |
| `Entity.GetChestplate()` | `ItemStack` | Napierśnik |
| `Entity.SetChestplate(item)` | `void` | Ustaw napierśnik |
| `Entity.GetLeggings()` | `ItemStack` | Spodnie |
| `Entity.SetLeggings(item)` | `void` | Ustaw spodnie |
| `Entity.GetBoots()` | `ItemStack` | Buty |
| `Entity.SetBoots(item)` | `void` | Ustaw buty |
| `Entity.GetEquipment(slot)` | `ItemStack` | Przedmiot w slocie (0=hand, 1-4=armor, 5=off) |
| `Entity.SetEquipment(slot, item)` | `void` | Ustaw przedmiot w slocie |
| `Entity.GetAllEquipment()` | `List<ItemStack>` | Wszystkie przedmioty |
| `Entity.GetArmorContents()` | `ItemStack[]` | Zawartość armor slotów |
| `Entity.SetArmorContents(items[])` | `void` | Ustaw armor |
| `Entity.GetDropChance(slot)` | `float` | Szansa dropu slotu |
| `Entity.SetDropChance(slot, chance)` | `void` | Ustaw szansę dropu |
| `Entity.GetHandDropChances()` | `float[]` | Szanse dropu rąk |
| `Entity.GetArmorDropChances()` | `float[]` | Szanse dropu armora |
| `Entity.CanPickUpLoot` | `bool` | Czy może podnieść loot |
| `Entity.SetCanPickUpLoot(bool)` | `void` | Ustaw podnoszenie lootu |
| `Entity.ShouldDropEquipment` | `bool` | Czy dropić equipment |
| `Entity.SetShouldDropEquipment(bool)` | `void` | Ustaw drop equipmentu |
| `Entity.ShouldDropLoot` | `bool` | Czy dropić loot |
| `Entity.SetShouldDropLoot(bool)` | `void` | Ustaw drop lootu |

### NBT
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetNBT()` | `string` | Pobierz NBT jako string |
| `Entity.SetNBT(string)` | `void` | Ustaw całe NBT |
| `Entity.MergeNBT(string)` | `void` | Scal NBT |
| `Entity.HasNBT(key)` | `bool` | Czy ma klucz NBT |
| `Entity.GetNBTCompound()` | `NBTCompound` | NBT jako obiekt |
| `Entity.SetNBTTag(key, value)` | `void` | Ustaw tag NBT |
| `Entity.GetNBTTag(key)` | `object` | Pobierz tag NBT |

### Świat i wymiar
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.Dimension` | `string` | Wymiar encji |
| `Entity.SetDimension(string)` | `void` | Zmień wymiar |
| `Entity.GetWorld()` | `World` | Świat encji |
| `Entity.ChunkX` | `int` | Chunki X |
| `Entity.ChunkZ` | `int` | Chunki Z |

### Interakcja
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.Interact(entity)` | `bool` | Interakcja z encją |
| `Entity.Interact(player)` | `bool` | Interakcja z graczem |
| `Entity.InteractAt(entity, pos)` | `bool` | Interakcja w punkcie |
| `Entity.Attack()` | `void` | Atak |
| `Entity.SwingMainHand()` | `void` | Machnięcie główną ręką |
| `Entity.SwingOffHand()` | `void` | Machnięcie drugą ręką |
| `Entity.UseItem()` | `void` | Użyj przedmiotu |
| `Entity.BreakItem()` | `void` | Zniszcz trzymany przedmiot |
| `Entity.DropItem()` | `void` | Upuść przedmiot |

### Dźwięki
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.PlaySound(sound)` | `void` | Odtwórz dźwięk |
| `Entity.PlaySound(sound, volume, pitch)` | `void` | Dźwięk z parametrami |
| `Entity.GetHurtSound()` | `string` | Dźwięk obrażeń |
| `Entity.GetDeathSound()` | `string` | Dźwięk śmierci |
| `Entity.GetStepSound()` | `string` | Dźwięk kroków |
| `Entity.GetFallSound()` | `string` | Dźwięk upadku |
| `Entity.GetSwimSound()` | `string` | Dźwięk pływania |
| `Entity.GetSplashSound()` | `string` | Dźwięk plusku |

### Wiek i rozwój
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.Age` | `int` | Wiek encji (ticki) |
| `Entity.SetAge(int)` | `void` | Ustaw wiek |
| `Entity.IsBaby` | `bool` | Czy dziecko |
| `Entity.SetBaby(bool)` | `void` | Ustaw dziecko |
| `Entity.GetScale()` | `float` | Skala encji |
| `Entity.GetBreed()` | `bool` | Czy może się rozmnażać |
| `Entity.CanBreed` | `bool` | Czy może się rozmnażać |
| `Entity.SetBreed(bool)` | `void` | Ustaw możliwość rozmnażania |
| `Entity.IsInLove` | `bool` | Czy w miłosnym trybie |
| `Entity.SetInLove(bool)` | `void` | Ustaw miłosny tryb |
| `Entity.GetLoveCause()` | `string` | Kto wywołał miłosny tryb |
| `Entity.GetAgeTimer()` | `int` | Timer wieku |
| `Entity.SetAgeTimer(int)` | `void` | Ustaw timer wieku |

### Tame (oswojenie)
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.IsTamed` | `bool` | Czy oswojona |
| `Entity.SetTamed(bool)` | `void` | Ustaw oswojenie |
| `Entity.GetOwner()` | `string` | Nazwa właściciela |
| `Entity.GetOwnerUUID()` | `string` | UUID właściciela |
| `Entity.SetOwnerUUID(string)` | `void` | Ustaw właściciela (UUID) |
| `Entity.SetOwner(player)` | `void` | Ustaw gracza jako właściciela |
| `Entity.SetOwnerName(string)` | `void` | Ustaw nazwę właściciela |
| `Entity.IsSitting` | `bool` | Czy siedzi |
| `Entity.SetSitting(bool)` | `void` | Ustaw siedzenie |
| `Entity.IsTameable` | `bool` | Czy można oswoić |

### Moby — targetowanie
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetTarget()` | `Entity` | Aktualny target |
| `Entity.SetTarget(entity)` | `void` | Ustaw target |
| `Entity.ClearTarget()` | `void` | Wyczyść target |
| `Entity.GetLastHurtByMob()` | `Entity` | Ostatni mob który zranił |
| `Entity.SetLastHurtByMob(entity)` | `void` | Ustaw ostatniego który zranił |
| `Entity.GetLastHurtByPlayer()` | `Player` | Ostatni gracz który zranił |
| `Entity.GetLastHurtMob()` | `Entity` | Ostatni zraniony mob |
| `Entity.SetLastHurtMob(entity)` | `void` | Ustaw ostatniego zranionego |
| `Entity.GetAngerTime()` | `int` | Czas gniewu |
| `Entity.SetAngerTime(int)` | `void` | Ustaw czas gniewu |
| `Entity.GetAngryAt()` | `string` | UUID na kogo zły |
| `Entity.SetAngryAt(uuid)` | `void` | Ustaw na kogo zły |
| `Entity.Revenge()` | `void` | Zemsta na ostatnim atakującym |

### Navigation / Pathfinding
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.NavigateTo(x, y, z)` | `bool` | Nawiguj do punktu |
| `Entity.NavigateTo(entity)` | `bool` | Nawiguj do encji |
| `Entity.NavigateTo(player)` | `bool` | Nawiguj do gracza |
| `Entity.StopNavigation()` | `void` | Zatrzymaj nawigację |
| `Entity.HasPath` | `bool` | Czy ma ścieżkę |
| `Entity.GetPath()` | `Path` | Ścieżka |
| `Entity.SetPath(path)` | `void` | Ustaw ścieżkę |
| `Entity.GetNavigation()` | `Navigation` | Obiekt nawigacji |
| `Entity.IsNavigating` | `bool` | Czy nawiguje |
| `Entity.GetSpeed()` | `float` | Prędkość poruszania |
| `Entity.SetSpeed(float)` | `void` | Ustaw prędkość |
| `Entity.Follow(entity, speed)` | `bool` | Podążaj za encją |
| `Entity.Follow(player, speed)` | `bool` | Podążaj za graczem |
| `Entity.Wander()` | `void` | Losowe chodzenie |
| `Entity.MoveTo(x, y, z, speed)` | `bool` | Idź do punktu |

### Moby — specyficzne
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetVillagerProfession()` | `string` | Profesja villagera |
| `Entity.SetVillagerProfession(string)` | `void` | Ustaw profesję |
| `Entity.GetVillagerLevel()` | `int` | Poziom villagera |
| `Entity.SetVillagerLevel(int)` | `void` | Ustaw poziom |
| `Entity.GetVillagerXP()` | `int` | XP villagera |
| `Entity.SetVillagerXP(int)` | `void` | Ustaw XP |
| `Entity.IsVillagerSleeping` | `bool` | Czy villager śpi |
| `Entity.IsZombieVillager` | `bool` | Czy zombie villager |
| `Entity.CureZombieVillager()` | `void` | Wylecz zombie villager |
| `Entity.GetCatType()` | `int` | Typ kota (0-9) |
| `Entity.SetCatType(int)` | `void` | Ustaw typ kota |
| `Entity.GetFoxType()` | `string` | Typ lisa: "red", "snow" |
| `Entity.SetFoxType(string)` | `void` | Ustaw typ lisa |
| `Entity.GetMooshroomType()` | `string` | Typ mooshroom: "red", "brown" |
| `Entity.SetMooshroomType(string)` | `void` | Ustaw typ mooshroom |
| `Entity.GetParrotVariant()` | `int` | Wariant papugi (0-3) |
| `Entity.SetParrotVariant(int)` | `void` | Ustaw wariant |
| `Entity.GetRabbitType()` | `int` | Typ królika (0-5) |
| `Entity.SetRabbitType(int)` | `void` | Ustaw typ |
| `Entity.GetHorseColor()` | `string` | Kolor konia |
| `Entity.SetHorseColor(string)` | `void` | Ustaw kolor |
| `Entity.GetHorseMarkings()` | `string` | Znaki konia |
| `Entity.SetHorseMarkings(string)` | `void` | Ustaw znaki |
| `Entity.GetHorseArmor()` | `ItemStack` | Zbroja konia |
| `Entity.SetHorseArmor(item)` | `void` | Ustaw zbroję konia |
| `Entity.IsHorseSaddled` | `bool` | Czy koń ma siodło |
| `Entity.SetHorseSaddled(bool)` | `void` | Ustaw siodło |
| `Entity.GetLlamaStrength()` | `int` | Siła lamy (1-5) |
| `Entity.SetLlamaStrength(int)` | `void` | Ustaw siłę |
| `Entity.GetLlamaColor()` | `int` | Kolor lamy |
| `Entity.SetLlamaColor(int)` | `void` | Ustaw kolor |
| `Entity.GetSheepColor()` | `string` | Kolor owcy (dye color) |
| `Entity.SetSheepColor(string)` | `void` | Ustaw kolor |
| `Entity.IsSheepSheared` | `bool` | Czy owca ostrzyżona |
| `Entity.SetSheepSheared(bool)` | `void` | Ostrzyż |
| `Entity.GetGoatHorns()` | `int` | Liczba rogów kozy |
| `Entity.SetGoatHorns(int)` | `void` | Ustaw rogi |
| `Entity.IsScreamingGoat` | `bool` | Czy krzycząca koza |
| `Entity.SetScreamingGoat(bool)` | `void` | Ustaw krzyczącą kozę |
| `Entity.GetPandaGenes()` | `Dict` | Geny panda (main/hidden) |
| `Entity.SetPandaGene(gene, value)` | `void` | Ustaw gen panda |
| `Entity.GetBeeHivePos()` | `BlockPos` | Pozycja ula pszczoły |
| `Entity.SetBeeHivePos(x, y, z)` | `void` | Ustaw pozycję ula |
| `Entity.GetBeeHasNectar` | `bool` | Czy pszczoła ma nektar |
| `Entity.GetBeeHasStung` | `bool` | Czy pszczoła użądliła |
| `Entity.GetAxolotlVariant()` | `int` | Wariant aksolotla (0-4) |
| `Entity.SetAxolotlVariant(int)` | `void` | Ustaw wariant |
| `Entity.GetFrogVariant()` | `string` | Wariant żaby: "temperate", "warm", "cold" |
| `Entity.SetFrogVariant(string)` | `void` | Ustaw wariant |
| `Entity.GetCamelDashing` | `bool` | Czy wielbłąd sprintuje |
| `Entity.SetCamelDashing(bool)` | `void` | Ustaw sprint wielbłąda |
| `Entity.GetSnailageState()` | `string` | Stan ślimaka |
| `Entity.GetWardenAnger()` | `int` | Gniew wardena |
| `Entity.SetWardenAnger(int)` | `void` | Ustaw gniew |

### Slimes i Magma Cubes
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetSlimeSize()` | `int` | Rozmiar slime'a |
| `Entity.SetSlimeSize(int)` | `void` | Ustaw rozmiar |

### Creeper
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetCreeperFuse()` | `int` | Czas zapłonu (ticki) |
| `Entity.SetCreeperFuse(int)` | `void` | Ustaw czas zapłonu |
| `Entity.GetCreeperExplosionRadius()` | `int` | Promień eksplozji |
| `Entity.SetCreeperExplosionRadius(int)` | `void` | Ustaw promień |
| `Entity.IsCreeperCharged` | `bool` | Czy naładowany (piorun) |
| `Entity.SetCreeperCharged(bool)` | `void` | Ustaw naładowanie |
| `Entity.IgniteCreeper()` | `void` | Zapal creepera |

### Enderman
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetEndermanHeldBlock()` | `string` | Trzymany blok |
| `Entity.SetEndermanHeldBlock(block)` | `void` | Ustaw trzymany blok |
| `Entity.IsEndermanScreaming` | `bool` | Czy krzyczy |
| `Entity.SetEndermanScreaming(bool)` | `void` | Ustaw krzyk |

### Phantom
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetPhantomSize()` | `int` | Rozmiar phantoma |
| `Entity.SetPhantomSize(int)` | `void` | Ustaw rozmiar |

### Shulker
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetShulkerColor()` | `string` | Kolor shulkera |
| `Entity.SetShulkerColor(string)` | `void` | Ustaw kolor |
| `Entity.GetShulkerAttachedFace()` | `string` | Ściana do której przyklejony |
| `Entity.GetShulkerPeekAmount()` | `int` | Jak bardzo otwarty |

### Area Effect Cloud
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetAoeRadius()` | `float` | Promień chmury |
| `Entity.SetAoeRadius(float)` | `void` | Ustaw promień |
| `Entity.GetAoeColor()` | `int` | Kolor chmury (RGB) |
| `Entity.SetAoeColor(int)` | `void` | Ustaw kolor |
| `Entity.GetAoeDuration()` | `int` | Czas trwania |
| `Entity.SetAoeDuration(int)` | `void` | Ustaw czas |
| `Entity.GetAoeWaitTime()` | `int` | Czas od odtworzenia |
| `Entity.GetAoeParticle()` | `string` | Particle chmury |
| `Entity.SetAoeParticle(string)` | `void` | Ustaw particle |

### Item Frame
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetItemFrameItem()` | `ItemStack` | Przedmiot w ramce |
| `Entity.SetItemFrameItem(item)` | `void` | Ustaw przedmiot w ramce |
| `Entity.GetItemFrameRotation()` | `int` | Rotacja (0-7) |
| `Entity.SetItemFrameRotation(int)` | `void` | Ustaw rotację |
| `Entity.IsItemFrameFixed` | `bool` | Czy ramka stała |
| `Entity.SetItemFrameFixed(bool)` | `void` | Ustaw stałą ramkę |
| `Entity.IsItemFrameVisible` | `bool` | Czy ramka widoczna |
| `Entity.SetItemFrameVisible(bool)` | `void` | Ustaw widoczność |
| `Entity.IsItemFrameMap` | `bool` | Czy mapa w ramce |

### Armor Stand
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.IsArmorStandSmall` | `bool` | Czy mały armor stand |
| `Entity.SetArmorStandSmall(bool)` | `void` | Ustaw mały |
| `Entity.IsArmorStandMarker` | `bool` | Czy marker (niewidzialny, hitbox) |
| `Entity.SetArmorStandMarker(bool)` | `void` | Ustaw marker |
| `Entity.IsArmorStandShowArms` | `bool` | Czy pokazywać ręce |
| `Entity.SetArmorStandShowArms(bool)` | `void` | Ustaw ręce |
| `Entity.IsArmorStandNoBasePlate` | `bool` | Czy bez podstawki |
| `Entity.SetArmorStandNoBasePlate(bool)` | `void` | Ustaw podstawkę |
| `Entity.IsArmorStandNoGravity` | `bool` | Czy bez grawitacji |
| `Entity.SetArmorStandNoGravity(bool)` | `void` | Ustaw grawitację |
| `Entity.IsArmorStandNoClip` | `bool` | Czy noclip |
| `Entity.SetArmorStandNoClip(bool)` | `void` | Ustaw noclip |
| `Entity.SetArmorStandPose(part, x, y, z)` | `void` | Ustaw pozę (head, body, leftArm, rightArm, leftLeg, rightLeg) |
| `Entity.GetArmorStandPose(part)` | `Vector3` | Pobierz pozę |
| `Entity.SetArmorStandHeadPose(x, y, z)` | `void` | Pozycja głowy |
| `Entity.SetArmorStandBodyPose(x, y, z)` | `void` | Pozycja ciała |
| `Entity.SetArmorStandLeftArmPose(x, y, z)` | `void` | Lewa ręka |
| `Entity.SetArmorStandRightArmPose(x, y, z)` | `void` | Prawa ręka |
| `Entity.SetArmorStandLeftLegPose(x, y, z)` | `void` | Lewa noga |
| `Entity.SetArmorStandRightLegPose(x, y, z)` | `void` | Prawa noga |

### Text Display (1.19+)
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.SetTextDisplayText(text)` | `void` | Ustaw tekst wyświetlania |
| `Entity.GetTextDisplayText()` | `string` | Pobierz tekst |
| `Entity.SetTextDisplayBackgroundColor(int)` | `void` | Kolor tła (ARGB) |
| `Entity.GetTextDisplayBackgroundColor()` | `int` | Pobierz kolor tła |
| `Entity.SetTextDisplayTextOpacity(byte)` | `void` | Przezroczystość tekstu |
| `Entity.SetTextDisplayLineWidth(int)` | `void` | Szerokość linii |
| `Entity.SetTextDisplayAlignment(string)` | `void` | Wyrównanie: "center", "left", "right" |
| `Entity.SetTextDisplayBillboard(string)` | `void` | Billboard: "fixed", "vertical", "horizontal", "center" |
| `Entity.SetTextDisplayScale(float)` | `void` | Skala tekstu |
| `Entity.SetTextDisplayShadow(bool)` | `void` | Cień tekstu |
| `Entity.SetTextDisplaySeeThrough(bool)` | `void` | Widoczny przez bloki |
| `Entity.SetTextDisplayDefaultBackground(bool)` | `void` | Domyślne tło |

### Display Entity (wspólne)
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.SetDisplayTranslation(transformation)` | `void` | Ustaw transformację |
| `Entity.SetDisplayScale(x, y, z)` | `void` | Ustaw skalę |
| `Entity.SetDisplayTranslation(x, y, z)` | `void` | Ustaw translację |
| `Entity.SetDisplayLeftRotation(x, y, z)` | `void` | Lewa rotacja |
| `Entity.SetDisplayRightRotation(x, y, z)` | `void` | Prawa rotacja |
| `Entity.SetDisplayBillboard(string)` | `void` | Billboard mode |
| `Entity.SetDisplayBrightness(block, sky)` | `void` | Jasność |
| `Entity.SetDisplayViewRange(float)` | `void` | Zasięg widzenia |
| `Entity.SetDisplayShadowRadius(float)` | `void` | Promień cienia |
| `Entity.SetDisplayShadowStrength(float)` | `void` | Siła cienia |
| `Entity.SetDisplayGlowColorOverride(int)` | `void` | Kolor świecenia |
| `Entity.SetDisplayStartInterpolation(int)` | `void` | Start interpolacji |
| `Entity.SetDisplayInterpolationDuration(int)` | `void` | Czas interpolacji |
| `Entity.SetDisplayTeleportDuration(int)` | `void` | Czas teleportacji |

### Misc
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Entity.GetTicksLived()` | `int` | Ticki życia |
| `Entity.GetPose()` | `string` | Poza: "standing", "fall_flying", "sleeping", "swimming", "spin_attack", "sneaking", "long_jumping", "dying", "croaking", "using_tongue", "sitting", "sniffing", "digging" |
| `Entity.SetPose(string)` | `void` | Ustaw pozę |
| `Entity.GetRemovalReason()` | `string` | Powód usunięcia |
| `Entity.SetRemovalReason(string)` | `void` | Ustaw powód usunięcia |
| `Entity.ShouldBeSaved` | `bool` | Czy powinien być zapisany |
| `Entity.SetShouldBeSaved(bool)` | `void` | Ustaw zapisywanie |
| `Entity.GetEntityCategory()` | `string` | Kategoria: "monster", "creature", "ambient", "water_creature", "water_ambient", "misc" |
| `Entity.GetClassification()` | `string` | Klasyfikacja |
| `Entity.GetMobType()` | `string` | Typ moba |
| `Entity.GetCreatureAttribute()` | `string` | Atrybut stwora: "undead", "arthropod", "undefined", "water", "illager" |
| `Entity.GetExperienceReward()` | `int` | XP za zabicie |
| `Entity.SetExperienceReward(int)` | `void` | Ustaw XP |
| `Entity.GetEnchantmentSeed()` | `int` | Seed enchantmentu |
| `Entity.CopyDataFrom(entity)` | `void` | Kopiuj dane z encji |
| `Entity.SendMessage(message)` | `void` | Wyślij wiadomość (jeśli może odbierać) |

---

## Przykłady

### Modyfikacja mobów
```glang
// Spawn zombie z ekwipunkiem
var zombie = World.Summon("minecraft:zombie", 100, 64, -200)
zombie.SetCustomName("§6Elitarny Zombie")
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
zombie.SetDropChance(0, 0.0f)   // główna ręka nie dropi
zombie.SetDropChance(1, 0.0f)   // buty nie dropią

// Ustaw target na gracza
zombie.SetTarget(Player)
```

### Armor stand pose
```glang
var stand = World.SpawnArmorStand(100, 64, -200)
stand.SetArmorStandShowArms(true)
stand.SetArmorStandSmall(false)
stand.SetArmorStandMarker(false)
stand.SetArmorStandHeadPose(30, 0, 0)     // głowa lekko w dół
stand.SetArmorStandRightArmPose(-45, 0, 0) // ręka wyciągnięta

// Ubierz
stand.SetHelmet(ItemStack("minecraft:carved_pumpkin"))
stand.SetChestplate(ItemStack("minecraft:leather_chestplate"))
```
