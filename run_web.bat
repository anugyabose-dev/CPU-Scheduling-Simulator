@echo off
title CPU Scheduling Simulator - Web Server
cls
echo ========================================================
echo  RUNGTA INTERNATIONAL SKILLS UNIVERSITY
echo  Starting CPU Scheduling Simulator Web Server...
echo ========================================================
echo.

set JAVA_BIN=java
if exist "C:\Program Files\JetBrains\PyCharm 2025.3.3\jbr\bin\java.exe" (
    set "JAVA_BIN=C:\Program Files\JetBrains\PyCharm 2025.3.3\jbr\bin\java.exe"
)

echo Starting browser at http://localhost:8080 ...
start "" "http://localhost:8080"
"%JAVA_BIN%" -cp "%~dp0" CpuSchedulingSimulator --web 8080
pause
