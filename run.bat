@echo off
title CineAlert - BMS & District Show Monitor
echo ========================================================
echo        Starting CineAlert Movie Show Monitor
echo ========================================================
echo.

python -c "import fastapi, uvicorn" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing missing dependencies...
    pip install -r requirements.txt
)

echo Starting CineAlert on http://127.0.0.1:8000 ...
python main.py
pause
