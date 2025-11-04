Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\Administrator\Downloads\my_site\start_flask.bat" & Chr(34), 0
Set WshShell = Nothing
