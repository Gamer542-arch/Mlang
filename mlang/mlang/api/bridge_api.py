"""API bridge - connects GLanguage interpreter to Minecraft via WebSocket bridge client.

This provides the Python-side API classes that the interpreter can call.
"""

from typing import Any, Optional

from ..bridge import BridgeClient


class PlayerProxy:
    """Proxy for Minecraft Player API."""

    def __init__(self, bridge: BridgeClient):
        self._bridge = bridge

    async def get_health(self) -> float:
        return await self._bridge.player_get_health()

    async def set_health(self, health: float):
        return await self._bridge.player_set_health(health)

    async def get_position(self) -> dict:
        return await self._bridge.player_get_position()

    async def teleport(self, x: float, y: float, z: float, yaw: float = None, pitch: float = None):
        return await self._bridge.player_teleport(x, y, z, yaw, pitch)

    async def send_message(self, message: str):
        return await self._bridge.player_send_message(message)

    async def get_name(self) -> str:
        return await self._bridge.player_get_name()

    async def get_gamemode(self) -> str:
        return await self._bridge.player_get_gamemode()

    async def set_gamemode(self, gamemode: str):
        return await self._bridge.player_set_gamemode(gamemode)

    async def give_item(self, item: str, count: int = 1):
        return await self._bridge.player_give_item(item, count)

    async def get_food(self) -> int:
        return await self._bridge.player_get_food_level()

    async def set_food(self, level: int):
        return await self._bridge.player_set_food_level(level)


class WorldProxy:
    """Proxy for Minecraft World API."""

    def __init__(self, bridge: BridgeClient):
        self._bridge = bridge

    async def get_block(self, x: int, y: int, z: int) -> str:
        return await self._bridge.world_get_block(x, y, z)

    async def set_block(self, x: int, y: int, z: int, block: str):
        return await self._bridge.world_set_block(x, y, z, block)

    async def break_block(self, x: int, y: int, z: int):
        return await self._bridge.world_break_block(x, y, z)

    async def get_biome(self, x: int, y: int, z: int) -> str:
        return await self._bridge.world_get_biome(x, y, z)

    async def get_time(self) -> int:
        return await self._bridge.world_get_time()

    async def set_time(self, time: int):
        return await self._bridge.world_set_time(time)

    async def get_weather(self) -> str:
        return await self._bridge.world_get_weather()

    async def set_weather(self, weather: str):
        return await self._bridge.world_set_weather(weather)

    async def run_command(self, command: str) -> str:
        return await self._bridge.world_run_command(command)

    async def create_explosion(self, x: float, y: float, z: float, power: float):
        return await self._bridge.world_create_explosion(x, y, z, power)


class ChatProxy:
    """Proxy for Minecraft Chat API."""

    def __init__(self, bridge: BridgeClient):
        self._bridge = bridge

    async def send(self, message: str):
        return await self._bridge.chat_send(message)

    async def broadcast(self, message: str):
        return await self._bridge.chat_broadcast(message)

    async def run_command(self, command: str) -> str:
        return await self._bridge.chat_run_command(command)


class SoundProxy:
    """Proxy for Minecraft Sound API."""

    def __init__(self, bridge: BridgeClient):
        self._bridge = bridge

    async def play(self, sound: str, x: float = None, y: float = None, z: float = None,
                   volume: float = 1.0, pitch: float = 1.0):
        # will be implemented via world methods
        pass


class ParticleProxy:
    """Proxy for Minecraft Particle API."""

    def __init__(self, bridge: BridgeClient):
        self._bridge = bridge

    async def spawn(self, particle: str, x: float, y: float, z: float, count: int = 1):
        return await self._bridge.world_spawn_particle(particle, x, y, z, count)


class ItemStackProxy:
    """Proxy for creating Minecraft items from Python."""

    def __init__(self, item_id: str, count: int = 1, nbt: str = None):
        self._id = item_id
        self._count = count
        self._nbt = nbt
        self._name = None
        self._lore = []
        self._enchants = {}
        self._unbreakable = False
        self._custom_model_data = None

    def set_name(self, name: str):
        self._name = name
        return self

    def add_lore(self, line: str):
        self._lore.append(line)
        return self

    def add_enchant(self, enchant: str, level: int):
        self._enchants[enchant] = level
        return self

    def set_unbreakable(self, unbreakable: bool = True):
        self._unbreakable = unbreakable
        return self

    def set_custom_model_data(self, data: int):
        self._custom_model_data = data
        return self

    def to_dict(self) -> dict:
        result = {
            "id": self._id,
            "count": self._count,
        }
        if self._name:
            result["name"] = self._name
        if self._lore:
            result["lore"] = self._lore
        if self._enchants:
            result["enchants"] = self._enchants
        if self._unbreakable:
            result["unbreakable"] = True
        if self._custom_model_data:
            result["custom_model_data"] = self._custom_model_data
        if self._nbt:
            result["nbt"] = self._nbt
        return result

    def __repr__(self):
        return f"ItemStack({self._id}, count={self._count})"
