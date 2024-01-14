import tkinter as tk
from tkinter import ttk
import sv_ttk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Chat App By Pyae Sone Htoo')
        self.geometry('450x600')
        sv_ttk.set_theme('light')
        
if __name__ == '__main__':
    app = Main()
    app.mainloop()