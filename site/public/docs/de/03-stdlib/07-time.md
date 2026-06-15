# GL.Time — Zeit und Timer

| Funktion | Rückgabe | Beschreibung |
|----------|----------|--------------|
| `Time.Now()` | `long` | Aktueller Zeitstempel (ms) |
| `Time.NowSeconds()` | `long` | Aktueller Zeitstempel (s) |
| `Time.Format(timestamp, format)` | `string` | Zeit formatieren |
| `Time.FormatNow(format)` | `string` | Aktuelle Zeit formatieren |
| `Time.Parse(timeString, format)` | `long` | String in Zeitstempel parsen |
| `Time.Diff(start, end)` | `long` | Differenz in ms |
| `Time.DiffSeconds(start, end)` | `long` | Differenz in s |
| `Time.DiffMinutes(start, end)` | `long` | Differenz in min |
| `Time.DiffHours(start, end)` | `long` | Differenz in h |
| `Time.DiffDays(start, end)` | `long` | Differenz in Tagen |
| `Time.Sleep(ms)` | `void` | Für ms anhalten |
| `Time.Timer()` | `Timer` | Timer erstellen |
| `timer.Start()` | `void` | Start |
| `timer.Stop()` | `long` | Stop (gibt ms zurück) |
| `timer.Reset()` | `void` | Zurücksetzen |
| `timer.Elapsed` | `long` | Zeit seit Start (ms) |

## Formate
```glang
Time.FormatNow("YYYY-MM-DD HH:mm:ss")  // 2026-06-15 14:30:00
Time.FormatNow("DD/MM/YYYY")           // 15/06/2026
Time.FormatNow("HH:mm")                // 14:30
```
