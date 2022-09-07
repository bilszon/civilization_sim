"""Graphic engine of the simulation. Executes all drawing on the canvas.
"""

from . import window_creator
import PIL
import PIL.ImageTk
import numpy as np
from world_generation import chunk, chunk_manager

class GraphicEngine:
    """Engine managing drawing onscreen.
    """
    def __init__(self, simulation_window: window_creator.SimulationWindow):
        """Initialize the engine.

        Args:
            simulation_window (window_creator.SimulationWindow): Window containing the simulation. It will be updated by the engine.
        """
        self.simulation_window = simulation_window

        self.chmng = chunk_manager.ChunkManager()
    
        self.simulation_window.canvas.create_image(128, 128, image=self.chmng.get_chunk_image(0, 0))
        
        


    def graphic_update(self) -> None:
        """Redraw everything onscreen. A single frame of the simulation.
        """
    
    
    def _RGB_to_Image(self, RGB_array):
        image1 = PIL.Image.fromarray(RGB_array, mode="RGB")
        return PIL.ImageTk.PhotoImage(image1)

