# GL.List — list operations

| Method | Returns | Description |
|--------|--------|------|
| `list.Count` | int | Number of elements |
| `list.IsEmpty` | bool | Is empty |
| `list[index]` | T | Get element |
| `list[index] = value` | void | Set element |
| `list.Add(item)` | void | Add to end |
| `list.AddRange(items)` | void | Add collection |
| `list.Insert(index, item)` | void | Insert at position |
| `list.Remove(item)` | bool | Remove first match |
| `list.RemoveAt(index)` | void | Remove at index |
| `list.RemoveRange(index, count)` | void | Remove range |
| `list.Clear()` | void | Clear |
| `list.Contains(item)` | bool | Contains |
| `list.IndexOf(item)` | int | Index of element |
| `list.LastIndexOf(item)` | int | Last index |
| `list.Sort()` | void | Sort |
| `list.Sort(comparer)` | void | Sort with comparer |
| `list.Reverse()` | void | Reverse |
| `list.ToArray()` | T[] | To array |
| `list.GetRange(index, count)` | List<T> | Get range |
| `list.Find(predicate)` | T | Find element |
| `list.FindAll(predicate)` | List<T> | Find all |
| `list.Exists(predicate)` | bool | Exists |
| `list.TrueForAll(predicate)` | bool | All satisfy |
| `list.ForEach(action)` | void | For each |
| `list.Map(func)` | List<T> | Map (transform) |
| `list.Filter(predicate)` | List<T> | Filter |
| `list.Reduce(func, initial)` | T | Reduce |
| `list.Any(predicate)` | bool | Any |
| `list.All(predicate)` | bool | All |
| `list.First()` | T | First |
| `list.FirstOrDefault()` | T | First or null |
| `list.Last()` | T | Last |
| `list.LastOrDefault()` | T | Last or null |
| `list.Sum()` | double | Sum |
| `list.Average()` | double | Average |
| `list.Min()` | T | Minimum |
| `list.Max()` | T | Maximum |
| `list.Enumerate()` | List<(int, T)> | With index |
| `list.Shuffle()` | void | Shuffle |
| `list.Slice(start, end)` | List<T> | Slice |
| `list.Unique()` | List<T> | Unique |
| `list.Concat(other)` | List<T> | Concatenate |
| `list.Intersect(other)` | List<T> | Intersection |
| `list.Except(other)` | List<T> | Difference |
| `list.Union(other)` | List<T> | Union |
