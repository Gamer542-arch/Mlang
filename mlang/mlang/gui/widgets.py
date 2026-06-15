"""GUI Widget System — all interactive and display widgets."""

from __future__ import annotations
import math
import time
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Callable, Optional, Union

from .effects import VisualState, get_effect_preset, blend_colors
from .animations import Animation, AnimationManager, Easing, apply_easing


class WidgetState(Enum):
    NORMAL = auto()
    HOVER = auto()
    ACTIVE = auto()
    DISABLED = auto()
    FOCUSED = auto()


class Widget:
    """Base class for all GUI widgets."""

    def __init__(self, name: str = "", **kwargs):
        self.name = name
        self.parent: Optional[Widget] = None
        self.children: list[Widget] = []
        self.visible: bool = True
        self.enabled: bool = True
        self.state: WidgetState = WidgetState.NORMAL

        # Position & size
        self.x: float = 0.0
        self.y: float = 0.0
        self.width: float = 100.0
        self.height: float = 28.0
        self.z_index: int = 0

        # Visual
        self.color: str = ""
        self.text_color: str = ""
        self.border_color: str = ""
        self.opacity: float = 1.0
        self.background_color: str = ""
        self.visual_state: VisualState = VisualState.default()
        self.tooltip_text: str = ""

        # Draggable
        self.draggable: bool = False
        self._dragging: bool = False
        self._drag_start_x: float = 0.0
        self._drag_start_y: float = 0.0

        # Animation
        self.animations: list[Animation] = []
        self.anim_opacity: float = 1.0  # animated opacity
        self.anim_x: float = 0.0
        self.anim_y: float = 0.0
        self.anim_scale: float = 1.0
        self.anim_color_progress: float = 0.0

        # Styles (applied from theme)
        self.style_class: str = ""

        # Callbacks
        self.on_click: Optional[Callable] = None
        self.on_right_click: Optional[Callable] = None
        self.on_hover_enter: Optional[Callable] = None
        self.on_hover_leave: Optional[Callable] = None
        self.on_drag_start: Optional[Callable] = None
        self.on_drag: Optional[Callable] = None
        self.on_drag_end: Optional[Callable] = None

        # Styles (applied from theme)
        self.style_class: str = ""

        # Apply kwargs after all attributes initialized
        self._apply_kwargs(kwargs)

    def _apply_kwargs(self, kwargs: dict):
        for k, v in kwargs.items():
            if hasattr(self, k) and not k.startswith("_"):
                setattr(self, k, v)

    def add(self, *widgets: Widget):
        for w in widgets:
            w.parent = self
            self.children.append(w)

    def remove(self, widget: Widget):
        if widget in self.children:
            self.children.remove(widget)

    def find(self, name: str) -> Optional[Widget]:
        if self.name == name:
            return self
        for child in self.children:
            result = child.find(name)
            if result:
                return result
        return None

    @property
    def absolute_x(self) -> float:
        base = self.parent.absolute_x if self.parent else 0.0
        return base + self.x

    @property
    def absolute_y(self) -> float:
        base = self.parent.absolute_y if self.parent else 0.0
        return base + self.y

    def contains(self, px: float, py: float) -> bool:
        ax, ay = self.absolute_x, self.absolute_y
        return ax <= px <= ax + self.width and ay <= py <= ay + self.height

    def handle_click(self, x: float, y: float, button: int = 0) -> bool:
        if not self.visible or not self.enabled:
            return False
        if self.contains(x, y):
            if self.draggable and button == 0:
                self._dragging = True
                self._drag_start_x = x - self.x
                self._drag_start_y = y - self.y
                if self.on_drag_start:
                    self.on_drag_start(x, y)
            if button == 0 and self.on_click:
                self.on_click()
            elif button == 1 and self.on_right_click:
                self.on_right_click()
            return True
        return False

    def handle_drag(self, x: float, y: float) -> bool:
        if self._dragging and self.draggable:
            self.x = x - self._drag_start_x
            self.y = y - self._drag_start_y
            if self.on_drag:
                self.on_drag(self.x, self.y)
            return True
        return False

    def handle_drag_end(self) -> bool:
        if self._dragging:
            self._dragging = False
            if self.on_drag_end:
                self.on_drag_end(self.x, self.y)
            return True
        return False

    def handle_hover(self, x: float, y: float) -> bool:
        if not self.visible or not self.enabled:
            return False
        was_hovering = self.state == WidgetState.HOVER
        is_hovering = self.contains(x, y)
        if is_hovering and not was_hovering:
            self.state = WidgetState.HOVER
            if self.on_hover_enter:
                self.on_hover_enter()
        elif not is_hovering and was_hovering:
            self.state = WidgetState.NORMAL
            if self.on_hover_leave:
                self.on_hover_leave()
        return is_hovering

    def animate(self, anim_type: str, duration_ms: int = 200, easing: Easing = Easing.EASE_OUT) -> "Animation":
        if anim_type == "fadeIn":
            self.opacity = 0.0
            anim = Animation(self, duration_ms, easing).tween("opacity", 1.0)
        elif anim_type == "slideDown":
            start_y = self.y - 30
            self.y = start_y
            anim = Animation(self, duration_ms, easing).tween("y", start_y + 30)
        elif anim_type == "slideLeft":
            start_x = self.x + 50
            self.x = start_x
            anim = Animation(self, duration_ms, easing).tween("x", start_x - 50)
        elif anim_type == "bounceIn":
            self.anim_scale = 0.3
            self.opacity = 0.0
            anim = Animation(self, duration_ms, Easing.BOUNCE)
            anim.tween("anim_scale", 1.0)
            anim.tween("opacity", 1.0)
        elif anim_type == "zoomIn":
            self.anim_scale = 0.5
            self.opacity = 0.0
            anim = Animation(self, duration_ms, easing).tween("anim_scale", 1.0).tween("opacity", 1.0)
        else:
            anim = Animation(self, duration_ms, easing)
        self.animations.append(anim)
        return anim

    def animate_loop(self, anim_type: str, duration_ms: int = 1000):
        if anim_type == "pulse":
            anim = Animation(self, duration_ms, Easing.EASE_IN_OUT)
            anim.tween("opacity", 0.5)
            anim.on_complete = lambda: self.animate_loop("pulse", duration_ms)
        elif anim_type == "shake":
            anim = Animation(self, duration_ms // 2, Easing.LINEAR)
            anim.tween("x", self.x + 5)
            anim2 = Animation(self, duration_ms // 2, Easing.LINEAR)
            anim2.tween("x", self.x)
            anim.on_complete = lambda: self.animate_loop("shake", duration_ms)
        elif anim_type == "rainbow":
            self.anim_color_progress = 0.0
            anim = Animation(self, duration_ms, Easing.LINEAR)
            anim.tween("anim_color_progress", 1.0)
            anim.on_complete = lambda: self.animate_loop("rainbow", duration_ms)
        self.animations.append(anim)

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r})"


# ===== INTERACTIVE WIDGETS =====


class Button(Widget):
    """Clickable button with hover/active effects."""

    def __init__(self, label: str = "Button", icon: str = "", **kwargs):
        super().__init__()
        self.label: str = label
        self.icon: str = icon
        self.style: str = "default"  # default, danger, success, warning, ghost
        self.rounded: bool = True
        self.bindable_key: str = ""  # keyboard shortcut
        self.height = 32
        self.width = 100
        self._apply_kwargs(kwargs)

    @property
    def computed_color(self) -> str:
        if self.state == WidgetState.ACTIVE:
            return "#FF6B81"
        if self.state == WidgetState.HOVER:
            return "#FF6B81"
        return "#E94560"


class Toggle(Widget):
    """ON/OFF toggle switch."""

    def __init__(self, label: str = "Toggle", **kwargs):
        super().__init__()
        self.label: str = label
        self.value: bool = False
        self.on_label: str = "ON"
        self.off_label: str = "OFF"
        self.bindable_key: str = ""
        self.on_change: Optional[Callable[[bool], None]] = None
        self.width = 120
        self.height = 28
        self._apply_kwargs(kwargs)

    def toggle(self):
        self.value = not self.value
        if self.on_change:
            self.on_change(self.value)
        if self.on_click:
            self.on_click()

    def handle_click(self, x, y, button=0):
        if super().handle_click(x, y, button):
            self.toggle()
            return True
        return False


class Slider(Widget):
    """Draggable slider for numeric values."""

    def __init__(self, label: str = "Slider", **kwargs):
        super().__init__()
        self.label: str = label
        self.min: float = 0.0
        self.max: float = 100.0
        self.step: float = 1.0
        self.value: float = 50.0
        self.show_value: bool = True
        self.format_str: str = "{0:F1}"
        self.on_change: Optional[Callable[[float], None]] = None
        self.width = 200
        self.height = 28
        self._sliding: bool = False
        self._apply_kwargs(kwargs)

    @property
    def normalized(self) -> float:
        if self.max == self.min:
            return 0.0
        return (self.value - self.min) / (self.max - self.min)

    @property
    def handle_x(self) -> float:
        return self.normalized * (self.width - 16)

    def set_from_normalized(self, t: float):
        t = max(0.0, min(1.0, t))
        raw = self.min + t * (self.max - self.min)
        if self.step > 0:
            raw = round(raw / self.step) * self.step
        self.value = max(self.min, min(self.max, raw))
        if self.on_change:
            self.on_change(self.value)

    def handle_click(self, x, y, button=0):
        if not self.visible or not self.enabled:
            return False
        ax = self.absolute_x
        if self.contains(x, y) or self._sliding:
            rel_x = x - ax
            self.set_from_normalized(rel_x / self.width)
            self._sliding = True
            return True
        return False

    def handle_drag(self, x, y):
        if self._sliding:
            ax = self.absolute_x
            rel_x = x - ax
            self.set_from_normalized(rel_x / self.width)
            return True
        return False

    def handle_drag_end(self):
        self._sliding = False
        return True


class Input(Widget):
    """Text input field."""

    def __init__(self, placeholder: str = "Type here...", **kwargs):
        super().__init__()
        self.placeholder: str = placeholder
        self.text: str = ""
        self.max_length: int = 0  # 0 = unlimited
        self.input_type: str = "text"  # text, number, password
        self.on_change: Optional[Callable[[str], None]] = None
        self.on_enter: Optional[Callable[[str], None]] = None
        self.on_focus: Optional[Callable] = None
        self.on_blur: Optional[Callable] = None
        self.cursor_pos: int = 0
        self.width = 200
        self.height = 28
        self._apply_kwargs(kwargs)

    def focus(self):
        self.state = WidgetState.FOCUSED
        if self.on_focus:
            self.on_focus()

    def blur(self):
        self.state = WidgetState.NORMAL
        if self.on_blur:
            self.on_blur()

    def handle_click(self, x, y, button=0):
        if super().handle_click(x, y, button):
            self.focus()
            return True
        self.blur()
        return False


class Label(Widget):
    """Static text label."""

    def __init__(self, text: str = "Label", **kwargs):
        super().__init__()
        self.text: str = text
        self.text_align: str = "left"
        self.font_size: int = 10
        self.bold: bool = False
        self.italic: bool = False
        self.height = 20
        self._apply_kwargs(kwargs)


class ProgressBar(Widget):
    """Progress / loading bar."""

    def __init__(self, **kwargs):
        super().__init__()
        self.min: float = 0.0
        self.max: float = 100.0
        self.value: float = 50.0
        self.show_label: bool = True
        self.label_format: str = "{0:F0}%"
        self.indeterminate: bool = False
        self.width = 200
        self.height = 16
        self._apply_kwargs(kwargs)

    @property
    def normalized(self) -> float:
        if self.max == self.min:
            return 0.0
        return max(0.0, min(1.0, (self.value - self.min) / (self.max - self.min)))


class Dropdown(Widget):
    """Dropdown selection list."""

    def __init__(self, label: str = "Select", **kwargs):
        super().__init__()
        self.label: str = label
        self.options: list[str] = []
        self.selected_index: int = -1
        self._expanded: bool = False
        self.on_select: Optional[Callable[[int, str], None]] = None
        self.width = 180
        self.height = 28
        self._apply_kwargs(kwargs)

    @property
    def selected_value(self) -> Optional[str]:
        if 0 <= self.selected_index < len(self.options):
            return self.options[self.selected_index]
        return None

    @property
    def expanded(self) -> bool:
        return self._expanded

    def toggle_expand(self):
        self._expanded = not self._expanded

    def select(self, index: int):
        if 0 <= index < len(self.options):
            self.selected_index = index
            self._expanded = False
            if self.on_select:
                self.on_select(index, self.options[index])


class ColorPicker(Widget):
    """Color picker widget."""

    def __init__(self, **kwargs):
        super().__init__()
        self.color: str = "#E94560"
        self.on_change: Optional[Callable[[str], None]] = None
        self.width = 200
        self.height = 150
        self._mode: str = "hex"  # hex, rgb, hsl
        self._apply_kwargs(kwargs)

    def set_color(self, hex_color: str):
        self.color = hex_color
        if self.on_change:
            self.on_change(hex_color)


# ===== CONTAINER WIDGETS =====


class Separator(Widget):
    """Horizontal or vertical line separator."""

    def __init__(self, **kwargs):
        super().__init__()
        self.orientation: str = "horizontal"
        self.color: str = "#2A2A4A"
        self.thickness: int = 1
        if self.orientation == "horizontal":
            self.width = 200
            self.height = 1
        else:
            self.width = 1
            self.height = 200
        self._apply_kwargs(kwargs)


class Category(Widget):
    """Collapsible category container with header."""

    def __init__(self, title: str = "Category", **kwargs):
        super().__init__()
        self.title: str = title
        self.collapsible: bool = True
        self.collapsed: bool = False
        self.header_height: int = 28
        self.width = 300
        self.height = 200
        self._apply_kwargs(kwargs)

    @property
    def body_height(self) -> float:
        if self.collapsed:
            return 0.0
        return sum(max(c.y + c.height for c in self.children) if self.children else 0.0,
                   self.height - self.header_height)

    def toggle_collapse(self):
        self.collapsed = not self.collapsed

    def handle_click(self, x, y, button=0):
        ax, ay = self.absolute_x, self.absolute_y
        if ax <= x <= ax + self.width and ay <= y <= ay + self.header_height:
            if self.collapsible:
                self.toggle_collapse()
            if self.on_click:
                self.on_click()
            return True
        if not self.collapsed:
            return super().handle_click(x, y, button)
        return False


class Tab(Widget):
    """Single tab within a Window."""

    def __init__(self, title: str = "Tab", **kwargs):
        super().__init__()
        self.title: str = title
        self.icon: str = ""
        self.active: bool = False
        self._apply_kwargs(kwargs)


class Window(Widget):
    """Floating window with title bar, close/minimize, and tabs."""

    def __init__(self, title: str = "Window", **kwargs):
        super().__init__()
        self.title: str = title
        self.resizable: bool = True
        self.closeable: bool = True
        self.minimizable: bool = True
        self.minimized: bool = False
        self.tabs: list[Tab] = []
        self.active_tab: Optional[Tab] = None
        self.width = 400
        self.height = 300
        self.titlebar_height: int = 32
        self.min_width: int = 200
        self.min_height: int = 100
        self.max_width: int = 0
        self.max_height: int = 0
        self.on_close: Optional[Callable] = None
        self.draggable = True
        self._apply_kwargs(kwargs)

    def add_tab(self, tab: Tab):
        self.tabs.append(tab)
        self.add(tab)
        if self.active_tab is None:
            self.active_tab = tab

    def switch_tab(self, tab_name: str):
        for tab in self.tabs:
            tab.active = False
            if tab.title == tab_name or tab.name == tab_name:
                tab.active = True
                self.active_tab = tab

    def close(self):
        if self.on_close:
            self.on_close()
        self.visible = False

    def center_on_screen(self, screen_w: int = 1920, screen_h: int = 1080):
        self.x = (screen_w - self.width) / 2
        self.y = (screen_h - self.height) / 2

    def handle_click(self, x, y, button=0):
        ax, ay = self.absolute_x, self.absolute_y
        # Title bar close/minimize buttons
        if self.closeable and ax + self.width - 20 <= x <= ax + self.width and ay <= y <= ay + 20:
            self.close()
            return True
        if self.minimizable and ax + self.width - 40 <= x <= ax + self.width - 20 and ay <= y <= ay + 20:
            self.minimized = not self.minimized
            return True
        return super().handle_click(x, y, button)


# ===== SPECIAL WIDGETS =====


class Hotbar(Widget):
    """Horizontal hotbar with numbered slots (like Minecraft)."""

    def __init__(self, **kwargs):
        super().__init__()
        self.slots: list[Optional[str]] = [None] * 9
        self.selected_slot: int = 0
        self.width = 200
        self.height = 28
        self.slot_size: int = 22
        self._apply_kwargs(kwargs)

    def select(self, index: int):
        if 0 <= index < 9:
            self.selected_slot = index


class Minimap(Widget):
    """Simple minimap display widget."""

    def __init__(self, **kwargs):
        super().__init__()
        self.width = 120
        self.height = 120
        self.zoom: float = 1.0
        self.center_x: float = 0.0
        self.center_z: float = 0.0
        self.show_player: bool = True
        self.show_entities: bool = False
        self.rotation: float = 0.0
        self._apply_kwargs(kwargs)


class Notification(Widget):
    """Popup notification that auto-dismisses."""

    def __init__(self, text: str = "", **kwargs):
        super().__init__()
        self.text: str = text
        self.duration_ticks: int = 60  # ~3 seconds
        self.type: str = "info"  # info, success, warning, error
        self._start_time: float = 0.0
        self._dismissed: bool = False
        self.width = 250
        self.height = 40
        self._apply_kwargs(kwargs)

    def show(self):
        self.visible = True
        self._start_time = time.time()
        self.animate("slideDown", 200)

    def dismiss(self):
        self._dismissed = True
        self.visible = False

    def update(self):
        if self.visible and self.duration_ticks > 0:
            elapsed = (time.time() - self._start_time) * 20  # convert to ticks
            if elapsed >= self.duration_ticks:
                self.dismiss()


class Tooltip(Widget):
    """Hover tooltip that follows the cursor."""

    def __init__(self, text: str = "", **kwargs):
        super().__init__()
        self.text: str = text
        self.target: Optional[Widget] = None
        self.delay_ms: int = 500
        self._hover_start: float = 0.0
        self._showing: bool = False
        self.width = 150
        self.height = 24
        self._apply_kwargs(kwargs)

    def check_show(self, x: float, y: float):
        if self.target and self.target.contains(x, y):
            if not self._showing:
                self._hover_start = time.time()
            if (time.time() - self._hover_start) * 1000 >= self.delay_ms:
                if not self._showing:
                    self._showing = True
                    self.visible = True
                    self.animate("fadeIn", 100)
            self.x = x + 10
            self.y = y + 10
        else:
            if self._showing:
                self._showing = False
                self.visible = False


class ContextMenu(Widget):
    """Right-click context menu with options."""

    def __init__(self, **kwargs):
        super().__init__()
        self.items: list[tuple[str, Callable]] = []
        self._open: bool = False
        self.width = 150
        self.item_height: int = 24
        self._apply_kwargs(kwargs)

    @property
    def height(self) -> float:
        return len(self.items) * self.item_height

    def show_at(self, x: float, y: float):
        self.x = x
        self.y = y
        self.visible = True
        self._open = True

    def hide(self):
        self.visible = False
        self._open = False

    def add_item(self, label: str, callback: Callable):
        self.items.append((label, callback))

    def handle_click(self, x, y, button=0):
        if not self.visible:
            return False
        ax, ay = self.absolute_x, self.absolute_y
        if ax <= x <= ax + self.width and ay <= y <= ay + self.height:
            idx = int((y - ay) // self.item_height)
            if 0 <= idx < len(self.items):
                _, callback = self.items[idx]
                callback()
                self.hide()
            return True
        self.hide()
        return False


class Image(Widget):
    """Image/texture display widget."""

    def __init__(self, texture_path: str = "", **kwargs):
        super().__init__()
        self.texture: str = texture_path
        self.scale_mode: str = "fit"
        self.width = 64
        self.height = 64
        self._apply_kwargs(kwargs)
