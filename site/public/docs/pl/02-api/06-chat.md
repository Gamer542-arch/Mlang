# Chat API

## Metody

### Wysyłanie wiadomości
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Chat.Send(text)` | `void` | Wyślij wiadomość (do nadawcy) |
| `Chat.Send(text, player)` | `void` | Wyślij do konkretnego gracza |
| `Chat.SendRaw(json)` | `void` | Wyślij surowy JSON (Component) |
| `Chat.Broadcast(text)` | `void` | Wyślij do wszystkich |
| `Chat.Whisper(player, text)` | `void` | Szept do gracza |
| `Chat.ActionBar(text)` | `void` | Wyślij w action bar |
| `Chat.ActionBar(text, player)` | `void` | Action bar do gracza |
| `Chat.Title(title, subtitle?)` | `void` | Tytuł na środku ekranu |
| `Chat.Subtitle(text)` | `void` | Podtytuł |
| `Chat.Hotbar(text)` | `void` | Wiadomość w hotbarze |

### Formatowanie
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

### Kody kolorów
| Kod | Kolor | Kod | Kolor |
|-----|-------|-----|-------|
| `§0` | Czarny | `§1` | Ciemnoniebieski |
| `§2` | Ciemnozielony | `§3` | Ciemny aqua |
| `§4` | Ciemnoczerwony | `§5` | Ciemny fiolet |
| `§6` | Złoty | `§7` | Szary |
| `§8` | Ciemnoszary | `§9` | Niebieski |
| `§a` | Zielony | `§b` | Aqua |
| `§c` | Czerwony | `§d` | Jasny fiolet |
| `§e` | Żółty | `§f` | Biały |

### Kody formatowania
| Kod | Format |
|-----|--------|
| `§l` | Pogrubienie (bold) |
| `§n` | Podkreślenie (underline) |
| `§o` | Kursywa (italic) |
| `§m` | Przekreślenie (strikethrough) |
| `§k` | Obfuskacja (magic) |
| `§r` | Reset |

### Klikalne wiadomości
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Chat.SendClickable(text, action, value)` | `void` | Klikalna wiadomość |
| `Chat.SendHoverable(text, hover)` | `void` | Z tooltipem po najechaniu |
| `Chat.SendInteractive(text, clickAction, clickValue, hover)` | `void` | Pełna interaktywna |

### Typy akcji kliknięcia
| Akcja | Opis |
|-------|------|
| `"run_command"` | Wykonaj komendę |
| `"suggest_command"` | Zaproponuj komendę w polu czatu |
| `"open_url"` | Otwórz URL (ostrożnie) |
| `"change_page"` | Zmień stronę w książce |
| `"copy_to_clipboard"` | Kopiuj do schowka |

### Typy akcji hover
| Akcja | Opis |
|-------|------|
| `"show_text"` | Pokaż tekst |
| `"show_item"` | Pokaż przedmiot (tooltip) |
| `"show_entity"` | Pokaż encję |

### Komendy
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Chat.RunCommand(command)` | `string` | Wykonaj komendę |
| `Chat.RunCommandAs(player, command)` | `string` | Wykonaj jako gracz |

### Klasa Chat.Color
| Metoda | Zwraca | Opis |
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

### Formatowanie zaawansowane
| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Chat.Format(template, args...)` | `string` | Formatuj jak String.Format |
| `Chat.StripColor(text)` | `string` | Usuń kody kolorów |
| `Chat.Translate(key, args...)` | `string` | Tłumaczenie klucza |
| `Chat.Sanitize(text)` | `string` | Oczyść tekst (HTML entities) |

### Klasa Chat.Clear
| Metoda | Opis |
|--------|------|
| `Chat.Clear()` | Wyczyść czat |
| `Chat.Clear(player)` | Wyczyść czat gracza |
| `Chat.Clear(100)` | Wyczyść ostatnie 100 linii |

---

## Przykłady

```glang
// Podstawowe
Chat.Send("§aHello World!")
Chat.Send("§6Cześć §c" + Player.Name + "§r, masz §b" + Player.Health + " HP")
Chat.Broadcast("§c§lUwaga! §rGracz " + Player.Name + " umarł!")
Chat.Whisper("Steve", "§dSekretna wiadomość")

// Formatowanie
Chat.Send(Chat.Color.GOLD + Chat.Color.BOLD + "Pogrubiony Złoty!")
Chat.Send(Chat.Color.RED + "Czerwony " + Chat.Color.RESET + "normalny")
Chat.Send("§6§lMLang §r§7v1.0 §a- §fgotowy do działania!")

// Klikalne
Chat.SendClickable("§a[KLIKNIJ MNIE]", "run_command", "/say kliknięto!")
Chat.SendClickable("§b[TELEPORT]", "run_command", "/tp " + Player.Name + " 0 64 0")
Chat.SendHoverable("§eNajedź na mnie!", "§7Tooltip z informacjami")

// Interaktywne
Chat.SendInteractive(
    "§6[Daj diamenty]",
    "run_command",
    "/give @s minecraft:diamond 64",
    "§aKliknij aby dostać diamenty!"
)

// Kopiuj do schowka
Chat.SendClickable("§7[KOPIUJ IP]", "copy_to_clipboard", "mc.mojang.com")

// Formatowanie tekstu
Chat.SendFormatted("Gracz {0} ma {1} HP i {2} poziomów", 
    Player.Name, Player.Health, Player.Level)

// Komendy
Chat.RunCommand("/gamemode creative")
Chat.RunCommand("/give @s minecraft:diamond 64")
Chat.RunCommand("/effect give @s minecraft:speed 999 5 true")
```
