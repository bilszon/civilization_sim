"""File to be run to start the whole program."""

import core.core
from core.randomizer import Randomizer

Randomizer.set_seed("Development")

core.core.main()