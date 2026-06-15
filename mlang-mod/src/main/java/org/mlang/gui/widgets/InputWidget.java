package org.mlang.gui.widgets;

import com.google.gson.JsonObject;
import net.minecraft.client.gui.DrawContext;

public class InputWidget extends WidgetBase {
    public String placeholder = "Type here...";
    public String text = "";
    public int maxLength = 0;
    public String inputType = "text";
    public int cursorPos = 0;

    public InputWidget() { type = "Input"; width = 200; height = 28; }

    public InputWidget(JsonObject json) {
        super(json);
        type = "Input";
        if (json.has("placeholder")) placeholder = json.get("placeholder").getAsString();
        if (json.has("text")) text = json.get("text").getAsString();
        if (json.has("max_length")) maxLength = json.get("max_length").getAsInt();
        if (json.has("input_type")) inputType = json.get("input_type").getAsString();
    }

    public void focus() {
        state = State.FOCUSED;
    }

    public void blur() {
        state = State.NORMAL;
    }

    @Override
    public boolean handleClick(double mx, double my, int button) {
        if (contains(mx, my)) {
            focus();
            return true;
        }
        blur();
        return false;
    }

    public void handleChar(char c) {
        if (state != State.FOCUSED) return;
        if (maxLength > 0 && text.length() >= maxLength) return;
        text += c;
        if (onClick != null) onClick.accept(null);
    }

    public void handleKey(int key, int scancode, int modifiers) {
        if (state != State.FOCUSED) return;
        if (key == 259 && !text.isEmpty()) { // backspace
            text = text.substring(0, text.length() - 1);
        }
        if (onClick != null) onClick.accept(null);
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("placeholder", placeholder);
        json.addProperty("text", text);
        return json;
    }
}
