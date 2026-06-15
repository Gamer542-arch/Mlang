# Fehlerbehandlung

## try/catch/finally
```glang
try {
    var result = RiskyOperation()
    print(result)
} catch (GException e) {
    print("Fehler: " + e.Message)
} catch (Exception e) {
    print("Unbekannter Fehler: " + e)
} finally {
    print("Wird immer ausgeführt")
}
```

## throw
```glang
public void CheckHealth(float hp) {
    if (hp <= 0) {
        throw new GException("HP darf nicht null sein!")
    }
}
```

## Debugging
```glang
Debug.Break()              // Debugger anhalten
Debug.Log("Wert: " + x)    // Protokollierung
Debug.Warn("Warnung!")     // Warnung
Debug.Error("Fehler!")     // Fehler
Debug.Assert(x > 0, "x muss > 0 sein")
Debug.Trace()              // Stack-Trace
```
