@echo off
title CPU Scheduling Simulator - PS No. 80
cls
echo ========================================================
echo  RUNGTA INTERNATIONAL SKILLS UNIVERSITY
echo  SCHOOL OF COMPUTER SCIENCE AND ENGINEERING
echo  Project PS No. 80: CPU Scheduling Simulator
echo ========================================================
echo.

set JAVA_BIN=java
if exist "C:\Program Files\JetBrains\PyCharm 2025.3.3\jbr\bin\java.exe" (
    set "JAVA_BIN=C:\Program Files\JetBrains\PyCharm 2025.3.3\jbr\bin\java.exe"
)

"%JAVA_BIN%" -cp "%~dp0" CpuSchedulingSimulator %*
echo.
pause
