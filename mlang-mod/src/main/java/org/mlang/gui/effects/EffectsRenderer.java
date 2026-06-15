package org.mlang.gui.effects;

import net.minecraft.client.gui.DrawContext;
import org.mlang.gui.theme.Theme;

public class EffectsRenderer {

    public static void drawShadow(DrawContext ctx, float x, float y, float w, float h, Theme theme) {
        int shadow = theme.shadow;
        int r = theme.shadowRadius;
        float opacity = theme.shadowOpacity;

        for (int i = 0; i < r; i++) {
            float a = opacity * (1f - (float)i / r) * 0.3f;
            int col = (shadow & 0x00FFFFFF) | (((int)(a * 255)) << 24);
            ctx.fill((int)(x - i), (int)(y - i + 2), (int)(x + w + i), (int)(y + h + i), col);
        }
    }

    public static void drawGlow(DrawContext ctx, float x, float y, float w, float h, int glowColor, float glowOpacity) {
        int r = 6;
        for (int i = 0; i < r; i++) {
            float a = glowOpacity * (1f - (float)i / r) * 0.5f;
            int col = (glowColor & 0x00FFFFFF) | (((int)(a * 255)) << 24);
            ctx.fill((int)(x - i), (int)(y - i), (int)(x + w + i), (int)(y + h + i), col);
        }
    }

    public static void drawBlurOverlay(DrawContext ctx, float x, float y, float w, float h, Theme theme) {
        float a = theme.blurOpacity;
        int col = (theme.background & 0x00FFFFFF) | (((int)(a * 255)) << 24);
        ctx.fill((int)x, (int)y, (int)(x + w), (int)(y + h), col);
    }

    public static void drawGradient(DrawContext ctx, float x, float y, float w, float h,
                                     int colStart, int colEnd, float alpha) {
        for (int row = 0; row < h; row++) {
            float t = (float) row / h;
            int r = lerp((colStart >> 16) & 0xFF, (colEnd >> 16) & 0xFF, t);
            int g = lerp((colStart >> 8) & 0xFF, (colEnd >> 8) & 0xFF, t);
            int b = lerp(colStart & 0xFF, colEnd & 0xFF, t);
            int a = (int)(alpha * 255);
            int col = (a << 24) | (r << 16) | (g << 8) | b;
            ctx.fill((int)x, (int)(y + row), (int)(x + w), (int)(y + row + 1), col);
        }
    }

    public static void drawRoundedRect(DrawContext ctx, float x, float y, float w, float h,
                                        int color, int radius) {
        if (radius <= 0) {
            ctx.fill((int)x, (int)y, (int)(x + w), (int)(y + h), color);
            return;
        }
        int r = Math.min(radius, (int)Math.min(w / 2, h / 2));

        ctx.fill((int)(x + r), (int)y, (int)(x + w - r), (int)(y + r), color);
        ctx.fill((int)x, (int)(y + r), (int)(x + w), (int)(y + h - r), color);
        ctx.fill((int)(x + r), (int)(y + h - r), (int)(x + w - r), (int)(y + h), color);
        ctx.fill((int)x, (int)(y + r), (int)(x + r), (int)(y + h - r), color);
        ctx.fill((int)(x + w - r), (int)(y + r), (int)(x + w), (int)(y + h - r), color);

        drawArc(ctx, x + r, y + r, r, color, 180, 270);
        drawArc(ctx, x + w - r - 1, y + r, r, color, 270, 360);
        drawArc(ctx, x + r, y + h - r - 1, r, color, 90, 180);
        drawArc(ctx, x + w - r - 1, y + h - r - 1, r, color, 0, 90);
    }

    private static void drawArc(DrawContext ctx, float cx, float cy, int r, int color, int startDeg, int endDeg) {
        for (int dy = 0; dy <= r; dy++) {
            int dx = (int) Math.sqrt(r * r - dy * dy);
            for (int x = (int)cx - dx; x <= cx + dx; x++) {
                double angle = Math.toDegrees(Math.atan2((cy) - (cy - dy), x - cx));
                if (angle < 0) angle += 360;
                if (angle >= startDeg && angle <= endDeg) {
                    if (x >= 0 && (cy - dy) >= 0) ctx.fill(x, (int)(cy - dy), x + 1, (int)(cy - dy + 1), color);
                }
            }
            for (int x = (int)cx - dx; x <= cx + dx; x++) {
                double angle = Math.toDegrees(Math.atan2((cy + dy) - cy, x - cx));
                if (angle < 0) angle += 360;
                if (angle >= startDeg && angle <= endDeg) {
                    if (x >= 0 && (cy + dy) >= 0) ctx.fill(x, (int)(cy + dy), x + 1, (int)(cy + dy + 1), color);
                }
            }
        }
    }

    public static void drawOutline(DrawContext ctx, float x, float y, float w, float h, int color, int thickness) {
        for (int t = 0; t < thickness; t++) {
            ctx.drawHorizontalLine((int)x, (int)(x + w - 1), (int)(y + t), color);
            ctx.drawHorizontalLine((int)x, (int)(x + w - 1), (int)(y + h - 1 - t), color);
            ctx.drawVerticalLine((int)(x + t), (int)y, (int)(y + h - 1), color);
            ctx.drawVerticalLine((int)(x + w - 1 - t), (int)y, (int)(y + h - 1), color);
        }
    }

    private static int lerp(int a, int b, float t) {
        return Math.round(a + (b - a) * t);
    }
}
