"""Canvas creator - used to create the basic window and canvas on which the simulation will be displayed."""

import tkinter as tk

class simulation_window():
    """Class containing and creating game's window and its core components"""
    def __init__(self, width, height):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=width, height=height, bg = "#ffffff")
        self.canvas.pack()
        self.image = tk.PhotoImage(width=width, height=height)
        self.canvas.create_image((width/2, height/2), image=self.image, state="normal")
    def mainloop(self):
        tk.mainloop()

