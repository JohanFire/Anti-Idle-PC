# Anti-Idle-PC
Anti Idle PC simple app

## Create one-file bundled executable
```bash
pyinstaller main.py --onefile -w --name "Anti Idle PC"

# or

pyinstaller --onefile -w --name "Anti Idle PC" --icon=assets\icon.ico --add-data "assets/icon.ico;." .\main.py
```

## auto-py-to-exe
Working command with icon for app and taskbar.
```bash
pyinstaller --noconfirm --onefile --windowed --icon "C:\Users\tjo1ga\Documents\Github\Anti-Idle-PC\assets\icon.ico" --name "Anti Idle PC" --add-data "C:\Users\tjo1ga\Documents\Github\Anti-Idle-PC\assets;assets/"  "C:\Users\tjo1ga\Documents\Github\Anti-Idle-PC\main.py"
```