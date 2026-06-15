package org.mlang.gui;

import net.minecraft.client.MinecraftClient;
import net.minecraft.client.gui.DrawContext;
import net.minecraft.client.gui.screen.Screen;
import net.minecraft.text.Text;
import org.lwjgl.glfw.GLFW;

public class GuiScreen extends Screen {
    private final GuiRenderer renderer;
    private boolean pauseGame = false;

    public GuiScreen(GuiRenderer renderer) {
        super(Text.literal(""));
        this.renderer = renderer;
    }

    public GuiScreen(GuiRenderer renderer, boolean pauseGame) {
        super(Text.literal(""));
        this.renderer = renderer;
        this.pauseGame = pauseGame;
    }

    @Override
    public boolean shouldPause() {
        return pauseGame;
    }

    @Override
    public boolean shouldCloseOnEsc() {
        return true;
    }

    @Override
    protected void init() {
        super.init();
    }

    @Override
    public void render(DrawContext ctx, int mouseX, int mouseY, float delta) {
        renderer.update();
        renderer.render(ctx, mouseX, mouseY, delta);
        super.render(ctx, mouseX, mouseY, delta);
    }

    @Override
    public boolean mouseClicked(double mouseX, double mouseY, int button) {
        boolean handled = renderer.handleClick(mouseX, mouseY, button);
        if (handled) return true;
        return super.mouseClicked(mouseX, mouseY, button);
    }

    @Override
    public boolean mouseReleased(double mouseX, double mouseY, int button) {
        renderer.handleDragEnd();
        return super.mouseReleased(mouseX, mouseY, button);
    }

    @Override
    public boolean mouseDragged(double mouseX, double mouseY, int button, double deltaX, double deltaY) {
        boolean handled = renderer.handleDrag(mouseX, mouseY);
        if (handled) return true;
        return super.mouseDragged(mouseX, mouseY, button, deltaX, deltaY);
    }

    @Override
    public void mouseMoved(double mouseX, double mouseY) {
        renderer.handleHover(mouseX, mouseY);
        super.mouseMoved(mouseX, mouseY);
    }

    @Override
    public boolean charTyped(char chr, int modifiers) {
        renderer.handleChar(chr);
        return true;
    }

    @Override
    public boolean keyPressed(int keyCode, int scanCode, int modifiers) {
        if (keyCode == GLFW.GLFW_KEY_ESCAPE) {
            MinecraftClient.getInstance().setScreen(null);
            return true;
        }
        renderer.handleKey(keyCode, scanCode, modifiers);
        return true;
    }

    @Override
    public void close() {
        super.close();
    }

    @Override
    public void tick() {
        renderer.update();
        super.tick();
    }
}
