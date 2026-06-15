"""Animation engine for GUI widgets — smooth transitions, bounce, pulse, shake effects."""

import math
import time
from enum import Enum, auto
from typing import Any, Callable, Optional


class Easing(Enum):
    LINEAR = auto()
    EASE_IN = auto()
    EASE_OUT = auto()
    EASE_IN_OUT = auto()
    BOUNCE = auto()
    ELASTIC = auto()
    BACK_IN = auto()
    BACK_OUT = auto()
    CUBIC_IN = auto()
    CUBIC_OUT = auto()
    QUARTIC_IN = auto()
    QUARTIC_OUT = auto()
    QUINTIC_IN = auto()
    QUINTIC_OUT = auto()


def _clamp(t: float) -> float:
    return max(0.0, min(1.0, t))


def _easing_none(t: float) -> float:
    return 1.0


def _easing_linear(t: float) -> float:
    return t


def _easing_in(t: float, power: float = 2.0) -> float:
    return t ** power


def _easing_out(t: float, power: float = 2.0) -> float:
    return 1.0 - (1.0 - t) ** power


def _easing_in_out(t: float, power: float = 2.0) -> float:
    return t * t if t < 0.5 else 1.0 - (-2.0 * t + 2.0) ** power / 2.0


def _easing_bounce(t: float) -> float:
    n1, d1 = 7.5625, 2.75
    if t < 1.0 / d1:
        return n1 * t * t
    elif t < 2.0 / d1:
        t -= 1.5 / d1
        return n1 * t * t + 0.75
    elif t < 2.5 / d1:
        t -= 2.25 / d1
        return n1 * t * t + 0.9375
    else:
        t -= 2.625 / d1
        return n1 * t * t + 0.984375


def _easing_elastic(t: float) -> float:
    c4 = (2.0 * math.pi) / 3.0
    return 0.0 if t == 0.0 else 1.0 if t == 1.0 else -2.0 ** (10.0 * t - 10.0) * math.sin((t * 10.0 - 10.75) * c4)


def _easing_back_in(t: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return c3 * t * t * t - c1 * t * t


def _easing_back_out(t: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return 1.0 + c3 * (t - 1.0) ** 3 + c1 * (t - 1.0) ** 2


EASING_FUNCTIONS: dict[Easing, Callable[[float], float]] = {
    Easing.LINEAR: _easing_linear,
    Easing.EASE_IN: lambda t: _easing_in(t, 2.0),
    Easing.EASE_OUT: lambda t: _easing_out(t, 2.0),
    Easing.EASE_IN_OUT: lambda t: _easing_in_out(t, 2.0),
    Easing.BOUNCE: _easing_bounce,
    Easing.ELASTIC: _easing_elastic,
    Easing.BACK_IN: _easing_back_in,
    Easing.BACK_OUT: _easing_back_out,
    Easing.CUBIC_IN: lambda t: _easing_in(t, 3.0),
    Easing.CUBIC_OUT: lambda t: _easing_out(t, 3.0),
    Easing.QUARTIC_IN: lambda t: _easing_in(t, 4.0),
    Easing.QUARTIC_OUT: lambda t: _easing_out(t, 4.0),
    Easing.QUINTIC_IN: lambda t: _easing_in(t, 5.0),
    Easing.QUINTIC_OUT: lambda t: _easing_out(t, 5.0),
}


def apply_easing(t: float, easing: Easing) -> float:
    func = EASING_FUNCTIONS.get(easing, _easing_linear)
    return _clamp(func(_clamp(t)))


class Tween:
    """Single animated value transition."""

    def __init__(
        self,
        start: float,
        end: float,
        duration_ms: int = 200,
        easing: Easing = Easing.EASE_OUT,
        on_update: Optional[Callable[[float], None]] = None,
        on_complete: Optional[Callable[[], None]] = None,
    ):
        self.start_val = start
        self.end_val = end
        self.duration = duration_ms / 1000.0
        self.easing = easing
        self.on_update = on_update
        self.on_complete = on_complete
        self.start_time: float = 0.0
        self.running: bool = False

    def start(self):
        self.start_time = time.time()
        self.running = True

    def update(self) -> bool:
        if not self.running:
            return False
        elapsed = time.time() - self.start_time
        t = _clamp(elapsed / self.duration)
        eased = apply_easing(t, self.easing)
        val = self.start_val + (self.end_val - self.start_val) * eased
        if self.on_update:
            self.on_update(val)
        if t >= 1.0:
            self.running = False
            if self.on_complete:
                self.on_complete()
            return False
        return True

    @property
    def value(self) -> float:
        if not self.running:
            return self.end_val
        elapsed = time.time() - self.start_time
        t = _clamp(elapsed / self.duration)
        eased = apply_easing(t, self.easing)
        return self.start_val + (self.end_val - self.start_val) * eased


class Animation:
    """Complex multi-property animation for a widget."""

    def __init__(self, widget, duration_ms: int = 200, easing: Easing = Easing.EASE_OUT):
        self.widget = widget
        self.duration = duration_ms
        self.easing = easing
        self.tweens: list[Tween] = []
        self.running = False

    def tween(self, attr: str, end_val: float) -> "Animation":
        start = getattr(self.widget, attr, 0.0)
        tween = Tween(
            start=start,
            end=end_val,
            duration_ms=self.duration,
            easing=self.easing,
            on_update=lambda v: setattr(self.widget, attr, v),
        )
        self.tweens.append(tween)
        return self

    def tween_color(self, attr: str, end_hex: str) -> "Animation":
        start = getattr(self.widget, attr, "#000000")
        tween = ColorTween(
            start_hex=start,
            end_hex=end_hex,
            duration_ms=self.duration,
            easing=self.easing,
            on_update=lambda c: setattr(self.widget, attr, c),
        )
        self.tweens.append(tween)
        return self

    def start(self):
        self.running = True
        for t in self.tweens:
            t.start()

    def update(self) -> bool:
        if not self.running:
            return False
        alive = any(t.update() for t in self.tweens)
        if not alive:
            self.running = False
        return alive


class ColorTween:
    """Tween between two hex colors."""

    def __init__(
        self,
        start_hex: str,
        end_hex: str,
        duration_ms: int = 200,
        easing: Easing = Easing.EASE_OUT,
        on_update: Optional[Callable[[str], None]] = None,
    ):
        self.start_rgb = self._hex_to_rgb(start_hex)
        self.end_rgb = self._hex_to_rgb(end_hex)
        self.duration = duration_ms / 1000.0
        self.easing = easing
        self.on_update = on_update
        self.start_time: float = 0.0
        self.running: bool = False

    def _hex_to_rgb(self, hex_str: str) -> tuple[float, float, float]:
        hex_str = hex_str.lstrip("#")
        return (
            int(hex_str[0:2], 16),
            int(hex_str[2:4], 16),
            int(hex_str[4:6], 16),
        )

    def _rgb_to_hex(self, r: float, g: float, b: float) -> str:
        return f"#{int(r):02X}{int(g):02X}{int(b):02X}"

    def start(self):
        self.start_time = time.time()
        self.running = True

    def update(self) -> bool:
        if not self.running:
            return False
        elapsed = time.time() - self.start_time
        t = _clamp(elapsed / self.duration)
        eased = apply_easing(t, self.easing)
        r = self.start_rgb[0] + (self.end_rgb[0] - self.start_rgb[0]) * eased
        g = self.start_rgb[1] + (self.end_rgb[1] - self.start_rgb[1]) * eased
        b = self.start_rgb[2] + (self.end_rgb[2] - self.start_rgb[2]) * eased
        if self.on_update:
            self.on_update(self._rgb_to_hex(r, g, b))
        if t >= 1.0:
            self.running = False
            return False
        return True


class AnimationManager:
    """Manages all active animations globally."""

    def __init__(self):
        self.animations: list[Animation] = []

    def add(self, anim: Animation):
        anim.start()
        self.animations.append(anim)

    def update_all(self):
        self.animations = [a for a in self.animations if a.update()]

    def clear(self):
        self.animations.clear()

    @property
    def is_active(self) -> bool:
        return len(self.animations) > 0


class AnimatedProperty:
    """Property descriptor that auto-animates on set."""

    def __init__(self, default: float = 0.0, duration_ms: int = 200, easing: Easing = Easing.EASE_OUT):
        self.default = default
        self.duration = duration_ms
        self.easing = easing
        self.values: dict[int, float] = {}
        self.tweens: dict[int, Tween] = {}

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        oid = id(obj)
        return self.values.get(oid, self.default)

    def __set__(self, obj, value: float):
        oid = id(obj)
        current = self.values.get(oid, self.default)
        if abs(current - value) < 0.001:
            return
        self.values[oid] = value
        # Animation handled externally by AnimationManager


__all__ = [
    "Easing", "Tween", "Animation", "ColorTween",
    "AnimationManager", "AnimatedProperty", "apply_easing",
]
