package org.mlang.api;

import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.network.chat.Component;
import org.mlang.MlangMod;
import org.mlang.bridge.ApiHandler;

import java.util.HashMap;
import java.util.Map;

public class PlayerAPI implements ApiHandler {

    private MinecraftServer s() { return MlangMod.SERVER; }
    private ServerPlayer p() { return s().getPlayerList().getPlayers().getFirst(); }

    private void exec(String cmd) {
        var srv = s();
        srv.getCommands().performCommand(srv.getCommands().getDispatcher().parse(cmd, srv.createCommandSourceStack()), cmd);
    }

    @Override
    public Object handle(String method, Map<String, Object> params) {
        return switch (method) {
            case "player.getHealth" -> p().getHealth();
            case "player.setHealth" -> {
                exec("attribute " + p().getName().getString() + " minecraft:generic.max_health base set " + ((Number) params.get("health")).doubleValue());
                yield true;
            }
            case "player.getPosition" -> {
                var pl = p();
                Map<String, Object> pos = new HashMap<>();
                pos.put("x", pl.getX()); pos.put("y", pl.getY()); pos.put("z", pl.getZ());
                pos.put("yaw", (double) pl.getYRot()); pos.put("pitch", (double) pl.getXRot());
                yield pos;
            }
            case "player.teleport" -> {
                double x = ((Number) params.get("x")).doubleValue();
                double y = ((Number) params.get("y")).doubleValue();
                double z = ((Number) params.get("z")).doubleValue();
                exec("tp " + p().getName().getString() + " " + x + " " + y + " " + z);
                yield true;
            }
            case "player.getGameMode" -> p().gameMode.getGameModeForPlayer().getName();
            case "player.setGameMode" -> {
                exec("gamemode " + params.get("gamemode") + " " + p().getName().getString());
                yield true;
            }
            case "player.getFoodLevel" -> p().getFoodData().getFoodLevel();
            case "player.setFoodLevel" -> {
                exec("effect give " + p().getName().getString() + " minecraft:saturation 1 " + ((Number) params.get("level")).intValue());
                yield true;
            }
            case "player.getExperience" -> p().totalExperience;
            case "player.getLevel" -> p().experienceLevel;
            case "player.giveItem" -> {
                String item = params.get("item").toString();
                int count = params.containsKey("count") ? ((Number) params.get("count")).intValue() : 1;
                exec("give " + p().getName().getString() + " " + item + " " + count);
                yield true;
            }
            case "player.sendMessage" -> {
                p().sendSystemMessage(Component.literal(params.get("message").toString()));
                yield true;
            }
            case "player.kill" -> { exec("kill " + p().getName().getString()); yield true; }
            case "player.getName" -> p().getName().getString();
            case "player.getUUID" -> p().getStringUUID();
            case "player.getDimension" -> p().level().dimension().location().toString();
            case "player.isAlive" -> p().isAlive();
            case "player.isFlying" -> p().getAbilities().flying;
            case "player.isSneaking" -> p().isCrouching();
            case "player.isSprinting" -> p().isSprinting();
            case "player.isOnGround" -> p().onGround();
            case "player.isInWater" -> p().isInWater();
            case "player.isOnFire" -> p().isOnFire();
            default -> throw new IllegalArgumentException("Unknown: " + method);
        };
    }
}
