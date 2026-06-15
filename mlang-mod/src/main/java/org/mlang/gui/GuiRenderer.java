package org.mlang.gui;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import net.minecraft.client.MinecraftClient;
import net.minecraft.client.font.TextRenderer;
import net.minecraft.client.gui.DrawContext;
import net.minecraft.text.Text;
import org.mlang.gui.animation.AnimationEngine;
import org.mlang.gui.effects.EffectsRenderer;
import org.mlang.gui.theme.Theme;
import org.mlang.gui.theme.ThemeManager;
import org.mlang.gui.widgets.*;

import java.util.*;
import java.util.function.Consumer;

public class GuiRenderer {
    public final ThemeManager themeManager = new ThemeManager();
    public final AnimationEngine animations = new AnimationEngine();
    public final List<WidgetBase> widgets = new ArrayList<>();
    public final List<WindowWidget> windows = new ArrayList<>();
    public final Map<String, Consumer<JsonObject>> callbacks = new HashMap<>();

    private float deltaTime = 0;
    private long lastTime = System.currentTimeMillis();

    public void addWidget(WidgetBase w) {
        if (w instanceof WindowWidget ww) windows.add(ww);
        else widgets.add(w);
    }

    public void removeWidget(String name) {
        widgets.removeIf(w -> w.name.equals(name));
        windows.removeIf(w -> w.name.equals(name));
    }

    public WidgetBase find(String name) {
        for (var w : widgets) {
            WidgetBase f = w.find(name);
            if (f != null) return f;
        }
        for (var w : windows) {
            WidgetBase f = w.find(name);
            if (f != null) return f;
        }
        return null;
    }

    public void loadFromJson(String json) {
        try {
            JsonObject root = JsonParser.parseString(json).getAsJsonObject();
            widgets.clear();
            windows.clear();

            if (root.has("widgets")) {
                JsonArray arr = root.getAsJsonArray("widgets");
                for (JsonElement el : arr) {
                    WidgetBase w = WidgetFactory.create(el.getAsJsonObject());
                    widgets.add(w);
                }
            }

            if (root.has("windows")) {
                JsonArray arr = root.getAsJsonArray("windows");
                for (JsonElement el : arr) {
                    WidgetBase w = WidgetFactory.create(el.getAsJsonObject());
                    if (w instanceof WindowWidget ww) windows.add(ww);
                    else widgets.add(w);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void update() {
        long now = System.currentTimeMillis();
        deltaTime = (now - lastTime) / 1000f;
        lastTime = now;

        animations.update(deltaTime);

        for (var w : windows) updateRecursive(w, deltaTime);
        for (var w : widgets) updateRecursive(w, deltaTime);
    }

    private void updateRecursive(WidgetBase w, float dt) {
        w.update(dt);
        for (var c : w.children) updateRecursive(c, dt);
    }

    public void render(DrawContext ctx, int mouseX, int mouseY, float delta) {
        Theme theme = themeManager.getCurrent();
        TextRenderer textRenderer = MinecraftClient.getInstance().textRenderer;

        List<WidgetBase> toRender = new ArrayList<>();
        for (var w : windows) collectVisible(toRender, w);
        for (var w : widgets) collectVisible(toRender, w);
        toRender.sort(Comparator.comparingInt(w -> w.zIndex));

        for (var w : toRender) {
            renderWidget(ctx, textRenderer, w, mouseX, mouseY, delta, theme);
        }
    }

    private void collectVisible(List<WidgetBase> out, WidgetBase w) {
        if (!w.visible) return;
        out.add(w);
        for (var c : w.children) collectVisible(out, c);
    }

    private void renderWidget(DrawContext ctx, TextRenderer tr, WidgetBase w,
                               int mx, int my, float delta, Theme theme) {
        float ax = w.absoluteX(), ay = w.absoluteY();
        float ww = w.width, wh = w.height;

        switch (w.type) {
            case "Window" -> renderWindow(ctx, tr, (WindowWidget) w, mx, my, theme);
            case "Button" -> renderButton(ctx, tr, (ButtonWidget) w, mx, my, theme);
            case "Toggle" -> renderToggle(ctx, tr, (ToggleWidget) w, theme);
            case "Slider" -> renderSlider(ctx, tr, (SliderWidget) w, theme);
            case "Input" -> renderInput(ctx, tr, (InputWidget) w, theme);
            case "Label" -> renderLabel(ctx, tr, (LabelWidget) w, theme);
            case "ProgressBar" -> renderProgressBar(ctx, tr, (ProgressBarWidget) w, theme);
            case "Category" -> renderCategory(ctx, tr, (CategoryWidget) w, mx, my, theme);
            case "Separator" -> renderSeparator(ctx, w, theme);
            case "Notification" -> renderNotification(ctx, tr, (NotificationWidget) w, theme);
        }
    }

    private void renderWindow(DrawContext ctx, TextRenderer tr, WindowWidget w,
                               int mx, int my, Theme theme) {
        float ax = w.absoluteX(), ay = w.absoluteY();

        EffectsRenderer.drawShadow(ctx, ax, ay, w.width, w.height, theme);
        EffectsRenderer.drawRoundedRect(ctx, ax, ay, w.width, w.height, theme.surface, theme.borderRadius);
        EffectsRenderer.drawRoundedRect(ctx, ax, ay, w.width, w.titlebarHeight, theme.surfaceSecondary, theme.borderRadius);
        ctx.fill((int)ax, (int)(ay + w.titlebarHeight - 1), (int)(ax + w.width), (int)(ay + w.titlebarHeight), theme.border);

        int textW = tr.getWidth(Text.of(w.title));
        ctx.drawText(tr, Text.of(w.title), (int)(ax + theme.padding), (int)(ay + (w.titlebarHeight - 9)/2f), theme.text, true);

        if (w.closeable) {
            int cx = (int)(ax + w.width - 20);
            int col = mx >= cx && mx <= cx + 16 && my >= ay && my <= ay + 16 ? 0xFFE74C3C : 0xFF888888;
            ctx.drawText(tr, Text.of("X"), cx + 4, (int)(ay + 2), col, true);
        }
        if (w.minimizable) {
            int mx2 = (int)(ax + w.width - 44);
            ctx.drawText(tr, Text.of("_"), mx2 + 4, (int)(ay - 2), 0xFF888888, true);
        }

        if (w.tabs != null && !w.tabs.isEmpty()) {
            float tabX = ax + theme.padding;
            float tabY = ay + w.titlebarHeight + 2;
            for (TabWidget tab : w.tabs) {
                float tw = tr.getWidth(Text.of(tab.title)) + 16;
                int tabCol = tab.active || (tab == w.activeTab) ? theme.accent : theme.surfaceSecondary;
                EffectsRenderer.drawRoundedRect(ctx, tabX, tabY, tw, 18, tabCol, 2);
                ctx.drawText(tr, Text.of(tab.title), (int)(tabX + 8), (int)(tabY + 4), theme.text, false);
                tabX += tw + 4;
            }
        }

        if (!w.minimized) {
            for (var child : w.children) {
                if (child instanceof TabWidget) continue;
                renderWidget(ctx, tr, child, mx, my, 0, theme);
            }
        }
    }

    private void renderButton(DrawContext ctx, TextRenderer tr, ButtonWidget b,
                               int mx, int my, Theme theme) {
        float ax = b.absoluteX(), ay = b.absoluteY();
        int bg = b.state == WidgetBase.State.HOVER ? theme.accentHover : theme.accent;
        if (b.style.equals("danger")) bg = b.state == WidgetBase.State.HOVER ? 0xFFE74C3C : 0xFFC0392B;
        else if (b.style.equals("success")) bg = b.state == WidgetBase.State.HOVER ? 0xFF2ECC71 : 0xFF27AE60;
        else if (b.style.equals("warning")) bg = b.state == WidgetBase.State.HOVER ? 0xFFF39C12 : 0xFFE67E22;
        else if (b.style.equals("ghost")) bg = theme.surfaceSecondary;

        EffectsRenderer.drawRoundedRect(ctx, ax, ay, b.width, b.height, bg, b.rounded ? theme.borderRadius : 0);

        int textW = tr.getWidth(Text.of(b.label));
        ctx.drawText(tr, Text.of(b.label),
                (int)(ax + (b.width - textW) / 2f), (int)(ay + (b.height - 9) / 2f),
                theme.textAccent, false);
    }

    private void renderToggle(DrawContext ctx, TextRenderer tr, ToggleWidget tgl, Theme theme) {
        float ax = tgl.absoluteX(), ay = tgl.absoluteY();
        int labelW = tr.getWidth(Text.of(tgl.label));
        ctx.drawText(tr, Text.of(tgl.label), (int)ax, (int)(ay + 10), theme.text, false);

        float tx = ax + labelW + 12;
        float tw = 36, th = 18;
        int trackCol = tgl.value ? theme.toggleOn : theme.toggleOff;
        EffectsRenderer.drawRoundedRect(ctx, tx, ay + (tgl.height - th)/2f, tw, th, trackCol, th/2);

        float hx = tgl.value ? tx + tw - th : tx;
        ctx.fill((int)hx, (int)(ay + (tgl.height - th)/2f), (int)(hx + th), (int)(ay + (tgl.height + th)/2f), theme.sliderHandle);
    }

    private void renderSlider(DrawContext ctx, TextRenderer tr, SliderWidget sld, Theme theme) {
        float ax = sld.absoluteX(), ay = sld.absoluteY();

        int labelW = tr.getWidth(Text.of(sld.label));
        ctx.drawText(tr, Text.of(sld.label), (int)ax, (int)(ay + 6), theme.text, false);

        float sx = ax + labelW + 12;
        float sw = sld.width - labelW - 12 - (sld.showValue ? 40 : 0);
        float sy = ay + sld.height / 2f - 3;

        ctx.fill((int)sx, (int)sy, (int)(sx + sw), (int)(sy + 5), theme.sliderTrack);

        float fill = (float) sld.normalized() * sw;
        ctx.fill((int)sx, (int)sy, (int)(sx + fill), (int)(sy + 5), theme.sliderFill);

        float hx = sx + fill - 4;
        ctx.fill((int)hx, (int)(ay + sld.height/2f - 6), (int)(hx + 8), (int)(ay + sld.height/2f + 6), theme.sliderHandle);

        if (sld.showValue) {
            ctx.drawText(tr, Text.of(String.format("%.1f", sld.value)),
                    (int)(sx + sw + 6), (int)(ay + 6), theme.textSecondary, false);
        }
    }

    private void renderInput(DrawContext ctx, TextRenderer tr, InputWidget inp, Theme theme) {
        float ax = inp.absoluteX(), ay = inp.absoluteY();
        int borderCol = inp.state == WidgetBase.State.FOCUSED ? theme.borderFocus : theme.border;
        EffectsRenderer.drawOutline(ctx, ax, ay, inp.width, inp.height, borderCol, 1);
        ctx.fill((int)(ax + 1), (int)(ay + 1), (int)(ax + inp.width - 1), (int)(ay + inp.height - 1), theme.background);

        String display = inp.text.isEmpty() ? inp.placeholder : inp.text;
        int col = inp.text.isEmpty() ? theme.textSecondary : theme.text;
        ctx.drawText(tr, Text.of(display), (int)(ax + 6), (int)(ay + inp.height/2f - 4), col, false);

        if (inp.state == WidgetBase.State.FOCUSED && (System.currentTimeMillis() / 500) % 2 == 0) {
            int textW = tr.getWidth(Text.of(display));
            ctx.fill((int)(ax + 7 + textW), (int)(ay + 5), (int)(ax + 8 + textW), (int)(ay + inp.height - 5), theme.borderFocus);
        }
    }

    private void renderLabel(DrawContext ctx, TextRenderer tr, LabelWidget lbl, Theme theme) {
        float ax = lbl.absoluteX(), ay = lbl.absoluteY();
        ctx.drawText(tr, Text.of(lbl.text), (int)ax, (int)ay, theme.text, false);
    }

    private void renderProgressBar(DrawContext ctx, TextRenderer tr, ProgressBarWidget p, Theme theme) {
        float ax = p.absoluteX(), ay = p.absoluteY();
        ctx.fill((int)ax, (int)ay, (int)(ax + p.width), (int)(ay + p.height), theme.sliderTrack);

        float fill = (float) p.normalized() * p.width;
        ctx.fill((int)ax, (int)ay, (int)(ax + fill), (int)(ay + p.height), theme.sliderFill);

        if (p.showLabel) {
            String label = String.format("%.0f%%", p.normalized() * 100);
            int textW = tr.getWidth(Text.of(label));
            ctx.drawText(tr, Text.of(label),
                    (int)(ax + (p.width - textW) / 2f), (int)(ay + 2), theme.text, false);
        }
    }

    private void renderSeparator(DrawContext ctx, WidgetBase sep, Theme theme) {
        float ax = sep.absoluteX(), ay = sep.absoluteY();
        ctx.fill((int)ax, (int)ay, (int)(ax + sep.width), (int)(ay + sep.height), theme.border);
    }

    private void renderCategory(DrawContext ctx, TextRenderer tr, CategoryWidget cat,
                                 int mx, int my, Theme theme) {
        float ax = cat.absoluteX(), ay = cat.absoluteY();
        EffectsRenderer.drawRoundedRect(ctx, ax, ay, cat.width, cat.height, theme.surface, theme.borderRadius);
        EffectsRenderer.drawRoundedRect(ctx, ax, ay, cat.width, cat.headerHeight,
                theme.surfaceSecondary, theme.borderRadius);

        String expandIcon = cat.collapsed ? ">" : "v";
        ctx.drawText(tr, Text.of(expandIcon + "  " + cat.title),
                (int)(ax + 10), (int)(ay + cat.headerHeight/2f - 4), theme.text, false);

        if (!cat.collapsed) {
            for (var child : cat.children) {
                renderWidget(ctx, tr, child, mx, my, 0, theme);
            }
        }
    }

    private void renderNotification(DrawContext ctx, TextRenderer tr, NotificationWidget n, Theme theme) {
        float ax = n.absoluteX(), ay = n.absoluteY();
        int bg = switch (n.ntype) {
            case "success" -> 0xCC27AE60;
            case "warning" -> 0xCCE67E22;
            case "error" -> 0xCCC0392B;
            default -> 0xCC2980B9;
        };
        EffectsRenderer.drawRoundedRect(ctx, ax, ay, n.width, n.height, bg, theme.borderRadius);
        ctx.drawText(tr, Text.of(n.text), (int)(ax + 10), (int)(ay + 12), 0xFFFFFFFF, false);
    }

    // ---- INPUT HANDLING ----

    public boolean handleClick(double mx, double my, int button) {
        for (int i = windows.size() - 1; i >= 0; i--) {
            if (windows.get(i).handleClick(mx, my, button)) return true;
        }
        for (int i = widgets.size() - 1; i >= 0; i--) {
            if (widgets.get(i).handleClick(mx, my, button)) return true;
        }
        return false;
    }

    public boolean handleDrag(double mx, double my) {
        for (var w : windows) if (w.handleDrag(mx, my)) return true;
        for (var w : widgets) if (w.handleDrag(mx, my)) return true;
        return false;
    }

    public void handleDragEnd() {
        windows.forEach(WidgetBase::handleDragEnd);
        widgets.forEach(WidgetBase::handleDragEnd);
    }

    public void handleHover(double mx, double my) {
        for (var w : windows) w.handleHover(mx, my);
        for (var w : widgets) w.handleHover(mx, my);
    }

    public void handleChar(char c) {
        for (var w : windows) handleCharRecursive(w, c);
        for (var w : widgets) handleCharRecursive(w, c);
    }

    private void handleCharRecursive(WidgetBase w, char c) {
        if (w instanceof InputWidget inp) inp.handleChar(c);
        for (var child : w.children) handleCharRecursive(child, c);
    }

    public void handleKey(int key, int scancode, int mods) {
        for (var w : windows) handleKeyRecursive(w, key, scancode, mods);
        for (var w : widgets) handleKeyRecursive(w, key, scancode, mods);
    }

    private void handleKeyRecursive(WidgetBase w, int key, int scancode, int mods) {
        if (w instanceof InputWidget inp) inp.handleKey(key, scancode, mods);
        for (var child : w.children) handleKeyRecursive(child, key, scancode, mods);
    }

    public String serializeState() {
        JsonObject root = new JsonObject();
        JsonArray widgetArr = new JsonArray();
        for (var w : widgets) widgetArr.add(w.toJson());
        JsonArray winArr = new JsonArray();
        for (var w : windows) winArr.add(w.toJson());
        root.add("widgets", widgetArr);
        root.add("windows", winArr);
        return root.toString();
    }
}
