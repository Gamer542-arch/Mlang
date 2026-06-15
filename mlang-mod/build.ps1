# MLang Mod Build Script
# Requirements: JDK 21+ (https://adoptium.net/)
# This script downloads Gradle and builds the mod .jar

$ErrorActionPreference = "Stop"

Write-Host "=== MLang Mod Builder ===" -ForegroundColor Cyan

# Check Java
$java = Get-Command java -ErrorAction SilentlyContinue
if (-not $java) {
    Write-Host "ERROR: Java not found! Install JDK 21+ from https://adoptium.net/" -ForegroundColor Red
    exit 1
}

$javaVer = & java -version 2>&1 | Select-String "version" | ForEach-Object { $_.ToString() }
Write-Host "Java: $javaVer"

# Check Gradle
$gradle = Get-Command gradle -ErrorAction SilentlyContinue
if (-not $gradle) {
    Write-Host "Gradle not found, downloading Gradle Wrapper..."
    $wrapperUrl = "https://services.gradle.org/distributions/gradle-8.12-bin.zip"
    $wrapperDir = "$env:TEMP\gradle-8.12"
    if (-not (Test-Path "$wrapperDir")) {
        Invoke-WebRequest $wrapperUrl -OutFile "$env:TEMP\gradle.zip"
        Expand-Archive "$env:TEMP\gradle.zip" -DestinationPath $env:TEMP -Force
    }
    $env:GRADLE_HOME = "$env:TEMP\gradle-8.12"
    $env:Path = "$env:GRADLE_HOME\bin;$env:Path"
}

# Generate wrapper
Write-Host "Generating Gradle Wrapper..."
gradle wrapper --gradle-version 8.12

# Build
Write-Host "Building mod..." -ForegroundColor Green
& .\gradlew.bat build

# Show result
$jar = Get-ChildItem "build\libs\*.jar" | Where-Object { $_.Name -like "mlang-mod*" -and $_.Name -notlike "*sources*" }
if ($jar) {
    Write-Host "BUILD SUCCESS!" -ForegroundColor Green
    Write-Host "Output: $($jar.FullName)" -ForegroundColor Yellow
    Write-Host "Size: $([math]::Round($jar.Length/1KB,1))KB" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Copy to Minecraft mods/ folder to use." -ForegroundColor Cyan
}
