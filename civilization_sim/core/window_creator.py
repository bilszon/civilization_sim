"""Window creator - used to create the basic window and canvas on which the simulation will be displayed."""

import tkinter as tk

class SimulationWindow():
    """Class containing and creating game's window and its core components"""

    def __init__(self, width: int, height: int):
        """Default constructor that initializes all basic window components.

        Args:
            width (int): The width of created window.
            height (int): The height of created window.
        """

        self.width = width
        self.height = height

        self.window = tk.Tk()

        self.canvas = tk.Canvas(self.window, width=width, height=height, bg = "#ffffff")
        self.canvas.pack()

        # Create a background empty image to force window's width and height.
        self.image = tk.PhotoImage(width=width, height=height)
        self.canvas.create_image((width/2, height/2), image=self.image, state="normal")

    def mainloop(self):
        """Calls the mainloop of the window. Locks.
        """
        tk.mainloop()

