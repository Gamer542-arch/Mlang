# Error handling

## try/catch/finally
```glang
try {
    var result = RiskyOperation()
    print(result)
} catch (GException e) {
    print("Błąd: " + e.Message)
} catch (Exception e) {
    print("Nieznany błąd: " + e)
} finally {
    print("Zawsze się wykonuje")
}
```

## throw
```glang
public void CheckHealth(float hp) {
    if (hp <= 0) {
        throw new GException("HP nie może być zerowe!")
    }
}
```

## Debugging
```glang
Debug.Break()              // zatrzymaj debugger
Debug.Log("wartość: " + x)  // logowanie
Debug.Warn("ostrzeżenie!")  // ostrzeżenie
Debug.Error("błąd!")        // błąd
Debug.Assert(x > 0, "x musi być > 0")
Debug.Trace()               // ślad stosu
```
