# Widgets — Übersicht

## Schnellstart

```python
from mlang.gui import *

# Fenster erstellen
win = Window("§6§l MLang Panel §r", width=400, height=500)
win.center_on_screen()
win.draggable = True
win.theme("dark")

# Kategorie erstellen
cat = Category("Spieler")
cat.add(
    Toggle("Fliegen").bindable("F").on_change(lambda v: print(f"Fly: {v}")),
    Slider("Geschwindigkeit", min=0.1, max=5.0, step=0.1, value=1.0),
    Button("§aHeilen").style("success").on_click(lambda: print("Heal!")),
    Button("§cTöten").style("danger").on_click(lambda: print("Kill!")),
)

# Zweite Kategorie
cat2 = Category("Welt")
cat2.add(
    Button("☀ Tag").on_click(lambda: print("Day")),
    Button("🌙 Nacht").on_click(lambda: print("Night")),
    Slider("Zeit", min=0, max=24000, value=6000),
)

# Tabs hinzufügen
tab1 = Tab("Spieler")
tab1.add(cat)
tab2 = Tab("Welt")
tab2.add(cat2)

win.add_tab(tab1)
win.add_tab(tab2)

# Anzeigen
manager = WindowManager()
manager.add(win)
manager.show(win)
```

## Eingebaute Themes

| Theme | Beschreibung |
|-------|-------------|
| `dark` | Dunkel mit neonrotem Akzent (Standard) |
| `light` | Hell mit Akzent |
| `minecraft` | Minecraft-Stil — scharfe Kanten |
| `glass` | Glas-Effekt — Weichzeichnung + Transparenz |
| `neon` | Neon — Magenta + Cyan Glühen |
| `minimal` | Minimalistisch, schwarz-weiß |
| `future` | Future-Client-Stil — blauer Akzent |

```python
GUI.SetTheme("glass")
GUI.SetTheme("neon")
GUI.SetTheme("future")
```

## Visuelle Effekte

### Weichzeichnung
```python
widget.blur(radius=10, opacity=0.85)
```

### Schatten
```python
widget.shadow(radius=8, offset_y=2, opacity=0.5)
```

### Glühen (Neon)
```python
widget.glow(color="#FF00FF", radius=8, opacity=0.6, pulse=1.0)
```

### Farbverlauf
```python
widget.gradient(start="#E94560", end="#0F3460", angle=135, opacity=0.3)
```

## Animationen

### Eingangsanimationen
```python
widget.animate("fadeIn", 200)
widget.animate("slideDown", 300)
widget.animate("slideLeft", 300)
widget.animate("bounceIn", 400)
widget.animate("zoomIn", 250)
```

### Schleifenanimationen
```python
widget.animate_loop("pulse", 1000)    // Transparenz pulsieren
widget.animate_loop("shake", 500)     // Wackeln
widget.animate_loop("rainbow", 2000)  // Regenbogen-Farben
```

## Widget-Liste

| Widget | Beschreibung |
|--------|-------------|
| `Button` | Klickbarer Knopf mit Hover-Effekt |
| `Toggle` | AN/AUS-Schalter |
| `Slider` | Schieberegler mit Bereich |
| `Input` | Textfeld |
| `Label` | Textbeschriftung |
| `ProgressBar` | Fortschrittsbalken |
| `Dropdown` | Dropdown-Liste |
| `ColorPicker` | Farbauswahl |
| `Separator` | Trennlinie |
| `Category` | Gruppe mit Überschrift |
| `Window` | Fenster mit Titelleiste |
| `Tab` | Tab in einem Fenster |
| `Hotbar` | Schnellzugriffsleiste |
| `Minimap` | Minimap |
| `Notification` | Benachrichtigung |
| `Tooltip` | Tooltip beim Hover |
| `ContextMenu` | Rechtsklick-Menü |
| `Image` | Bild / Textur |
