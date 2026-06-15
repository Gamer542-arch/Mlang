# Quick hot-reload: rebuild + copy to mods
$McModsDir = "H:\Crystal-Launcher\instances\u.Axiom\.minecraft\mods"

$env:JAVA_HOME = "C:\Program Files\Java\jdk-23"
$env:Path = "$env:JAVA_HOME\bin;$env:Path"

Write-Host "[BUILDING]" -ForegroundColor Cyan
Push-Location "H:\proj\MLang\mlang-mod"
& .\gradlew.bat remapJar 2>&1 | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Host "BUILD FAILED" -ForegroundColor Red
    Pop-Location; exit 1
}

$jar = Get-ChildItem "build\libs\mlang-mod-*.jar" | Where-Object { $_.Name -notlike "*sources*" } | Select-Object -First 1
Copy-Item $jar.FullName $McModsDir -Force
Write-Host "[DONE] $($jar.Name) -> $McModsDir" -ForegroundColor Green
Pop-Location
