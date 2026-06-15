"""Visual effects — blur, shadow, glow, gradient overlays."""

from dataclasses import dataclass
from typing import Optional, Callable


@dataclass
class BlurEffect:
    """Gaussian blur configuration for widget backgrounds."""
    radius: int = 10
    opacity: float = 0.85
    enabled: bool = True
    passes: int = 3  # render passes for quality


@dataclass
class ShadowEffect:
    """Drop shadow configuration."""
    radius: int = 8
    offset_x: int = 0
    offset_y: int = 2
    color: str = "#000000"
    opacity: float = 0.5
    enabled: bool = True
    inset: bool = False


@dataclass
class GlowEffect:
    """Outer glow / neon glow effect."""
    color: str = "#E94560"
    radius: int = 6
    opacity: float = 0.6
    enabled: bool = False
    pulse_speed: float = 0.0  # 0 = static, >0 = pulse frequency


@dataclass
class GradientOverlay:
    """Gradient overlay for backgrounds."""
    start_color: str = "#E94560"
    end_color: str = "#0F3460"
    angle: float = 135.0  # degrees
    opacity: float = 0.3
    enabled: bool = False


@dataclass
class BorderEffect:
    """Border styling."""
    width: int = 1
    color: str = "#2A2A4A"
    radius: int = 4  # corner radius (0 = sharp)
    hover_color: Optional[str] = None
    focus_color: Optional[str] = None
    animated: bool = True


@dataclass
class VisualState:
    """Combined visual state for a widget."""

    blur: BlurEffect = None
    shadow: ShadowEffect = None
    glow: GlowEffect = None
    gradient: GradientOverlay = None
    border: BorderEffect = None

    @classmethod
    def default(cls) -> "VisualState":
        return cls(
            blur=BlurEffect(),
            shadow=ShadowEffect(),
            border=BorderEffect(),
        )

    @classmethod
    def glass(cls) -> "VisualState":
        """Glassmorphism effect."""
        return cls(
            blur=BlurEffect(radius=15, opacity=0.65),
            shadow=ShadowEffect(radius=10, offset_y=4, opacity=0.3),
            border=BorderEffect(width=1, color="#FFFFFF30", radius=8),
        )

    @classmethod
    def neon(cls) -> "VisualState":
        """Neon glow effect."""
        return cls(
            blur=BlurEffect(radius=8, opacity=0.9),
            shadow=ShadowEffect(radius=12, color="#FF00FF", opacity=0.4),
            glow=GlowEffect(color="#FF00FF", radius=8, opacity=0.6, pulse_speed=1.0),
            border=BorderEffect(width=1, color="#303050", radius=2),
        )

    @classmethod
    def sharp(cls) -> "VisualState":
        """Sharp, clean, no frills."""
        return cls(
            blur=BlurEffect(radius=0, opacity=1.0),
            shadow=ShadowEffect(enabled=False),
            border=BorderEffect(width=1, color="#333333", radius=0),
        )

    @classmethod
    def none(cls) -> "VisualState":
        return cls()


EFFECT_PRESETS: dict[str, Callable[[], VisualState]] = {
    "default": VisualState.default,
    "glass": VisualState.glass,
    "neon": VisualState.neon,
    "sharp": VisualState.sharp,
    "none": VisualState.none,
}


def get_effect_preset(name: str) -> VisualState:
    builder = EFFECT_PRESETS.get(name, EFFECT_PRESETS["default"])
    return builder()


def blend_colors(hex1: str, hex2: str, t: float) -> str:
    """Blend two hex colors with t=0.0→hex1, t=1.0→hex2."""
    r1, g1, b1 = int(hex1[1:3], 16), int(hex1[3:5], 16), int(hex1[5:7], 16)
    r2, g2, b2 = int(hex2[1:3], 16), int(hex2[3:5], 16), int(hex2[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02X}{g:02X}{b:02X}"
