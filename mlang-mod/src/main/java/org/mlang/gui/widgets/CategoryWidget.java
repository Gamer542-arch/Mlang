package org.mlang.gui.widgets;

import com.google.gson.JsonObject;
import net.minecraft.client.gui.DrawContext;

public class CategoryWidget extends WidgetBase {
    public String title = "Category";
    public boolean collapsible = true;
    public boolean collapsed = false;
    public float headerHeight = 28;

    public CategoryWidget() { type = "Category"; width = 300; height = 200; }

    public CategoryWidget(JsonObject json) {
        super(json);
        type = "Category";
        if (json.has("title")) title = json.get("title").getAsString();
        if (json.has("collapsible")) collapsible = json.get("collapsible").getAsBoolean();
        if (json.has("collapsed")) collapsed = json.get("collapsed").getAsBoolean();
        if (json.has("header_height")) headerHeight = json.get("header_height").getAsFloat();
    }

    public void toggleCollapse() {
        collapsed = !collapsed;
    }

    @Override
    public boolean handleClick(double mx, double my, int button) {
        float ax = absoluteX(), ay = absoluteY();
        if (ax <= mx && mx <= ax + width && ay <= my && my <= ay + headerHeight) {
            if (collapsible) toggleCollapse();
            if (onClick != null) onClick.accept(null);
            return true;
        }
        if (!collapsed) {
            return super.handleClick(mx, my, button);
        }
        return false;
    }

    @Override
    public JsonObject toJson() {
        JsonObject json = super.toJson();
        json.addProperty("title", title);
        json.addProperty("collapsed", collapsed);
        return json;
    }
}
