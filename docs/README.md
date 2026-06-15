# MLang — Dokumentacja

Własny język programowania do sterowania Minecraftem. Skrypty w `.GLang`, interpreter w Pythonie, most WebSocket do gry.

---

## 📚 Spis treści

### 1. Język GLanguage
- [Składnia](01-language/01-syntax.md) — zmienne, funkcje, klasy, operatory
- [System typów](01-language/02-types.md) — typy prymitywne, konwersje, casting
- [Kontrola przepływu](01-language/03-control-flow.md) — if/else, switch/match, pętle
- [Klasy i dziedziczenie](01-language/04-classes.md) — OOP w GLanguage
- [Obsługa błędów](01-language/05-error-handling.md) — try/catch/finally, throw
- [Kolekcje](01-language/06-collections.md) — tablice, List, Dict, Set
- [Generyki](01-language/07-generics.md) — uproszczone generyki
- [Async/Await](01-language/08-async.md) — asynchroniczność, Schedule

### 2. Minecraft API
- [Player API](02-api/01-player.md) — gracz: pozycja, ruch, zdrowie, ekwipunek, efekty
- [World API](02-api/02-world.md) — świat: bloki, encje, czas, pogoda, cząsteczki
- [Entity API](02-api/03-entity.md) — encje: moby, zwierzęta, item frames, armor stands
- [Item API](02-api/04-item.md) — przedmioty: tworzenie, enchanty, NBT
- [Inventory API](02-api/05-inventory.md) — ekwipunek, skrzynie, shulkery
- [Chat API](02-api/06-chat.md) — czat, komendy, klikalne wiadomości
- [Sound API](02-api/07-sound.md) — dźwięki
- [Particle API](02-api/08-particle.md) — cząsteczki, efekty wizualne
- [NBT API](02-api/09-nbt.md) — tagi NBT, parsowanie, modyfikacja
- [Effect API](02-api/10-effect.md) — efekty statusu
- [Enchant API](02-api/11-enchant.md) — enchantmenty
- [Biome & Dimension API](02-api/12-biome-dimension.md) — biomy, wymiary
- [Scoreboard & BossBar API](02-api/13-scoreboard.md) — scoreboard, bossbar

### 3. Biblioteka standardowa
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
- [GL.IO](03-stdlib/11-io.md)
- [GL.Crypto](03-stdlib/12-crypto.md)

### 4. System GUI
- [Widgety](04-gui/01-widgets.md)
- [Okna i zakładki](04-gui/02-windows.md)
- [Motywy](04-gui/03-themes.md)
- [Animacje](04-gui/04-animations.md)

### 5. Poradniki
- [Instalacja](05-tutorials/01-installation.md)
- [Pierwszy skrypt](05-tutorials/02-first-script.md)
- [Praca z graczem](05-tutorials/03-working-with-player.md)
- [Budowanie świata](05-tutorials/04-building-with-world.md)
- [Tworzenie GUI](05-tutorials/05-creating-gui.md)
- [System teleportacji](05-tutorials/06-teleport-system.md)
- [AutoFarm](05-tutorials/07-autofarm.md)

### 6. Bridge (WebSocket)
- [Protokół JSON-RPC](06-bridge/01-protocol.md)
- [Konfiguracja moda](06-bridge/02-setup.md)
- [Python client](06-bridge/03-python-client.md)
- [Rozwiązywanie problemów](06-bridge/04-troubleshooting.md)

### 7. Inne
- [Debugger i REPL](07-debugger.md)
- [Mapa rozwoju](08-roadmap.md)

---

## Quick Start

```bash
# 1. Zainstaluj Python package
cd mlang
pip install -e .

# 2. Uruchom Minecraft z modem MLang Bridge
# (wrzuć .jar do mods/)

# 3. Napisz skrypt
echo 'Player.TeleportTo(0, 64, 0)' > test.GLang

# 4. Uruchom
python -m mlang test.GLang
```
