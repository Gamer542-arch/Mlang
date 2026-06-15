# GL.Time — czas i timery

| Funkcja | Zwraca | Opis |
|---------|--------|------|
| `Time.Now()` | `long` | Aktualny timestamp (ms) |
| `Time.NowSeconds()` | `long` | Aktualny timestamp (s) |
| `Time.Format(timestamp, format)` | `string` | Formatuj czas |
| `Time.FormatNow(format)` | `string` | Formatuj aktualny czas |
| `Time.Parse(timeString, format)` | `long` | Parsuj string na timestamp |
| `Time.Diff(start, end)` | `long` | Różnica w ms |
| `Time.DiffSeconds(start, end)` | `long` | Różnica w s |
| `Time.DiffMinutes(start, end)` | `long` | Różnica w min |
| `Time.DiffHours(start, end)` | `long` | Różnica w h |
| `Time.DiffDays(start, end)` | `long` | Różnica w dniach |
| `Time.Sleep(ms)` | `void` | Zatrzymaj na ms |
| `Time.Timer()` | `Timer` | Stwórz timer |
| `timer.Start()` | `void` | Start |
| `timer.Stop()` | `long` | Stop (zwraca ms) |
| `timer.Reset()` | `void` | Reset |
| `timer.Elapsed` | `long` | Czas od startu (ms) |

## Formaty
```glang
Time.FormatNow("YYYY-MM-DD HH:mm:ss")  // 2026-06-15 14:30:00
Time.FormatNow("DD/MM/YYYY")           // 15/06/2026
Time.FormatNow("HH:mm")                // 14:30
```
