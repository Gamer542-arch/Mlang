package org.mlang.gui.widgets;

import com.google.gson.JsonObject;

public class LabelWidget extends WidgetBase {
    public String text = "Label";
    public String textAlign = "left";
    public int fontSize = 10;
    public boolean bold = false;
    public boolean italic = false;

    public LabelWidget() { type = "Label"; width = 100; height = 20; }

    public LabelWidget(JsonObject json) {
        super(json);
        type = "Label";
        if (json.has("text")) text = json.get("text").getAsString();
        if (json.has("text_align")) textAlign = json.get("text_align").getAsString();
        if (json.has("font_size")) fontSize = json.get("font_size").getAsInt();
        if (json.has("bold")) bold = json.get("bold").getAsBoolean();
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("text", text);
        return json;
    }
}
