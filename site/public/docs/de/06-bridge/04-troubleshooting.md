# Fehlerbehebung

## Verbindungsprobleme

### „Verbindung fehlgeschlagen“
- Sicherstellen, dass Minecraft mit installiertem Mod läuft
- Prüfen, ob Port 27678 nicht von der Firewall blockiert wird
- Die Mod-Konfiguration `config/mlang.json` überprüfen

### „Authentifizierung fehlgeschlagen“
- Token im Python-Client muss mit `authToken` in der Mod-Konfiguration übereinstimmen
- Standard-Token: `mlang-secret-key`

### „Kein Spieler online“
- Mindestens ein Spieler muss in der Welt sein
- Die Bridge kann ohne Spieler-Entität nicht arbeiten

## Python-Probleme

### ImportError
```bash
pip install -e .  # Im Entwicklungsmodus installieren
```

### websockets nicht gefunden
```bash
pip install websockets
```

## GUI-Probleme

### Widgets werden nicht gerendert
- Überprüfen, ob das Widget-JSON gültig ist
- Prüfen, ob der Bildschirm geöffnet ist: `MinecraftClient.getInstance().setScreen(...)`
- Widget-Koordinaten müssen innerhalb der Bildschirmgrenzen liegen (0-1920, 0-1080)

### Theme wird nicht angewendet
- Theme-Namen sind case-sensitiv: `dark`, `light`, `minecraft`, `glass`, `neon`, `minimal`, `future`

## Häufige Lösungen

1. **Minecraft neustarten** — manchmal braucht der Mod einen frischen Start
2. **Logs prüfen** — nach Fehlern in `logs/latest.log` suchen
3. **Mod-Version prüfen** — sicherstellen, dass die Mod-Version mit der Python-Paket-Version übereinstimmt
4. **Verbindung testen**:
```python
import asyncio
from mlang.bridge import BridgeClient

async def test():
    b = BridgeClient()
    await b.connect()
    print(await b.ping())
    await b.disconnect()

asyncio.run(test())
```
