package org.mlang.gui.widgets;

import com.google.gson.JsonObject;
import net.minecraft.client.gui.DrawContext;

public class ToggleWidget extends WidgetBase {
    public String label = "Toggle";
    public boolean value = false;
    public String onLabel = "ON", offLabel = "OFF";
    public String bindableKey = "";

    public ToggleWidget() { type = "Toggle"; width = 120; height = 28; }

    public ToggleWidget(JsonObject json) {
        super(json);
        type = "Toggle";
        if (json.has("label")) label = json.get("label").getAsString();
        if (json.has("value")) value = json.get("value").getAsBoolean();
        if (json.has("bindable_key")) bindableKey = json.get("bindable_key").getAsString();
    }

    public void toggle() {
        value = !value;
        if (onClick != null) onClick.accept(null);
    }

    @Override
    public boolean handleClick(double mx, double my, int button) {
        if (contains(mx, my)) {
            toggle();
            return true;
        }
        return false;
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("label", label);
        json.addProperty("value", value);
        return json;
    }
}
