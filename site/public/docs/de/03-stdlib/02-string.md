# GL.String — Textoperationen

## String-Methoden

| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `s.Length` | int | String-Länge |
| `s.ToUpper()` | string | Großbuchstaben |
| `s.ToLower()` | string | Kleinbuchstaben |
| `s.Trim()` | string | Leerzeichen an den Enden entfernen |
| `s.TrimStart()` | string | Vom Anfang entfernen |
| `s.TrimEnd()` | string | Vom Ende entfernen |
| `s.Substring(start)` | string | Teilstring ab start |
| `s.Substring(start, length)` | string | Teilstring ab start mit Länge |
| `s.Contains(sub)` | bool | Enthält Teilstring |
| `s.StartsWith(sub)` | bool | Beginnt mit |
| `s.EndsWith(sub)` | bool | Endet mit |
| `s.IndexOf(sub)` | int | Index des ersten Vorkommens |
| `s.LastIndexOf(sub)` | int | Index des letzten Vorkommens |
| `s.Replace(old, new)` | string | Text ersetzen |
| `s.Split(delimiter)` | string[] | In Array aufteilen |
| `s.Split(delimiter, count)` | string[] | In max count Teile aufteilen |
| `s.Join(separator, items)` | string | Array mit String verbinden |
| `s.PadLeft(totalWidth)` | string | Mit Leerzeichen links auffüllen |
| `s.PadRight(totalWidth)` | string | Rechts auffüllen |
| `s.PadLeft(totalWidth, char)` | string | Mit Zeichen links auffüllen |
| `s.Reverse()` | string | String umkehren |
| `s.Repeat(count)` | string | n-mal wiederholen |
| `s.ToCharArray()` | char[] | In Zeichenarray |
| `s.IsEmpty()` | bool | Ist leer |
| `s.IsNullOrEmpty()` | bool | Ist null oder leer |
| `s.IsNullOrWhitespace()` | bool | Ist null oder Leerzeichen |
| `s.IsNumeric()` | bool | Ist numerisch |
| `s.IsAlpha()` | bool | Nur Buchstaben |
| `s.IsAlphaNumeric()` | bool | Buchstaben und Ziffern |
| `s.ToInt()` | int | Zu int |
| `s.ToFloat()` | float | Zu float |
| `s.ToDouble()` | double | Zu double |
| `s.ToBool()` | bool | Zu bool |
| `s.Format(args...)` | string | Formatierung (wie String.Format) |

## Statische GL.String-Methoden

| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `String.Format(template, args...)` | string | String formatieren |
| `String.Join(separator, items)` | string | Sammlung verbinden |
| `String.Concat(strings...)` | string | Strings verketten |
| `String.IsNullOrEmpty(s)` | bool | Ist null oder leer |
| `String.IsNullOrWhitespace(s)` | bool | Ist null oder Leerzeichen |
| `String.Compare(a, b)` | int | Vergleichen (0=gleich) |
| `String.Equals(a, b)` | bool | Sind gleich |
| `String.ToTitleCase(s)` | string | Großschreibung |
| `String.Repeat(s, count)` | string | Wiederholen |
| `String.Reverse(s)` | string | Umkehren |
