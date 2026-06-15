package org.mlang.gui.animation;

import net.minecraft.util.math.MathHelper;
import org.mlang.gui.widgets.WidgetBase;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class AnimationEngine {
    private final List<Animation> animations = new ArrayList<>();

    public Animation animate(WidgetBase widget, String type, int durationMs) {
        Animation anim = new Animation(widget, type, durationMs);
        anim.start();
        animations.add(anim);
        return anim;
    }

    public void animateLoop(WidgetBase widget, String type, int durationMs) {
        Animation anim = new Animation(widget, type, durationMs);
        anim.loop = true;
        anim.start();
        animations.add(anim);
    }

    public void update(float delta) {
        float dt = delta * 1000f;
        Iterator<Animation> it = animations.iterator();
        while (it.hasNext()) {
            Animation anim = it.next();
            if (!anim.run(dt)) {
                if (anim.loop) {
                    anim.restart();
                } else {
                    it.remove();
                }
            }
        }
    }

    public static class Animation {
        public final WidgetBase widget;
        public final String type;
        public final int durationMs;
        public float progress = 0;
        public boolean loop = false;
        private long startTime;

        public Animation(WidgetBase widget, String type, int durationMs) {
            this.widget = widget;
            this.type = type;
            this.durationMs = durationMs;
        }

        public void start() {
            startTime = System.currentTimeMillis();
            progress = 0;
        }

        public void restart() {
            startTime = System.currentTimeMillis();
            progress = 0;
            // Reverse for continuous animations
            switch (type) {
                case "pulse":
                    widget.animOpacity = widget.animOpacity < 0.5f ? 1.0f : 0.0f;
                    break;
                case "shake":
                    widget.animX = widget.animX > 0 ? -5 : 5;
                    break;
            }
        }

        public boolean run(float dt) {
            long elapsed = System.currentTimeMillis() - startTime;
            progress = MathHelper.clamp((float) elapsed / durationMs, 0f, 1f);
            float t = easeOut(progress);

            switch (type) {
                case "fadeIn":
                    widget.opacity = MathHelper.lerp(0f, 1f, t);
                    break;
                case "fadeOut":
                    widget.opacity = MathHelper.lerp(1f, 0f, t);
                    break;
                case "slideDown":
                    widget.animY = MathHelper.lerp(-30f, 0f, t);
                    break;
                case "slideLeft":
                    widget.animX = MathHelper.lerp(50f, 0f, t);
                    break;
                case "bounceIn":
                    float b = bounce(progress);
                    widget.animScale = MathHelper.lerp(0.3f, 1f, b);
                    widget.opacity = MathHelper.lerp(0f, 1f, t);
                    break;
                case "zoomIn":
                    widget.animScale = MathHelper.lerp(0.5f, 1f, t);
                    widget.opacity = MathHelper.lerp(0f, 1f, t);
                    break;
                case "pulse":
                    float p = (float) (Math.sin(progress * Math.PI * 2) * 0.5 + 0.5);
                    widget.animOpacity = MathHelper.lerp(0.5f, 1f, p);
                    break;
                case "shake":
                    widget.animX = (float) (Math.sin(progress * 16) * 4 * (1 - progress));
                    break;
                case "rainbow":
                    widget.animScale = (progress * 2) % 1f;
                    break;
            }
            return progress < 1f;
        }

        private float easeOut(float t) {
            return 1f - (1f - t) * (1f - t);
        }

        private float bounce(float t) {
            return (float) (1.0 - Math.pow(1.0 - t, 3) * Math.cos(t * Math.PI * 4.5));
        }
    }
}
