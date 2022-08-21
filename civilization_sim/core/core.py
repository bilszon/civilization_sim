# Core - main engine of the sim.

import window_creator

def setup():
    simulation_window = window_creator.simulation_window(800, 600)
    simulation_window.mainloop()

def simulate_single_day():
    pass

setup()