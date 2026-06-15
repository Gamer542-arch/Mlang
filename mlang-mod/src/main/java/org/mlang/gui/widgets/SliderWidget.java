package org.mlang.gui.widgets;

import com.google.gson.JsonObject;
import net.minecraft.client.gui.DrawContext;

public class SliderWidget extends WidgetBase {
    public String label = "Slider";
    public double min = 0, max = 100, step = 1, value = 50;
    public boolean showValue = true;
    public String format = "{0:F1}";
    public boolean sliding = false;

    public SliderWidget() { type = "Slider"; width = 200; height = 28; }

    public SliderWidget(JsonObject json) {
        super(json);
        type = "Slider";
        if (json.has("label")) label = json.get("label").getAsString();
        if (json.has("min")) min = json.get("min").getAsDouble();
        if (json.has("max")) max = json.get("max").getAsDouble();
        if (json.has("step")) step = json.get("step").getAsDouble();
        if (json.has("value")) value = json.get("value").getAsDouble();
        if (json.has("show_value")) showValue = json.get("show_value").getAsBoolean();
    }

    public double normalized() {
        if (max == min) return 0;
        return (value - min) / (max - min);
    }

    public void setFromNormalized(double t) {
        t = Math.max(0, Math.min(1, t));
        double raw = min + t * (max - min);
        if (step > 0) raw = Math.round(raw / step) * step;
        value = Math.max(min, Math.min(max, raw));
    }

    @Override
    public boolean handleClick(double mx, double my, int button) {
        if (!visible || !enabled) return false;
        if (contains(mx, my) || sliding) {
            double rel = (mx - absoluteX()) / width;
            setFromNormalized(rel);
            sliding = true;
            return true;
        }
        return false;
    }

    @Override
    public boolean handleDrag(double mx, double my) {
        if (sliding) {
            double rel = (mx - absoluteX()) / width;
            setFromNormalized(rel);
            return true;
        }
        return false;
    }

    @Override
    public void handleDragEnd() { sliding = false; }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("label", label);
        json.addProperty("min", min);
        json.addProperty("max", max);
        json.addProperty("value", value);
        return json;
    }
}
