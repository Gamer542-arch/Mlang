import asyncio
import json
import logging
from typing import Any, Callable, Optional

import websockets

from .errors import AuthError, BridgeError, ConnectionError, MethodNotFoundError

logger = logging.getLogger("mlang.bridge")


class BridgeClient:
    """WebSocket client for connecting to MLang Minecraft mod bridge."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 27678,
        token: str = "mlang-secret-key",
        auto_reconnect: bool = True,
    ):
        self.url = f"ws://{host}:{port}"
        self.token = token
        self.auto_reconnect = auto_reconnect
        self.ws: Optional[websockets.WebSocketClientProtocol] = None
        self._callbacks: dict[str, list[Callable]] = {}
        self._pending: dict[str, asyncio.Future] = {}
        self._msg_id = 0
        self._connected = False
        self._running = False

    @property
    def connected(self) -> bool:
        return self._connected

    async def connect(self):
        try:
            self.ws = await websockets.connect(self.url, ping_interval=20, ping_timeout=10)
            await self._authenticate()
            self._connected = True
            self._running = True
            asyncio.create_task(self._listen_loop())
            logger.info(f"Connected to MLang bridge at {self.url}")
        except websockets.WebSocketException as e:
            raise ConnectionError(f"Failed to connect: {e}") from e

    async def _authenticate(self):
        result = await self._call("auth", {"token": self.token})
        if not result:
            raise AuthError("Authentication failed - invalid token")

    async def _call(self, method: str, params: dict = None) -> Any:
        if params is None:
            params = {}
        self._msg_id += 1
        msg_id = str(self._msg_id)
        request = {
            "jsonrpc": "2.0",
            "id": msg_id,
            "method": method,
            "params": params,
        }
        future = asyncio.get_event_loop().create_future()
        self._pending[msg_id] = future
        try:
            await self.ws.send(json.dumps(request))
            result = await asyncio.wait_for(future, timeout=30)
            return result
        except asyncio.TimeoutError:
            self._pending.pop(msg_id, None)
            raise BridgeError("Request timed out") from None

    async def _listen_loop(self):
        while self._running and self.ws:
            try:
                message = await self.ws.recv()
                data = json.loads(message)
                await self._handle_message(data)
            except websockets.WebSocketException:
                logger.warning("WebSocket connection lost")
                self._connected = False
                if self.auto_reconnect:
                    await self._reconnect()
                break
            except Exception as e:
                logger.error(f"Error in listen loop: {e}")

    async def _handle_message(self, data: dict):
        if "id" in data and data["id"] in self._pending:
            future = self._pending.pop(data["id"])
            if "error" in data:
                future.set_exception(BridgeError(data["error"].get("message", "Unknown error")))
            else:
                future.set_result(data.get("result"))
        elif data.get("method") == "event":
            await self._handle_event(data.get("params", {}))
        elif data.get("method") == "tick":
            pass  # silently ignore ticks

    async def _handle_event(self, params: dict):
        event_type = params.get("type")
        event_data = params.get("data", {})
        if event_type in self._callbacks:
            for cb in self._callbacks[event_type]:
                if asyncio.iscoroutinefunction(cb):
                    await cb(event_data)
                else:
                    cb(event_data)

    async def _reconnect(self):
        retries = 0
        while self.auto_reconnect and not self._connected:
            try:
                await asyncio.sleep(min(2 ** retries, 30))
                await self.connect()
                logger.info("Reconnected to MLang bridge")
                return
            except Exception as e:
                logger.warning(f"Reconnect attempt {retries + 1} failed: {e}")
                retries += 1

    async def disconnect(self):
        self._running = False
        self._connected = False
        if self.ws:
            await self.ws.close()
            self.ws = None

    def on(self, event: str, callback: Callable):
        """Register event handler."""
        if event not in self._callbacks:
            self._callbacks[event] = []
        self._callbacks[event].append(callback)

    def off(self, event: str, callback: Callable = None):
        if callback:
            self._callbacks[event].remove(callback)
        else:
            self._callbacks.pop(event, None)

    # --- Player API ---
    async def player_get_health(self) -> float:
        return await self._call("player.getHealth")

    async def player_set_health(self, health: float):
        return await self._call("player.setHealth", {"health": health})

    async def player_get_max_health(self) -> float:
        return await self._call("player.getMaxHealth")

    async def player_set_max_health(self, max_health: float):
        return await self._call("player.setMaxHealth", {"maxHealth": max_health})

    async def player_get_position(self) -> dict:
        return await self._call("player.getPosition")

    async def player_teleport(self, x: float, y: float, z: float, yaw: float = None, pitch: float = None):
        params = {"x": x, "y": y, "z": z}
        if yaw is not None:
            params["yaw"] = yaw
        if pitch is not None:
            params["pitch"] = pitch
        return await self._call("player.teleport", params)

    async def player_get_velocity(self) -> dict:
        return await self._call("player.getVelocity")

    async def player_set_velocity(self, x: float, y: float, z: float):
        return await self._call("player.setVelocity", {"x": x, "y": y, "z": z})

    async def player_get_gamemode(self) -> str:
        return await self._call("player.getGameMode")

    async def player_set_gamemode(self, gamemode: str):
        return await self._call("player.setGameMode", {"gamemode": gamemode})

    async def player_get_food_level(self) -> int:
        return await self._call("player.getFoodLevel")

    async def player_set_food_level(self, level: int):
        return await self._call("player.setFoodLevel", {"level": level})

    async def player_get_saturation(self) -> float:
        return await self._call("player.getSaturation")

    async def player_set_saturation(self, saturation: float):
        return await self._call("player.setSaturation", {"saturation": saturation})

    async def player_get_experience(self) -> int:
        return await self._call("player.getExperience")

    async def player_set_experience(self, xp: int):
        return await self._call("player.setExperience", {"xp": xp})

    async def player_get_level(self) -> int:
        return await self._call("player.getLevel")

    async def player_set_level(self, level: int):
        return await self._call("player.setLevel", {"level": level})

    async def player_give_item(self, item: str, count: int = 1):
        return await self._call("player.giveItem", {"item": item, "count": count})

    async def player_get_mainhand(self) -> str:
        return await self._call("player.getMainHandItem")

    async def player_send_message(self, message: str):
        return await self._call("player.sendMessage", {"message": message})

    async def player_get_name(self) -> str:
        return await self._call("player.getName")

    async def player_get_uuid(self) -> str:
        return await self._call("player.getUUID")

    async def player_get_dimension(self) -> str:
        return await self._call("player.getDimension")

    async def player_is_alive(self) -> bool:
        return await self._call("player.isAlive")

    async def player_is_flying(self) -> bool:
        return await self._call("player.isFlying")

    async def player_is_sneaking(self) -> bool:
        return await self._call("player.isSneaking")

    async def player_is_sprinting(self) -> bool:
        return await self._call("player.isSprinting")

    # --- World API ---
    async def world_get_block(self, x: int, y: int, z: int) -> str:
        return await self._call("world.getBlock", {"x": x, "y": y, "z": z})

    async def world_set_block(self, x: int, y: int, z: int, block: str):
        return await self._call("world.setBlock", {"x": x, "y": y, "z": z, "block": block})

    async def world_break_block(self, x: int, y: int, z: int):
        return await self._call("world.breakBlock", {"x": x, "y": y, "z": z})

    async def world_get_biome(self, x: int, y: int, z: int) -> str:
        return await self._call("world.getBiome", {"x": x, "y": y, "z": z})

    async def world_get_time(self) -> int:
        return await self._call("world.getTime")

    async def world_set_time(self, time: int):
        return await self._call("world.setTime", {"time": time})

    async def world_get_weather(self) -> str:
        return await self._call("world.getWeather")

    async def world_set_weather(self, weather: str):
        return await self._call("world.setWeather", {"weather": weather})

    async def world_get_difficulty(self) -> str:
        return await self._call("world.getDifficulty")

    async def world_set_difficulty(self, difficulty: str):
        return await self._call("world.setDifficulty", {"difficulty": difficulty})

    async def world_run_command(self, command: str) -> str:
        return await self._call("world.runCommand", {"command": command})

    async def world_create_explosion(self, x: float, y: float, z: float, power: float):
        return await self._call("world.createExplosion", {"x": x, "y": y, "z": z, "power": power})

    async def world_spawn_particle(self, particle: str, x: float, y: float, z: float, count: int = 1):
        return await self._call("world.spawnParticle", {
            "particle": particle, "x": x, "y": y, "z": z, "count": count})

    # --- Chat API ---
    async def chat_send(self, message: str):
        return await self._call("chat.send", {"message": message})

    async def chat_broadcast(self, message: str):
        return await self._call("chat.broadcast", {"message": message})

    async def chat_run_command(self, command: str) -> str:
        return await self._call("chat.runCommand", {"command": command})

    # --- Entity API ---
    async def entity_get_health(self, entity_id: int) -> float:
        return await self._call("entity.getHealth", {"id": entity_id})

    async def entity_set_health(self, entity_id: int, health: float):
        return await self._call("entity.setHealth", {"id": entity_id, "health": health})

    async def entity_get_position(self, entity_id: int) -> dict:
        return await self._call("entity.getPosition", {"id": entity_id})

    async def entity_teleport(self, entity_id: int, x: float, y: float, z: float):
        return await self._call("entity.teleport", {"id": entity_id, "x": x, "y": y, "z": z})

    async def entity_set_custom_name(self, entity_id: int, name: str):
        return await self._call("entity.setCustomName", {"id": entity_id, "name": name})

    async def entity_set_glowing(self, entity_id: int, glowing: bool):
        return await self._call("entity.setGlowing", {"id": entity_id, "glowing": glowing})

    async def entity_set_invisible(self, entity_id: int, invisible: bool):
        return await self._call("entity.setInvisible", {"id": entity_id, "invisible": invisible})

    async def entity_kill(self, entity_id: int):
        return await self._call("entity.kill", {"id": entity_id})

    async def entity_add_effect(self, entity_id: int, effect: str, duration: int, amplifier: int):
        return await self._call("entity.addEffect", {
            "id": entity_id, "type": effect, "duration": duration, "amplifier": amplifier})

    async def entity_get_type(self, entity_id: int) -> str:
        return await self._call("entity.getType", {"id": entity_id})

    # --- Inventory API ---
    async def inventory_get_items(self) -> list:
        return await self._call("inventory.getItems")

    async def inventory_give(self, item: str, count: int = 1):
        return await self._call("inventory.giveItem", {"item": item, "count": count})

    async def inventory_has(self, item: str) -> bool:
        return await self._call("inventory.hasItem", {"item": item})

    async def inventory_remove(self, item: str, count: int = 1):
        return await self._call("inventory.removeItem", {"item": item, "count": count})

    async def inventory_clear(self):
        return await self._call("inventory.clear")

    # --- Sound API ---
    async def sound_play(self, sound: str, volume: float = 1.0, pitch: float = 1.0):
        return await self._call("sound.play", {"sound": sound, "volume": volume, "pitch": pitch})

    async def sound_play_at(self, sound: str, x: float, y: float, z: float,
                            volume: float = 1.0, pitch: float = 1.0):
        return await self._call("sound.playAt", {
            "sound": sound, "x": x, "y": y, "z": z, "volume": volume, "pitch": pitch})

    async def sound_stop_all(self):
        return await self._call("sound.stopAll")

    # --- Particle API ---
    async def particle_spawn(self, particle: str, x: float, y: float, z: float,
                             count: int = 1, dx: float = 0.0, dy: float = 0.0,
                             dz: float = 0.0, speed: float = 0.0):
        return await self._call("particle.spawn", {
            "particle": particle, "x": x, "y": y, "z": z,
            "count": count, "dx": dx, "dy": dy, "dz": dz, "speed": speed})

    # --- Scoreboard API ---
    async def scoreboard_set(self, player: str, objective: str, score: int):
        return await self._call("scoreboard.set", {"player": player, "objective": objective, "score": score})

    async def scoreboard_get(self, player: str, objective: str) -> int:
        return await self._call("scoreboard.get", {"player": player, "objective": objective})

    async def scoreboard_add_objective(self, name: str, criteria: str, display: str):
        return await self._call("scoreboard.addObjective", {"name": name, "criteria": criteria, "display": display})

    # --- World methods ---
    async def world_fill(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, block: str):
        return await self._call("world.fillBlocks", {
            "x1": x1, "y1": y1, "z1": z1, "x2": x2, "y2": y2, "z2": z2, "block": block})

    async def world_summon(self, entity: str, x: float, y: float, z: float) -> dict:
        return await self._call("world.summon", {"entity": entity, "x": x, "y": y, "z": z})

    async def world_strike_lightning(self, x: float, y: float, z: float):
        return await self._call("world.strikeLightning", {"x": x, "y": y, "z": z})

    async def world_get_players(self) -> list:
        return await self._call("world.getPlayers")

    async def world_get_nearby_entities(self, x: float, y: float, z: float, radius: float) -> list:
        return await self._call("world.getNearbyEntities", {"x": x, "y": y, "z": z, "radius": radius})

    # --- GUI Bridge API ---
    async def gui_show(self, widget_data: dict):
        """Send a widget to display in-game."""
        return await self._call("gui.show", {"widget": widget_data})

    async def gui_hide(self, widget_name: str):
        return await self._call("gui.hide", {"name": widget_name})

    async def gui_toggle(self, widget_name: str):
        return await self._call("gui.toggle", {"name": widget_name})

    async def gui_update(self, widget_name: str, properties: dict):
        """Update widget properties (position, size, color, etc.)."""
        return await self._call("gui.update", {"name": widget_name, "properties": properties})

    async def gui_set_theme(self, theme_name: str):
        return await self._call("gui.setTheme", {"theme": theme_name})

    async def gui_notification(self, text: str, duration: int = 60, type_: str = "info"):
        return await self._call("gui.notification", {"text": text, "duration": duration, "type": type_})

    # --- System ---
    async def ping(self) -> str:
        return await self._call("system.ping")

    async def get_mod_version(self) -> str:
        return await self._call("system.getModVersion")

    async def get_mc_version(self) -> str:
        return await self._call("system.getMcVersion")

    async def get_players_list(self) -> list:
        return await self._call("system.getPlayers")

    async def get_server_tick(self) -> int:
        return await self._call("system.getServerTick")

    # --- High-level GUI bridge ---
    async def gui_send_state(self, gui_json: str):
        """Send complete GUI state (from serialize_gui_state)."""
        import json as _json
        return await self._call("gui.show", {"widget": _json.loads(gui_json)})

    async def gui_send_theme(self, theme_json: str):
        """Load theme from JSON."""
        return await self._call("gui.loadThemeFromJson", {"json": theme_json})

    async def gui_clear_all(self):
        return await self._call("gui.clearAll")
