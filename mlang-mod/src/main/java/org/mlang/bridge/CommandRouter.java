package org.mlang.bridge;

import org.mlang.api.*;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class CommandRouter {
    private final Map<String, ApiHandler> handlers = new ConcurrentHashMap<>();

    public void register(String prefix, ApiHandler handler) {
        handlers.put(prefix, handler);
    }

    public void registerAll() {
        register("player.", new PlayerAPI());
        register("world.", new WorldAPI());
        register("chat.", new ChatAPI());
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
