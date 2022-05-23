
$cmd = "wsl.exe ./send-image -g 64x64 -h <localhost> test.jpg"
$ps = Start-Process PowerShell.exe -ArgumentList $cmd