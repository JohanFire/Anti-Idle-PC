import tkinter
from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading

from utils.image_handler import resource_path
from utils.constants import IMAGE_ICON

class SystemTray:
    def __init__(self, root: tkinter.Tk):
        self.root = root

        self.imageIcon = Image.open(resource_path(IMAGE_ICON))

        # Create System Tray icon
        self.icon = Icon("App", self.imageIcon, menu=Menu(
            MenuItem("Open", self.show_window),
            MenuItem("Hide", self.hide_window),
            MenuItem("Exit", self.quit_app)
        ))

        # Run System Tray icon in a separate thread
        self.tray_thread = threading.Thread(target=self.icon.run, daemon=True)
        self.tray_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.hide_window) # When closing app with 'X'
        self.root.bind("<Unmap>", self.handle_minimize) # When minimizing app

    def handle_minimize(self, event):
        """ Handle minimize event to hide the window. """
        if self.root.state() == "iconic": # if minimized
            self.hide_window()
    
    def show_window(self):
        """ Show main window. """
        self.root.deiconify()

    def hide_window(self):
        """ Hide main window. """
        self.root.withdraw()
        # tkinter.messagebox.showinfo("Info", "App still running in System Tray.")

    def quit_app(self, icon=None, item=None):
        """ Close the app. """
        self.icon.stop()
        self.root.destroy()

    def run(self):
        """ Run the app in the System Tray. """
        self.root.mainloop()