package org.mlang.api;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Text;
import net.minecraft.util.math.Vec3d;
import org.mlang.MlangMod;

import java.util.HashMap;
import java.util.Map;

public class PlayerAPI implements ApiHandler {

    private ServerPlayerEntity getPlayer() {
        var server = MlangMod.SERVER;
        if (server == null) throw new IllegalStateException("Server not ready");
        var player = server.getPlayerManager().getPlayerList().stream().findFirst().orElse(null);
        if (player == null) throw new IllegalStateException("No player online");
        return player;
    }

    @Override
    public Object handle(String method, Map<String, Object> params) {
        return switch (method) {
            case "player.getHealth" -> getPlayer().getHealth();
            case "player.setHealth" -> {
                double h = ((Number) params.get("health")).doubleValue();
                getPlayer().setHealth((float) h);
                yield true;
            }
            case "player.getMaxHealth" -> getPlayer().getMaxHealth();
            case "player.setMaxHealth" -> {
                double h = ((Number) params.get("maxHealth")).doubleValue();
                getPlayer().getAttributeInstance(net.minecraft.entity.attribute.EntityAttributes.GENERIC_MAX_HEALTH)
                        .setBaseValue(h);
                yield true;
            }
            case "player.getPosition" -> {
                var p = getPlayer();
                Map<String, Object> pos = new HashMap<>();
                pos.put("x", p.getX());
                pos.put("y", p.getY());
                pos.put("z", p.getZ());
                pos.put("yaw", (double) p.getYaw());
                pos.put("pitch", (double) p.getPitch());
                yield pos;
            }
            case "player.teleport" -> {
                var p = getPlayer();
                double x = ((Number) params.get("x")).doubleValue();
                double y = ((Number) params.get("y")).doubleValue();
                double z = ((Number) params.get("z")).doubleValue();
                float yaw = params.containsKey("yaw") ? ((Number) params.get("yaw")).floatValue() : p.getYaw();
                float pitch = params.containsKey("pitch") ? ((Number) params.get("pitch")).floatValue() : p.getPitch();
                p.teleport(p.getServerWorld(), x, y, z, yaw, pitch);
                yield true;
            }
            case "player.getVelocity" -> {
                var v = getPlayer().getVelocity();
                Map<String, Object> vel = new HashMap<>();
                vel.put("x", v.x);
                vel.put("y", v.y);
                vel.put("z", v.z);
                yield vel;
            }
            case "player.setVelocity" -> {
                var p = getPlayer();
                double vx = ((Number) params.get("x")).doubleValue();
                double vy = ((Number) params.get("y")).doubleValue();
                double vz = ((Number) params.get("z")).doubleValue();
                p.setVelocity(vx, vy, vz);
                yield true;
            }
            case "player.getGameMode" -> getPlayer().interactionManager.getGameMode().getName();
            case "player.setGameMode" -> {
                var gm = net.minecraft.world.GameMode.valueOf(params.get("gamemode").toString().toUpperCase());
                getPlayer().changeGameMode(gm);
                yield true;
            }
            case "player.getFoodLevel" -> getPlayer().getHungerManager().getFoodLevel();
            case "player.setFoodLevel" -> {
                getPlayer().getHungerManager().setFoodLevel(((Number) params.get("level")).intValue());
                yield true;
            }
            case "player.getSaturation" -> getPlayer().getHungerManager().getSaturationLevel();
            case "player.setSaturation" -> {
                getPlayer().getHungerManager().setSaturationLevel(((Number) params.get("saturation")).floatValue());
                yield true;
            }
            case "player.getExperience" -> getPlayer().totalExperience;
            case "player.setExperience" -> {
                getPlayer().totalExperience = ((Number) params.get("xp")).intValue();
                getPlayer().calculateScore();
                getPlayer().applyExperienceChanges();
                yield true;
            }
            case "player.getLevel" -> getPlayer().experienceLevel;
            case "player.setLevel" -> {
                getPlayer().experienceLevel = ((Number) params.get("level")).intValue();
                getPlayer().applyExperienceChanges();
                yield true;
            }
            case "player.giveItem" -> {
                String item = params.get("item").toString();
                int count = params.containsKey("count") ? ((Number) params.get("count")).intValue() : 1;
                getPlayer().giveItemStack(new net.minecraft.item.ItemStack(
                        net.minecraft.registry.Registries.ITEM.get(new net.minecraft.util.Identifier(item)), count));
                yield true;
            }
            case "player.getMainHandItem" -> getPlayer().getMainHandStack().getItem().toString();
            case "player.sendMessage" -> {
                getPlayer().sendMessage(Text.literal(params.get("message").toString()), false);
                yield true;
            }
            case "player.kill" -> {
                getPlayer().kill();
                yield true;
            }
            case "player.getName" -> getPlayer().getName().getString();
            case "player.getUUID" -> getPlayer().getUuid().toString();
            case "player.getDimension" -> getPlayer().getServerWorld().getRegistryKey().getValue().toString();
            case "player.isAlive" -> getPlayer().isAlive();
            case "player.isFlying" -> getPlayer().getAbilities().flying;
            case "player.isSneaking" -> getPlayer().isSneaking();
            case "player.isSprinting" -> getPlayer().isSprinting();
            case "player.isOnGround" -> getPlayer().isOnGround();
            case "player.isInWater" -> getPlayer().isTouchingWater();
            case "player.isOnFire" -> getPlayer().isOnFire();
            default -> throw new IllegalArgumentException("Unknown method: " + method);
        };
    }
}
