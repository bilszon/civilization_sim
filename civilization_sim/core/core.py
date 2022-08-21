"""Core - main engine of the sim."""

import window_creator

class Core():
    """Class being the backbone of the simulation.

    Manages logic updates, graphical updates etc.
    """
    def __init__(self):
        """Create and setup the simulation
        """
        self.simulation_window = window_creator.SimulationWindow(800, 600)
    
    def begin_simulation(self) -> None:
        """Begin the simulation and enter the update loop.
        """
        # Enter the main loop and lock this thread's execution permanently.
        self.simulation_window.mainloop()

    def simulate_single_day(self):
        pass

def main():
    core = Core()
    core.begin_simulation()

if __name__ == "__main__":
    main()