"""Provides seed-dependent randomness, required to be able to reproduce worlds."""

from hashlib import sha256
from random import Random

class Randomizer():
    """Static class providing seed-dependent randomness. Set seed before using.

    
    """
    _seed = 0

    # Is the randomizer ready to use? Is the seed set?
    _randomizer_set = False

    # Salt used to improve unpredictability of the results
    _GAME_SALT = "CIVILIZATION_SIM"
    _CHUNK_SALT = "CHUNK"
    _TILE_SALT = "TILE"

    def set_seed(seed):
        Randomizer._randomizer_set = True
        Randomizer._seed = seed

    def get_chunk_randomness(x: int, y: int) -> str:
        """Generates 256 bits of pseudo-random data used for chunk generation.
        For same seed and same (x, y) coordinates it gives the same data, so results can be reproduced.

        Args:
            x (int): x (horizontal) coordinate of the chunk (in chunk coords, not tile/world).
            y (int): y (vertical) coordinate of the chunk (in chunk coords, not tile/world).

        Returns:
            str: 256 bits of pseudo-randomness as hexadecimal.
        """

        if not Randomizer._randomizer_set:
            randomizer = Random()
            Randomizer.set_seed(randomizer.getrandbits(64))

        chunk_string = str(x) + "," + str(y)
        hash_base = str(Randomizer._seed) + Randomizer._GAME_SALT + Randomizer._CHUNK_SALT + chunk_string
        return sha256(hash_base.encode("utf-8")).digest()

    def get_chunk_randomness(x: int, y: int) -> str:
        """Generates 256 bits of pseudo-random data used for tile generation.
        For same seed and same (x, y) coordinates it gives the same data, so results can be reproduced.

        Args:
            x (int): x (horizontal) coordinate of the tile.
            y (int): y (vertical) coordinate of the tile.

        Returns:
            str: 256 bits of pseudo-randomness as hexadecimal.
        """

        if not Randomizer._randomizer_set:
            randomizer = Random()
            Randomizer.set_seed(randomizer.getrandbits(64))

        chunk_string = str(x) + "," + str(y)
        hash_base = str(Randomizer._seed) + Randomizer._GAME_SALT + Randomizer._TILE_SALT + chunk_string
        return sha256(hash_base.encode("utf-8")).digest()

