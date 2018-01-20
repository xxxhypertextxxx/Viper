import sys
import tkinter as tk

class Std:
    def __init__(self):
        self.core = "core.class"
        self.std = tk.Tk()

    def out(self, text):
        tk.Label(self.std, text=text).grid()

    def quit(self):
        self.std.destroy()
        sys.exit()

    def run(self):
        self.std.mainloop()
