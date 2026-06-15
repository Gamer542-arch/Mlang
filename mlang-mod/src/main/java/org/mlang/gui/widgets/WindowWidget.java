package org.mlang.gui.widgets;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import net.minecraft.client.gui.DrawContext;

import java.util.ArrayList;
import java.util.List;

public class WindowWidget extends WidgetBase {
    public String title = "Window";
    public boolean resizable = true;
    public boolean closeable = true;
    public boolean minimizable = true;
    public boolean minimized = false;
    public final List<TabWidget> tabs = new ArrayList<>();
    public TabWidget activeTab;
    public float titlebarHeight = 32;
    public float minWidth = 200, minHeight = 100;
    public float maxWidth = 0, maxHeight = 0;
    public Consumer<Void> onClose;

    public boolean moving = false;
    public float moveOffsetX, moveOffsetY;

    public WindowWidget() { type = "Window"; width = 400; height = 300; draggable = true; }

    public WindowWidget(JsonObject json) {
        super(json);
        type = "Window";
        if (json.has("title")) title = json.get("title").getAsString();
        if (json.has("resizable")) resizable = json.get("resizable").getAsBoolean();
        if (json.has("closeable")) closeable = json.get("closeable").getAsBoolean();
        if (json.has("minimized")) minimized = json.get("minimized").getAsBoolean();
        if (json.has("tabs")) {
            JsonArray arr = json.getAsJsonArray("tabs");
            for (var el : arr) {
                TabWidget tab = new TabWidget(el.getAsJsonObject());
                tab.parent = this;
                tabs.add(tab);
                children.add(tab);
            }
            if (!tabs.isEmpty()) activeTab = tabs.get(0);
        }
        draggable = true;
    }

    public void addTab(TabWidget tab) {
        tab.parent = this;
        tabs.add(tab);
        children.add(tab);
        if (activeTab == null) activeTab = tab;
    }

    public void switchTab(String tabTitle) {
        for (TabWidget tab : tabs) {
            tab.active = tab.title.equals(tabTitle);
            if (tab.active) activeTab = tab;
        }
    }

    public void centerOnScreen(int screenW, int screenH) {
        x = (screenW - width) / 2f;
        y = (screenH - height) / 2f;
    }

    @Override
    public boolean handleClick(double mx, double my, int button) {
        if (!visible) return false;
        float ax = absoluteX(), ay = absoluteY();
        if (closeable && ax + width - 24 <= mx && mx <= ax + width - 4 && ay <= my && my <= ay + 20) {
            visible = false;
            if (onClose != null) onClose.accept(null);
            return true;
        }
        if (minimizable && ax + width - 48 <= mx && mx <= ax + width - 28 && ay <= my && my <= ay + 20) {
            minimized = !minimized;
            return true;
        }
        if (ay <= my && my <= ay + titlebarHeight && ax <= mx && mx <= ax + width) {
            if (draggable) {
                moving = true;
                moveOffsetX = (float)(mx - x);
                moveOffsetY = (float)(my - y);
            }
            return true;
        }
        return super.handleClick(mx, my, button);
    }

    @Override
    public boolean handleDrag(double mx, double my) {
        if (moving) {
            x = (float)(mx - moveOffsetX);
            y = (float)(my - moveOffsetY);
            return true;
        }
        return super.handleDrag(mx, my);
    }

    @Override
    public void handleDragEnd() {
        super.handleDragEnd();
        moving = false;
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("title", title);
        json.addProperty("resizable", resizable);
        json.addProperty("minimized", minimized);
        return json;
    }
}
