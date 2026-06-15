package org.mlang.gui.widgets;

import com.google.gson.JsonObject;

public class NotificationWidget extends WidgetBase {
    public String text = "";
    public int durationTicks = 60;
    public String ntype = "info";
    public long startTime = 0;
    public boolean dismissed = false;

    public NotificationWidget() { type = "Notification"; width = 250; height = 40; }

    public NotificationWidget(JsonObject json) {
        super(json);
        type = "Notification";
        if (json.has("text")) text = json.get("text").getAsString();
        if (json.has("duration")) durationTicks = json.get("duration").getAsInt();
        if (json.has("type")) ntype = json.get("type").getAsString();
    }

    @Override
    public void update(float delta) {
        if (visible && durationTicks > 0) {
            long elapsed = System.currentTimeMillis() - startTime;
            if (elapsed >= durationTicks * 50) {
                dismissed = true;
                visible = false;
            }
        }
    }

    public void show() {
        visible = true;
        startTime = System.currentTimeMillis();
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("text", text);
        json.addProperty("type", ntype);
        return json;
    }
}
