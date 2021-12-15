@echo off
for /f "tokens=*" %%s in (pid.txt) do (
  taskkill /F /PID %%s
)
@Rem Add create a shortcut of this file to stop the program after start up.