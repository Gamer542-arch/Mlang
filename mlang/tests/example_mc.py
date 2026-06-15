"""
MLang Bridge — przykładowy skrypt sterowania Minecraftem.

Uruchomienie:
  1. Odpal Minecraft 1.21.8 z modem mlang-mod w mods/
  2. W Pythonie:
       pip install mlang-py
       python example_mc.py
"""

import asyncio
from mlang.bridge import BridgeClient


async def main():
    bridge = BridgeClient(token="mlang-secret-key")
    await bridge.connect()
    print("Polaczono z Minecraft!")

    # Gracz
    name = await bridge.player_get_name()
    hp = await bridge.player_get_health()
    gm = await bridge.player_get_gamemode()
    print(f"Gracz: {name}, HP: {hp}, Tryb: {gm}")

    # Teleport
    await bridge.player_teleport(0, 64, 0)
    print("Teleport na 0,64,0")

    # Chat
    await bridge.chat_send("&aCzesc z MLang!")
    print("Wiadomosc wyslana!")

    # Daj item
    await bridge.player_give_item("minecraft:diamond", 64)
    print("Dostales 64 diamenty!")

    # Swiat — postaw blok
    await bridge.world_set_block(0, 65, 0, "minecraft:glowstone")
    print("Postawiono glowstone na spawnie!")

    # Ustaw czas na dzien
    await bridge.world_set_time(6000)
    print("Ustawiono dzien!")

    # Ustaw gamemode
    await bridge.player_set_gamemode("creative")
    print("Creative mode!")

    await bridge.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
