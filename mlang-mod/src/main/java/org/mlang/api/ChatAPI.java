package org.mlang.api;

import net.minecraft.text.Text;
import org.mlang.MlangMod;

import java.util.Map;

public class ChatAPI implements ApiHandler {

    @Override
    public Object handle(String method, Map<String, Object> params) {
        return switch (method) {
            case "chat.send" -> {
                var server = MlangMod.SERVER;
                if (server == null) throw new IllegalStateException("Server not ready");
                var player = server.getPlayerManager().getPlayerList().stream().findFirst().orElse(null);
                if (player == null) throw new IllegalStateException("No player online");
                player.sendMessage(Text.literal(params.get("message").toString()), false);
                yield true;
            }
            case "chat.broadcast" -> {
                var server = MlangMod.SERVER;
                if (server == null) throw new IllegalStateException("Server not ready");
                server.getPlayerManager().broadcast(Text.literal(params.get("message").toString()), false);
                yield true;
            }
            case "chat.runCommand" -> {
                var server = MlangMod.SERVER;
                if (server == null) throw new IllegalStateException("Server not ready");
                String cmd = params.get("command").toString();
                if (cmd.startsWith("/")) cmd = cmd.substring(1);
                var result = server.getCommandManager().executeWithPrefix(
                        server.getCommandSource(), cmd);
                yield String.valueOf(result);
            }
            default -> throw new IllegalArgumentException("Unknown method: " + method);
        };
    }
}
