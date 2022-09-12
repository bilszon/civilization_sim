""" A single tile in the game's world."""

from core.randomizer import Randomizer


class Tile():
    """Class representing a single tile.
    """


    def __init__(self, x: int, y: int, rgb=None):

        randomness = Randomizer.get_tile_randomness(x, y)

        if rgb == None:
            h = Randomizer.get_noise_at_point(x, y) + 10
            if h < 0:
                R = 0
                G = 15
                B = 255 + 4 * h
            elif h == 0:
                R = 100
                G = 100
                B = 255
            elif h < 3:
                R = 255
                G = 255
                B = 0
            elif h < 20:
                R = 0
                G = 155 + 5 * h
                B = 15
            elif h == 20:
                R = 127
                G = 255
                B = 127
            else:
                R = 255 - h
                G = 255 - h
                B = 255 - h
        else:
            R = rgb[0]
            G = rgb[1]
            B = rgb[2]
        self.color = [R, G, B]  #TODO: Actual color processing

    def get_color(self):
        """Get the RGB value of this tile.
        """
        return self.color