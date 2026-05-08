# Creating new folders with if statements in PowerShell

# If new_folder exists, create if_folder
if (Test-Path "new_folder") {
    New-Item -ItemType Directory -Name "if_folder"
}


# If if_folder exists create hyperionDev otherwise create new-projects
if (Test-Path "if_folder") {
    New-Item -ItemType Directory -Name "hyperionDev"
}
else {
    New-Item -ItemType Directory -Name "new-projects"
}