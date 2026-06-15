package org.mlang.bridge;

import com.google.gson.*;
import org.java_websocket.WebSocket;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.server.WebSocketServer;
import org.mlang.MlangMod;

import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class BridgeServer extends WebSocketServer {
    private static final Gson GSON = new Gson();
    private final String authToken;
    private final Map<WebSocket, Boolean> authenticated = new ConcurrentHashMap<>();
    private final CommandRouter router;

    public BridgeServer(int port, String authToken) {
        super(new InetSocketAddress("localhost", port));
        this.authToken = authToken;
        this.router = new CommandRouter();
        router.registerAll();
    }

    @Override
    public void onOpen(WebSocket conn, ClientHandshake handshake) {
        authenticated.put(conn, false);
        MlangMod.LOGGER.info("New client connected from {}", conn.getRemoteSocketAddress());
    }

    @Override
    public void onClose(WebSocket conn, int code, String reason, boolean remote) {
        authenticated.remove(conn);
        MlangMod.LOGGER.info("Client disconnected: {}", conn.getRemoteSocketAddress());
    }

    @Override
    public void onMessage(WebSocket conn, String message) {
        try {
            JsonObject json = JsonParser.parseString(message).getAsJsonObject();
            String method = json.get("method").getAsString();

            Boolean auth = authenticated.getOrDefault(conn, false);
            if (!auth && !method.equals("auth")) {
                sendError(conn, json, -32000, "Not authenticated");
                return;
            }

            if (method.equals("auth")) {
                handleAuth(conn, json);
                return;
            }

            String id = json.has("id") && !json.get("id").isJsonNull()
                    ? json.get("id").getAsString() : null;
            Map<String, Object> params = new HashMap<>();

            if (json.has("params") && json.get("params").isJsonObject()) {
                JsonObject p = json.getAsJsonObject("params");
                for (var entry : p.entrySet()) {
                    params.put(entry.getKey(), jsonElementToJava(entry.getValue()));
                }
            }

            try {
                Object result = router.execute(method, params);
                sendResult(conn, id, result);
            } catch (Exception e) {
                MlangMod.LOGGER.error("Error executing method {}: {}", method, e.getMessage());
                sendError(conn, id, -32603, e.getMessage());
            }
        } catch (Exception e) {
            MlangMod.LOGGER.error("Error parsing message", e);
            sendError(conn, null, -32700, "Parse error: " + e.getMessage());
        }
    }

    private void handleAuth(WebSocket conn, JsonObject json) {
        JsonObject p = json.getAsJsonObject("params");
        String token = p.get("token").getAsString();
        String id = json.has("id") ? json.get("id").getAsString() : "0";

        if (authToken.equals(token)) {
            authenticated.put(conn, true);
            sendResult(conn, id, true);
            MlangMod.LOGGER.info("Client authenticated");
        } else {
            sendError(conn, id, -32001, "Invalid auth token");
            conn.close();
        }
    }

    private void sendResult(WebSocket conn, String id, Object result) {
        JsonObject json = new JsonObject();
        json.addProperty("jsonrpc", "2.0");
        if (id != null) json.addProperty("id", id);
        json.add("result", javaToJsonElement(result));
        conn.send(json.toString());
    }

    private void sendError(WebSocket conn, String id, int code, String message) {
        JsonObject json = new JsonObject();
        json.addProperty("jsonrpc", "2.0");
        if (id != null) json.addProperty("id", id);
        JsonObject err = new JsonObject();
        err.addProperty("code", code);
        err.addProperty("message", message);
        json.add("error", err);
        conn.send(json.toString());
    }

    private Object jsonElementToJava(JsonElement el) {
        if (el.isJsonPrimitive()) {
            JsonPrimitive prim = el.getAsJsonPrimitive();
            if (prim.isBoolean()) return prim.getAsBoolean();
            if (prim.isNumber()) return prim.getAsDouble();
            return prim.getAsString();
        }
        if (el.isJsonObject()) {
            Map<String, Object> map = new HashMap<>();
            for (var entry : el.getAsJsonObject().entrySet()) {
                map.put(entry.getKey(), jsonElementToJava(entry.getValue()));
            }
            return map;
        }
        if (el.isJsonArray()) {
            return GSON.fromJson(el, Object.class);
        }
        return el.toString();
    }

    private JsonElement javaToJsonElement(Object val) {
        if (val == null) return JsonNull.INSTANCE;
        if (val instanceof Boolean b) return new JsonPrimitive(b);
        if (val instanceof Number n) return new JsonPrimitive(n);
        if (val instanceof String s) {
            try {
                return JsonParser.parseString(s);
            } catch (Exception e) {
                return new JsonPrimitive(s);
            }
        }
        if (val instanceof Map) return GSON.toJsonTree(val);
        return GSON.toJsonTree(val);
    }

    @Override
    public void onError(WebSocket conn, Exception ex) {
        MlangMod.LOGGER.error("WebSocket error", ex);
    }

    @Override
    public void onStart() {
        MlangMod.LOGGER.info("MLang WebSocket server started on {}", getAddress());
    }
}
