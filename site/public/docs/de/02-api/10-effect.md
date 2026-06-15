# Effekt-API

## Effekte hinzufügen

```glang
Player.AddEffect("speed", 200, 1)         // typ, duration (ticks), amplifier
Player.AddEffect("speed", 200, 1, true)   // particles visible
Player.AddEffect("speed", 200, 1, true, true)  // particles + icon
```

## Liste der Effekte

| ID | Effekt |
|----|-------|
| `"speed"` | Geschwindigkeit |
| `"slowness"` | Langsamkeit |
| `"haste"` | Eile |
| `"mining_fatigue"` | Abbau-Müdigkeit |
| `"strength"` | Stärke |
| `"instant_health"` | Sofortige Heilung |
| `"instant_damage"` | Sofortiger Schaden |
| `"jump_boost"` | Sprungkraft |
| `"nausea"` | Übelkeit |
| `"regeneration"` | Regeneration |
| `"resistance"` | Resistenz |
| `"fire_resistance"` | Feuerresistenz |
| `"water_breathing"` | Unterwasseratmung |
| `"invisibility"` | Unsichtbarkeit |
| `"blindness"` | Blindheit |
| `"night_vision"` | Nachtsicht |
| `"hunger"` | Hunger |
| `"weakness"` | Schwäche |
| `"poison"` | Gift |
| `"wither"` | Wither |
| `"health_boost"` | Gesundheitsboost |
| `"absorption"` | Absorption |
| `"saturation"` | Sättigung |
| `"glowing"` | Leuchten |
| `"levitation"` | Levitation |
| `"luck"` | Glück |
| `"unluck"` | Pech |
| `"slow_falling"` | Sanfter Fall |
| `"conduit_power"` | Aura-Kraft |
| `"dolphins_grace"` | Delfingunst |
| `"bad_omen"` | Böses Omen |
| `"hero_of_the_village"` | Held des Dorfes |
| `"darkness"` | Dunkelheit |

## Methoden

| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.AddEffect(type, duration, amp)` | `bool` | Effekt hinzufügen |
| `Player.RemoveEffect(type)` | `bool` | Effekt entfernen |
| `Player.ClearEffects()` | `void` | Alle löschen |
| `Player.HasEffect(type)` | `bool` | Hat Effekt |
| `Player.GetEffect(type)` | `Effect` | Effekt abrufen |
| `Player.GetEffects()` | `List<Effect>` | Liste der Effekte |
| `effect.Type` | `string` | Effekttyp |
| `effect.Duration` | `int` | Dauer (ticks) |
| `effect.Amplifier` | `int` | Verstärkung (0 = I) |
| `effect.IsAmbient` | `bool` | Ist ambient (weniger Partikel) |
| `effect.ShowParticles` | `bool` | Zeigt Partikel |
| `effect.ShowIcon` | `bool` | Zeigt Symbol |
| `effect.GetDuration()` | `int` | Dauer |
| `effect.GetAmplifier()` | `int` | Verstärkungsstufe |
