package org.mlang.api;

import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.network.chat.Component;
import org.mlang.MlangMod;
import org.mlang.bridge.ApiHandler;

import java.util.Map;

public class ChatAPI implements ApiHandler {

    private MinecraftServer server() {
        if (MlangMod.SERVER == null) throw new IllegalStateException("Server not ready");
        return MlangMod.SERVER;
    }

    private void exec(String cmd) {
        var s = server();
        s.getCommands().performCommand(s.getCommands().getDispatcher().parse(cmd, s.createCommandSourceStack()), cmd);
    }

    @Override
    public Object handle(String method, Map<String, Object> params) {
        var s = server();
        return switch (method) {
            case "chat.send" -> {
                var p = s.getPlayerList().getPlayers().getFirst();
                p.sendSystemMessage(Component.literal(params.get("message").toString()));
                yield true;
            }
            case "chat.broadcast" -> {
                for (var p : s.getPlayerList().getPlayers())
                    p.sendSystemMessage(Component.literal(params.get("message").toString()));
                yield true;
            }
            case "chat.runCommand" -> {
                String cmd = params.get("command").toString();
                if (cmd.startsWith("/")) cmd = cmd.substring(1);
                exec(cmd);
                yield "ok";
            }
            default -> throw new IllegalArgumentException("Unknown: " + method);
        };
    }
}
