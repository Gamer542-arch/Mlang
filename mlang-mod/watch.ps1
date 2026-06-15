# MLang Mod Hot-Reload Watcher
# Auto-rebuilds + copies JAR to mods on file changes
# Stop with Ctrl+C

$ErrorActionPreference = "SilentlyContinue"
$scriptDir = "H:\proj\MLang\mlang-mod"
$McModsDir = "H:\Crystal-Launcher\instances\u.Axiom\.minecraft\mods"

Write-Host "=== MLang Hot-Reload Watcher ===" -ForegroundColor Cyan
Write-Host "Mods dir: $McModsDir" -ForegroundColor Gray
Write-Host "Watching: $scriptDir\src\" -ForegroundColor Gray
Write-Host "Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

# Initial build
function Build-And-Copy {
    Write-Host "[BUILD]" -ForegroundColor Yellow -NoNewline
    Push-Location $scriptDir
    $env:JAVA_HOME = "C:\Program Files\Java\jdk-23"
    $env:Path = "$env:JAVA_HOME\bin;$env:Path"
    $out = & .\gradlew.bat remapJar 2>&1 | Out-String
    Pop-Location
  
    if ($LASTEXITCODE -eq 0) {
        $jar = Get-ChildItem "$scriptDir\build\libs\mlang-mod-*.jar" | Where-Object { $_.Name -notlike "*sources*" } | Select-Object -First 1
        if ($jar) {
            Copy-Item $jar.FullName $McModsDir -Force
            Write-Host " OK -> $McModsDir" -ForegroundColor Green
        }
    } else {
        Write-Host " FAIL" -ForegroundColor Red
    }
}

Build-And-Copy

# Watcher
$watcher = [System.IO.FileSystemWatcher]::new("$scriptDir\src", "*.java")
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

$global:debouncing = $false

Register-ObjectEvent $watcher "Changed" -Action {
    if ($global:debouncing) { return }
    $global:debouncing = $true
    Start-Sleep -Seconds 2
    Build-And-Copy
    $global:debouncing = $false
} | Out-Null

Write-Host "[WATCHING] Auto-rebuilding on changes..." -ForegroundColor Cyan
try { while ($true) { Start-Sleep 1 } }
finally { $watcher.Dispose(); Write-Host "Stopped." }
