""" A single tile in the game's world."""

from core.randomizer import Randomizer


class Tile():
    """Class representing a single tile.
    """


    def __init__(self, x: int, y: int, rgb=None):

        randomness = Randomizer.get_tile_randomness(x, y)

        if rgb == None:
            R = abs(x * 2 % 511 - 255)
            G = abs(y * 2% 511 - 255)
            B = randomness[0]
        else:
            R = rgb[0]
            G = rgb[1]
            B = rgb[2]
        self.color = [R, G, B]  #TODO: Actual color processing

    def get_color(self):
        """Get the RGB value of this tile.
        """
        return self.color