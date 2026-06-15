package org.mlang.gui;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import net.minecraft.client.MinecraftClient;
import org.mlang.MlangMod;
import org.mlang.bridge.ApiHandler;
import org.mlang.gui.widgets.NotificationWidget;
import org.mlang.gui.widgets.WidgetBase;
import org.mlang.gui.widgets.WindowWidget;

import java.util.Map;

public class GuiCommandHandler implements ApiHandler {
    private static final Gson GSON = new Gson();
    public static final GuiRenderer RENDERER = new GuiRenderer();

    public static void showScreen() {
        MinecraftClient.getInstance().execute(() -> {
            MinecraftClient.getInstance().setScreen(new GuiScreen(RENDERER, false));
        });
    }

    public static void hideScreen() {
        MinecraftClient.getInstance().execute(() -> {
            MinecraftClient.getInstance().setScreen(null);
        });
    }

    @Override
    public Object handle(String method, Map<String, Object> params) throws Exception {
        return switch (method) {
            case "gui.show" -> {
                JsonObject json;
                if (params.get("widget") instanceof Map) {
                    json = GSON.toJsonTree(params.get("widget")).getAsJsonObject();
                } else {
                    json = JsonParser.parseString(GSON.toJson(params.get("widget"))).getAsJsonObject();
                }
                RENDERER.loadFromJson(GSON.toJson(json));
                showScreen();
                yield true;
            }
            case "gui.hide" -> {
                String name = params.get("name").toString();
                RENDERER.removeWidget(name);
                yield true;
            }
            case "gui.toggle" -> {
                String name = params.get("name").toString();
                WidgetBase w = RENDERER.find(name);
                if (w != null) w.visible = !w.visible;
                yield w != null;
            }
            case "gui.update" -> {
                String name = params.get("name").toString();
                WidgetBase w = RENDERER.find(name);
                if (w != null && params.get("properties") instanceof Map) {
                    JsonObject props = GSON.toJsonTree(params.get("properties")).getAsJsonObject();
                    w.fromJson(props);
                }
                yield w != null;
            }
            case "gui.setTheme" -> {
                String theme = params.get("theme").toString();
                RENDERER.themeManager.setTheme(theme);
                yield true;
            }
            case "gui.loadThemeFromJson" -> {
                String json = params.get("json").toString();
                RENDERER.themeManager.loadFromJson(json);
                yield true;
            }
            case "gui.notification" -> {
                String text = params.get("text").toString();
                int duration = params.containsKey("duration") ? ((Number) params.get("duration")).intValue() : 60;
                String type = params.containsKey("type") ? params.get("type").toString() : "info";
                NotificationWidget n = new NotificationWidget();
                n.text = text;
                n.durationTicks = duration;
                n.ntype = type;
                n.width = Math.min(300, MinecraftClient.getInstance().textRenderer.getWidth(net.minecraft.text.Text.of(text)) + 40);
                n.x = (MinecraftClient.getInstance().getWindow().getScaledWidth() - n.width) / 2f;
                n.y = 10;
                n.show();
                RENDERER.widgets.add(n);
                yield true;
            }
            case "gui.serializeState" -> RENDERER.serializeState();
            case "gui.clearAll" -> {
                RENDERER.widgets.clear();
                RENDERER.windows.clear();
                yield true;
            }
            default -> throw new IllegalArgumentException("Unknown GUI method: " + method);
        };
    }
}
