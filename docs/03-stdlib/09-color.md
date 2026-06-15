# GL.Color — kolory

## Tworzenie kolorów

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

// Z hex
var c = Color.FromHex("#FF0000")
var c = Color.FromHex("#E94560")

// Z RGB
var c = Color.FromRGB(255, 0, 0)
var c = Color.FromRGBA(255, 0, 0, 128)

// Z HSL
var c = Color.FromHSL(0.0, 1.0, 0.5)

// Z nazwy Minecraft
var c = Color.FromMinecraft("red")
```

## Metody
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `c.R` | `int` | Red (0-255) |
| `c.G` | `int` | Green (0-255) |
| `c.B` | `int` | Blue (0-255) |
| `c.A` | `int` | Alpha (0-255) |
| `c.ToHex()` | `string` | "#FF0000" |
| `c.ToRGBA()` | `string` | "rgba(255, 0, 0, 1.0)" |
| `c.ToHSL()` | `(double, double, double)` | Hue, Saturation, Lightness |
| `c.ToMinecraft()` | `string` | Kod koloru Minecraft (§c) |
| `c.WithAlpha(alpha)` | `Color` | Nowy kolor z alfa (0.0-1.0) |
| `c.Lighten(amount)` | `Color` | Rozjaśnij (0.0-1.0) |
| `c.Darken(amount)` | `Color` | Przyciemnij (0.0-1.0) |
| `c.IsDark()` | `bool` | Czy ciemny kolor |
| `c.IsLight()` | `bool` | Czy jasny kolor |
| `c.Contrast()` | `Color` | Kontrastujący kolor |
| `c.ToString()` | `string` | Hex string |

## Statyczne metody Color

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Color.Mix(a, b, t)` | `Color` | Mieszanie kolorów (t=0.0 → a, t=1.0 → b) |
| `Color.Lerp(a, b, t)` | `Color` | Interpolacja kolorów |
| `Color.Random()` | `Color` | Losowy kolor |
| `Color.RandomPastel()` | `Color` | Losowy pastelowy |
| `Color.Blend(colors[])` | `Color` | Mieszanie wielu kolorów |
| `Color.Gradient(from, to, steps)` | `Color[]` | Gradient |
| `Color.Rainbow(progress)` | `Color` | Kolor tęczy (0.0-1.0) |
| `Color.Heatmap(value, min, max)` | `Color` | Mapa ciepła (niebieski→czerwony) |
