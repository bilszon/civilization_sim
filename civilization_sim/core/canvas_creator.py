"""Canvas creator - used to create the basic window and canvas on which the simulation will be displayed."""

import tkinter as tk

def create_canvas(width, height):
    window = tk.Tk()
    canvas = tk.Canvas(window, width=width, height=height, bg = "#ffffff")
    canvas.pack()
    image = tk.PhotoImage(width=width, height=height)
    canvas.create_image((width/2, height/2), image=image, state="normal")
    tk.mainloop()
    return image
