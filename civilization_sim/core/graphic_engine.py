"""Graphic engine of the simulation. Executes all drawing on the canvas.
"""

from email.mime import image
from . import window_creator
import PIL
import PIL.ImageTk
import numpy as np
from world_generation import chunk

class GraphicEngine:
    """Engine managing drawing onscreen.
    """
    def __init__(self, simulation_window: window_creator.SimulationWindow):
        """Initialize the engine.

        Args:
            simulation_window (window_creator.SimulationWindow): Window containing the simulation. It will be updated by the engine.
        """
        self.simulation_window = simulation_window

        self.chunk = chunk.Chunk()
        

        self.img1 = self.RGB_to_Image(self.chunk.RGB_array())
        self.simulation_window.canvas.create_image(128, 128, image=self.img1)
        print("Wow")
    def graphic_update(self) -> None:
        """Redraw everything onscreen. A single frame of the simulation.
        """
    
    
    def RGB_to_Image(self, RGB_array):
        print(RGB_array)
        image1 = PIL.Image.fromarray(RGB_array, mode="RGB")
        self.simulation_window.canvas.create_image(128, 128, image=PIL.ImageTk.PhotoImage(image1))
        return PIL.ImageTk.PhotoImage(image1)

