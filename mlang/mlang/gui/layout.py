"""Layout engine — auto-arranges widgets with flexbox-like behavior."""

from __future__ import annotations
from enum import Enum, auto
from typing import Optional

from .widgets import Widget


class LayoutDirection(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()


class LayoutAlign(Enum):
    START = auto()
    CENTER = auto()
    END = auto()
    FILL = auto()


class Layout:
    """Container layout manager."""

    def __init__(
        self,
        direction: LayoutDirection = LayoutDirection.VERTICAL,
        padding: int = 8,
        spacing: int = 4,
        align_h: LayoutAlign = LayoutAlign.FILL,
        align_v: LayoutAlign = LayoutAlign.START,
    ):
        self.direction = direction
        self.padding = padding
        self.spacing = spacing
        self.align_h = align_h
        self.align_v = align_v

    def arrange(self, container: Widget):
        if not container.children:
            return

        cx, cy = container.x + self.padding, container.y + self.padding
        cw = container.width - self.padding * 2
        ch = container.height - self.padding * 2

        if self.direction == LayoutDirection.VERTICAL:
            self._arrange_vertical(container, cx, cy, cw, ch)
        else:
            self._arrange_horizontal(container, cx, cy, cw, ch)

    def _arrange_vertical(self, container: Widget, cx: float, cy: float, cw: float, ch: float):
        y_offset = cy
        for child in container.children:
            if not child.visible:
                continue
            child.x = cx + self._align_offset(child.width, cw, self.align_h)
            child.y = y_offset

            if self.align_h == LayoutAlign.FILL:
                child.width = cw

            y_offset += child.height + self.spacing

    def _arrange_horizontal(self, container: Widget, cx: float, cy: float, cw: float, ch: float):
        x_offset = cx
        for child in container.children:
            if not child.visible:
                continue
            child.x = x_offset
            child.y = cy + self._align_offset(child.height, ch, self.align_v)

            if self.align_v == LayoutAlign.FILL:
                child.height = ch

            x_offset += child.width + self.spacing

    def _align_offset(self, child_size: float, container_size: float, align: LayoutAlign) -> float:
        if align == LayoutAlign.CENTER:
            return (container_size - child_size) / 2
        elif align == LayoutAlign.END:
            return container_size - child_size
        return 0.0
