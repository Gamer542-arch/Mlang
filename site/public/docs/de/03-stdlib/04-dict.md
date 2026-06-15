# GL.Dict — Dictionary-Operationen

| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `dict.Count` | int | Anzahl der Paare |
| `dict.IsEmpty` | bool | Ist leer |
| `dict[key]` | V | Wert abrufen |
| `dict[key] = value` | void | Wert setzen |
| `dict.Add(key, value)` | void | Paar hinzufügen |
| `dict.Remove(key)` | bool | Paar entfernen |
| `dict.Clear()` | void | Leeren |
| `dict.ContainsKey(key)` | bool | Enthält Schlüssel |
| `dict.ContainsValue(value)` | bool | Enthält Wert |
| `dict.Keys()` | List<K> | Schlüsselliste |
| `dict.Values()` | List<V> | Werteliste |
| `dict.Get(key)` | V | Abrufen (null falls nicht vorhanden) |
| `dict.GetOrDefault(key, default)` | V | Abrufen mit Standardwert |
| `dict.SetDefault(key, default)` | V | Abrufen oder Standard setzen |
| `dict.Update(other)` | void | Mit anderem Dictionary zusammenführen |
| `dict.ToList()` | List<(K, V)> | Paarliste |
| `dict.MapKeys(func)` | Dict | Schlüssel abbilden |
| `dict.MapValues(func)` | Dict | Werte abbilden |
| `dict.Filter(predicate)` | Dict | Paare filtern |
| `dict.Clone()` | Dict | Kopieren |
| `dict.Merge(other)` | Dict | Zusammenführen (überschreibt) |
