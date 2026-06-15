package org.mlang.gui.widgets;

import com.google.gson.JsonObject;

public class ProgressBarWidget extends WidgetBase {
    public double min = 0, max = 100, value = 50;
    public boolean showLabel = true;
    public String labelFormat = "{0:F0}%";
    public boolean indeterminate = false;

    public ProgressBarWidget() { type = "ProgressBar"; width = 200; height = 16; }

    public ProgressBarWidget(JsonObject json) {
        super(json);
        type = "ProgressBar";
        if (json.has("min")) min = json.get("min").getAsDouble();
        if (json.has("max")) max = json.get("max").getAsDouble();
        if (json.has("value")) value = json.get("value").getAsDouble();
        if (json.has("show_label")) showLabel = json.get("show_label").getAsBoolean();
        if (json.has("indeterminate")) indeterminate = json.get("indeterminate").getAsBoolean();
    }

    public double normalized() {
        if (max == min) return 0;
        return Math.max(0, Math.min(1, (value - min) / (max - min)));
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("value", value);
        return json;
    }
}
