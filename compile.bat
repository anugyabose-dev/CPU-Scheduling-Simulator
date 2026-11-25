@echo off
title Compile CPU Scheduling Simulator
cls
echo Compiling CpuSchedulingSimulator.java ...

set JAVAC_BIN=javac
if exist "C:\Program Files\JetBrains\PyCharm 2025.3.3\jbr\bin\javac.exe" (
    set "JAVAC_BIN=C:\Program Files\JetBrains\PyCharm 2025.3.3\jbr\bin\javac.exe"
)

"%JAVAC_BIN%" -d "%~dp0" "%~dp0CpuSchedulingSimulator.java" "%~dp0WebAssets.java"
if %errorlevel% equ 0 (
    echo Compilation successful!
) else (
    echo Compilation failed with error code %errorlevel%.
)
echo.
pause
