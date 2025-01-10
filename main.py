import tkinter

from utils.App import App
from utils.screen import render_center_of_screen

def main():
    root = tkinter.Tk()

    root.title("Anti Idle PC")

    width, height, x, y = render_center_of_screen(root, width=400, height=120)
    
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(width=False, height=False)
    root.configure(bg='#333333')

    app = App(root, userNumber=3, userType="minutes")

    root.mainloop()

if __name__ == '__main__':
    main()