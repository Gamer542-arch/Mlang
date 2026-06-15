# Widgets — overview

## Quick start

```python
from mlang.gui import *

# Create a window
win = Window("§6§l MLang Panel §r", width=400, height=500)
win.center_on_screen()
win.draggable = True
win.theme("dark")

# Create a category
cat = Category("Player")
cat.add(
    Toggle("Fly").bindable("F").on_change(lambda v: print(f"Fly: {v}")),
    Slider("Speed", min=0.1, max=5.0, step=0.1, value=1.0),
    Button("§aHeal").style("success").on_click(lambda: print("Heal!")),
    Button("§cKill").style("danger").on_click(lambda: print("Kill!")),
)

# Create a second category
cat2 = Category("World")
cat2.add(
    Button("☀ Day").on_click(lambda: print("Day")),
    Button("🌙 Night").on_click(lambda: print("Night")),
    Slider("Time", min=0, max=24000, value=6000),
)

# Add tabs
tab1 = Tab("Player")
tab1.add(cat)
tab2 = Tab("World")
tab2.add(cat2)

win.add_tab(tab1)
win.add_tab(tab2)

# Show
manager = WindowManager()
manager.add(win)
manager.show(win)
```

## Built-in themes

| Theme | Description |
|-------|------|
| `dark` | Dark with neon red accent (default) |
| `light` | Light with accent |
| `minecraft` | Minecraft style — sharp edges |
| `glass` | Glassmorphism — blur + transparency |
| `neon` | Neon — magenta + cyan glow |
| `minimal` | Minimalist, black and white |
| `future` | Future client style — blue accent |

```python
GUI.SetTheme("glass")
GUI.SetTheme("neon")
GUI.SetTheme("future")
```

## Visual effects

### Blur
```python
widget.blur(radius=10, opacity=0.85)
```

### Shadow
```python
widget.shadow(radius=8, offset_y=2, opacity=0.5)
```

### Glow (neon)
```python
widget.glow(color="#FF00FF", radius=8, opacity=0.6, pulse=1.0)
```

### Gradient
```python
widget.gradient(start="#E94560", end="#0F3460", angle=135, opacity=0.3)
```

## Animations

### Entry animations
```python
widget.animate("fadeIn", 200)
widget.animate("slideDown", 300)
widget.animate("slideLeft", 300)
widget.animate("bounceIn", 400)
widget.animate("zoomIn", 250)
```

### Loop animations
```python
widget.animate_loop("pulse", 1000)    // transparency pulsing
widget.animate_loop("shake", 500)     // shaking
widget.animate_loop("rainbow", 2000)  // rainbow colors
```

## Widget list

| Widget | Description |
|--------|------|
| `Button` | Clickable button with hover effect |
| `Toggle` | ON/OFF toggle |
| `Slider` | Range slider |
| `Input` | Text field |
| `Label` | Text label |
| `ProgressBar` | Progress bar |
| `Dropdown` | Dropdown list |
| `ColorPicker` | Color picker |
| `Separator` | Separator line |
| `Category` | Group with header |
| `Window` | Window with title bar |
| `Tab` | Tab in a window |
| `Hotbar` | Hotbar |
| `Minimap` | Minimap |
| `Notification` | Notification |
| `Tooltip` | Hover tooltip |
| `ContextMenu` | Right-click menu |
| `Image` | Image / texture |
