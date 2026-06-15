# GL.Vector — 2D/3D-Vektoren

## Erstellung
```glang
var v = new Vector3(1.0, 2.0, 3.0)
var v2 = new Vector2(1.0, 2.0)
var zero = Vector3.Zero
var up = Vector3.Up
var down = Vector3.Down
var left = Vector3.Left
var right = Vector3.Right
var forward = Vector3.Forward
var back = Vector3.Back
```

## Vector3-Methoden
| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `v.X, v.Y, v.Z` | `double` | Komponenten |
| `v.Length()` | `double` | Vektorlänge |
| `v.LengthSqr()` | `double` | Länge² |
| `v.Normalize()` | `Vector3` | Normalisieren (gibt neuen zurück) |
| `v.Normalized` | `Vector3` | Normalisierter Vektor |
| `v.Add(other)` | `Vector3` | Addieren |
| `v.Sub(other)` | `Vector3` | Subtrahieren |
| `v.Mul(scalar)` | `Vector3` | Mit Skalar multiplizieren |
| `v.Div(scalar)` | `Vector3` | Durch Skalar dividieren |
| `v.Dot(other)` | `double` | Skalarprodukt |
| `v.Cross(other)` | `Vector3` | Kreuzprodukt |
| `v.DistanceTo(other)` | `double` | Distanz zum Vektor |
| `v.DistanceToSqr(other)` | `double` | Distanz² |
| `v.AngleTo(other)` | `double` | Winkel zwischen Vektoren (rad) |
| `v.AngleDegTo(other)` | `double` | Winkel zwischen Vektoren (deg) |
| `v.Lerp(other, t)` | `Vector3` | Lineare Interpolation |
| `v.ClampMagnitude(max)` | `Vector3` | Länge begrenzen |
| `v.Reflect(normal)` | `Vector3` | Reflexion |
| `v.Project(onNormal)` | `Vector3` | Projektion |
| `v.RotateX(angle)` | `Vector3` | Rotation um X |
| `v.RotateY(angle)` | `Vector3` | Rotation um Y |
| `v.RotateZ(angle)` | `Vector3` | Rotation um Z |
| `v.ToVector2()` | `Vector2` | Konvertierung zu Vector2 (X,Y) |
| `v.Flatten()` | `Vector3` | Y auf null setzen |
| `v.ToString()` | `string` | "(X, Y, Z)" |
| `v.Clone()` | `Vector3` | Kopieren |

## Operatoren
```glang
var sum = v1 + v2
var diff = v1 - v2
var scaled = v1 * 2.0
var halved = v1 / 2.0
var neg = -v1
```
