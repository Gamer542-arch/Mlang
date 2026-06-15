# Troubleshooting

## Connection Issues

### "Failed to connect"
- Make sure Minecraft is running with the mod installed
- Check if port 27678 is not blocked by firewall
- Verify the mod config `config/mlang.json`

### "Authentication failed"
- Token in Python client must match `authToken` in mod config
- Default token: `mlang-secret-key`

### "No player online"
- At least one player must be in the world
- The bridge cannot operate without a player entity

## Python Issues

### ImportError
```bash
pip install -e .  # Install in development mode
```

### websockets not found
```bash
pip install websockets
```

## GUI Issues

### Widgets not rendering
- Verify the widget JSON is valid
- Check that the screen is open
- Widget coordinates must be within screen bounds (0-1920, 0-1080)

### Theme not applying
- Theme names are case-sensitive: `dark`, `light`, `minecraft`, `glass`, `neon`, `minimal`, `future`

## Common Fixes

1. **Restart Minecraft** — sometimes the mod needs a fresh start
2. **Check logs** — look for errors in `logs/latest.log`
3. **Verify mod version** — ensure mod version matches Python package version
4. **Test connection**:
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
