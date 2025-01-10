# Anti-Idle-PC
**Anti Idle PC** app is designed to prevent your computer from going idle by simulating key presses at regular intervals. This helps to keep your PC awake and active, ensuring that it does not enter sleep mode or lock itself due to inactivity. The app allows you to customize the interval and unit of time for the simulated key presses, providing flexibility to suit your needs.

[Download Anti Idle PC](https://github.com/JohanFire/Anti-Idle-PC/releases/tag/v1.0)

![Demo v1.0](./images/demo_v_1_0.png)

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