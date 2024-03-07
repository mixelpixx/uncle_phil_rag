@echo off
start /min cmd /C python main.py
start /min cmd /C GUI\build\windows\runner\Release\app.exe
exit