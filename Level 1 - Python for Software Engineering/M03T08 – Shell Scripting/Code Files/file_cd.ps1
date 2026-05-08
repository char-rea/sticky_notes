#Creating, navigating, and removing folders in PowerShell

# Create three new folders
New-Item -ItemType Directory -Name "Love"
New-Item -ItemType Directory -Name "Happy"
New-Item -ItemType Directory -Name "Excited"

# Navigate inside one of the folders
Set-Location Love

# Create three new folders inside the current folder
New-Item -ItemType Directory -Name "One"
New-Item -ItemType Directory -Name "Two"
New-Item -ItemType Directory -Name "Three"

# Remove two of the folders created
Remove-Item "Two"
Remove-Item "Three"