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
    
    def get_noise_at_point(x: int, y: int) -> int:
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

        if x in Randomizer._x_noise.keys() and y in Randomizer._y_noise.keys():
            return (Randomizer._x_noise[x] + Randomizer._y_noise[y]) // 2

        noise_step = 128 # "Big steps" in generating noise.
        extremeness = 300

        max_x_step = (x // noise_step) * noise_step # Largest multiplication of noise_step smaller than x
        max_y_step = (y // noise_step) * noise_step # Largest multiplication of noise_step smaller than y

        target_x = max_x_step

        flag = True
        current_x = target_x

        while flag:
            if current_x in Randomizer._x_noise.keys():
                flag = False
            elif current_x > 0:
                current_x -= noise_step
            else:
                current_x += noise_step
        
        # Now we are sure that _x_noise[current_x] exists.

        while current_x != target_x:
            current_noise = Randomizer._x_noise[current_x]
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
            r = sha256(("NOISE_X" + str(Randomizer._seed) + str(current_x)).encode("utf-8")).digest()[0] / 256 # Terrible line. Hope it works.

            if r < chance_more_extreme:
                Randomizer._x_noise[current_x] = current_noise + c
            elif r < 0.65:
                Randomizer._x_noise[current_x] = current_noise
            else:
                Randomizer._x_noise[current_x] = current_noise - c

        x_noise = Randomizer._x_noise[current_x]

        target_y = max_y_step

        flag = True
        current_y = target_y

        while flag:
            if current_y in Randomizer._y_noise.keys():
                flag = False
            elif current_y > 0:
                current_y -= noise_step
            else:
                current_y += noise_step
        
        # Now we are sure that _y_noise[current_y] exists.

        while current_y != target_y:
            current_noise = Randomizer._y_noise[current_y]
            if target_y >= 0:
                current_y += noise_step
            else:
                current_y -= noise_step
            
            c = 0
            if current_noise > 0:
                    c = 1
            else:
                    c = -1
            chance_more_extreme = extremeness / (9 * abs(current_noise) + 3 * extremeness)
            r = sha256(("NOISE_Y" + str(Randomizer._seed) + str(current_y)).encode("utf-8")).digest()[0] / 256 # Terrible line. Hope it works.

            if r < chance_more_extreme:
                Randomizer._y_noise[current_y] = current_noise + c
            elif r < 0.65:
                Randomizer._y_noise[current_y] = current_noise
            else:
                Randomizer._y_noise[current_y] = current_noise - c

        y_noise = Randomizer._y_noise[current_y]

        return (x_noise + y_noise) // 2


#Randomizer.set_seed("aaa")
print(Randomizer.get_noise_at_point(10240, 10240))
print(Randomizer.get_noise_at_point(102400, 102400))
print(Randomizer.get_noise_at_point(102400, 102400))