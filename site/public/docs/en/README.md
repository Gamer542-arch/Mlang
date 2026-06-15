# MLang — Documentation

A custom programming language for controlling Minecraft. `.GLang` scripts, Python interpreter, WebSocket bridge to the game.

---

## 📚 Table of contents

### 1. GLanguage Language
- [Syntax](01-language/01-syntax.md) — variables, functions, classes, operators
- [Type system](01-language/02-types.md) — primitive types, conversions, casting
- [Control flow](01-language/03-control-flow.md) — if/else, switch/match, loops
- [Classes and inheritance](01-language/04-classes.md) — OOP in GLanguage
- [Error handling](01-language/05-error-handling.md) — try/catch/finally, throw
- [Collections](01-language/06-collections.md) — arrays, List, Dict, Set
- [Generics](01-language/07-generics.md) — simplified generics
- [Async/Await](01-language/08-async.md) — asynchrony, Schedule

### 2. Minecraft API
- [Player API](02-api/01-player.md) — player: position, movement, health, inventory, effects
- [World API](02-api/02-world.md) — world: blocks, entities, time, weather, particles
- [Entity API](02-api/03-entity.md) — entities: mobs, animals, item frames, armor stands
- [Item API](02-api/04-item.md) — items: creation, enchants, NBT
- [Inventory API](02-api/05-inventory.md) — inventory, chests, shulkers
- [Chat API](02-api/06-chat.md) — chat, commands, clickable messages
- [Sound API](02-api/07-sound.md) — sounds
- [Particle API](02-api/08-particle.md) — particles, visual effects
- [NBT API](02-api/09-nbt.md) — NBT tags, parsing, modification
- [Effect API](02-api/10-effect.md) — status effects
- [Enchant API](02-api/11-enchant.md) — enchantments
- [Biome & Dimension API](02-api/12-biome-dimension.md) — biomes, dimensions
- [Scoreboard & BossBar API](02-api/13-scoreboard.md) — scoreboard, bossbar

### 3. Standard library
- [GL.Math](03-stdlib/01-math.md)
- [GL.String](03-stdlib/02-string.md)
- [GL.List](03-stdlib/03-list.md)
- [GL.Dict](03-stdlib/04-dict.md)
- [GL.JSON](03-stdlib/05-json.md)
- [GL.Regex](03-stdlib/06-regex.md)
- [GL.Time](03-stdlib/07-time.md)
- [GL.Vector](03-stdlib/08-vector.md)
- [GL.Color](03-stdlib/09-color.md)
- [GL.Event](03-stdlib/10-event.md)

### 4. GUI System
- [Widgets](04-gui/01-widgets.md) — Button, Toggle, Slider, all widgets
- [Windows and tabs](04-gui/02-windows.md)
- [Themes](04-gui/03-themes.md)
- [Animations](04-gui/04-animations.md)

### 5. Tutorials
- [Installation](05-tutorials/01-installation.md)
- [First script](05-tutorials/02-first-script.md)
- [Working with player](05-tutorials/03-working-with-player.md)
- [Building the world](05-tutorials/04-building-with-world.md)

### 6. Bridge (WebSocket)
- [JSON-RPC Protocol](06-bridge/01-protocol.md)
- [Mod configuration](06-bridge/02-setup.md)
- [Python client](06-bridge/03-python-client.md)
- [Troubleshooting](06-bridge/04-troubleshooting.md)

### 7. Other
- [Debugger and REPL](07-debugger.md)
- [Roadmap](08-roadmap.md)

---

## Quick Start

```bash
# 1. Install Python package
cd mlang
pip install -e .

# 2. Run Minecraft with MLang Bridge mod
# (put .jar into mods/)

# 3. Write a script
echo 'Player.TeleportTo(0, 64, 0)' > test.GLang

# 4. Run
python -m mlang test.GLang
```
