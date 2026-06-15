# Building the world

## Basics

```glang
World.SetBlock(0, 64, 0, "minecraft:diamond_block")
World.BreakBlock(0, 64, 0)
var block = World.GetBlock(0, 64, 0)
```

## Fill (area filling)

```glang
// Fill an area
World.Fill(0, 60, 0, 10, 60, 10, "minecraft:stone")

// Destroy and replace
World.Fill(0, 60, 0, 10, 60, 10, "minecraft:air", "destroy")

// Hollow
World.Fill(0, 60, 0, 10, 65, 10, "minecraft:stone", "hollow")

// Outline (edges only)
World.Fill(0, 60, 0, 10, 65, 10, "minecraft:stone", "outline")
```

## Advanced shapes

```glang
// Sphere
World.Sphere(0, 64, 0, 5, "minecraft:glass", false)
World.Sphere(0, 64, 0, 5, "minecraft:glass", true)    // hollow

// Cylinder
World.Cylinder(0, 64, 0, 5, 10, "minecraft:stone")

// Pyramid
World.Pyramid(0, 64, 0, 10, "minecraft:sandstone")
```

## Example: Building a house

```glang
#version 1.0
#name "Build House"

var x = 100, y = 64, z = 0
var w = 10, h = 5, d = 8

// Floor
World.Fill(x, y, z, x + w, y, z + d, "minecraft:oak_planks")

// Walls
World.Fill(x, y + 1, z, x + w, y + h, z + d, "minecraft:oak_log", "outline")

// Roof
World.Fill(x - 1, y + h + 1, z - 1, x + w + 1, y + h + 1, z + d + 1, "minecraft:spruce_stairs")

// Window
World.SetBlock(x + w/2, y + 2, z, "minecraft:glass_pane")

// Door
World.SetBlock(x + w/2, y + 1, z, "minecraft:air")
World.SetBlock(x + w/2, y + 2, z, "minecraft:air")
```
