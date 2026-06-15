# Inventar-API

| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `Player.GetInventory()` | `Inventory` | Inventar des Spielers abrufen |
| `inv.MainHand` | `ItemStack` | Gegenstand in der Haupthand |
| `inv.OffHand` | `ItemStack` | Gegenstand in der Zweithand |
| `inv.Helmet` | `ItemStack` | Helm |
| `inv.Chestplate` | `ItemStack` | Brustpanzer |
| `inv.Leggings` | `ItemStack` | Hose |
| `inv.Boots` | `ItemStack` | Stiefel |
| `inv.SetMainHand(item)` | `void` | Haupthand setzen |
| `inv.SetOffHand(item)` | `void` | Zweithand setzen |
| `inv.SetHelmet(item)` | `void` | Helm setzen |
| `inv.SetChestplate(item)` | `void` | Brustpanzer setzen |
| `inv.SetLeggings(item)` | `void` | Hose setzen |
| `inv.SetBoots(item)` | `void` | Stiefel setzen |
| `inv.GetItem(slot)` | `ItemStack` | Gegenstand im Slot (0-40) |
| `inv.SetItem(slot, item)` | `void` | Gegenstand im Slot setzen |
| `inv.GetHotbar()` | `ItemStack[]` | Hotbar (0-8) |
| `inv.GetMainInventory()` | `ItemStack[]` | Hauptinventar (9-35) |
| `inv.GetArmor()` | `ItemStack[]` | Rüstung (36-39) |
| `inv.GetOffhand()` | `ItemStack` | Zweithand (40) |
| `inv.Clear()` | `void` | Gesamtes Inventar leeren |
| `inv.Clear(slot)` | `void` | Slot leeren |
| `inv.HasItem(item)` | `bool` | Hat Gegenstand |
| `inv.Count(item)` | `int` | Anzahl des Gegenstands |
| `inv.Add(item)` | `bool` | Gegenstand hinzufügen |
| `inv.Add(item, count)` | `bool` | Mit Anzahl hinzufügen |
| `inv.Remove(item)` | `bool` | Gegenstand entfernen |
| `inv.Remove(item, count)` | `bool` | Mit Anzahl entfernen |
| `inv.Contains(item)` | `bool` | Enthält |
| `inv.GetAllItems()` | `List<ItemStack>` | Alle Gegenstände |
| `inv.IsEmpty()` | `bool` | Ist leer |
| `inv.IsFull()` | `bool` | Ist voll |
| `inv.GetFreeSlots()` | `int` | Anzahl freier Slots |
| `inv.Open()` | `void` | Oberfläche öffnen |
| `inv.Close()` | `void` | Schließen |

## Container-API (Kisten, Öfen usw.)

| Methode | Rückgabe | Beschreibung |
|--------|--------|------|
| `World.OpenChest(x, y, z)` | `Inventory` | Kiste öffnen |
| `World.OpenBarrel(x, y, z)` | `Inventory` | Fass öffnen |
| `World.OpenShulker(x, y, z)` | `Inventory` | Shulker öffnen |
| `World.OpenHopper(x, y, z)` | `Inventory` | Trichter öffnen |
| `World.OpenDispenser(x, y, z)` | `Inventory` | Werfer öffnen |
| `World.OpenFurnace(x, y, z)` | `Inventory` | Ofen öffnen |
| `World.OpenBrewingStand(x, y, z)` | `Inventory` | Braustand öffnen |
| `inv.GetSlotCount()` | `int` | Anzahl Slots |
| `inv.GetTitle()` | `string` | Titel des Containers |
| `inv.AddListener(callback)` | `void` | Auf Änderungen lauschen |
