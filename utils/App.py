""" 
Colors:
    - Pink: #FF3399
    - Gray background: #333333
"""

import tkinter
from tkinter import ttk
import webbrowser
import re
from pyautogui import press

from utils.screen import render_center_of_screen

class App:
    def __init__(self, master):
        self.userNumber: int = 3
        self.userType: str = "seconds"
        self.interval_ms: int = self.calculate_interval_ms(self.userNumber, self.userType)
        self.pressKey: str = "f3"

        self.master = master
        # master.title("Anti Idle PC")

        self.frame = tkinter.Frame(bg='#333333')

        """ Frame Widgets """
        self.wakeLabel  = tkinter.Label(
            self.frame, text='Wake PC every: ', bg='#333333', fg='white', font=("Arial", 12)
            ).grid(row=0, column=0, sticky='news', pady=10)

        self.idleEveryNumberVar = tkinter.IntVar()
        self.idleEveryNumber = tkinter.Spinbox(
            self.frame, from_=1, to='infinity', increment=1,
            font=("Arial", 10), width=6, # validate='key',
            textvariable=self.idleEveryNumberVar , # command=self.get_idle_time
        )
        self.idleEveryNumber.grid(row=0, column=1, pady=10)
        self.idleEveryNumber.delete(0, "end")  # delete every existing value
        self.idleEveryNumber.insert(0, self.userNumber)  # stablish default value to 3 in index 0

        self.cmbBoxSeconds = ttk.Combobox(
            self.frame, values=["seconds", "minutes", "hours"],
            font=("Arial", 10), width=10, state='readonly'
        )
        self.cmbBoxSeconds.grid(row=0, column=2, pady=10, padx=5)
        self.cmbBoxSeconds.set(self.userType)
        # self.cmbBoxSeconds.bind('<<ComboboxSelected>>', self.get_idle_time)


        self.info_button = tkinter.Button(
            self.frame, text='info', border=0, bg='#333333', fg='#636e72', font=("Arial", 14),
            cursor='hand2', activebackground='#333333', activeforeground='#FFFFFF',
            command=self.info_action
            ).grid(row=3, column=1, pady=25)

        self.frame.pack()

        self.get_idle_time()
        self.press_key()

    def calculate_interval_ms(self, number, unit):
        if unit == "seconds":
            return number * 1000
        elif unit == "minutes":
            return number * 60 * 1000
        elif unit == "hours":
            return number * 60 * 60 * 1000

    def get_idle_time(self, event = None) -> None:
        updatedUserNumber = int(self.idleEveryNumber.get())
        updatedUserType = str(self.cmbBoxSeconds.get())

        # print(f"Default: {self.userNumber} {self.userType}")
        # print(f"Wake every {updatedUserNumber} {updatedUserType}")
        # print(f"DefaultType: {type(self.userNumber)} {type(self.userType)}")
        # print(f"Wake every Type {type(updatedUserNumber)} {type(updatedUserType)}")
        # print()

        self.master.after(1000, self.get_idle_time)  # Check for updates every second

        if self.userNumber != updatedUserNumber or self.userType != updatedUserType:
            self.userNumber = updatedUserNumber
            self.userType = updatedUserType
            self.interval_ms = self.calculate_interval_ms(self.userNumber, self.userType)
            print(f"Updated: {self.userNumber} {self.userType}, Interval: {self.interval_ms} ms")
    
    def press_key(self):
        print(f"{self.pressKey} pressed")
        press(self.pressKey)  # Simulate pressing the self.pressKey key
        print(f"Waiting {self.interval_ms} ms")
        self.master.after(self.interval_ms, self.press_key)  # Schedule the next key press

    # def press_key(self):
    #     print(f"{self.pressKey} pressed")
    #     press(self.pressKey)  # Simulate pressing the self.pressKey key
    #     self.schedule_next_key_press()

    # def schedule_next_key_press(self):
    #     print(f"Waiting {self.interval_ms} ms")
    #     self.master.after(self.interval_ms, self.press_key)  # Schedule the next key press

    def callback(self, url: str):
        webbrowser.open_new_tab(url)

    def info_action(self):
        info_window = tkinter.Toplevel(self.master)
        info_window.title("Info")
        # width, height, x, y = render_center_of_screen(info_window, width=400, height=200)
        width, height, x, y = render_center_of_screen(info_window, width=320, height=90)
        info_window.geometry(f"{width}x{height}+{x}+{y}")
        info_window.resizable(width=False, height=False)
        info_window.configure(bg='#333333')

        # blankSpace = tkinter.Label(info_window, text='', bg='#333333', pady=50).pack()

        version = tkinter.Label(info_window, 
            text='v1.0', 
            bg='#333333', fg='white', font=("Arial", 12),
            ).pack()

        github = tkinter.Label(info_window, 
            text='Check open source project', 
            bg='#333333', fg='#74dfec', font=("Arial", 12), #pady=60,
            cursor='hand2',
            )
        github.pack()
        github.bind("<Button-1>", lambda e: self.callback("http://www.github.com/johanfire"))
        
        johanfire = tkinter.Label(info_window, 
            text='www.johanfire.com', cursor='hand2',
            bg='#333333', fg='#f86b93', font=("Arial", 12),
            )
        johanfire.pack()
        johanfire.bind("<Button-1>", lambda e: self.callback("http://www.johanfire.com"))