@ECHO OFF
START /B gallery_server.exe
FOR /L %%i IN (1,1,100) DO (
  (TASKLIST | FIND /I "gallery_server.exe") && GOTO :startnext
  ping 127.0.0.1 -n 1 > nul
  :: you might add here some delaying
)
ECHO Timeout waiting for gallery_server.exe to start
GOTO :EOF

:startnext
START /B f.exe
FOR /L %%i IN (1,1,100) DO (
  (TASKLIST | FIND /I "f.exe") && GOTO :startnext1
  ping 127.0.0.1 -n 1 > nul
  :: you might add here some delaying
)
ECHO Timeout waiting for f.exe to start
GOTO :EOF

:startnext1
START aris.exe