# Obsługa błędów

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
        throw new GException("HP cannot be zero!")
    }
}
```

## Debugowanie
```glang
Debug.Break()              // zatrzymaj debugger
Debug.Log("value: " + x)  // logowanie
Debug.Warn("warning!")    // warning
Debug.Error("error!")     // error
Debug.Assert(x > 0, "x must be > 0")
Debug.Trace()             // stack trace
```
