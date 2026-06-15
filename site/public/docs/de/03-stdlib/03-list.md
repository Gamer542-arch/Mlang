# GL.List — Listenoperationen

| Methode | Rückgabe | Beschreibung |
|---------|----------|--------------|
| `list.Count` | int | Anzahl der Elemente |
| `list.IsEmpty` | bool | Ist leer |
| `list[index]` | T | Element abrufen |
| `list[index] = value` | void | Element setzen |
| `list.Add(item)` | void | Am Ende hinzufügen |
| `list.AddRange(items)` | void | Sammlung hinzufügen |
| `list.Insert(index, item)` | void | An Position einfügen |
| `list.Remove(item)` | bool | Erstes passendes entfernen |
| `list.RemoveAt(index)` | void | Am Index entfernen |
| `list.RemoveRange(index, count)` | void | Bereich entfernen |
| `list.Clear()` | void | Leeren |
| `list.Contains(item)` | bool | Enthält |
| `list.IndexOf(item)` | int | Index des Elements |
| `list.LastIndexOf(item)` | int | Letzter Index |
| `list.Sort()` | void | Sortieren |
| `list.Sort(comparer)` | void | Sortieren mit Vergleicher |
| `list.Reverse()` | void | Umkehren |
| `list.ToArray()` | T[] | In Array |
| `list.GetRange(index, count)` | List<T> | Bereich abrufen |
| `list.Find(predicate)` | T | Element finden |
| `list.FindAll(predicate)` | List<T> | Alle finden |
| `list.Exists(predicate)` | bool | Existiert |
| `list.TrueForAll(predicate)` | bool | Alle erfüllen |
| `list.ForEach(action)` | void | Für jedes |
| `list.Map(func)` | List<T> | Abbilden (transformieren) |
| `list.Filter(predicate)` | List<T> | Filtern |
| `list.Reduce(func, initial)` | T | Reduzieren |
| `list.Any(predicate)` | bool | Irgendeines |
| `list.All(predicate)` | bool | Alle |
| `list.First()` | T | Erstes |
| `list.FirstOrDefault()` | T | Erstes oder null |
| `list.Last()` | T | Letztes |
| `list.LastOrDefault()` | T | Letztes oder null |
| `list.Sum()` | double | Summe |
| `list.Average()` | double | Durchschnitt |
| `list.Min()` | T | Minimum |
| `list.Max()` | T | Maximum |
| `list.Enumerate()` | List<(int, T)> | Mit Index |
| `list.Shuffle()` | void | Mischen |
| `list.Slice(start, end)` | List<T> | Ausschnitt |
| `list.Unique()` | List<T> | Eindeutige |
| `list.Concat(other)` | List<T> | Verketten |
| `list.Intersect(other)` | List<T> | Schnittmenge |
| `list.Except(other)` | List<T> | Differenz |
| `list.Union(other)` | List<T> | Vereinigung |
