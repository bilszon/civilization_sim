""" A single tile in the game's world."""

import random #TEMP


class Tile():
    """Class representing a single tile.
    """


    def __init__(self, x: int, y: int, rgb=None):

        if rgb == None:
            R = x % 255
            G = y // 2 % 255
            B = 0
        else:
            R = rgb[0]
            G = rgb[1]
            B = rgb[2]
        self.color = [R, G, B]  #TODO: Actual color processing

    def get_color(self):
        """Get the RGB value of this tile.
        """
        return self.color