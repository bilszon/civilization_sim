"""Core - main engine of the sim."""

import time
from core import window_creator, graphic_engine
from core.framerate_counter import FramerateCounter

class Core():
    """Class being the backbone of the simulation.

    Manages logic updates, graphic updates etc.
    """

    _MAX_FRAMERATE = 30 # Preferred max framerate for the game

    def __init__(self):
        """Create and setup the simulation
        """

        self.simulation_window = window_creator.SimulationWindow(1600, 900)
        self.graphic_engine = graphic_engine.GraphicEngine(self.simulation_window)

        self.begin_time = time.time_ns()
    
    def begin_simulation(self) -> None:
        """Begin the simulation and enter the update loop.
        """

        self.simulation_window.window.after(0, self._main_loop)

        # Enter the main loop and lock this thread's execution permanently.
        self.simulation_window.mainloop()

    def _main_loop(self) -> None:
        """Main loop of the simulation. Repeatedly calls graphical updates, logic updates etc. Locks.
        """

        t = time.time_ns()

        #TODO: Logic update.

        self.graphic_engine.graphic_update()

        FramerateCounter.frame()

        # Wait for the next frame at least 1ms
        millis_elapsed = (time.time_ns() - t) // 1_000_000
        time_to_next_frame = max(1, 1000 // Core._MAX_FRAMERATE - millis_elapsed)

        self.simulation_window.window.after(time_to_next_frame - 10, self._main_loop) # Very dirty, framerate is shitty :-(

    def _simulate_single_day(self):
        pass

def main():
    core = Core()
    core.begin_simulation()

if __name__ == "__main__":
    main()