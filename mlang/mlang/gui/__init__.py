"""MLang GUI System — cheat-client style GUI framework."""

from .themes import Theme, get_theme, register_theme, BUILTIN_THEMES
from .widgets import (
    Widget, Button, Toggle, Slider, Input, Label, ProgressBar,
    Dropdown, ColorPicker, Separator, Category, Window, Tab,
    Hotbar, Minimap, Notification, Tooltip, ContextMenu, Image,
    WidgetState,
)
from .window import WindowManager
from .layout import Layout, LayoutDirection, LayoutAlign
from .animations import Animation, AnimationManager, Easing, ColorTween, Tween, apply_easing
from .effects import VisualState, BlurEffect, ShadowEffect, GlowEffect, GradientOverlay
from .renderer import ConsoleRenderer, serialize_widget, serialize_gui_state

__all__ = [
    # Themes
    "Theme", "get_theme", "register_theme",
    # Widgets
    "Widget", "Button", "Toggle", "Slider", "Input", "Label",
    "ProgressBar", "Dropdown", "ColorPicker", "Separator",
    "Category", "Window", "Tab", "Hotbar", "Minimap",
    "Notification", "Tooltip", "ContextMenu", "Image",
    "WidgetState",
    # Manager
    "WindowManager",
    # Layout
    "Layout", "LayoutDirection", "LayoutAlign",
    # Animations
    "Animation", "AnimationManager", "Easing", "ColorTween", "Tween", "apply_easing",
    # Effects
    "VisualState", "BlurEffect", "ShadowEffect", "GlowEffect", "GradientOverlay",
    # Renderer
    "ConsoleRenderer", "serialize_widget", "serialize_gui_state",
]
