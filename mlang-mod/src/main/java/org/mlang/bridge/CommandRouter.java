package org.mlang.bridge;

import org.mlang.api.*;
import org.mlang.gui.GuiCommandHandler;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class CommandRouter {
    private final Map<String, ApiHandler> handlers = new ConcurrentHashMap<>();

    public void register(String prefix, ApiHandler handler) {
        handlers.put(prefix, handler);
    }

    public void registerAll() {
        PlayerAPI player = new PlayerAPI();
        register("player.", player);

        WorldAPI world = new WorldAPI();
        register("world.", world);

        ChatAPI chat = new ChatAPI();
        register("chat.", chat);

        GuiCommandHandler gui = new GuiCommandHandler();
        register("gui.", gui);
    }

    public Object execute(String method, Map<String, Object> params) throws Exception {
        for (var entry : handlers.entrySet()) {
            if (method.startsWith(entry.getKey())) {
                return entry.getValue().handle(method, params);
            }
        }
        throw new IllegalArgumentException("Unknown method: " + method);
    }
}
