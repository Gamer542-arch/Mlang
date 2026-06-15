# Budowanie świata

## Podstawy

```glang
World.SetBlock(0, 64, 0, "minecraft:diamond_block")
World.BreakBlock(0, 64, 0)
var block = World.GetBlock(0, 64, 0)
```

## Fill (wypełnianie obszarów)

```glang
// Wypełnij obszar
World.Fill(0, 60, 0, 10, 60, 10, "minecraft:stone")

// Zniszcz i zastąp
World.Fill(0, 60, 0, 10, 60, 10, "minecraft:air", "destroy")

// Hollow (wydrążony)
World.Fill(0, 60, 0, 10, 65, 10, "minecraft:stone", "hollow")

// Outline (same krawędzie)
World.Fill(0, 60, 0, 10, 65, 10, "minecraft:stone", "outline")
```

## Zaawansowane kształty

```glang
// Kula
World.Sphere(0, 64, 0, 5, "minecraft:glass", false)
World.Sphere(0, 64, 0, 5, "minecraft:glass", true)    // hollow

// Cylinder
World.Cylinder(0, 64, 0, 5, 10, "minecraft:stone")

// Piramida
World.Pyramid(0, 64, 0, 10, "minecraft:sandstone")
```

## Przykład: Budowa domu

```glang
#version 1.0
#name "Build House"

var x = 100, y = 64, z = 0
var w = 10, h = 5, d = 8

// Podłoga
World.Fill(x, y, z, x + w, y, z + d, "minecraft:oak_planks")

// Ściany
World.Fill(x, y + 1, z, x + w, y + h, z + d, "minecraft:oak_log", "outline")

// Dach
World.Fill(x - 1, y + h + 1, z - 1, x + w + 1, y + h + 1, z + d + 1, "minecraft:spruce_stairs")

// Okno
World.SetBlock(x + w/2, y + 2, z, "minecraft:glass_pane")

// Drzwi
World.SetBlock(x + w/2, y + 1, z, "minecraft:air")
World.SetBlock(x + w/2, y + 2, z, "minecraft:air")
```
