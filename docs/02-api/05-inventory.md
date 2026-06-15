# Inventory API — pełna dokumentacja

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `Player.GetInventory()` | `Inventory` | Pobierz ekwipunek gracza |
| `inv.MainHand` | `ItemStack` | Przedmiot w głównej ręce |
| `inv.OffHand` | `ItemStack` | Przedmiot w drugiej ręce |
| `inv.Helmet` | `ItemStack` | Hełm |
| `inv.Chestplate` | `ItemStack` | Napierśnik |
| `inv.Leggings` | `ItemStack` | Spodnie |
| `inv.Boots` | `ItemStack` | Buty |
| `inv.SetMainHand(item)` | `void` | Ustaw główną rękę |
| `inv.SetOffHand(item)` | `void` | Ustaw drugą rękę |
| `inv.SetHelmet(item)` | `void` | Ustaw hełm |
| `inv.SetChestplate(item)` | `void` | Ustaw napierśnik |
| `inv.SetLeggings(item)` | `void` | Ustaw spodnie |
| `inv.SetBoots(item)` | `void` | Ustaw buty |
| `inv.GetItem(slot)` | `ItemStack` | Item w slocie (0-40) |
| `inv.SetItem(slot, item)` | `void` | Ustaw item w slocie |
| `inv.GetHotbar()` | `ItemStack[]` | Hotbar (0-8) |
| `inv.GetMainInventory()` | `ItemStack[]` | Główny ekwipunek (9-35) |
| `inv.GetArmor()` | `ItemStack[]` | Armor (36-39) |
| `inv.GetOffhand()` | `ItemStack` | Offhand (40) |
| `inv.Clear()` | `void` | Wyczyść cały ekwipunek |
| `inv.Clear(slot)` | `void` | Wyczyść slot |
| `inv.HasItem(item)` | `bool` | Czy ma przedmiot |
| `inv.Count(item)` | `int` | Ilość przedmiotu |
| `inv.Add(item)` | `bool` | Dodaj przedmiot |
| `inv.Add(item, count)` | `bool` | Dodaj z ilością |
| `inv.Remove(item)` | `bool` | Usuń przedmiot |
| `inv.Remove(item, count)` | `bool` | Usuń z ilością |
| `inv.Contains(item)` | `bool` | Czy zawiera |
| `inv.GetAllItems()` | `List<ItemStack>` | Wszystkie itemy |
| `inv.IsEmpty()` | `bool` | Czy pusty |
| `inv.IsFull()` | `bool` | Czy pełny |
| `inv.GetFreeSlots()` | `int` | Liczba wolnych slotów |
| `inv.Open()` | `void` | Otwórz interfejs |
| `inv.Close()` | `void` | Zamknij |

## Container API (skrzynie, piece itp.)

| Metoda | Zwraca | Opis |
|--------|--------|------|
| `World.OpenChest(x, y, z)` | `Inventory` | Otwórz skrzynię |
| `World.OpenBarrel(x, y, z)` | `Inventory` | Otwórz beczkę |
| `World.OpenShulker(x, y, z)` | `Inventory` | Otwórz shulker |
| `World.OpenHopper(x, y, z)` | `Inventory` | Otwórz hopper |
| `World.OpenDispenser(x, y, z)` | `Inventory` | Otwórz dispenser |
| `World.OpenFurnace(x, y, z)` | `Inventory` | Otwórz piec |
| `World.OpenBrewingStand(x, y, z)` | `Inventory` | Otwórz brewing stand |
| `inv.GetSlotCount()` | `int` | Ilość slotów |
| `inv.GetTitle()` | `string` | Tytuł kontenera |
| `inv.AddListener(callback)` | `void` | Nasłuchuj zmian |
