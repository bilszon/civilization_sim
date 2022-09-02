"""Graphic engine of the simulation. Executes all drawing on the canvas.
"""

import window_creator
import PIL
import PIL.ImageTk
import numpy as np

class GraphicEngine:
    """Engine managing drawing onscreen.
    """
    def __init__(self, simulation_window: window_creator.SimulationWindow):
        """Initialize the engine.

        Args:
            simulation_window (window_creator.SimulationWindow): Window containing the simulation. It will be updated by the engine.
        """
        self.simulation_window = simulation_window

        self.chunk = Chunk([255, 255, 0],[0, 255, 255])

        #self.simulation_window.canvas.create_image(128, 128, image=self.chunk.image)

    def graphic_update(self) -> None:
        """Redraw everything onscreen. A single frame of the simulation.
        """
        
        #print(self.chunk.image.width())

    #def display_chunk(self):
    #    self.simulation_window.canvas.create_image(128, 128, image=self.chunk)


class Chunk():
    def __init__(self, color1, color2):
        chunkdata = np.zeros((64, 64, 3), dtype=np.uint8)

        for i in range(64):
            for j in range(64):
                if i % 2 == 0:
                    chunkdata[i][j] = color1
                else:
                    chunkdata[i][j] = color2


        """ row1 = [color1] * 64
        row2 = [color2] * 64
        chunkdata = []
        for i in range(32):
            chunkdata.append(row1)
            chunkdata.append(row2)
        chunkdata = np.array(chunkdata)
        print(chunkdata) """
        image = PIL.Image.fromarray(chunkdata, mode="RGB")
        self.image = PIL.ImageTk.PhotoImage(image)


