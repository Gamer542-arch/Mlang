# Chat-API

## Methoden

### Nachrichten senden
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Chat.Send(text)` | `void` | Nachricht senden (an Absender) |
| `Chat.Send(text, player)` | `void` | An bestimmten Spieler senden |
| `Chat.SendRaw(json)` | `void` | Rohes JSON senden (Component) |
| `Chat.Broadcast(text)` | `void` | An alle senden |
| `Chat.Whisper(player, text)` | `void` | Flüstern an Spieler |
| `Chat.ActionBar(text)` | `void` | In Aktionsleiste senden |
| `Chat.ActionBar(text, player)` | `void` | Aktionsleiste an Spieler |
| `Chat.Title(title, subtitle?)` | `void` | Titel in Bildschirmmitte |
| `Chat.Subtitle(text)` | `void` | Untertitel |
| `Chat.Hotbar(text)` | `void` | Nachricht in Hotbar |

### Formatierung
```glang
Chat.Send("§aZielony tekst")
Chat.Send("§cCzerwony §lPogrubiony")
Chat.Send("§6Złoty §nPodkreślony")
Chat.Send("§dRóżowy §oKursywa")
Chat.Send("§eŻółty §mPrzekreślony")
Chat.Send("§5Fioletowy")
Chat.Send("§bBłękitny")
Chat.Send("§2Ciemnozielony")
Chat.Send("§4Ciemnoczerwony")
Chat.Send("§3Ciemnoniebieski")
```

### Farbcodes
| Code | Farbe | Code | Farbe |
|-----|-------|-----|-------|
| `§0` | Schwarz | `§1` | Dunkelblau |
| `§2` | Dunkelgrün | `§3` | Dunkles Aqua |
| `§4` | Dunkelrot | `§5` | Dunkelviolett |
| `§6` | Gold | `§7` | Grau |
| `§8` | Dunkelgrau | `§9` | Blau |
| `§a` | Grün | `§b` | Aqua |
| `§c` | Rot | `§d` | Hellviolett |
| `§e` | Gelb | `§f` | Weiß |

### Formatierungscodes
| Code | Format |
|-----|--------|
| `§l` | Fett (bold) |
| `§n` | Unterstrichen (underline) |
| `§o` | Kursiv (italic) |
| `§m` | Durchgestrichen (strikethrough) |
| `§k` | Verschleierung (magic) |
| `§r` | Zurücksetzen |

### Klickbare Nachrichten
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Chat.SendClickable(text, action, value)` | `void` | Klickbare Nachricht |
| `Chat.SendHoverable(text, hover)` | `void` | Mit Tooltip beim Darüberfahren |
| `Chat.SendInteractive(text, clickAction, clickValue, hover)` | `void` | Vollständig interaktiv |

### Klick-Aktionstypen
| Aktion | Beschreibung |
|-------|------|
| `"run_command"` | Befehl ausführen |
| `"suggest_command"` | Befehl im Chatfeld vorschlagen |
| `"open_url"` | URL öffnen (Vorsicht) |
| `"change_page"` | Seite im Buch wechseln |
| `"copy_to_clipboard"` | In Zwischenablage kopieren |

### Hover-Aktionstypen
| Aktion | Beschreibung |
|-------|------|
| `"show_text"` | Text anzeigen |
| `"show_item"` | Gegenstand anzeigen (Tooltip) |
| `"show_entity"` | Entität anzeigen |

### Befehle
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Chat.RunCommand(command)` | `string` | Befehl ausführen |
| `Chat.RunCommandAs(player, command)` | `string` | Als Spieler ausführen |

### Klasse Chat.Color
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Chat.Color.RED` | `string` | `"§c"` |
| `Chat.Color.GREEN` | `string` | `"§a"` |
| `Chat.Color.BLUE` | `string` | `"§9"` |
| `Chat.Color.GOLD` | `string` | `"§6"` |
| `Chat.Color.YELLOW` | `string` | `"§e"` |
| `Chat.Color.PURPLE` | `string` | `"§d"` |
| `Chat.Color.AQUA` | `string` | `"§b"` |
| `Chat.Color.GRAY` | `string` | `"§7"` |
| `Chat.Color.DARK_RED` | `string` | `"§4"` |
| `Chat.Color.DARK_GREEN` | `string` | `"§2"` |
| `Chat.Color.DARK_BLUE` | `string` | `"§1"` |
| `Chat.Color.DARK_PURPLE` | `string` | `"§5"` |
| `Chat.Color.BLACK` | `string` | `"§0"` |
| `Chat.Color.WHITE` | `string` | `"§f"` |
| `Chat.Color.RESET` | `string` | `"§r"` |
| `Chat.Color.BOLD` | `string` | `"§l"` |
| `Chat.Color.UNDERLINE` | `string` | `"§n"` |
| `Chat.Color.ITALIC` | `string` | `"§o"` |
| `Chat.Color.STRIKETHROUGH` | `string` | `"§m"` |
| `Chat.Color.MAGIC` | `string` | `"§k"` |

### Erweiterte Formatierung
| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Chat.Format(template, args...)` | `string` | Formatieren wie String.Format |
| `Chat.StripColor(text)` | `string` | Farbcodes entfernen |
| `Chat.Translate(key, args...)` | `string` | Schlüssel übersetzen |
| `Chat.Sanitize(text)` | `string` | Text bereinigen (HTML entities) |

### Klasse Chat.Clear
| Methode | Beschreibung |
|--------|------|
| `Chat.Clear()` | Chat leeren |
| `Chat.Clear(player)` | Chat des Spielers leeren |
| `Chat.Clear(100)` | Letzte 100 Zeilen leeren |

---

## Beispiele

```glang
// Grundlagen
Chat.Send("§aHello World!")
Chat.Send("§6Cześć §c" + Player.Name + "§r, masz §b" + Player.Health + " HP")
Chat.Broadcast("§c§lUwaga! §rGracz " + Player.Name + " umarł!")
Chat.Whisper("Steve", "§dSekretna wiadomość")

// Formatierung
Chat.Send(Chat.Color.GOLD + Chat.Color.BOLD + "Pogrubiony Złoty!")
Chat.Send(Chat.Color.RED + "Czerwony " + Chat.Color.RESET + "normalny")
Chat.Send("§6§lMLang §r§7v1.0 §a- §fgotowy do działania!")

// Klickbar
Chat.SendClickable("§a[KLIKNIJ MNIE]", "run_command", "/say kliknięto!")
Chat.SendClickable("§b[TELEPORT]", "run_command", "/tp " + Player.Name + " 0 64 0")
Chat.SendHoverable("§eNajedź na mnie!", "§7Tooltip z informacjami")

// Interaktiv
Chat.SendInteractive(
    "§6[Daj diamenty]",
    "run_command",
    "/give @s minecraft:diamond 64",
    "§aKliknij aby dostać diamenty!"
)

// In Zwischenablage kopieren
Chat.SendClickable("§7[KOPIUJ IP]", "copy_to_clipboard", "mc.mojang.com")

// Text formatieren
Chat.SendFormatted("Gracz {0} ma {1} HP i {2} poziomów", 
    Player.Name, Player.Health, Player.Level)

// Befehle
Chat.RunCommand("/gamemode creative")
Chat.RunCommand("/give @s minecraft:diamond 64")
Chat.RunCommand("/effect give @s minecraft:speed 999 5 true")
```
