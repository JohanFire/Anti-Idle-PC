# Anti-Idle-PC
Anti Idle PC simple app

## Create one-file bundled executable
```bash
pyinstaller main.py --onefile -w --name "Anti Idle PC"

# or

pyinstaller --onefile -w --name "Anti Idle PC" --icon=assets\icon.ico --add-data "assets/icon.ico;." .\main.py
```