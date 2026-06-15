# GL.List — operacje na listach

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `list.Count` | int | Ilość elementów |
| `list.IsEmpty` | bool | Czy pusta |
| `list[index]` | T | Pobierz element |
| `list[index] = value` | void | Ustaw element |
| `list.Add(item)` | void | Dodaj na koniec |
| `list.AddRange(items)` | void | Dodaj kolekcję |
| `list.Insert(index, item)` | void | Wstaw na pozycję |
| `list.Remove(item)` | bool | Usuń pierwszy pasujący |
| `list.RemoveAt(index)` | void | Usuń na indeksie |
| `list.RemoveRange(index, count)` | void | Usuń zakres |
| `list.Clear()` | void | Wyczyść |
| `list.Contains(item)` | bool | Czy zawiera |
| `list.IndexOf(item)` | int | Indeks elementu |
| `list.LastIndexOf(item)` | int | Ostatni indeks |
| `list.Sort()` | void | Sortuj |
| `list.Sort(comparer)` | void | Sortuj z komparatorem |
| `list.Reverse()` | void | Odwróć |
| `list.ToArray()` | T[] | Na tablicę |
| `list.GetRange(index, count)` | List<T> | Pobierz zakres |
| `list.Find(predicate)` | T | Znajdź element |
| `list.FindAll(predicate)` | List<T> | Znajdź wszystkie |
| `list.Exists(predicate)` | bool | Czy istnieje |
| `list.TrueForAll(predicate)` | bool | Czy wszystkie spełniają |
| `list.ForEach(action)` | void | Dla każdego |
| `list.Map(func)` | List<T> | Mapuj (transform) |
| `list.Filter(predicate)` | List<T> | Filtruj |
| `list.Reduce(func, initial)` | T | Redukuj |
| `list.Any(predicate)` | bool | Czy któryś |
| `list.All(predicate)` | bool | Czy wszystkie |
| `list.First()` | T | Pierwszy |
| `list.FirstOrDefault()` | T | Pierwszy lub null |
| `list.Last()` | T | Ostatni |
| `list.LastOrDefault()` | T | Ostatni lub null |
| `list.Sum()` | double | Suma |
| `list.Average()` | double | Średnia |
| `list.Min()` | T | Minimum |
| `list.Max()` | T | Maksimum |
| `list.Enumerate()` | List<(int, T)> | Z indeksem |
| `list.Shuffle()` | void | Wymieszaj |
| `list.Slice(start, end)` | List<T> | Wycinek |
| `list.Unique()` | List<T> | Unikalne |
| `list.Concat(other)` | List<T> | Połącz |
| `list.Intersect(other)` | List<T> | Wspólne |
| `list.Except(other)` | List<T> | Różnica |
| `list.Union(other)` | List<T> | Suma |
