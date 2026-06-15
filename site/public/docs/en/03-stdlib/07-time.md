# GL.Time — time and timers

| Function | Returns | Description |
|---------|--------|------|
| `Time.Now()` | `long` | Current timestamp (ms) |
| `Time.NowSeconds()` | `long` | Current timestamp (s) |
| `Time.Format(timestamp, format)` | `string` | Format time |
| `Time.FormatNow(format)` | `string` | Format current time |
| `Time.Parse(timeString, format)` | `long` | Parse string to timestamp |
| `Time.Diff(start, end)` | `long` | Difference in ms |
| `Time.DiffSeconds(start, end)` | `long` | Difference in s |
| `Time.DiffMinutes(start, end)` | `long` | Difference in min |
| `Time.DiffHours(start, end)` | `long` | Difference in h |
| `Time.DiffDays(start, end)` | `long` | Difference in days |
| `Time.Sleep(ms)` | `void` | Sleep for ms |
| `Time.Timer()` | `Timer` | Create timer |
| `timer.Start()` | `void` | Start |
| `timer.Stop()` | `long` | Stop (returns ms) |
| `timer.Reset()` | `void` | Reset |
| `timer.Elapsed` | `long` | Time since start (ms) |

## Formats
```glang
Time.FormatNow("YYYY-MM-DD HH:mm:ss")  // 2026-06-15 14:30:00
Time.FormatNow("DD/MM/YYYY")           // 15/06/2026
Time.FormatNow("HH:mm")                // 14:30
```
