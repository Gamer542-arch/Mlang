# Classes and inheritance

## Classes
```glang
public class Waypoint {
    public string Name
    public double X, Y, Z
    private bool active = true

    public Waypoint(string name, double x, double y, double z) {
        this.Name = name
        this.X = x
        this.Y = y
        this.Z = z
    }

    public void Teleport() {
        Player.TeleportTo(X, Y, Z)
    }
}
```

## Inheritance
```glang
public class BaseEntity {
    public double X, Y, Z

    public virtual void Update() {
        print("Aktualizacja bazowa")
    }
}

public class PlayerEntity : BaseEntity {
    public string Name

    public override void Update() {
        base.Update()
        print("Gracz: " + Name)
    }
}
```

## Interfaces
```glang
public interface IClickable {
    void OnClick()
}

public interface IDamageable {
    void TakeDamage(float amount)
    float Health { get; }
}

public class Button : IClickable {
    public void OnClick() {
        print("Kliknięto!")
    }
}
```

## Abstract classes
```glang
public abstract class Vehicle {
    public abstract void Drive()

    public void Stop() {
        print("Zatrzymano")
    }
}
```

## Properties (getters/setters)
```glang
public class PlayerData {
    private int health = 20

    public int Health {
        get { return health }
        set { health = Math.Clamp(value, 0, 20) }
    }
}
```

## Static members
```glang
public class MathHelper {
    public static double PI = 3.14159

    public static double Square(double x) {
        return x * x
    }
}
```
