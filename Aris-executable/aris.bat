@ECHO OFF
START /B gallery_server.exe
START /B f.exe
ping 127.0.0.1 -n 3 > nul
START aris.exe