^Numpad1::
If WinExist("C:\Windows\py.exe")
	WinClose
Else
	Run, D:\Code\Private Code\D3 Bot\main.py
Return