# Widgety — przegląd

## Szybki start

```python
from mlang.gui import *

# Utwórz okno
win = Window("§6§l MLang Panel §r", width=400, height=500)
win.center_on_screen()
win.draggable = True
win.theme("dark")

# Utwórz kategorię
cat = Category("Gracz")
cat.add(
    Toggle("Leć").bindable("F").on_change(lambda v: print(f"Fly: {v}")),
    Slider("Prędkość", min=0.1, max=5.0, step=0.1, value=1.0),
    Button("§aUlecz").style("success").on_click(lambda: print("Heal!")),
    Button("§cZabij").style("danger").on_click(lambda: print("Kill!")),
)

# Utwórz drugą kategorię
cat2 = Category("Świat")
cat2.add(
    Button("☀ Dzień").on_click(lambda: print("Day")),
    Button("🌙 Noc").on_click(lambda: print("Night")),
    Slider("Czas", min=0, max=24000, value=6000),
)

# Dodaj zakładki
tab1 = Tab("Gracz")
tab1.add(cat)
tab2 = Tab("Świat")
tab2.add(cat2)

win.add_tab(tab1)
win.add_tab(tab2)

# Pokaż
manager = WindowManager()
manager.add(win)
manager.show(win)
```

## Wbudowane motywy

| Motyw | Opis |
|-------|------|
| `dark` | Ciemny z neon czerwonym akcentem (domyślny) |
| `light` | Jasny z akcentem |
| `minecraft` | Styl Minecraft — ostre krawędzie |
| `glass` | Szkłomorfizm — rozmycie + przezroczystość |
| `neon` | Neonowy — magenta + cyan glow |
| `minimal` | Minimalistyczny, czarno-biały |
| `future` | Styl future client — niebieski akcent |

```python
GUI.SetTheme("glass")
GUI.SetTheme("neon")
GUI.SetTheme("future")
```

## Efekty wizualne

### Rozmycie
```python
widget.blur(radius=10, opacity=0.85)
```

### Cień
```python
widget.shadow(radius=8, offset_y=2, opacity=0.5)
```

### Poświata (neon)
```python
widget.glow(color="#FF00FF", radius=8, opacity=0.6, pulse=1.0)
```

### Gradient
```python
widget.gradient(start="#E94560", end="#0F3460", angle=135, opacity=0.3)
```

## Animacje

### Animacje wejścia
```python
widget.animate("fadeIn", 200)
widget.animate("slideDown", 300)
widget.animate("slideLeft", 300)
widget.animate("bounceIn", 400)
widget.animate("zoomIn", 250)
```

### Animacje w pętli
```python
widget.animate_loop("pulse", 1000)    // pulsowanie przezroczystości
widget.animate_loop("shake", 500)     // trzęsienie
widget.animate_loop("rainbow", 2000)  // tęcza kolorów
```

## Lista widgetów

| Widget | Opis |
|--------|------|
| `Button` | Klikalny przycisk z efektem hover |
| `Toggle` | Przełącznik ON/OFF |
| `Slider` | Suwak z zakresem |
| `Input` | Pole tekstowe |
| `Label` | Etykieta tekstowa |
| `ProgressBar` | Pasek postępu |
| `Dropdown` | Lista rozwijana |
| `ColorPicker` | Wybór koloru |
| `Separator` | Linia oddzielająca |
| `Category` | Grupa z nagłówkiem |
| `Window` | Okno z paskiem tytułu |
| `Tab` | Zakładka w oknie |
| `Hotbar` | Pasek skrótów |
| `Minimap` | Minimapa |
| `Notification` | Powiadomienie |
| `Tooltip` | Dymek po najechaniu |
| `ContextMenu` | Menu prawego kliknięcia |
| `Image` | Obrazek / tekstura |
