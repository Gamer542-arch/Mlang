# GL.Vector — 2D/3D vectors

## Creation
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

## Vector3 Methods
| Method | Returns | Description |
|--------|--------|------|
| `v.X, v.Y, v.Z` | `double` | Components |
| `v.Length()` | `double` | Vector length |
| `v.LengthSqr()` | `double` | Length² |
| `v.Normalize()` | `Vector3` | Normalize (returns new) |
| `v.Normalized` | `Vector3` | Normalized vector |
| `v.Add(other)` | `Vector3` | Add |
| `v.Sub(other)` | `Vector3` | Subtract |
| `v.Mul(scalar)` | `Vector3` | Multiply by scalar |
| `v.Div(scalar)` | `Vector3` | Divide by scalar |
| `v.Dot(other)` | `double` | Dot product |
| `v.Cross(other)` | `Vector3` | Cross product |
| `v.DistanceTo(other)` | `double` | Distance to vector |
| `v.DistanceToSqr(other)` | `double` | Distance² |
| `v.AngleTo(other)` | `double` | Angle between vectors (rad) |
| `v.AngleDegTo(other)` | `double` | Angle between vectors (deg) |
| `v.Lerp(other, t)` | `Vector3` | Linear interpolation |
| `v.ClampMagnitude(max)` | `Vector3` | Clamp length |
| `v.Reflect(normal)` | `Vector3` | Reflect |
| `v.Project(onNormal)` | `Vector3` | Project |
| `v.RotateX(angle)` | `Vector3` | Rotate around X |
| `v.RotateY(angle)` | `Vector3` | Rotate around Y |
| `v.RotateZ(angle)` | `Vector3` | Rotate around Z |
| `v.ToVector2()` | `Vector2` | Convert to Vector2 (X,Y) |
| `v.Flatten()` | `Vector3` | Zero out Y |
| `v.ToString()` | `string` | "(X, Y, Z)" |
| `v.Clone()` | `Vector3` | Clone |

## Operators
```glang
var sum = v1 + v2
var diff = v1 - v2
var scaled = v1 * 2.0
var halved = v1 / 2.0
var neg = -v1
```
