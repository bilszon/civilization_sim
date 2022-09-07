""" Chunk represents a single 64*64 part of the world"""

from pickletools import uint8
import numpy as np
from . import tile

class Chunk():
    """A single chunk of the game's world. Takes 64*64 tiles, which means it takes 128*128 pixels onscreen.
    """

    CHUNK_SIZE = 64 # Measured in tiles, square

    def __init__(self):
        """Generate the chunk and all of the tiles within it.
        """
        self.tiles = np.empty((self.CHUNK_SIZE, self.CHUNK_SIZE), dtype=tile.Tile)
        for r in range(self.CHUNK_SIZE):
            for c in range(self.CHUNK_SIZE):
                self.tiles[r, c] = tile.Tile() #TODO: Generate proper tiles

    def RGB_array(self):
        """Return an array of RGB values of chunk's tiles
        """
        
        array = np.empty((self.CHUNK_SIZE, self.CHUNK_SIZE, 3), dtype=np.uint8)
        for r in range(self.CHUNK_SIZE):
            for c in range(self.CHUNK_SIZE):
                array[r, c] = self.tiles[r, c].get_color()
        
        return array
