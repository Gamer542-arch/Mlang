# GL.Dict — operacje na słownikach

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `dict.Count` | int | Ilość par |
| `dict.IsEmpty` | bool | Czy pusty |
| `dict[key]` | V | Pobierz wartość |
| `dict[key] = value` | void | Ustaw wartość |
| `dict.Add(key, value)` | void | Dodaj parę |
| `dict.Remove(key)` | bool | Usuń parę |
| `dict.Clear()` | void | Wyczyść |
| `dict.ContainsKey(key)` | bool | Czy zawiera klucz |
| `dict.ContainsValue(value)` | bool | Czy zawiera wartość |
| `dict.Keys()` | List<K> | Lista kluczy |
| `dict.Values()` | List<V> | Lista wartości |
| `dict.Get(key)` | V | Pobierz (null jeśli brak) |
| `dict.GetOrDefault(key, default)` | V | Pobierz z domyślną |
| `dict.SetDefault(key, default)` | V | Pobierz lub ustaw domyślną |
| `dict.Update(other)` | void | Scal z innym słownikiem |
| `dict.ToList()` | List<(K, V)> | Lista par |
| `dict.MapKeys(func)` | Dict | Mapuj klucze |
| `dict.MapValues(func)` | Dict | Mapuj wartości |
| `dict.Filter(predicate)` | Dict | Filtruj pary |
| `dict.Clone()` | Dict | Kopiuj |
| `dict.Merge(other)` | Dict | Połącz (nadpisuje) |
