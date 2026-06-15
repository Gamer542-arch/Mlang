package org.mlang.gui.widgets;

import com.google.gson.JsonObject;

public class SeparatorWidget extends WidgetBase {
    public String orientation = "horizontal";

    public SeparatorWidget() { type = "Separator"; width = 200; height = 1; }

    public SeparatorWidget(JsonObject json) {
        super(json);
        type = "Separator";
        if (json.has("orientation")) orientation = json.get("orientation").getAsString();
    }
}
