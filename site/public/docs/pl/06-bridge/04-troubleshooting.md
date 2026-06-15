# Rozwiązywanie problemów

## Problemy z połączeniem

### „Nie udało się połączyć”
- Upewnij się, że Minecraft jest uruchomiony z zainstalowanym modem
- Sprawdź, czy port 27678 nie jest blokowany przez firewall
- Zweryfikuj konfigurację moda `config/mlang.json`

### „Uwierzytelnianie nie powiodło się”
- Token w kliencie Python musi odpowiadać `authToken` w konfiguracji moda
- Domyślny token: `mlang-secret-key`

### „Brak gracza online”
- Przynajmniej jeden gracz musi być w świecie
- Bridge nie może działać bez encji gracza

## Problemy z Pythonem

### ImportError
```bash
pip install -e .  # Zainstaluj w trybie deweloperskim
```

### Nie znaleziono websockets
```bash
pip install websockets
```

## Problemy z GUI

### Widgety się nie renderują
- Sprawdź, czy JSON widgeta jest poprawny
- Sprawdź, czy ekran jest otwarty: `MinecraftClient.getInstance().setScreen(...)`
- Współrzędne widgetów muszą mieścić się w granicach ekranu (0-1920, 0-1080)

### Motyw nie jest stosowany
- Nazwy motywów rozróżniają wielkość liter: `dark`, `light`, `minecraft`, `glass`, `neon`, `minimal`, `future`

## Typowe rozwiązania

1. **Zrestartuj Minecraft** — czasami mod potrzebuje świeżego startu
2. **Sprawdź logi** — szukaj błędów w `logs/latest.log`
3. **Zweryfikuj wersję moda** — upewnij się, że wersja moda pasuje do wersji pakietu Python
4. **Test połączenia**:
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
