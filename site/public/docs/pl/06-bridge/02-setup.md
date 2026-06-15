# Konfiguracja moda

## Instalacja moda MLang Fabric

1. Pobierz `mlang-mod-1.0.0.jar` z katalogu build
2. Umieść go w folderze `mods/` Minecrafta
3. Uruchom Minecraft z Fabric Loader 0.16.0+

## Konfiguracja

Mod tworzy plik konfiguracyjny w `config/mlang.json`:

```json
{
  "port": 27678,
  "authToken": "mlang-secret-key"
}
```

| Ustawienie | Domyślnie | Opis |
|-----------|-----------|------|
| `port` | `27678` | Port serwera WebSocket |
| `authToken` | `mlang-secret-key` | Token uwierzytelniania |

## Bezpieczeństwo

- WebSocket nasłuchuje tylko na `localhost` (127.0.0.1)
- Wymaga uwierzytelniania tokenem
- Zmień domyślny token w środowisku produkcyjnym!
