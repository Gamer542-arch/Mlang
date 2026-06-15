package org.mlang.gui.widgets;

import com.google.gson.JsonObject;

public class TabWidget extends WidgetBase {
    public String title = "Tab";
    public String icon = "";
    public boolean active = false;

    public TabWidget() { type = "Tab"; width = 80; height = 28; }

    public TabWidget(JsonObject json) {
        super(json);
        type = "Tab";
        if (json.has("title")) title = json.get("title").getAsString();
        if (json.has("icon")) icon = json.get("icon").getAsString();
        if (json.has("active")) active = json.get("active").getAsBoolean();
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("title", title);
        json.addProperty("active", active);
        return json;
    }
}
