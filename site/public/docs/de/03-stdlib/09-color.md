# GL.Color — Farben

## Farben erstellen

```glang
var red = Color.Red
var green = Color.Green
var blue = Color.Blue
var white = Color.White
var black = Color.Black
var yellow = Color.Yellow
var cyan = Color.Cyan
var magenta = Color.Magenta
var orange = Color.Orange
var purple = Color.Purple
var gray = Color.Gray
var transparent = Color.Transparent

// Aus Hex
var c = Color.FromHex("#FF0000")
var c = Color.FromHex("#E94560")

// Aus RGB
var c = Color.FromRGB(255, 0, 0)
var c = Color.FromRGBA(255, 0, 0, 128)

// Aus HSL
var c = Color.FromHSL(0.0, 1.0, 0.5)

// Aus Minecraft-Name
var c = Color.FromMinecraft("red")
```

## Methoden
| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `c.R` | `int` | Rot (0-255) |
| `c.G` | `int` | Grün (0-255) |
| `c.B` | `int` | Blau (0-255) |
| `c.A` | `int` | Alpha (0-255) |
| `c.ToHex()` | `string` | "#FF0000" |
| `c.ToRGBA()` | `string` | "rgba(255, 0, 0, 1.0)" |
| `c.ToHSL()` | `(double, double, double)` | Farbton, Sättigung, Helligkeit |
| `c.ToMinecraft()` | `string` | Minecraft-Farbcode (§c) |
| `c.WithAlpha(alpha)` | `Color` | Neue Farbe mit Alpha (0.0-1.0) |
| `c.Lighten(amount)` | `Color` | Aufhellen (0.0-1.0) |
| `c.Darken(amount)` | `Color` | Abdunkeln (0.0-1.0) |
| `c.IsDark()` | `bool` | Ist dunkle Farbe |
| `c.IsLight()` | `bool` | Ist helle Farbe |
| `c.Contrast()` | `Color` | Kontrastfarbe |
| `c.ToString()` | `string` | Hex-String |

## Statische Color-Methoden

| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `Color.Mix(a, b, t)` | `Color` | Farbmischung (t=0.0 → a, t=1.0 → b) |
| `Color.Lerp(a, b, t)` | `Color` | Farbinterpolation |
| `Color.Random()` | `Color` | Zufällige Farbe |
| `Color.RandomPastel()` | `Color` | Zufällige Pastellfarbe |
| `Color.Blend(colors[])` | `Color` | Mehrere Farben mischen |
| `Color.Gradient(from, to, steps)` | `Color[]` | Farbverlauf |
| `Color.Rainbow(progress)` | `Color` | Regenbogenfarbe (0.0-1.0) |
| `Color.Heatmap(value, min, max)` | `Color` | Heatmap (blau→rot) |
