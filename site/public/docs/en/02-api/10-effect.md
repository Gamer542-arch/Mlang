# Effect API

## Adding effects

```glang
Player.AddEffect("speed", 200, 1)         // type, duration (ticks), amplifier
Player.AddEffect("speed", 200, 1, true)   // particles visible
Player.AddEffect("speed", 200, 1, true, true)  // particles + icon
```

## Effect list

| ID | Effect |
|----|--------|
| `"speed"` | Speed |
| `"slowness"` | Slowness |
| `"haste"` | Haste |
| `"mining_fatigue"` | Mining Fatigue |
| `"strength"` | Strength |
| `"instant_health"` | Instant Health |
| `"instant_damage"` | Instant Damage |
| `"jump_boost"` | Jump Boost |
| `"nausea"` | Nausea |
| `"regeneration"` | Regeneration |
| `"resistance"` | Resistance |
| `"fire_resistance"` | Fire Resistance |
| `"water_breathing"` | Water Breathing |
| `"invisibility"` | Invisibility |
| `"blindness"` | Blindness |
| `"night_vision"` | Night Vision |
| `"hunger"` | Hunger |
| `"weakness"` | Weakness |
| `"poison"` | Poison |
| `"wither"` | Wither |
| `"health_boost"` | Health Boost |
| `"absorption"` | Absorption |
| `"saturation"` | Saturation |
| `"glowing"` | Glowing |
| `"levitation"` | Levitation |
| `"luck"` | Luck |
| `"unluck"` | Bad Luck |
| `"slow_falling"` | Slow Falling |
| `"conduit_power"` | Conduit Power |
| `"dolphins_grace"` | Dolphin's Grace |
| `"bad_omen"` | Bad Omen |
| `"hero_of_the_village"` | Hero of the Village |
| `"darkness"` | Darkness |

## Methods

| Method | Returns | Description |
|--------|--------|------|
| `Player.AddEffect(type, duration, amp)` | `bool` | Add effect |
| `Player.RemoveEffect(type)` | `bool` | Remove effect |
| `Player.ClearEffects()` | `void` | Clear all |
| `Player.HasEffect(type)` | `bool` | Whether has effect |
| `Player.GetEffect(type)` | `Effect` | Get effect |
| `Player.GetEffects()` | `List<Effect>` | List of effects |
| `effect.Type` | `string` | Effect type |
| `effect.Duration` | `int` | Duration (ticks) |
| `effect.Amplifier` | `int` | Amplifier (0 = I) |
| `effect.IsAmbient` | `bool` | Whether ambient (fewer particles) |
| `effect.ShowParticles` | `bool` | Whether shows particles |
| `effect.ShowIcon` | `bool` | Whether shows icon |
| `effect.GetDuration()` | `int` | Duration |
| `effect.GetAmplifier()` | `int` | Amplifier level |
