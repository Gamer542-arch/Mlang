package org.mlang.gui.widgets;

import com.google.gson.JsonObject;
import net.minecraft.client.gui.DrawContext;

public class ButtonWidget extends WidgetBase {
    public String label = "Button";
    public String icon = "";
    public String style = "default";
    public boolean rounded = true;
    public String bindableKey = "";

    public ButtonWidget() { type = "Button"; width = 100; height = 32; }

    public ButtonWidget(JsonObject json) {
        super(json);
        type = "Button";
        if (json.has("label")) label = json.get("label").getAsString();
        if (json.has("icon")) icon = json.get("icon").getAsString();
        if (json.has("style")) style = json.get("style").getAsString();
        if (json.has("rounded")) rounded = json.get("rounded").getAsBoolean();
        if (json.has("bindable_key")) bindableKey = json.get("bindable_key").getAsString();
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("label", label);
        json.addProperty("style", style);
        json.addProperty("rounded", rounded);
        return json;
    }
}
