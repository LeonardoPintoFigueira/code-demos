#Leonardo Pinto
#Date: 8/11/2023
#Objective: Automate Windows 10 Endpoint (Automatic screen lock; Antivirus installed and scanning; automatic OS enable)

#Automatci Screenlock

#Time for screenlock
$screenLockTimeoutInSeconds = 300  

#Set Screenlock
Write-Host "Setting screen lock timeout to $screenLockTimeoutInSeconds seconds..."
$timeoutInMilliseconds = $screenLockTimeoutInSeconds * 1000
$regPath = "HKCU:\Control Panel\Desktop"
Set-ItemProperty -Path $regPath -Name ScreenSaveTimeOut -Value $timeoutInMilliseconds

#Enable
Write-Host "Enabling screen lock..."
$regPath = "HKCU:\Software\Policies\Microsoft\Windows\Control Panel\Desktop"
$lockScreenRegKey = "ScreenSaverIsSecure"
$lockScreenValue = 1
if (Test-Path -Path $regPath) {
    Set-ItemProperty -Path $regPath -Name $lockScreenRegKey -Value $lockScreenValue
} else {
    New-Item -Path $regPath
    Set-ItemProperty -Path $regPath -Name $lockScreenRegKey -Value $lockScreenValue
}

# Script to automate Antivirus check and enable Automatic OS Updates for Windows 10

# Check if antivirus software is installed
Write-Host "Checking for installed antivirus software..."
$antivirusProducts = Get-WmiObject -Namespace "root\SecurityCenter2" -Class AntiVirusProduct
$antivirusInstalled = $antivirusProducts.Count -gt 0

if ($antivirusInstalled) {
    Write-Host "Antivirus software is installed on this system."
} else {
    Write-Host "No antivirus software is installed on this system."
}

# Enable Automatic OS Updates
Write-Host "Enabling Automatic OS Updates..."
$automaticUpdates = New-Object -ComObject Microsoft.Update.AutoUpdate
$automaticUpdates.SetPolicy(3)  # 3 means "Auto download and notify for install"


# Force a Group Policy update to apply changes immediately
gpupdate /force

Write-Host "Automatic screen lock configuration completed."
