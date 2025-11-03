.\.venv\Scripts\activate.ps1
pyinstaller --onefile --icon=.\Grass_Block_JE7_BE6.ico .\SchematicToObj.py

Copy-Item -Path ".\assets" -Destination ".\dist" -Recurse -Force