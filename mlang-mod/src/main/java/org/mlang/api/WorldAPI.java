package org.mlang.api;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import org.mlang.MlangMod;
import org.mlang.bridge.ApiHandler;

import java.util.Map;

public class WorldAPI implements ApiHandler {

    private ServerLevel w() { return MlangMod.SERVER.overworld(); }

    private void exec(String cmd) {
        var s = MlangMod.SERVER;
        s.getCommands().performCommand(s.getCommands().getDispatcher().parse(cmd, s.createCommandSourceStack()), cmd);
    }

    @Override
    public Object handle(String method, Map<String, Object> params) {
        return switch (method) {
            case "world.getBlock" -> {
                int x = ((Number) params.get("x")).intValue();
                int y = ((Number) params.get("y")).intValue();
                int z = ((Number) params.get("z")).intValue();
                yield w().getBlockState(new BlockPos(x, y, z)).getBlock().toString();
            }
            case "world.setBlock" -> {
                int x = ((Number) params.get("x")).intValue();
                int y = ((Number) params.get("y")).intValue();
                int z = ((Number) params.get("z")).intValue();
                exec("setblock " + x + " " + y + " " + z + " " + params.get("block"));
                yield true;
            }
            case "world.breakBlock" -> {
                int x = ((Number) params.get("x")).intValue();
                int y = ((Number) params.get("y")).intValue();
                int z = ((Number) params.get("z")).intValue();
                w().destroyBlock(new BlockPos(x, y, z), true);
                yield true;
            }
            case "world.getTime" -> w().getDayTime();
            case "world.setTime" -> { exec("time set " + ((Number) params.get("time")).longValue()); yield true; }
            case "world.getWeather" -> {
                if (w().isThundering()) yield "thunder";
                if (w().isRaining()) yield "rain";
                yield "clear";
            }
            case "world.setWeather" -> {
                exec("weather " + params.get("weather"));
                yield true;
            }
            case "world.getDifficulty" -> w().getDifficulty().getKey();
            case "world.getDimension" -> w().dimension().location().toString();
            case "world.runCommand" -> {
                String cmd = params.get("command").toString();
                if (cmd.startsWith("/")) cmd = cmd.substring(1);
                exec(cmd);
                yield "ok";
            }
            case "world.createExplosion" -> {
                double x = ((Number) params.get("x")).doubleValue();
                double y = ((Number) params.get("y")).doubleValue();
                double z = ((Number) params.get("z")).doubleValue();
                float power = ((Number) params.get("power")).floatValue();
                w().explode(null, x, y, z, power, true, net.minecraft.world.level.Level.ExplosionInteraction.BLOCK);
                yield true;
            }
            default -> throw new IllegalArgumentException("Unknown: " + method);
        };
    }
}
