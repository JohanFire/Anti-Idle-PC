import tkinter
import ctypes

from utils.App import App
from utils.screen import render_center_of_screen
from utils.constants import *
from utils.image_handler import resource_path

def main():
    root = tkinter.Tk()

    root.title("Anti Idle PC")

    width, height, x, y = render_center_of_screen(root, width=400, height=120)
    
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(width=False, height=False)
    root.configure(bg='#333333')

    app = App(root, userNumber=3, userType="minutes")

    myAppID = 'JohanFire.Anti_Idle_PC'  # abitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)

    root.iconbitmap(resource_path(ICON))
    root.mainloop()

if __name__ == '__main__':
    main()