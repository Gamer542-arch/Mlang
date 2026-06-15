package org.mlang.gui.theme;

public class Theme {
    public String name = "dark";

    public int background = 0xFF0D0D0D;
    public int surface = 0xFF1A1A2E;
    public int surfaceSecondary = 0xFF16213E;
    public int accent = 0xFFE94560;
    public int accentHover = 0xFFFF6B81;
    public int text = 0xFFEAEAEA;
    public int textSecondary = 0xFF8A8A9A;
    public int textAccent = 0xFFFFFFFF;
    public int border = 0xFF2A2A4A;
    public int borderFocus = 0xFFE94560;
    public int shadow = 0x80000000;

    public int success = 0xFF2ECC71;
    public int warning = 0xFFF39C12;
    public int error = 0xFFE74C3C;
    public int info = 0xFF3498DB;

    public int sliderTrack = 0xFF2A2A4A;
    public int sliderFill = 0xFFE94560;
    public int sliderHandle = 0xFFFFFFFF;
    public int toggleOff = 0xFF2A2A4A;
    public int toggleOn = 0xFFE94560;

    public int blurRadius = 10;
    public float blurOpacity = 0.85f;
    public int borderRadius = 4;
    public int borderWidth = 1;
    public int shadowRadius = 8;
    public float shadowOpacity = 0.5f;
    public int fontSize = 10;
    public int widgetHeight = 28;
    public int titlebarHeight = 32;
    public int padding = 8;

    public static final Theme DARK = new Theme();
    public static final Theme LIGHT = initLight();
    public static final Theme MINECRAFT = initMC();
    public static final Theme GLASS = initGlass();
    public static final Theme NEON = initNeon();
    public static final Theme MINIMAL = initMinimal();
    public static final Theme FUTURE = initFuture();

    private static Theme initLight() {
        Theme t = new Theme();
        t.name = "light";
        t.background = 0xFFF5F5F5; t.surface = 0xFFFFFFFF;
        t.surfaceSecondary = 0xFFE8E8E8; t.accent = 0xFFE94560;
        t.text = 0xFF1A1A2E; t.textSecondary = 0xFF666666;
        t.border = 0xFFD0D0D0; t.borderFocus = 0xFFE94560;
        t.shadow = 0x20000000;
        return t;
    }

    private static Theme initMC() {
        Theme t = new Theme();
        t.name = "minecraft";
        t.background = 0xFF1A1A1A; t.surface = 0xFF2B2B2B;
        t.surfaceSecondary = 0xFF3C3C3C; t.accent = 0xFF55FF55;
        t.accentHover = 0xFF77FF77;
        t.text = 0xFFFFFFFF; t.textSecondary = 0xFFAAAAAA;
        t.border = 0xFF555555; t.borderFocus = 0xFF55FF55;
        t.borderRadius = 0; t.shadowRadius = 4;
        return t;
    }

    private static Theme initGlass() {
        Theme t = new Theme();
        t.name = "glass";
        t.background = 0x20000000; t.surface = 0x20FFFFFF;
        t.surfaceSecondary = 0x15FFFFFF; t.accent = 0xFF00FFC8;
        t.accentHover = 0xFF33FFD4;
        t.text = 0xFFFFFFFF; t.textSecondary = 0xCCAAAAAA;
        t.border = 0x30FFFFFF; t.borderFocus = 0xFF00FFC8;
        t.blurRadius = 15; t.blurOpacity = 0.65f;
        t.borderRadius = 6;
        return t;
    }

    private static Theme initNeon() {
        Theme t = new Theme();
        t.name = "neon";
        t.background = 0xFF08080F; t.surface = 0xFF12121F;
        t.surfaceSecondary = 0xFF1A1A30; t.accent = 0xFFFF00FF;
        t.accentHover = 0xFFFF44FF;
        t.text = 0xFFFFFFFF; t.textSecondary = 0xFF8888AA;
        t.border = 0xFF303050; t.borderFocus = 0xFFFF00FF;
        t.sliderFill = 0xFFFF00FF; t.toggleOn = 0xFFFF00FF;
        t.borderRadius = 2; t.blurOpacity = 0.9f;
        return t;
    }

    private static Theme initMinimal() {
        Theme t = new Theme();
        t.name = "minimal";
        t.background = 0xFF111111; t.surface = 0xFF1E1E1E;
        t.surfaceSecondary = 0xFF282828; t.accent = 0xFFFFFFFF;
        t.text = 0xFFFFFFFF; t.textSecondary = 0xFF888888;
        t.border = 0xFF333333; t.borderFocus = 0xFFFFFFFF;
        t.borderRadius = 0; t.shadowRadius = 4;
        return t;
    }

    private static Theme initFuture() {
        Theme t = new Theme();
        t.name = "future";
        t.background = 0xFF0A0A0A; t.surface = 0xFF141414;
        t.surfaceSecondary = 0xFF1E1E1E; t.accent = 0xFF00BFFF;
        t.accentHover = 0xFF33CCFF;
        t.text = 0xFFF0F0F0; t.textSecondary = 0xFF808088;
        t.border = 0xFF282828; t.borderFocus = 0xFF00BFFF;
        t.sliderFill = 0xFF00BFFF; t.toggleOn = 0xFF00BFFF;
        t.borderRadius = 2;
        return t;
    }
}
