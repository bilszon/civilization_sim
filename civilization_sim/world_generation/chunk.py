""" Chunk represents a single 64*64 part of the world"""

from pickletools import uint8
import numpy as np
from . import tile

class Chunk():
    """A single chunk of the game's world. Takes 64*64 tiles, which means it takes 128*128 pixels onscreen.
    """

    CHUNK_SIZE = 64 # Measured in tiles, square

    def __init__(self, x: int, y: int):
        """Generate the chunk and all of the tiles within it.

        Args:
            x (int): x (horizontal) coordinate of the chunk (in chunk coords, not tile/world).
            y (int): y (vertical) coordinate of the chunk (in chunk coords, not tile/world).
        """
        
        print("Generating new chunk at (" + str(x) + ", " + str(y) + ").")

        self.x = x
        self.y = y

        self.tiles = np.empty((self.CHUNK_SIZE, self.CHUNK_SIZE), dtype=tile.Tile)
        for r in range(self.CHUNK_SIZE):
            tile_y = y * Chunk.CHUNK_SIZE + r
            for c in range(self.CHUNK_SIZE):
                tile_x = x * Chunk.CHUNK_SIZE + c
                if r == 0 or c == 0:
                    self.tiles[r, c] = tile.Tile(tile_x, tile_y, rgb=(0, 0, 0))
                else:
                    self.tiles[r, c] = tile.Tile(tile_x, tile_y) #TODO: Generate proper tiles

    def RGB_array(self):
        """Return an array of RGB values of chunk's tiles. Each tile covers a 2x2 area, so it's 4 pixels.
        """
        
        array = np.empty((self.CHUNK_SIZE * 2, self.CHUNK_SIZE * 2, 3), dtype=np.uint8)
        for r in range(self.CHUNK_SIZE * 2):
            for c in range(self.CHUNK_SIZE * 2):
                array[r, c] = self.tiles[r//2, c//2].get_color()
        
        return array
