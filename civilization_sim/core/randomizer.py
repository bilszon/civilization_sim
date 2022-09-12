"""Provides seed-dependent randomness, required to be able to reproduce worlds."""

from math import pi, sin
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

    # Cache for height noise generation
    _x_noise = {0:0}
    _y_noise = {0:0}

    def set_seed(seed):
        Randomizer._randomizer_set = True
        Randomizer._seed = seed

    def get_chunk_randomness(x: int, y: int) -> bytes:
        """Generates 256 bits of pseudo-random data used for chunk generation.
        For same seed and same (x, y) coordinates it gives the same data, so results can be reproduced.

        Args:
            x (int): x (horizontal) coordinate of the chunk (in chunk coords, not tile/world).
            y (int): y (vertical) coordinate of the chunk (in chunk coords, not tile/world).

        Returns:
            bytes: 256 bits of pseudo-randomness as bytes.
        """

        if not Randomizer._randomizer_set:
            randomizer = Random()
            Randomizer.set_seed(randomizer.getrandbits(64))

        chunk_string = str(x) + "," + str(y)
        hash_base = str(Randomizer._seed) + Randomizer._GAME_SALT + Randomizer._CHUNK_SALT + chunk_string
        return sha256(hash_base.encode("utf-8")).digest()

    def get_tile_randomness(x: int, y: int) -> bytes:
        """Generates 256 bits of pseudo-random data used for tile generation.
        For same seed and same (x, y) coordinates it gives the same data, so results can be reproduced.

        Args:
            x (int): x (horizontal) coordinate of the tile.
            y (int): y (vertical) coordinate of the tile.

        Returns:
            bytes: 256 bits of pseudo-randomness as bytes.
        """

        if not Randomizer._randomizer_set:
            randomizer = Random()
            Randomizer.set_seed(randomizer.getrandbits(64))

        chunk_string = str(x) + "," + str(y)
        hash_base = str(Randomizer._seed) + Randomizer._GAME_SALT + Randomizer._TILE_SALT + chunk_string
        return sha256(hash_base.encode("utf-8")).digest()
    
    def get_noise_at_point(x: int, y: int) -> int: # Do not touch. It is cursed.
        """Gives a random height noise at point (x, y).

        Args:
            x (int): x (horizontal) coordinate of the tile.
            y (int): y (vertical) coordinate of the tile.

        Returns:
            int: Height noise at point (x, y)
        """

        if not Randomizer._randomizer_set:
            randomizer = Random()
            Randomizer.set_seed(randomizer.getrandbits(64))

        """ if x in Randomizer._x_noise.keys() and y in Randomizer._y_noise.keys():
            return (Randomizer._x_noise[x] + Randomizer._y_noise[y]) // 2 """

        noise_step = 128 # "Big steps" in generating noise.
        extremeness = 150

        max_x_step = (x // noise_step) * noise_step # Largest multiplication of noise_step smaller than x
        max_y_step = (y // noise_step) * noise_step # Largest multiplication of noise_step smaller than y

        def get_noise(value, axis):
            target_x = value

            if axis == "x":
                noise_cache = Randomizer._x_noise
                hash_str = "NOISE_X"
            else:
                noise_cache = Randomizer._y_noise
                hash_str = "NOISE_Y"

            flag = True
            current_x = target_x

            while flag:
                if current_x in noise_cache.keys():
                    flag = False
                elif current_x > 0:
                    current_x -= noise_step
                else:
                    current_x += noise_step

            while current_x != target_x:
                current_noise = noise_cache[current_x]
                if target_x >= 0:
                    current_x += noise_step
                else:
                    current_x -= noise_step
                
                c = 0
                if current_noise > 0:
                        c = 1
                else:
                        c = -1
                chance_more_extreme = extremeness / (9 * abs(current_noise) + 3 * extremeness)
                r = sha256((hash_str + str(Randomizer._seed) + str(current_x)).encode("utf-8")).digest()[0] / 256 # Terrible line. Hope it works.

                if r < chance_more_extreme:
                    noise_cache[current_x] = current_noise + c
                elif r < 0.65:
                    noise_cache[current_x] = current_noise
                else:
                    noise_cache[current_x] = current_noise - c

            return noise_cache[current_x]

        # "Main" noise
        x_noise = 10 * get_noise(max_x_step, "x")
        y_noise = 10 * get_noise(max_y_step, "y")

        next_x_noise = 10 * get_noise(max_x_step + noise_step, "x")
        next_y_noise = 10 * get_noise(max_y_step + noise_step, "y")

        """ noise_step = 1
        small_x_noise = get_noise(x, "x") - x_noise
        small_y_noise = get_noise(y, "y") - y_noise

        final_x_noise = 0 """

        x_sin_1 = sha256(("X_SIN_1" + str(Randomizer._seed) + str(max_x_step)).encode("utf-8")).digest()[0] // 128
        x_sin_2 = sha256(("X_SIN_2" + str(Randomizer._seed) + str(max_x_step)).encode("utf-8")).digest()[0] // 16
        y_sin_1 = sha256(("Y_SIN_1" + str(Randomizer._seed) + str(max_y_step)).encode("utf-8")).digest()[0] // 128
        y_sin_2 = sha256(("Y_SIN_2" + str(Randomizer._seed) + str(max_y_step)).encode("utf-8")).digest()[0] // 16

        x_proc = (x - max_x_step) / noise_step
        y_proc = (y - max_y_step) / noise_step

        x_mod = sin(2*pi* x_sin_1 * x_proc) + 0.2 * sin(2*pi* x_sin_2 * x_proc)
        y_mod = sin(2*pi* y_sin_1 * y_proc) + 0.2 * sin(2*pi* y_sin_2 * y_proc)

        final_x = (next_x_noise - x_noise) * x_proc + x_noise + x_mod
        final_y = (next_y_noise - y_noise) * y_proc + y_noise + y_mod

        return int((final_x + final_y)) // 2