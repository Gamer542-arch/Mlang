# Mod-Einrichtung

## Installation des MLang Fabric Mods

1. `mlang-mod-1.0.0.jar` aus dem Build-Verzeichnis herunterladen
2. In den Minecraft `mods/`-Ordner legen
3. Minecraft mit Fabric Loader 0.16.0+ starten

## Konfiguration

Der Mod erstellt eine Konfigurationsdatei unter `config/mlang.json`:

```json
{
  "port": 27678,
  "authToken": "mlang-secret-key"
}
```

| Einstellung | Standard | Beschreibung |
|-------------|----------|-------------|
| `port` | `27678` | WebSocket-Server-Port |
| `authToken` | `mlang-secret-key` | Authentifizierungs-Token |

## Sicherheit

- WebSocket lauscht nur auf `localhost` (127.0.0.1)
- Erfordert Token-Authentifizierung
- Standard-Token in der Produktion ändern!
