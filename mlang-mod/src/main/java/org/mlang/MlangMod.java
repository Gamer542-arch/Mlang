package org.mlang;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.minecraft.server.MinecraftServer;
import org.mlang.bridge.BridgeServer;
import org.mlang.config.ModConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MlangMod implements ModInitializer {
    public static final String MOD_ID = "mlang";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);
    private static BridgeServer wsServer;
    private static ModConfig config;
    public static MinecraftServer SERVER;

    @Override
    public void onInitialize() {
        LOGGER.info("Initializing MLang Bridge...");

        config = ModConfig.load();

        ServerLifecycleEvents.SERVER_STARTED.register(server -> {
            SERVER = server;
            wsServer = new BridgeServer(config.port, config.authToken);
            wsServer.start();
            LOGGER.info("MLang Bridge started on port {}", config.port);
        });

        ServerLifecycleEvents.SERVER_STOPPING.register(server -> {
            if (wsServer != null) {
                try { wsServer.stop(1000); } catch (Exception e) { LOGGER.error("Error stopping WS", e); }
            }
            LOGGER.info("MLang Bridge stopped");
        });
    }

    public static ModConfig getConfig() {
        return config;
    }

    public static BridgeServer getWebSocketServer() {
        return wsServer;
    }
}
