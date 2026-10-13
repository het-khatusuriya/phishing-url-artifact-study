@echo off
REM Start the Phishing URL Risk Checker desktop app
cd /d "%~dp0"
python url_checker_gui.py
if errorlevel 1 pause
