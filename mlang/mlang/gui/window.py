"""Window manager — manages all windows, handles input dispatch, rendering."""

from typing import Optional

from .widgets import Widget, Window
from .animations import AnimationManager


class WindowManager:
    """Manages all top-level windows and input routing."""

    def __init__(self):
        self.windows: list[Window] = []
        self.widgets: list[Widget] = []  # non-window top-level widgets
        self.animations = AnimationManager()
        self._mouse_x: float = 0.0
        self._mouse_y: float = 0.0
        self._focused_widget: Optional[Widget] = None
        self._dragging: bool = False
        self.context_menu: Optional[Widget] = None
        self.tooltips: list[Widget] = []

    def add(self, widget: Widget):
        if isinstance(widget, Window):
            self.windows.append(widget)
        else:
            self.widgets.append(widget)

    def remove(self, widget: Widget):
        if widget in self.windows:
            self.windows.remove(widget)
        elif widget in self.widgets:
            self.widgets.remove(widget)

    def find(self, name: str) -> Optional[Widget]:
        for w in self.widgets:
            result = w.find(name)
            if result:
                return result
        for win in self.windows:
            result = win.find(name)
            if result:
                return result
        return None

    def show(self, widget: Widget):
        widget.visible = True
        self.bring_to_front(widget)

    def hide(self, widget: Widget):
        widget.visible = False

    def toggle(self, widget: Widget):
        widget.visible = not widget.visible
        if widget.visible:
            self.bring_to_front(widget)

    def bring_to_front(self, widget: Widget):
        if widget in self.windows:
            self.windows.remove(widget)
            self.windows.append(widget)
        elif widget in self.widgets:
            self.widgets.remove(widget)
            self.widgets.append(widget)

    def handle_click(self, x: float, y: float, button: int = 0):
        if self.context_menu and self.context_menu.visible:
            if self.context_menu.handle_click(x, y, button):
                return True

        for win in reversed(self.windows):
            if not win.visible:
                continue
            if win.handle_click(x, y, button):
                self.bring_to_front(win)
                return True

        for w in reversed(self.widgets):
            if not w.visible:
                continue
            if w.handle_click(x, y, button):
                return True

        return False

    def handle_drag(self, x: float, y: float):
        for win in reversed(self.windows):
            if not win.visible:
                continue
            if win.handle_drag(x, y):
                return True
        for w in reversed(self.widgets):
            if not w.visible:
                continue
            if w.handle_drag(x, y):
                return True
        return False

    def handle_drag_end(self):
        for win in self.windows:
            win.handle_drag_end()
        for w in self.widgets:
            w.handle_drag_end()

    def handle_hover(self, x: float, y: float):
        self._mouse_x, self._mouse_y = x, y
        for win in self.windows:
            win.handle_hover(x, y)
        for w in self.widgets:
            w.handle_hover(x, y)
        for tooltip in self.tooltips:
            tooltip.check_show(x, y)

    def handle_key(self, key: str, action: str = "press"):
        if self._focused_widget and isinstance(self._focused_widget, Input):
            if action == "char":
                self._focused_widget.text += key
                if self._focused_widget.on_change:
                    self._focused_widget.on_change(self._focused_widget.text)
            elif key == "backspace":
                self._focused_widget.text = self._focused_widget.text[:-1]
                if self._focused_widget.on_change:
                    self._focused_widget.on_change(self._focused_widget.text)
            elif key == "enter":
                if self._focused_widget.on_enter:
                    self._focused_widget.on_enter(self._focused_widget.text)

    def update(self):
        self.animations.update_all()
        for win in self.windows:
            for child in win.children:
                if hasattr(child, 'update'):
                    child.update()
        for w in self.widgets:
            if hasattr(w, 'update'):
                w.update()

    def get_all_widgets_sorted(self) -> list[Widget]:
        result = []
        for w in sorted(self.widgets, key=lambda x: x.z_index):
            result.append(w)
            result.extend(self._collect_children(w))
        for win in sorted(self.windows, key=lambda x: x.z_index):
            result.append(win)
            result.extend(self._collect_children(win))
        return result

    def _collect_children(self, widget: Widget) -> list[Widget]:
        result = []
        for child in widget.children:
            result.append(child)
            result.extend(self._collect_children(child))
        return result


__all__ = ["WindowManager"]
