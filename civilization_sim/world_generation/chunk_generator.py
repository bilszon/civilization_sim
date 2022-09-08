from hashlib import sha256
from random import Random

class ChunkGenerator():
    seed = 0

    _randomizer_set = False

    _GAME_SALT = "CIVILIZATION_SIM"

    def set_seed(seed):
        ChunkGenerator._randomizer_set = True
        ChunkGenerator.seed = seed

    def get_chunk_randomness(x: int, y: int) -> str:
        """Generates 256 bits of pseudo-random data used for chunk generation.
        For same seed and same (x, y) coordinates it gives the same data, so results can be reproduced.

        Args:
            x (int): x (horizontal) coordinate of the chunk (in chunk coords, not tile/world).
            y (int): y (vertical) coordinate of the chunk (in chunk coords, not tile/world).

        Returns:
            str: 256 bits of pseudo-randomness as hexadecimal.
        """

        if not ChunkGenerator._randomizer_set:
            randomizer = Random()
            ChunkGenerator.set_seed(randomizer.getrandbits(64))

        chunk_string = str(x) + str(y)
        hash_base = str(ChunkGenerator.seed) + ChunkGenerator._GAME_SALT + chunk_string
        return sha256(hash_base.encode("utf-8")).hexdigest()