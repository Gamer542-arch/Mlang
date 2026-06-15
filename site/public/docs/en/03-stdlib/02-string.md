# GL.String — string operations

## String methods

| Method | Returns | Description |
|--------|--------|------|
| `s.Length` | int | String length |
| `s.ToUpper()` | string | Uppercase letters |
| `s.ToLower()` | string | Lowercase letters |
| `s.Trim()` | string | Remove whitespace from ends |
| `s.TrimStart()` | string | Remove from start |
| `s.TrimEnd()` | string | Remove from end |
| `s.Substring(start)` | string | Substring from start |
| `s.Substring(start, length)` | string | Substring from start with length |
| `s.Contains(sub)` | bool | Contains substring |
| `s.StartsWith(sub)` | bool | Starts with |
| `s.EndsWith(sub)` | bool | Ends with |
| `s.IndexOf(sub)` | int | Index of first occurrence |
| `s.LastIndexOf(sub)` | int | Index of last occurrence |
| `s.Replace(old, new)` | string | Replace text |
| `s.Split(delimiter)` | string[] | Split into array |
| `s.Split(delimiter, count)` | string[] | Split into max count parts |
| `s.Join(separator, items)` | string | Join array with string |
| `s.PadLeft(totalWidth)` | string | Pad spaces on the left |
| `s.PadRight(totalWidth)` | string | Pad on the right |
| `s.PadLeft(totalWidth, char)` | string | Pad char on the left |
| `s.Reverse()` | string | Reverse string |
| `s.Repeat(count)` | string | Repeat n times |
| `s.ToCharArray()` | char[] | To char array |
| `s.IsEmpty()` | bool | Is empty |
| `s.IsNullOrEmpty()` | bool | Is null or empty |
| `s.IsNullOrWhitespace()` | bool | Is null or whitespace |
| `s.IsNumeric()` | bool | Is numeric |
| `s.IsAlpha()` | bool | Is letters only |
| `s.IsAlphaNumeric()` | bool | Is letters and digits |
| `s.ToInt()` | int | To int |
| `s.ToFloat()` | float | To float |
| `s.ToDouble()` | double | To double |
| `s.ToBool()` | bool | To bool |
| `s.Format(args...)` | string | Format (like String.Format) |

## Static GL.String methods

| Method | Returns | Description |
|--------|--------|------|
| `String.Format(template, args...)` | string | Format string |
| `String.Join(separator, items)` | string | Join collection |
| `String.Concat(strings...)` | string | Concatenate strings |
| `String.IsNullOrEmpty(s)` | bool | Is null or empty |
| `String.IsNullOrWhitespace(s)` | bool | Is null or whitespace |
| `String.Compare(a, b)` | int | Compare (0=equal) |
| `String.Equals(a, b)` | bool | Is equal |
| `String.ToTitleCase(s)` | string | Capitalize |
| `String.Repeat(s, count)` | string | Repeat |
| `String.Reverse(s)` | string | Reverse |
