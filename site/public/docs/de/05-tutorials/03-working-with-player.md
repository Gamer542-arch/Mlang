# Spielersteuerung

## Teleportation

```glang
Player.TeleportTo(100, 64, -200)
Player.TeleportTo(0, 80, 0, 90.0, 45.0)  // mit Rotation
Player.TeleportTo(otherPlayer)
```

## Bewegung

```glang
Player.SetWalkSpeed(0.5)     // schnelleres Gehen
Player.SetFlySpeed(0.3)      // Fluggeschwindigkeit
Player.Fly(true)             // Fliegen aktivieren
Player.Jump()                // springen
Player.SetVelocity(0, 2, 0)  // hochwerfen
```

## Gesundheit und Hunger

```glang
Player.SetHealth(40)
Player.SetMaxHealth(40)
Player.SetFoodLevel(20)
Player.SetSaturation(5.0)
Player.AddEffect("regeneration", 200, 2)
```

## Inventar

```glang
Player.Give("minecraft:diamond_sword")
Player.Give("minecraft:diamond", 64)
Player.SetMainHandItem(ItemStack("minecraft:diamond_sword"))
Player.ClearInventory()
```

## Spielmodi

```glang
Player.SetGameMode("creative")
Player.SetGameMode("survival")
Player.SetGameMode("spectator")
```

## Kommunikation

```glang
Player.SendMessage("§aHallo!")
Player.ShowTitle("§6Title!", "§7Subtitle", 10, 70, 20)
Player.ShowActionBar("§eAction bar text")
```
