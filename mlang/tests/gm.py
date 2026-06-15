import asyncio
import websockets
import json

async def main():
    uri = "ws://localhost:27678"
    print(f"Connecting to {uri}...")
    
    try:
        async with websockets.connect(uri, ping_interval=None) as ws:
            print("Connected!")
            
            # Auth
            msg = json.dumps({"jsonrpc": "2.0", "id": "1", "method": "auth", "params": {"token": "mlang-secret-key"}})
            print(f"Sending: {msg}")
            await ws.send(msg)
            
            resp = await asyncio.wait_for(ws.recv(), timeout=5)
            print(f"Auth response: {resp}")
            
            # Get gamemode
            msg = json.dumps({"jsonrpc": "2.0", "id": "2", "method": "player.getGameMode", "params": {}})
            await ws.send(msg)
            resp = await asyncio.wait_for(ws.recv(), timeout=5)
            print(f"Gamemode: {resp}")
            
            # Set creative
            msg = json.dumps({"jsonrpc": "2.0", "id": "3", "method": "player.setGameMode", "params": {"gamemode": "creative"}})
            await ws.send(msg)
            resp = await asyncio.wait_for(ws.recv(), timeout=5)
            print(f"Set gamemode: {resp}")
            
            print("Done!")
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(main())
