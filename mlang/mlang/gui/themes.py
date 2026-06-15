"""GUI Theme System — cheat-client style themes with blur, shadow, and animations."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Theme:
    """Complete theme configuration for MLang GUI."""

    # Main colors
    background: str = "#0D0D0D"           # Main window bg (very dark)
    surface: str = "#1A1A2E"              # Widget surface bg
    surface_secondary: str = "#16213E"    # Secondary surface (dropdowns, etc.)
    accent: str = "#E94560"                # Primary accent (neon red/pink)
    accent_secondary: str = "#0F3460"     # Secondary accent (deep blue)
    accent_hover: str = "#FF6B81"         # Accent on hover
    text: str = "#EAEAEA"                 # Primary text
    text_secondary: str = "#8A8A9A"       # Secondary/muted text
    text_accent: str = "#FFFFFF"          # Text on accent backgrounds
    border: str = "#2A2A4A"               # Default border
    border_focus: str = "#E94560"         # Border when focused
    shadow: str = "#00000080"             # Shadow color (with alpha)
    blur_color: str = "#0D0D0DCC"        # Blur overlay color (with alpha)

    # Status colors
    success: str = "#2ECC71"              # Green
    warning: str = "#F39C12"              # Yellow/Orange
    error: str = "#E74C3C"                # Red
    info: str = "#3498DB"                 # Blue

    # Slider specifics
    slider_track: str = "#2A2A4A"
    slider_fill: str = "#E94560"
    slider_handle: str = "#FFFFFF"

    # Toggle specifics
    toggle_off: str = "#2A2A4A"
    toggle_on: str = "#E94560"
    toggle_handle: str = "#FFFFFF"

    # Input specifics
    input_bg: str = "#0D0D0D"
    input_border: str = "#2A2A4A"
    input_focus_border: str = "#E94560"
    input_placeholder: str = "#4A4A5A"

    # Scrollbar
    scrollbar_track: str = "#0D0D0D"
    scrollbar_thumb: str = "#2A2A4A"
    scrollbar_thumb_hover: str = "#E94560"

    # Category
    category_header: str = "#1A1A2E"
    category_body: str = "#0D0D0D"
    category_border: str = "#2A2A4A"

    # Window
    window_titlebar: str = "#1A1A2E"
    window_titlebar_active: str = "#16213E"
    window_close: str = "#E94560"
    window_close_hover: str = "#FF6B81"
    window_minimize: str = "#F39C12"
    window_resize: str = "#2ECC71"

    # Visual config
    blur_radius: int = 10                 # Gaussian blur radius for backgrounds
    blur_opacity: float = 0.85            # Background opacity when blur active
    border_radius: int = 4                # Widget corner rounding (0 = sharp)
    border_width: int = 1                 # Default border width
    shadow_radius: int = 8                # Shadow spread
    shadow_offset_x: int = 0
    shadow_offset_y: int = 2
    shadow_opacity: float = 0.5

    # Typography
    font_family: str = "Segoe UI"
    font_size: int = 10
    font_size_small: int = 8
    font_size_large: int = 14
    font_size_title: int = 18
    font_weight: str = "normal"
    font_weight_bold: str = "bold"

    # Sizing
    widget_height: int = 28
    widget_padding: int = 8
    widget_margin: int = 4
    window_padding: int = 12
    category_padding: int = 10

    # Animation
    animation_duration: int = 200         # ms - default transition
    animation_easing: str = "ease-out"    # transition type
    animation_enabled: bool = True

    def __post_init__(self):
        self._name = "custom"

    @property
    def name(self) -> str:
        return self._name

    def with_name(self, name: str) -> "Theme":
        self._name = name
        return self


BUILTIN_THEMES: dict[str, Theme] = {}


def register_theme(name: str, theme: Theme):
    theme.with_name(name)
    BUILTIN_THEMES[name] = theme


def get_theme(name: str = "dark") -> Theme:
    return BUILTIN_THEMES.get(name, dark_theme)


# ===== BUILT-IN THEMES =====

dark_theme = Theme(
    background="#0D0D0D",
    surface="#1A1A2E",
    surface_secondary="#16213E",
    accent="#E94560",
    accent_secondary="#0F3460",
    accent_hover="#FF6B81",
    text="#EAEAEA",
    text_secondary="#8A8A9A",
    text_accent="#FFFFFF",
    border="#2A2A4A",
    border_focus="#E94560",
    shadow="#00000080",
    blur_color="#0D0D0DCC",
    blur_radius=10,
    blur_opacity=0.85,
    border_radius=4,
    animation_duration=200,
).with_name("dark")
register_theme("dark", dark_theme)

light_theme = Theme(
    background="#F5F5F5",
    surface="#FFFFFF",
    surface_secondary="#E8E8E8",
    accent="#E94560",
    accent_secondary="#3498DB",
    accent_hover="#FF6B81",
    text="#1A1A2E",
    text_secondary="#666666",
    text_accent="#FFFFFF",
    border="#D0D0D0",
    border_focus="#E94560",
    shadow="#00000020",
    blur_color="#FFFFFFCC",
    blur_radius=8,
    blur_opacity=0.8,
    border_radius=4,
    animation_duration=150,
).with_name("light")
register_theme("light", light_theme)

minecraft_theme = Theme(
    background="#1A1A1A",
    surface="#2B2B2B",
    surface_secondary="#3C3C3C",
    accent="#55FF55",
    accent_secondary="#5555FF",
    accent_hover="#77FF77",
    text="#FFFFFF",
    text_secondary="#AAAAAA",
    text_accent="#FFFFFF",
    border="#555555",
    border_focus="#55FF55",
    shadow="#00000040",
    blur_color="#1A1A1ACC",
    blur_radius=4,
    blur_opacity=0.75,
    border_radius=0,  # Sharp edges like vanilla MC
    font_family="Minecraft",
    animation_duration=100,
).with_name("minecraft")
register_theme("minecraft", minecraft_theme)

glass_theme = Theme(
    background="#00000000",
    surface="#FFFFFF15",
    surface_secondary="#FFFFFF10",
    accent="#00FFC8",
    accent_secondary="#0088FF",
    accent_hover="#33FFD4",
    text="#FFFFFF",
    text_secondary="#AAAAAACC",
    text_accent="#000000",
    border="#FFFFFF30",
    border_focus="#00FFC8",
    shadow="#00000040",
    blur_color="#00000066",
    blur_radius=15,
    blur_opacity=0.65,
    border_radius=6,
    animation_duration=250,
).with_name("glass")
register_theme("glass", glass_theme)

neon_theme = Theme(
    background="#08080F",
    surface="#12121F",
    surface_secondary="#1A1A30",
    accent="#FF00FF",
    accent_secondary="#00FFFF",
    accent_hover="#FF44FF",
    text="#FFFFFF",
    text_secondary="#8888AA",
    text_accent="#000000",
    border="#303050",
    border_focus="#FF00FF",
    shadow="#FF00FF40",
    blur_color="#08080FEE",
    blur_radius=12,
    blur_opacity=0.9,
    border_radius=2,
    animation_duration=300,
).with_name("neon")
register_theme("neon", neon_theme)

minimal_theme = Theme(
    background="#111111",
    surface="#1E1E1E",
    surface_secondary="#282828",
    accent="#FFFFFF",
    accent_secondary="#666666",
    accent_hover="#CCCCCC",
    text="#FFFFFF",
    text_secondary="#888888",
    text_accent="#000000",
    border="#333333",
    border_focus="#FFFFFF",
    shadow="#00000040",
    blur_color="#111111CC",
    blur_radius=6,
    blur_opacity=0.8,
    border_radius=0,
    animation_duration=100,
).with_name("minimal")
register_theme("minimal", minimal_theme)

future_theme = Theme(
    background="#0A0A0A",
    surface="#141414",
    surface_secondary="#1E1E1E",
    accent="#00BFFF",
    accent_secondary="#1E90FF",
    accent_hover="#33CCFF",
    text="#F0F0F0",
    text_secondary="#808088",
    text_accent="#000000",
    border="#282828",
    border_focus="#00BFFF",
    shadow="#00000060",
    blur_color="#0A0A0ACC",
    blur_radius=8,
    blur_opacity=0.85,
    border_radius=2,
    animation_duration=200,
).with_name("future")
register_theme("future", future_theme)


__all__ = [
    "Theme", "get_theme", "register_theme",
    "dark_theme", "light_theme", "minecraft_theme",
    "glass_theme", "neon_theme", "minimal_theme", "future_theme",
]
