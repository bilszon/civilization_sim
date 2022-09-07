"""Core - main engine of the sim."""

from core import window_creator
from core import graphic_engine

class Core():
    """Class being the backbone of the simulation.

    Manages logic updates, graphic updates etc.
    """
    def __init__(self):
        """Create and setup the simulation
        """
        self.simulation_window = window_creator.SimulationWindow(400, 300)
        self.graphic_engine = graphic_engine.GraphicEngine(self.simulation_window)
    
    def begin_simulation(self) -> None:
        """Begin the simulation and enter the update loop.
        """
        self.simulation_window.window.after(0, self._main_loop)

        # Enter the main loop and lock this thread's execution permanently.
        self.simulation_window.mainloop()

    def _main_loop(self) -> None:
        """Main loop of the simulation. Repeatedly calls graphical updates, logic updates etc. Locks.
        """

        #TODO: Logic update.

        self.graphic_engine.graphic_update()

        #self.graphic_engine.display_chunk()

        self.simulation_window.window.after(10, self._main_loop)

    def _simulate_single_day(self):
        pass

def main():
    core = Core()
    core.begin_simulation()

if __name__ == "__main__":
    main()