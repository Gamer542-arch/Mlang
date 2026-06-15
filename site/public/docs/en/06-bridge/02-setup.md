# Mod Setup

## Installing the MLang Fabric Mod

1. Download `mlang-mod-1.0.0.jar` from the build directory
2. Place it in your Minecraft `mods/` folder
3. Start Minecraft with Fabric Loader 0.16.0+

## Configuration

The mod creates a config file at `config/mlang.json`:

```json
{
  "port": 27678,
  "authToken": "mlang-secret-key"
}
```

| Setting | Default | Description |
|---------|---------|-------------|
| `port` | `27678` | WebSocket server port |
| `authToken` | `mlang-secret-key` | Authentication token |

## Security

- WebSocket only listens on `localhost` (127.0.0.1)
- Requires token authentication
- Change the default token in production!
