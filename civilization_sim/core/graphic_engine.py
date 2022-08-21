"""Graphic engine of the simulation. Executes all drawing on the canvas.
"""

import window_creator

class GraphicEngine:
    """Engine managing drawing onscreen.
    """
    def __init__(self, simulation_window: window_creator.SimulationWindow):
        """Initialize the engine.

        Args:
            simulation_window (window_creator.SimulationWindow): Window containing the simulation. It will be updated by the engine.
        """
        self.simulation_window = simulation_window

    def graphic_update(self) -> None:
        """Redraw everything onscreen. A single frame of the simulation.
        """
        pass