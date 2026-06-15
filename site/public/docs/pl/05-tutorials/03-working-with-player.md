# Sterowanie graczem

## Teleportacja

```glang
Player.TeleportTo(100, 64, -200)
Player.TeleportTo(0, 80, 0, 90.0, 45.0)  // z obrotem
Player.TeleportTo(otherPlayer)
```

## Ruch

```glang
Player.SetWalkSpeed(0.5)     // szybsze chodzenie
Player.SetFlySpeed(0.3)      // prędkość lotu
Player.Fly(true)             // włącz latanie
Player.Jump()                // skok
Player.SetVelocity(0, 2, 0)  // wyrzuć w górę
```

## Zdrowie i głód

```glang
Player.SetHealth(40)
Player.SetMaxHealth(40)
Player.SetFoodLevel(20)
Player.SetSaturation(5.0)
Player.AddEffect("regeneration", 200, 2)
```

## Ekwipunek

```glang
Player.Give("minecraft:diamond_sword")
Player.Give("minecraft:diamond", 64)
Player.SetMainHandItem(ItemStack("minecraft:diamond_sword"))
Player.ClearInventory()
```

## Tryby gry

```glang
Player.SetGameMode("creative")
Player.SetGameMode("survival")
Player.SetGameMode("spectator")
```

## Komunikacja

```glang
Player.SendMessage("§aWitaj!")
Player.ShowTitle("§6Title!", "§7Subtitle", 10, 70, 20)
Player.ShowActionBar("§eAction bar text")
```
