# Effect API

## Dodawanie efektów

```glang
Player.AddEffect("speed", 200, 1)         // typ, duration (ticks), amplifier
Player.AddEffect("speed", 200, 1, true)   // particles visible
Player.AddEffect("speed", 200, 1, true, true)  // particles + icon
```

## Lista efektów

| ID | Efekt |
|----|-------|
| `"speed"` | Szybkość |
| `"slowness"` | Spowolnienie |
| `"haste"` | Pośpiech |
| `"mining_fatigue"` | Zmęczenie |
| `"strength"` | Siła |
| `"instant_health"` | Natychmiastowe leczenie |
| `"instant_damage"` | Natychmiastowe obrażenia |
| `"jump_boost"` | Wzmocniony skok |
| `"nausea"` | Nudności |
| `"regeneration"` | Regeneracja |
| `"resistance"` | Odporność |
| `"fire_resistance"` | Odporność na ogień |
| `"water_breathing"` | Oddychanie pod wodą |
| `"invisibility"` | Niewidzialność |
| `"blindness"` | Ślepota |
| `"night_vision"` | Widzenie w ciemności |
| `"hunger"` | Głód |
| `"weakness"` | Słabość |
| `"poison"` | Trucizna |
| `"wither"` | Wither |
| `"health_boost"` | Wzmocnienie zdrowia |
| `"absorption"` | Absorpcja |
| `"saturation"` | Saturacja |
| `"glowing"` | Świecenie |
| `"levitation"` | Lewitacja |
| `"luck"` | Szczęście |
| `"unluck"` | Pech |
| `"slow_falling"` | Powolny upadek |
| `"conduit_power"` | Moc conduita |
| `"dolphins_grace"` | Wdzięk delfina |
| `"bad_omen"` | Zły omen |
| `"hero_of_the_village"` | Bohater wioski |
| `"darkness"` | Ciemność |

## Metody

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.AddEffect(type, duration, amp)` | `bool` | Dodaj efekt |
| `Player.RemoveEffect(type)` | `bool` | Usuń efekt |
| `Player.ClearEffects()` | `void` | Wyczyść wszystkie |
| `Player.HasEffect(type)` | `bool` | Czy ma efekt |
| `Player.GetEffect(type)` | `Effect` | Pobierz efekt |
| `Player.GetEffects()` | `List<Effect>` | Lista efektów |
| `effect.Type` | `string` | Typ efektu |
| `effect.Duration` | `int` | Czas trwania (ticks) |
| `effect.Amplifier` | `int` | Wzmocnienie (0 = I) |
| `effect.IsAmbient` | `bool` | Czy ambient (mniej particle) |
| `effect.ShowParticles` | `bool` | Czy pokazuje particles |
| `effect.ShowIcon` | `bool` | Czy pokazuje ikonę |
| `effect.GetDuration()` | `int` | Czas trwania |
| `effect.GetAmplifier()` | `int` | Poziom wzmocnienia |
