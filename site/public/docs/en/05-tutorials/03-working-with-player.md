# Controlling the player

## Teleportation

```glang
Player.TeleportTo(100, 64, -200)
Player.TeleportTo(0, 80, 0, 90.0, 45.0)  // with rotation
Player.TeleportTo(otherPlayer)
```

## Movement

```glang
Player.SetWalkSpeed(0.5)     // faster walking
Player.SetFlySpeed(0.3)      // fly speed
Player.Fly(true)             // enable flying
Player.Jump()                // jump
Player.SetVelocity(0, 2, 0)  // launch upward
```

## Health and hunger

```glang
Player.SetHealth(40)
Player.SetMaxHealth(40)
Player.SetFoodLevel(20)
Player.SetSaturation(5.0)
Player.AddEffect("regeneration", 200, 2)
```

## Inventory

```glang
Player.Give("minecraft:diamond_sword")
Player.Give("minecraft:diamond", 64)
Player.SetMainHandItem(ItemStack("minecraft:diamond_sword"))
Player.ClearInventory()
```

## Game modes

```glang
Player.SetGameMode("creative")
Player.SetGameMode("survival")
Player.SetGameMode("spectator")
```

## Communication

```glang
Player.SendMessage("§aHello!")
Player.ShowTitle("§6Title!", "§7Subtitle", 10, 70, 20)
Player.ShowActionBar("§eAction bar text")
```
