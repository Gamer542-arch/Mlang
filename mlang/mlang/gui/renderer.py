"""GUI Renderer — console debug renderer and bridge serializer for Minecraft mod."""

from typing import Any, Optional
from dataclasses import dataclass, field, asdict
import json

from .widgets import (
    Widget, Button, Toggle, Slider, Input, Label, ProgressBar,
    Dropdown, ColorPicker, Separator, Category, Window, Tab,
    Hotbar, Minimap, Notification, Tooltip, ContextMenu, Image,
    WidgetState,
)


def serialize_widget(w: Widget) -> dict:
    """Serialize widget tree to JSON for bridge transport."""
    base = {
        "type": type(w).__name__,
        "name": w.name,
        "x": w.x, "y": w.y, "width": w.width, "height": w.height,
        "visible": w.visible, "enabled": w.enabled,
        "opacity": w.opacity, "z_index": w.z_index,
        "color": w.color, "text_color": w.text_color,
        "border_color": w.border_color,
        "children": [serialize_widget(c) for c in w.children],
    }

    if isinstance(w, Button):
        base["label"] = w.label
        base["icon"] = w.icon
        base["style"] = w.style
        base["rounded"] = w.rounded
        base["bindable_key"] = w.bindable_key
    elif isinstance(w, Toggle):
        base["label"] = w.label
        base["value"] = w.value
        base["bindable_key"] = w.bindable_key
    elif isinstance(w, Slider):
        base["label"] = w.label
        base["min"] = w.min
        base["max"] = w.max
        base["step"] = w.step
        base["value"] = w.value
        base["show_value"] = w.show_value
        base["format"] = w.format_str
    elif isinstance(w, Input):
        base["placeholder"] = w.placeholder
        base["text"] = w.text
        base["max_length"] = w.max_length
        base["input_type"] = w.input_type
    elif isinstance(w, Label):
        base["text"] = w.text
        base["text_align"] = w.text_align
        base["font_size"] = w.font_size
        base["bold"] = w.bold
    elif isinstance(w, ProgressBar):
        base["min"] = w.min
        base["max"] = w.max
        base["value"] = w.value
        base["show_label"] = w.show_label
        base["indeterminate"] = w.indeterminate
    elif isinstance(w, Dropdown):
        base["label"] = w.label
        base["options"] = w.options
        base["selected_index"] = w.selected_index
        base["expanded"] = w.expanded
    elif isinstance(w, ColorPicker):
        base["color"] = w.color
    elif isinstance(w, Separator):
        base["orientation"] = w.orientation
    elif isinstance(w, Category):
        base["title"] = w.title
        base["collapsed"] = w.collapsed
        base["collapsible"] = w.collapsible
    elif isinstance(w, Window):
        base["title"] = w.title
        base["resizable"] = w.resizable
        base["closeable"] = w.closeable
        base["minimized"] = w.minimized
        base["tabs"] = [serialize_widget(t) for t in w.tabs]
    elif isinstance(w, Tab):
        base["title"] = w.title
        base["icon"] = w.icon
        base["active"] = w.active
    elif isinstance(w, Hotbar):
        base["slots"] = w.slots
        base["selected_slot"] = w.selected_slot
    elif isinstance(w, Minimap):
        base["zoom"] = w.zoom
        base["center_x"] = w.center_x
        base["center_z"] = w.center_z
    elif isinstance(w, Notification):
        base["text"] = w.text
        base["type"] = w.type
        base["duration"] = w.duration_ticks
    elif isinstance(w, Tooltip):
        base["text"] = w.text
    elif isinstance(w, ContextMenu):
        base["items"] = [item[0] for item in w.items]

    return base


def serialize_gui_state(widgets: list[Widget], windows: list[Window]) -> str:
    """Serialize entire GUI state to JSON string for bridge."""
    data = {
        "widgets": [serialize_widget(w) for w in widgets],
        "windows": [serialize_widget(w) for w in windows],
    }
    return json.dumps(data)


class ConsoleRenderer:
    """ASCII/console renderer for development and debugging."""

    def __init__(self, width: int = 80, height: int = 40):
        self.width = width
        self.height = height
        self.buffer: list[list[str]] = [[" " for _ in range(width)] for _ in range(height)]

    def clear(self):
        self.buffer = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def render(self, widgets: list[Widget]):
        self.clear()
        sorted_widgets = sorted(widgets, key=lambda w: w.z_index)
        for w in sorted_widgets:
            self._render_widget(w)
        self._draw()

    def _render_widget(self, w: Widget, offset_x: int = 0, offset_y: int = 0):
        if not w.visible:
            return

        x = int(w.absolute_x) + offset_x
        y = int(w.absolute_y) + offset_y
        ww = int(w.width)
        wh = int(w.height)

        if isinstance(w, Button):
            self._draw_box(x, y, ww, wh, "BTN")
            label = w.label[:ww - 2]
            self._draw_text(x + 1, y + wh // 2, f" {label} ")
        elif isinstance(w, Toggle):
            self._draw_box(x, y, ww, wh, "TGL")
            val = "ON" if w.value else "OFF"
            self._draw_text(x + 1, y + wh // 2, f" {w.label}: [{val}] ")
        elif isinstance(w, Slider):
            self._draw_box(x, y, ww, wh, "SLD")
            filled = int(w.normalized * (ww - 4))
            self._draw_text(x + 1, y + wh // 2, f" {'#' * filled}{'-' * (ww - 4 - filled)} ")
        elif isinstance(w, Input):
            self._draw_box(x, y, ww, wh, "INP")
            text = w.text if w.text else w.placeholder
            self._draw_text(x + 1, y + wh // 2, f" {text} ")
        elif isinstance(w, Label):
            self._draw_text(x, y + wh // 2, f" {w.text} ")
        elif isinstance(w, ProgressBar):
            self._draw_box(x, y, ww, wh, "PRG")
            filled = int(w.normalized * (ww - 2))
            self._draw_text(x + 1, y + wh // 2, f" {'#' * filled}{'-' * (ww - 2 - filled)} ")
        elif isinstance(w, Category):
            self._draw_box(x, y, ww, wh, f"CAT {w.title}")
            if not w.collapsed:
                for child in w.children:
                    self._render_widget(child, offset_x, offset_y)
        elif isinstance(w, Window):
            self._draw_box(x, y, ww, wh, f"WIN {w.title}")
            self._draw_line(x, y + w.titlebar_height, x + ww, y + w.titlebar_height, "─")
            if not w.minimized:
                for child in w.children:
                    self._render_widget(child, offset_x, offset_y)
        elif isinstance(w, Separator):
            self._draw_line(x, y + wh // 2, x + ww, y + wh // 2, "─")
        elif isinstance(w, Dropdown):
            self._draw_box(x, y, ww, wh, "DRP")
            val = w.selected_value or w.label
            self._draw_text(x + 1, y + wh // 2, f" {val} ")
            if w.expanded:
                for i, opt in enumerate(w.options):
                    oy = y + wh + i * wh
                    self._draw_box(x, oy, ww, wh, "")
                    self._draw_text(x + 1, oy + wh // 2, f" {opt} ")
        else:
            self._draw_box(x, y, ww, wh, f"?{type(w).__name__[:3]}")

    def _draw_box(self, x: int, y: int, w: int, h: int, label: str = ""):
        if h < 1 or w < 2:
            return
        for row in range(max(0, y), min(self.height, y + h)):
            if row >= self.height:
                break
            for col in range(max(0, x), min(self.width, x + w)):
                if col >= self.width:
                    break
                ch = " "
                if row == y:
                    ch = "-" if 0 < col - x < w - 1 else "+" if col == x else "+"
                elif row == y + h - 1:
                    ch = "-" if 0 < col - x < w - 1 else "+" if col == x else "+"
                elif col == x or col == x + w - 1:
                    ch = "|"
                self.buffer[row][col] = ch

    def _draw_text(self, x: int, y: int, text: str):
        for i, ch in enumerate(text):
            cx, cy = x + i, y
            if 0 <= cy < self.height and 0 <= cx < self.width:
                self.buffer[cy][cx] = ch

    def _draw_line(self, x1: int, y1: int, x2: int, y2: int, ch: str = "-"):
        for cx in range(max(0, x1), min(self.width, x2)):
            if 0 <= y1 < self.height:
                self.buffer[y1][cx] = ch

    def _draw(self):
        print("+" + "-" * self.width + "+")
        for row in self.buffer:
            print("|" + "".join(row) + "|")
        print("+" + "-" * self.width + "+")


__all__ = ["serialize_widget", "serialize_gui_state", "ConsoleRenderer"]
