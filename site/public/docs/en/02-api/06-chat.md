# Chat API

## Methods

### Sending messages
| Method | Returns | Description |
|--------|--------|------|
| `Chat.Send(text)` | `void` | Send message (to sender) |
| `Chat.Send(text, player)` | `void` | Send to specific player |
| `Chat.SendRaw(json)` | `void` | Send raw JSON (Component) |
| `Chat.Broadcast(text)` | `void` | Send to everyone |
| `Chat.Whisper(player, text)` | `void` | Whisper to player |
| `Chat.ActionBar(text)` | `void` | Send in action bar |
| `Chat.ActionBar(text, player)` | `void` | Action bar to player |
| `Chat.Title(title, subtitle?)` | `void` | Title in center of screen |
| `Chat.Subtitle(text)` | `void` | Subtitle |
| `Chat.Hotbar(text)` | `void` | Message in hotbar |

### Formatting
```glang
Chat.Send("§aGreen text")
Chat.Send("§cRed §lBold")
Chat.Send("§6Gold §nUnderlined")
Chat.Send("§dPink §oItalic")
Chat.Send("§eYellow §mStrikethrough")
Chat.Send("§5Purple")
Chat.Send("§bAqua")
Chat.Send("§2Dark green")
Chat.Send("§4Dark red")
Chat.Send("§3Dark blue")
```

### Color codes
| Code | Color | Code | Color |
|------|-------|------|-------|
| `§0` | Black | `§1` | Dark blue |
| `§2` | Dark green | `§3` | Dark aqua |
| `§4` | Dark red | `§5` | Dark purple |
| `§6` | Gold | `§7` | Gray |
| `§8` | Dark gray | `§9` | Blue |
| `§a` | Green | `§b` | Aqua |
| `§c` | Red | `§d` | Light purple |
| `§e` | Yellow | `§f` | White |

### Formatting codes
| Code | Format |
|------|--------|
| `§l` | Bold |
| `§n` | Underline |
| `§o` | Italic |
| `§m` | Strikethrough |
| `§k` | Obfuscated (magic) |
| `§r` | Reset |

### Clickable messages
| Method | Returns | Description |
|--------|--------|------|
| `Chat.SendClickable(text, action, value)` | `void` | Clickable message |
| `Chat.SendHoverable(text, hover)` | `void` | With tooltip on hover |
| `Chat.SendInteractive(text, clickAction, clickValue, hover)` | `void` | Full interactive |

### Click action types
| Action | Description |
|--------|------|
| `"run_command"` | Execute command |
| `"suggest_command"` | Suggest command in chat input |
| `"open_url"` | Open URL (use with caution) |
| `"change_page"` | Change page in a book |
| `"copy_to_clipboard"` | Copy to clipboard |

### Hover action types
| Action | Description |
|--------|------|
| `"show_text"` | Show text |
| `"show_item"` | Show item (tooltip) |
| `"show_entity"` | Show entity |

### Commands
| Method | Returns | Description |
|--------|--------|------|
| `Chat.RunCommand(command)` | `string` | Execute command |
| `Chat.RunCommandAs(player, command)` | `string` | Execute as player |

### Chat.Color class
| Method | Returns | Description |
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

### Advanced formatting
| Method | Returns | Description |
|--------|--------|------|
| `Chat.Format(template, args...)` | `string` | Format like String.Format |
| `Chat.StripColor(text)` | `string` | Remove color codes |
| `Chat.Translate(key, args...)` | `string` | Translate key |
| `Chat.Sanitize(text)` | `string` | Sanitize text (HTML entities) |

### Chat.Clear class
| Method | Description |
|--------|------|
| `Chat.Clear()` | Clear chat |
| `Chat.Clear(player)` | Clear player's chat |
| `Chat.Clear(100)` | Clear last 100 lines |

---

## Examples

```glang
// Basic
Chat.Send("§aHello World!")
Chat.Send("§6Hello §c" + Player.Name + "§r, you have §b" + Player.Health + " HP")
Chat.Broadcast("§c§lWarning! §rPlayer " + Player.Name + " died!")
Chat.Whisper("Steve", "§dSecret message")

// Formatting
Chat.Send(Chat.Color.GOLD + Chat.Color.BOLD + "Bold Gold!")
Chat.Send(Chat.Color.RED + "Red " + Chat.Color.RESET + "normal")
Chat.Send("§6§lMLang §r§7v1.0 §a- §fready to go!")

// Clickable
Chat.SendClickable("§a[CLICK ME]", "run_command", "/say clicked!")
Chat.SendClickable("§b[TELEPORT]", "run_command", "/tp " + Player.Name + " 0 64 0")
Chat.SendHoverable("§eHover over me!", "§7Tooltip with info")

// Interactive
Chat.SendInteractive(
    "§6[Give Diamonds]",
    "run_command",
    "/give @s minecraft:diamond 64",
    "§aClick to receive diamonds!"
)

// Copy to clipboard
Chat.SendClickable("§7[COPY IP]", "copy_to_clipboard", "mc.mojang.com")

// Text formatting
Chat.SendFormatted("Player {0} has {1} HP and {2} levels", 
    Player.Name, Player.Health, Player.Level)

// Commands
Chat.RunCommand("/gamemode creative")
Chat.RunCommand("/give @s minecraft:diamond 64")
Chat.RunCommand("/effect give @s minecraft:speed 999 5 true")
```
