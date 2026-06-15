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
    public static MinecraftServer SERVER;

    private BridgeServer wsServer;

    @Override
    public void onInitialize() {
        LOGGER.info("MLang Bridge initializing...");
        var config = ModConfig.load();

        ServerLifecycleEvents.SERVER_STARTED.register(server -> {
            SERVER = server;
            wsServer = new BridgeServer(config.port, config.authToken);
            wsServer.start();
            LOGGER.info("MLang Bridge started on port {}", config.port);
        });

        ServerLifecycleEvents.SERVER_STOPPING.register(server -> {
            if (wsServer != null) {
                try { wsServer.stop(1000); } catch (Exception e) { LOGGER.error("WS stop error", e); }
            }
        });
    }
}
