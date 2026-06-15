# MLang — Dokumentation

Eigene Programmiersprache zur Steuerung von Minecraft. Skripte in `.GLang`, Interpreter in Python, WebSocket-Brücke zum Spiel.

---

## 📚 Inhaltsverzeichnis

### 1. GLanguage
- [Syntax](01-language/01-syntax.md) — Variablen, Funktionen, Klassen, Operatoren
- [Typsystem](01-language/02-types.md) — Primitive Typen, Konvertierung, Casting
- [Kontrollfluss](01-language/03-control-flow.md) — if/else, switch/match, Schleifen
- [Klassen & Vererbung](01-language/04-classes.md) — OOP in GLanguage
- [Fehlerbehandlung](01-language/05-error-handling.md) — try/catch/finally, throw
- [Sammlungen](01-language/06-collections.md) — Arrays, List, Dict, Set

### 2. Minecraft API
- [Player API](02-api/01-player.md) — Spieler: Position, Bewegung, Gesundheit, Inventar
- [World API](02-api/02-world.md) — Welt: Blöcke, Entities, Zeit, Wetter
- [Entity API](02-api/03-entity.md) — Entities: Mobs, Tiere, Item Frames
- [Item API](02-api/04-item.md) — Items: Erstellen, Verzauberungen, NBT
- [Chat API](02-api/06-chat.md) — Chat, Befehle, klickbare Nachrichten
- [Sound & Particle](02-api/07-sound-particle.md) — Geräusche & Partikel

### 3. Standardbibliothek
- [GL.Math](03-stdlib/01-math.md) — Mathematik
- [GL.String](03-stdlib/02-string.md) — Textoperationen
- [GL.List](03-stdlib/03-list.md) — Listen
- [GL.Dict](03-stdlib/04-dict.md) — Wörterbücher
- [GL.Vector](03-stdlib/08-vector.md) — Vektoren
- [GL.Color](03-stdlib/09-color.md) — Farben

### 4. GUI-System
- [Widgets](04-gui/01-widgets.md) — Button, Toggle, Slider, alle Widgets

### 5. Tutorials
- [Installation](05-tutorials/01-installation.md)
- [Erstes Skript](05-tutorials/02-first-script.md)

### 6. Bridge (WebSocket)
- [Protokoll JSON-RPC](06-bridge/01-protocol.md)
- [Mod-Einrichtung](06-bridge/02-setup.md)
- [Python-Client](06-bridge/03-python-client.md)

---

## Quick Start

```bash
# 1. Python-Paket installieren
cd mlang
pip install -e .

# 2. Minecraft mit MLang Bridge Mod starten
# (.jar in mods/ legen)

# 3. Skript schreiben
echo 'Player.TeleportTo(0, 64, 0)' > test.GLang

# 4. Ausführen
python -m mlang test.GLang
```
