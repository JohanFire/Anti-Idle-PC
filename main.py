import tkinter
import ctypes
import socket
import tkinter.messagebox

from utils.single_instance_manager import SingleInstanceManager
from utils.App import App
from utils.system_tray import SystemTray
from utils.screen import render_center_of_screen
from utils.constants import *
from utils.image_handler import resource_path

def main():
    instanceManager = SingleInstanceManager(port=PORT, address=ADDRESS)
    
    # Check if another instance is running
    if instanceManager.is_instance_running():
        print("Anti Idle PC is already running.")
        return

    root = tkinter.Tk()

    root.title("Anti Idle PC")

    width, height, x, y = render_center_of_screen(root, width=400, height=120)
    
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(width=False, height=False)
    root.configure(bg='#333333')

    app = App(root, userNumber=3, userType="minutes")
    
    systemTray = SystemTray(root)

    # Start the single instance server
    instanceManager.start_server(systemTray.show_window)

    myAppID = 'JohanFire.Anti_Idle_PC'  # abitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)
    root.iconbitmap(resource_path(ICON))

    root.mainloop()

if __name__ == '__main__':
    main()