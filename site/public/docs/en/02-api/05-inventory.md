# Inventory API

| Method | Returns | Description |
|--------|--------|------|
| `Player.GetInventory()` | `Inventory` | Get player inventory |
| `inv.MainHand` | `ItemStack` | Item in main hand |
| `inv.OffHand` | `ItemStack` | Item in off hand |
| `inv.Helmet` | `ItemStack` | Helmet |
| `inv.Chestplate` | `ItemStack` | Chestplate |
| `inv.Leggings` | `ItemStack` | Leggings |
| `inv.Boots` | `ItemStack` | Boots |
| `inv.SetMainHand(item)` | `void` | Set main hand |
| `inv.SetOffHand(item)` | `void` | Set off hand |
| `inv.SetHelmet(item)` | `void` | Set helmet |
| `inv.SetChestplate(item)` | `void` | Set chestplate |
| `inv.SetLeggings(item)` | `void` | Set leggings |
| `inv.SetBoots(item)` | `void` | Set boots |
| `inv.GetItem(slot)` | `ItemStack` | Item in slot (0-40) |
| `inv.SetItem(slot, item)` | `void` | Set item in slot |
| `inv.GetHotbar()` | `ItemStack[]` | Hotbar (0-8) |
| `inv.GetMainInventory()` | `ItemStack[]` | Main inventory (9-35) |
| `inv.GetArmor()` | `ItemStack[]` | Armor (36-39) |
| `inv.GetOffhand()` | `ItemStack` | Offhand (40) |
| `inv.Clear()` | `void` | Clear entire inventory |
| `inv.Clear(slot)` | `void` | Clear slot |
| `inv.HasItem(item)` | `bool` | Whether has item |
| `inv.Count(item)` | `int` | Item count |
| `inv.Add(item)` | `bool` | Add item |
| `inv.Add(item, count)` | `bool` | Add with count |
| `inv.Remove(item)` | `bool` | Remove item |
| `inv.Remove(item, count)` | `bool` | Remove with count |
| `inv.Contains(item)` | `bool` | Whether contains |
| `inv.GetAllItems()` | `List<ItemStack>` | All items |
| `inv.IsEmpty()` | `bool` | Whether empty |
| `inv.IsFull()` | `bool` | Whether full |
| `inv.GetFreeSlots()` | `int` | Number of free slots |
| `inv.Open()` | `void` | Open interface |
| `inv.Close()` | `void` | Close |

## Container API (chests, furnaces etc.)

| Method | Returns | Description |
|--------|--------|------|
| `World.OpenChest(x, y, z)` | `Inventory` | Open chest |
| `World.OpenBarrel(x, y, z)` | `Inventory` | Open barrel |
| `World.OpenShulker(x, y, z)` | `Inventory` | Open shulker |
| `World.OpenHopper(x, y, z)` | `Inventory` | Open hopper |
| `World.OpenDispenser(x, y, z)` | `Inventory` | Open dispenser |
| `World.OpenFurnace(x, y, z)` | `Inventory` | Open furnace |
| `World.OpenBrewingStand(x, y, z)` | `Inventory` | Open brewing stand |
| `inv.GetSlotCount()` | `int` | Slot count |
| `inv.GetTitle()` | `string` | Container title |
| `inv.AddListener(callback)` | `void` | Listen for changes |
