package org.mlang.gui.widgets;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

public class WidgetFactory {
    public static WidgetBase create(JsonObject json) {
        String type = json.has("type") ? json.get("type").getAsString() : "Widget";
        return switch (type) {
            case "Button" -> new ButtonWidget(json);
            case "Toggle" -> new ToggleWidget(json);
            case "Slider" -> new SliderWidget(json);
            case "Input" -> new InputWidget(json);
            case "Label" -> new LabelWidget(json);
            case "ProgressBar" -> new ProgressBarWidget(json);
            case "Separator" -> new SeparatorWidget(json);
            case "Category" -> new CategoryWidget(json);
            case "Window" -> new WindowWidget(json);
            case "Tab" -> new TabWidget(json);
            case "Notification" -> new NotificationWidget(json);
            default -> new WidgetBase(json);
        };
    }

    public static JsonObject serialize(WidgetBase w) {
        return w.toJson();
    }
}
