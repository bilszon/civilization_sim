""" A single tile in the game's world."""

import random #TEMP


class Tile():
    """Class representing a single tile.
    """

    def __init__(self):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        self.color = [R, G, B]  #TODO: Actual color processing

    def get_color(self):
        """Get the RGB value of this tile.
        """
        return self.color