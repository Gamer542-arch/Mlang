# GL.Color — colors

## Creating colors

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

// From hex
var c = Color.FromHex("#FF0000")
var c = Color.FromHex("#E94560")

// From RGB
var c = Color.FromRGB(255, 0, 0)
var c = Color.FromRGBA(255, 0, 0, 128)

// From HSL
var c = Color.FromHSL(0.0, 1.0, 0.5)

// From Minecraft name
var c = Color.FromMinecraft("red")
```

## Methods
| Method | Returns | Description |
|--------|--------|------|
| `c.R` | `int` | Red (0-255) |
| `c.G` | `int` | Green (0-255) |
| `c.B` | `int` | Blue (0-255) |
| `c.A` | `int` | Alpha (0-255) |
| `c.ToHex()` | `string` | "#FF0000" |
| `c.ToRGBA()` | `string` | "rgba(255, 0, 0, 1.0)" |
| `c.ToHSL()` | `(double, double, double)` | Hue, Saturation, Lightness |
| `c.ToMinecraft()` | `string` | Minecraft color code (§c) |
| `c.WithAlpha(alpha)` | `Color` | New color with alpha (0.0-1.0) |
| `c.Lighten(amount)` | `Color` | Lighten (0.0-1.0) |
| `c.Darken(amount)` | `Color` | Darken (0.0-1.0) |
| `c.IsDark()` | `bool` | Is dark color |
| `c.IsLight()` | `bool` | Is light color |
| `c.Contrast()` | `Color` | Contrasting color |
| `c.ToString()` | `string` | Hex string |

## Static Color methods

| Method | Returns | Description |
|--------|--------|------|
| `Color.Mix(a, b, t)` | `Color` | Mix colors (t=0.0 → a, t=1.0 → b) |
| `Color.Lerp(a, b, t)` | `Color` | Color interpolation |
| `Color.Random()` | `Color` | Random color |
| `Color.RandomPastel()` | `Color` | Random pastel |
| `Color.Blend(colors[])` | `Color` | Blend multiple colors |
| `Color.Gradient(from, to, steps)` | `Color[]` | Gradient |
| `Color.Rainbow(progress)` | `Color` | Rainbow color (0.0-1.0) |
| `Color.Heatmap(value, min, max)` | `Color` | Heat map (blue→red) |
