package org.mlang.api;

import net.minecraft.block.Blocks;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;
import net.minecraft.util.math.BlockPos;
import org.mlang.MlangMod;

import java.util.Map;

public class WorldAPI implements ApiHandler {

    private ServerWorld getWorld() {
        var server = MlangMod.SERVER;
        if (server == null) throw new IllegalStateException("Server not ready");
        return server.getOverworld();
    }

    @Override
    public Object handle(String method, Map<String, Object> params) {
        return switch (method) {
            case "world.getBlock" -> {
                int x = ((Number) params.get("x")).intValue();
                int y = ((Number) params.get("y")).intValue();
                int z = ((Number) params.get("z")).intValue();
                var state = getWorld().getBlockState(new BlockPos(x, y, z));
                yield state.getBlock().toString();
            }
            case "world.setBlock" -> {
                int x = ((Number) params.get("x")).intValue();
                int y = ((Number) params.get("y")).intValue();
                int z = ((Number) params.get("z")).intValue();
                String block = params.get("block").toString();
                var id = Identifier.tryParse(block);
                if (id == null) throw new IllegalArgumentException("Invalid block: " + block);
                var item = net.minecraft.registry.Registries.ITEM.get(id);
                var state = net.minecraft.block.Block.getBlockFromItem(item).getDefaultState();
                getWorld().setBlockState(new BlockPos(x, y, z), state);
                yield true;
            }
            case "world.breakBlock" -> {
                int x = ((Number) params.get("x")).intValue();
                int y = ((Number) params.get("y")).intValue();
                int z = ((Number) params.get("z")).intValue();
                BlockPos pos = new BlockPos(x, y, z);
                getWorld().breakBlock(pos, true);
                yield true;
            }
            case "world.getBiome" -> {
                int x = ((Number) params.get("x")).intValue();
                int y = ((Number) params.get("y")).intValue();
                int z = ((Number) params.get("z")).intValue();
                var biome = getWorld().getBiome(new BlockPos(x, y, z));
                yield biome.getKey().map(k -> k.getValue().toString()).orElse("unknown");
            }
            case "world.getTime" -> getWorld().getTimeOfDay();
            case "world.setTime" -> {
                getWorld().setTimeOfDay(((Number) params.get("time")).longValue());
                yield true;
            }
            case "world.getWeather" -> {
                if (getWorld().isThundering()) yield "thunder";
                if (getWorld().isRaining()) yield "rain";
                yield "clear";
            }
            case "world.setWeather" -> {
                String weather = params.get("weather").toString();
                switch (weather) {
                    case "clear" -> getWorld().setWeather(0, 0, false, false);
                    case "rain" -> getWorld().setWeather(0, 6000, true, false);
                    case "thunder" -> getWorld().setWeather(0, 6000, true, true);
                }
                yield true;
            }
            case "world.getDifficulty" -> getWorld().getDifficulty().getName();
            case "world.setDifficulty" -> {
                var diff = net.minecraft.world.Difficulty.valueOf(params.get("difficulty").toString().toUpperCase());
                getWorld().getServer().setDifficulty(diff, true);
                yield true;
            }
            case "world.getDimension" -> getWorld().getRegistryKey().getValue().toString();
            case "world.getGameRule" -> {
                var rule = params.get("rule").toString();
                var key = net.minecraft.world.GameRules.getKey(rule);
                if (key == null) throw new IllegalArgumentException("Unknown gamerule: " + rule);
                yield getWorld().getGameRules().get(key).toString();
            }
            case "world.setGameRule" -> {
                var rule = params.get("rule").toString();
                var value = params.get("value").toString();
                var key = net.minecraft.world.GameRules.getKey(rule);
                if (key == null) throw new IllegalArgumentException("Unknown gamerule: " + rule);
                var ruleObj = getWorld().getGameRules().get(key);
                if (ruleObj instanceof net.minecraft.world.GameRules.BooleanRule br) {
                    br.set(value.equals("true"), null);
                } else if (ruleObj instanceof net.minecraft.world.GameRules.IntRule ir) {
                    ir.set(Integer.parseInt(value), null);
                }
                yield true;
            }
            case "world.runCommand" -> {
                String cmd = params.get("command").toString();
                if (cmd.startsWith("/")) cmd = cmd.substring(1);
                var result = getWorld().getServer().getCommandManager().executeWithPrefix(
                        getWorld().getServer().getCommandSource(), cmd);
                yield String.valueOf(result);
            }
            case "world.createExplosion" -> {
                double x = ((Number) params.get("x")).doubleValue();
                double y = ((Number) params.get("y")).doubleValue();
                double z = ((Number) params.get("z")).doubleValue();
                float power = ((Number) params.get("power")).floatValue();
                getWorld().createExplosion(null, x, y, z, power, true, ServerWorld.ExplosionSourceType.BLOCK);
                yield true;
            }
            case "world.spawnParticle" -> {
                String particle = params.get("particle").toString();
                double x = ((Number) params.get("x")).doubleValue();
                double y = ((Number) params.get("y")).doubleValue();
                double z = ((Number) params.get("z")).doubleValue();
                int count = params.containsKey("count") ? ((Number) params.get("count")).intValue() : 1;
                getWorld().spawnParticles(
                        net.minecraft.particle.ParticleTypes.valueOf(particle.replace("minecraft:", "").toUpperCase()),
                        x, y, z, count, 0, 0, 0, 0);
                yield true;
            }
            case "world.playSound" -> {
                String sound = params.get("sound").toString();
                double x = ((Number) params.get("x")).doubleValue();
                double y = ((Number) params.get("y")).doubleValue();
                double z = ((Number) params.get("z")).doubleValue();
                float volume = params.containsKey("volume") ? ((Number) params.get("volume")).floatValue() : 1.0f;
                float pitch = params.containsKey("pitch") ? ((Number) params.get("pitch")).floatValue() : 1.0f;
                getWorld().playSound(null, x, y, z,
                        net.minecraft.sound.SoundEvents.ENTITY_PLAYER_LEVELUP,
                        net.minecraft.sound.SoundCategory.MASTER, volume, pitch);
                yield true;
            }
            default -> throw new IllegalArgumentException("Unknown method: " + method);
        };
    }
}
