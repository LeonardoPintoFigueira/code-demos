#Name: Leonardo Pinto 
#Date: November 18, 2023
#Objective: Change password complexety policy


# Specify the path for the temporary file
$tempFilePath = "C:\Temp\secpol.cfg"

# Export the current security policy to the temporary file
secedit.exe /export /cfg $tempFilePath

# Read the content of the temporary file
$content = Get-Content $tempFilePath

# Modify the line that sets PasswordComplexity from 0 to 1
$content = $content -replace 'PasswordComplexity = 0', 'PasswordComplexity = 1'

# Write the modified content back to the temporary file
$content | Set-Content $tempFilePath -Force

# Apply the modified security policy
secedit.exe /configure /db $env:windir\securitynew.sdb /cfg $tempFilePath /areas SECURITYPOLICY
