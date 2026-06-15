package org.mlang.config;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import net.fabricmc.loader.api.FabricLoader;
import org.mlang.MlangMod;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class ModConfig {
    private static final Path CONFIG_PATH = FabricLoader.getInstance().getConfigDir().resolve("mlang.json");
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();

    public int port = 27678;
    public String authToken = "mlang-secret-key";

    public static ModConfig load() {
        if (Files.exists(CONFIG_PATH)) {
            try {
                return GSON.fromJson(Files.readString(CONFIG_PATH), ModConfig.class);
            } catch (IOException e) {
                MlangMod.LOGGER.error("Failed to load config", e);
            }
        }
        var config = new ModConfig();
        config.save();
        return config;
    }

    public void save() {
        try {
            Files.createDirectories(CONFIG_PATH.getParent());
            Files.writeString(CONFIG_PATH, GSON.toJson(this));
        } catch (IOException e) {
            MlangMod.LOGGER.error("Failed to save config", e);
        }
    }
}
