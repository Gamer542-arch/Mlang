# GL.Dict — dictionary operations

| Method | Returns | Description |
|--------|--------|------|
| `dict.Count` | int | Number of pairs |
| `dict.IsEmpty` | bool | Is empty |
| `dict[key]` | V | Get value |
| `dict[key] = value` | void | Set value |
| `dict.Add(key, value)` | void | Add pair |
| `dict.Remove(key)` | bool | Remove pair |
| `dict.Clear()` | void | Clear |
| `dict.ContainsKey(key)` | bool | Contains key |
| `dict.ContainsValue(value)` | bool | Contains value |
| `dict.Keys()` | List<K> | List of keys |
| `dict.Values()` | List<V> | List of values |
| `dict.Get(key)` | V | Get (null if missing) |
| `dict.GetOrDefault(key, default)` | V | Get with default |
| `dict.SetDefault(key, default)` | V | Get or set default |
| `dict.Update(other)` | void | Merge with another dict |
| `dict.ToList()` | List<(K, V)> | List of pairs |
| `dict.MapKeys(func)` | Dict | Map keys |
| `dict.MapValues(func)` | Dict | Map values |
| `dict.Filter(predicate)` | Dict | Filter pairs |
| `dict.Clone()` | Dict | Clone |
| `dict.Merge(other)` | Dict | Merge (overwrites) |
