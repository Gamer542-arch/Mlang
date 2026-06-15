package org.mlang.gui.theme;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

public class ThemeManager {
    private static final Gson GSON = new Gson();
    private Theme current = Theme.DARK;

    public void loadFromJson(String json) {
        try {
            JsonObject obj = GSON.fromJson(json, JsonObject.class);
            current = new Theme();
            current.name = getStr(obj, "name", "custom");
            current.background = hexToInt(getStr(obj, "background", "#0D0D0D"));
            current.surface = hexToInt(getStr(obj, "surface", "#1A1A2E"));
            current.surfaceSecondary = hexToInt(getStr(obj, "surface_secondary", "#16213E"));
            current.accent = hexToInt(getStr(obj, "accent", "#E94560"));
            current.accentHover = hexToInt(getStr(obj, "accent_hover", "#FF6B81"));
            current.text = hexToInt(getStr(obj, "text", "#EAEAEA"));
            current.textSecondary = hexToInt(getStr(obj, "text_secondary", "#8A8A9A"));
            current.border = hexToInt(getStr(obj, "border", "#2A2A4A"));
            current.borderFocus = hexToInt(getStr(obj, "border_focus", "#E94560"));
            current.shadow = hexToInt(getStr(obj, "shadow", "#00000080"));
            current.success = hexToInt(getStr(obj, "success", "#2ECC71"));
            current.warning = hexToInt(getStr(obj, "warning", "#F39C12"));
            current.error = hexToInt(getStr(obj, "error", "#E74C3C"));
            current.info = hexToInt(getStr(obj, "info", "#3498DB"));

            current.sliderTrack = hexToInt(getStr(obj, "slider_track", "#2A2A4A"));
            current.sliderFill = hexToInt(getStr(obj, "slider_fill", "#E94560"));
            current.sliderHandle = hexToInt(getStr(obj, "slider_handle", "#FFFFFF"));
            current.toggleOff = hexToInt(getStr(obj, "toggle_off", "#2A2A4A"));
            current.toggleOn = hexToInt(getStr(obj, "toggle_on", "#E94560"));

            current.blurRadius = getInt(obj, "blur_radius", 10);
            current.blurOpacity = getFloat(obj, "blur_opacity", 0.85f);
            current.borderRadius = getInt(obj, "border_radius", 4);
            current.borderWidth = getInt(obj, "border_width", 1);
            current.shadowRadius = getInt(obj, "shadow_radius", 8);
            current.shadowOpacity = getFloat(obj, "shadow_opacity", 0.5f);
            current.fontSize = getInt(obj, "font_size", 10);
            current.widgetHeight = getInt(obj, "widget_height", 28);
        } catch (Exception e) {
            System.err.println("Failed to load theme: " + e.getMessage());
            current = Theme.DARK;
        }
    }

    public Theme getCurrent() { return current; }

    public void setTheme(String name) {
        current = switch (name) {
            case "dark" -> Theme.DARK;
            case "light" -> Theme.LIGHT;
            case "minecraft" -> Theme.MINECRAFT;
            case "glass" -> Theme.GLASS;
            case "neon" -> Theme.NEON;
            case "minimal" -> Theme.MINIMAL;
            case "future" -> Theme.FUTURE;
            default -> Theme.DARK;
        };
    }

    private String getStr(JsonObject obj, String key, String def) {
        return obj.has(key) ? obj.get(key).getAsString() : def;
    }

    private int getInt(JsonObject obj, String key, int def) {
        return obj.has(key) ? obj.get(key).getAsInt() : def;
    }

    private float getFloat(JsonObject obj, String key, float def) {
        return obj.has(key) ? obj.get(key).getAsFloat() : def;
    }

    private int hexToInt(String hex) {
        if (hex == null || hex.isEmpty()) return 0xFF000000;
        try {
            hex = hex.replace("#", "");
            if (hex.length() == 6) hex = "FF" + hex;
            else if (hex.length() == 8) { /* ok */ }
            return (int) Long.parseLong(hex, 16);
        } catch (Exception e) {
            return 0xFF000000;
        }
    }
}
