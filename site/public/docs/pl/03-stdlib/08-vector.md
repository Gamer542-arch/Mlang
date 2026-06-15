# GL.Vector — wektory 2D/3D

## Tworzenie
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

## Metody Vector3
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `v.X, v.Y, v.Z` | `double` | Komponenty |
| `v.Length()` | `double` | Długość wektora |
| `v.LengthSqr()` | `double` | Długość² |
| `v.Normalize()` | `Vector3` | Normalizuj (zwraca nowy) |
| `v.Normalized` | `Vector3` | Wektor znormalizowany |
| `v.Add(other)` | `Vector3` | Dodaj |
| `v.Sub(other)` | `Vector3` | Odejmij |
| `v.Mul(scalar)` | `Vector3` | Mnożenie przez skalar |
| `v.Div(scalar)` | `Vector3` | Dzielenie przez skalar |
| `v.Dot(other)` | `double` | Iloczyn skalarny |
| `v.Cross(other)` | `Vector3` | Iloczyn wektorowy |
| `v.DistanceTo(other)` | `double` | Dystans do wektora |
| `v.DistanceToSqr(other)` | `double` | Dystans² |
| `v.AngleTo(other)` | `double` | Kąt między wektorami (rad) |
| `v.AngleDegTo(other)` | `double` | Kąt między wektorami (deg) |
| `v.Lerp(other, t)` | `Vector3` | Interpolacja liniowa |
| `v.ClampMagnitude(max)` | `Vector3` | Ogranicz długość |
| `v.Reflect(normal)` | `Vector3` | Odbicie |
| `v.Project(onNormal)` | `Vector3` | Projekcja |
| `v.RotateX(angle)` | `Vector3` | Rotacja wokół X |
| `v.RotateY(angle)` | `Vector3` | Rotacja wokół Y |
| `v.RotateZ(angle)` | `Vector3` | Rotacja wokół Z |
| `v.ToVector2()` | `Vector2` | Konwersja do Vector2 (X,Y) |
| `v.Flatten()` | `Vector3` | Wyzeruj Y |
| `v.ToString()` | `string` | "(X, Y, Z)" |
| `v.Clone()` | `Vector3` | Kopiuj |

## Operatory
```glang
var sum = v1 + v2
var diff = v1 - v2
var scaled = v1 * 2.0
var halved = v1 / 2.0
var neg = -v1
```
