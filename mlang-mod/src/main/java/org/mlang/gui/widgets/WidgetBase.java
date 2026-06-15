package org.mlang.gui.widgets;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import net.minecraft.client.gui.DrawContext;
import net.minecraft.text.Text;
import net.minecraft.util.math.MathHelper;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public class WidgetBase {
    public enum State { NORMAL, HOVER, ACTIVE, DISABLED, FOCUSED }
    public enum AnimationType { FADE_IN, SLIDE_DOWN, SLIDE_LEFT, BOUNCE_IN, ZOOM_IN, PULSE, SHAKE, RAINBOW }

    public String type = "Widget";
    public String name = "";
    public boolean visible = true;
    public boolean enabled = true;
    public State state = State.NORMAL;

    public float x, y;
    public float width = 100, height = 28;
    public int zIndex = 0;

    public String color = "";
    public String textColor = "";
    public String borderColor = "";
    public String backgroundColor = "";
    public float opacity = 1.0f;

    public boolean draggable = false;
    public boolean dragging = false;
    public float dragStartX, dragStartY;

    public Consumer<Void> onClick;
    public Consumer<Void> onRightClick;
    public Consumer<Void> onHoverEnter;
    public Consumer<Void> onHoverLeave;

    public float animOpacity = 1.0f;
    public float animX = 0, animY = 0;
    public float animScale = 1.0f;

    public WidgetBase parent;
    public final List<WidgetBase> children = new ArrayList<>();

    public WidgetBase() {}

    public WidgetBase(JsonObject json) {
        fromJson(json);
    }

    public void fromJson(JsonObject json) {
        if (json.has("type")) type = json.get("type").getAsString();
        if (json.has("name")) name = json.get("name").getAsString();
        if (json.has("visible")) visible = json.get("visible").getAsBoolean();
        if (json.has("enabled")) enabled = json.get("enabled").getAsBoolean();
        if (json.has("x")) x = json.get("x").getAsFloat();
        if (json.has("y")) y = json.get("y").getAsFloat();
        if (json.has("width")) width = json.get("width").getAsFloat();
        if (json.has("height")) height = json.get("height").getAsFloat();
        if (json.has("z_index")) zIndex = json.get("z_index").getAsInt();
        if (json.has("color")) color = json.get("color").getAsString();
        if (json.has("text_color")) textColor = json.get("text_color").getAsString();
        if (json.has("border_color")) borderColor = json.get("border_color").getAsString();
        if (json.has("opacity")) opacity = json.get("opacity").getAsFloat();
        if (json.has("draggable")) draggable = json.get("draggable").getAsBoolean();

        if (json.has("children")) {
            JsonArray arr = json.getAsJsonArray("children");
            for (JsonElement el : arr) {
                WidgetBase child = WidgetFactory.create(el.getAsJsonObject());
                child.parent = this;
                children.add(child);
            }
        }
    }

    public JsonObject toJson() {
        JsonObject json = new JsonObject();
        json.addProperty("type", type);
        json.addProperty("name", name);
        json.addProperty("visible", visible);
        json.addProperty("enabled", enabled);
        json.addProperty("x", x);
        json.addProperty("y", y);
        json.addProperty("width", width);
        json.addProperty("height", height);
        json.addProperty("z_index", zIndex);
        json.addProperty("opacity", opacity);
        return json;
    }

    public float absoluteX() {
        return (parent != null ? parent.absoluteX() : 0) + x + animX;
    }

    public float absoluteY() {
        return (parent != null ? parent.absoluteY() : 0) + y + animY;
    }

    public boolean contains(double px, double py) {
        float ax = absoluteX(), ay = absoluteY();
        return ax <= px && px <= ax + width && ay <= py && py <= ay + height;
    }

    public WidgetBase find(String widgetName) {
        if (name.equals(widgetName)) return this;
        for (var c : children) {
            WidgetBase found = c.find(widgetName);
            if (found != null) return found;
        }
        return null;
    }

    public void add(WidgetBase... widgets) {
        for (var w : widgets) {
            w.parent = this;
            children.add(w);
        }
    }

    public void remove(WidgetBase w) {
        children.remove(w);
    }

    public void render(DrawContext ctx, int mouseX, int mouseY, float delta) {}

    public boolean handleClick(double mx, double my, int button) {
        if (!visible || !enabled) return false;
        if (contains(mx, my)) {
            if (draggable && button == 0) {
                dragging = true;
                dragStartX = (float)(mx - x);
                dragStartY = (float)(my - y);
            }
            if (button == 0 && onClick != null) onClick.accept(null);
            else if (button == 1 && onRightClick != null) onRightClick.accept(null);
            return true;
        }
        return false;
    }

    public boolean handleDrag(double mx, double my) {
        if (dragging && draggable) {
            x = (float)(mx - dragStartX);
            y = (float)(my - dragStartY);
            return true;
        }
        return false;
    }

    public void handleDragEnd() { dragging = false; }

    public boolean handleHover(double mx, double my) {
        if (!visible || !enabled) return false;
        boolean wasHovering = state == State.HOVER;
        boolean isHovering = contains(mx, my);
        if (isHovering && !wasHovering) {
            state = State.HOVER;
            if (onHoverEnter != null) onHoverEnter.accept(null);
        } else if (!isHovering && wasHovering) {
            state = State.NORMAL;
            if (onHoverLeave != null) onHoverLeave.accept(null);
        }
        return isHovering;
    }

    public void update(float delta) {}

    protected int parseColor(String hex, int defaultCol) {
        if (hex == null || hex.isEmpty()) return defaultCol;
        try {
            hex = hex.replace("#", "");
            long val = Long.parseLong(hex, 16);
            return 0xFF000000 | (int) val;
        } catch (Exception e) {
            return defaultCol;
        }
    }

    protected int alpha(int color, float a) {
        int alpha = MathHelper.clamp((int)(a * 255), 0, 255);
        return (color & 0x00FFFFFF) | (alpha << 24);
    }
}
