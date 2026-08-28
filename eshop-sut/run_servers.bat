@echo off
setlocal

set "ROOT=%~dp0"

where node >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js was not found in PATH.
    echo Install Node.js 18 or newer, then run this file again.
    exit /b 1
)

where npm >nul 2>&1
if errorlevel 1 (
    echo [ERROR] npm was not found in PATH.
    echo Reinstall Node.js with npm, then run this file again.
    exit /b 1
)

call :check_dependencies "backend"
if errorlevel 1 exit /b 1

call :check_dependencies "frontend-web"
if errorlevel 1 exit /b 1

call :check_dependencies "frontend-admin"
if errorlevel 1 exit /b 1

echo Starting EShop services...
echo.
echo Backend API:      http://localhost:3000
echo Customer Web:     http://localhost:5173
echo Admin Web:        http://localhost:5174
echo.
echo Each service opens in a separate window.
echo Press Ctrl+C in a service window to stop that service.
echo.

start "EShop Backend" /D "%ROOT%backend" cmd /k "node server.js"
start "EShop Customer Web" /D "%ROOT%frontend-web" cmd /k "npm run dev -- --host 0.0.0.0"
start "EShop Admin Web" /D "%ROOT%frontend-admin" cmd /k "npm run dev -- --host 0.0.0.0"

echo All service commands were launched.
exit /b 0

:check_dependencies
if not exist "%ROOT%%~1\node_modules\" (
    echo [ERROR] Dependencies are missing for %~1.
    echo Run: cd /d "%ROOT%%~1" ^&^& npm install
    exit /b 1
)
exit /b 0
