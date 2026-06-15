"""Test the MLang GUI system."""

from mlang.gui import *


def test_theme_system():
    """Verify all built-in themes load correctly."""
    themes = ["dark", "light", "minecraft", "glass", "neon", "minimal", "future"]
    for name in themes:
        theme = get_theme(name)
        assert theme.name == name
        assert theme.background is not None
        assert theme.accent is not None
        assert theme.text is not None
        print(f"  {name}: OK (bg={theme.background}, accent={theme.accent})")
    print("[PASS] Theme system OK")


def test_widget_creation():
    """Create all widget types."""
    w = Window("Test Window", width=400, height=300)
    assert w.title == "Test Window"
    assert w.width == 400

    btn = Button("Click", style="danger", rounded=True)
    assert btn.label == "Click"
    assert btn.style == "danger"

    tgl = Toggle("Fly", value=True)
    assert tgl.value is True
    assert tgl.label == "Fly"

    sld = Slider("Speed", min=0.0, max=5.0, value=2.5, step=0.1)
    assert sld.value == 2.5
    assert sld.min == 0.0

    inp = Input("Type...", text="hello")
    assert inp.text == "hello"
    assert inp.placeholder == "Type..."

    lbl = Label("Hello World", bold=True)
    assert lbl.text == "Hello World"

    cat = Category("Options", collapsed=True)
    assert cat.collapsed is True
    cat.toggle_collapse()
    assert cat.collapsed is False

    print("[PASS] Widget creation OK")


def test_widget_tree():
    """Test parent/child relationships."""
    win = Window("Root", name="root")
    cat = Category("Category", name="cat")
    btn = Button("Button", name="btn")
    tgl = Toggle("Toggle", name="tgl")

    win.add(cat)
    cat.add(btn, tgl)

    assert btn.parent is cat
    assert cat.parent is win
    assert win.find("cat") is cat
    assert win.find("btn") is btn

    print("[PASS] Widget tree OK")


def test_containment():
    """Test mouse containment detection."""
    btn = Button("Test", x=10, y=20, width=100, height=30)
    assert btn.contains(15, 25) is True
    assert btn.contains(5, 25) is False
    assert btn.contains(15, 10) is False
    assert btn.contains(120, 25) is False
    print("[PASS] Containment OK")


def test_click_handling():
    """Test click dispatch."""
    clicked = []

    btn = Button("Test", x=0, y=0, width=100, height=30)
    btn.on_click = lambda: clicked.append("click")

    btn.handle_click(50, 15)
    assert len(clicked) == 1

    btn.handle_click(150, 15)  # outside
    assert len(clicked) == 1

    print("[PASS] Click handling OK")


def test_toggle():
    """Test toggle behavior."""
    toggled = []

    tgl = Toggle("Test", x=0, y=0, width=100, height=30)
    tgl.on_change = lambda v: toggled.append(v)

    assert tgl.value is False
    tgl.handle_click(50, 15)
    assert tgl.value is True
    assert toggled == [True]
    tgl.handle_click(50, 15)
    assert tgl.value is False
    assert toggled == [True, False]

    print("[PASS] Toggle OK")


def test_slider():
    """Test slider value manipulation."""
    sld = Slider("Test", x=0, y=0, width=200, height=30, min=0, max=100, value=50)
    assert sld.normalized == 0.5

    sld.set_from_normalized(0.25)
    assert sld.value == 25.0

    sld.set_from_normalized(0.0)
    assert sld.value == 0.0

    sld.set_from_normalized(1.0)
    assert sld.value == 100.0

    print("[PASS] Slider OK")


def test_dropdown():
    """Test dropdown selection."""
    dd = Dropdown("Select", x=0, y=0, width=150, height=28)
    dd.options = ["Option A", "Option B", "Option C"]

    assert dd.selected_value is None
    dd.select(1)
    assert dd.selected_value == "Option B"
    assert dd.expanded is False

    print("[PASS] Dropdown OK")


def test_window():
    """Test window with tabs."""
    win = Window("Main", width=400, height=300)
    tab1 = Tab("Player")
    tab2 = Tab("World")
    win.add_tab(tab1)
    win.add_tab(tab2)

    assert len(win.tabs) == 2
    assert win.active_tab is tab1

    win.switch_tab("World")
    assert win.active_tab is tab2

    # Center on screen
    win.center_on_screen(1920, 1080)
    assert win.x == (1920 - 400) / 2
    assert win.y == (1080 - 300) / 2

    print("[PASS] Window OK")


def test_animation():
    """Test animation tweens."""
    anim = Animation(None, 200, Easing.BOUNCE)
    assert anim.duration == 200
    assert anim.easing == Easing.BOUNCE

    # Test easing functions
    assert apply_easing(0.0, Easing.LINEAR) == 0.0
    assert apply_easing(1.0, Easing.LINEAR) == 1.0
    assert apply_easing(0.5, Easing.LINEAR) == 0.5

    assert apply_easing(0.0, Easing.BOUNCE) == 0.0
    assert apply_easing(1.0, Easing.BOUNCE) == 1.0

    print("[PASS] Animation OK")


def test_serialization():
    """Test widget serialization."""
    win = Window("Test", x=10, y=20, width=300, height=200)
    btn = Button("Click", x=5, y=5, width=100, height=30)
    win.add(btn)

    data = serialize_widget(win)
    assert data["type"] == "Window"
    assert data["title"] == "Test"
    assert data["x"] == 10
    assert len(data["children"]) == 1
    assert data["children"][0]["type"] == "Button"
    assert data["children"][0]["label"] == "Click"

    print("[PASS] Serialization OK")


def test_visual_effects():
    """Test visual effect presets."""
    default = VisualState.default()
    assert default.blur is not None
    assert default.shadow is not None
    assert default.border is not None

    glass = VisualState.glass()
    assert glass.blur.radius == 15
    assert glass.border.radius == 8

    neon = VisualState.neon()
    assert neon.glow is not None
    assert neon.glow.color == "#FF00FF"

    print("[PASS] Visual effects OK")


def test_renderer():
    """Test console renderer."""
    renderer = ConsoleRenderer(60, 20)
    win = Window("Test", width=50, height=10)
    btn = Button("Click", width=20, height=3)
    win.add(btn)
    renderer.render([win])
    print("[PASS] Console renderer OK")


if __name__ == "__main__":
    print("\n=== MLang GUI Tests ===\n")
    test_theme_system()
    test_widget_creation()
    test_widget_tree()
    test_containment()
    test_click_handling()
    test_toggle()
    test_slider()
    test_dropdown()
    test_window()
    test_animation()
    test_serialization()
    test_visual_effects()
    test_renderer()
    print("\n[PASS] All GUI tests passed!")
