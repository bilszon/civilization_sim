"""Graphic engine of the simulation. Executes all drawing on the canvas.
"""

import PIL.ImageTk

from world_generation import chunk_manager
from world_generation.chunk import Chunk
from . import window_creator

class GraphicEngine:
    """Engine managing drawing onscreen.
    """

    def __init__(self, simulation_window: window_creator.SimulationWindow):
        """Initialize the engine.

        Args:
            simulation_window (window_creator.SimulationWindow): Window containing the simulation. It will be updated by the engine.
        """

        self.simulation_window = simulation_window
    
        # Center of the view.
        self.camera_x = 0
        self.camera_y = 0

        self.window_width = simulation_window.width
        self.window_height = simulation_window.height


    def graphic_update(self) -> None:
        """Redraw everything onscreen. A single frame of the simulation.
        """
        self.simulation_window.canvas.delete("all")

        mid_point = (self.window_width // 2, self.window_height // 2)

        l_border = self.camera_x - self.window_width // 2 - 1
        r_border = self.camera_x + self.window_width // 2 + 1
        b_border = self.camera_y + self.window_height // 2 + 1
        t_border = self.camera_y - self.window_height // 2 - 1

        l_chunk = l_border // (Chunk.CHUNK_SIZE * 2)
        r_chunk = r_border // (Chunk.CHUNK_SIZE * 2) + 1
        b_chunk = b_border // (Chunk.CHUNK_SIZE * 2) + 1
        t_chunk = t_border // (Chunk.CHUNK_SIZE * 2)

        for r in range(t_chunk, b_chunk + 1):
            for c in range(l_chunk, r_chunk + 1):
                self.simulation_window.canvas.create_image(mid_point[0] + c * (Chunk.CHUNK_SIZE * 2) - self.camera_x, mid_point[1] + r * (Chunk.CHUNK_SIZE * 2) - self.camera_y, image=chunk_manager.ChunkManager.get_chunk_image(c, r))

