# GL.String — operacje na tekstach

## Metody stringa

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `s.Length` | int | Długość stringa |
| `s.ToUpper()` | string | Wielkie litery |
| `s.ToLower()` | string | Małe litery |
| `s.Trim()` | string | Usuń białe znaki z końców |
| `s.TrimStart()` | string | Usuń z początku |
| `s.TrimEnd()` | string | Usuń z końca |
| `s.Substring(start)` | string | Podciąg od start |
| `s.Substring(start, length)` | string | Podciąg od start o długości |
| `s.Contains(sub)` | bool | Czy zawiera podciąg |
| `s.StartsWith(sub)` | bool | Czy zaczyna się od |
| `s.EndsWith(sub)` | bool | Czy kończy się na |
| `s.IndexOf(sub)` | int | Indeks pierwszego wystąpienia |
| `s.LastIndexOf(sub)` | int | Indeks ostatniego wystąpienia |
| `s.Replace(old, new)` | string | Zamień tekst |
| `s.Split(delimiter)` | string[] | Podziel na tablicę |
| `s.Split(delimiter, count)` | string[] | Podziel na max count części |
| `s.Join(separator, items)` | string | Połącz tablicę stringiem |
| `s.PadLeft(totalWidth)` | string | Dopełnij spacjami z lewej |
| `s.PadRight(totalWidth)` | string | Dopełnij z prawej |
| `s.PadLeft(totalWidth, char)` | string | Dopełnij znakiem z lewej |
| `s.Reverse()` | string | Odwróć string |
| `s.Repeat(count)` | string | Powtórz n razy |
| `s.ToCharArray()` | char[] | Na tablicę znaków |
| `s.IsEmpty()` | bool | Czy pusty |
| `s.IsNullOrEmpty()` | bool | Czy null lub pusty |
| `s.IsNullOrWhitespace()` | bool | Czy null lub biały znak |
| `s.IsNumeric()` | bool | Czy numeryczny |
| `s.IsAlpha()` | bool | Czy tylko litery |
| `s.IsAlphaNumeric()` | bool | Czy litery i cyfry |
| `s.ToInt()` | int | Na int |
| `s.ToFloat()` | float | Na float |
| `s.ToDouble()` | double | Na double |
| `s.ToBool()` | bool | Na bool |
| `s.Format(args...)` | string | Formatowanie (jak String.Format) |

## Statyczne metody GL.String

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `String.Format(template, args...)` | string | Formatuj string |
| `String.Join(separator, items)` | string | Połącz kolekcję |
| `String.Concat(strings...)` | string | Połącz stringi |
| `String.IsNullOrEmpty(s)` | bool | Czy null lub pusty |
| `String.IsNullOrWhitespace(s)` | bool | Czy null lub whitespace |
| `String.Compare(a, b)` | int | Porównaj (0=równe) |
| `String.Equals(a, b)` | bool | Czy równe |
| `String.ToTitleCase(s)` | string | Capitalize |
| `String.Repeat(s, count)` | string | Powtórz |
| `String.Reverse(s)` | string | Odwróć |
