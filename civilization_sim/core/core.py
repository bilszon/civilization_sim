"""Core - main engine of the sim."""

import time
from core import window_creator, graphic_engine
from core.framerate_counter import FramerateCounter
from core.input_manager import InputManager

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

        self.input_manager = InputManager(self.simulation_window)

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

        # Camera movement
        camera_speed = 10
        dx = 0
        dy = 0
        if self.input_manager.isDown("w"):
            dy -= camera_speed
        if self.input_manager.isDown("a"):
            dx -= camera_speed
        if self.input_manager.isDown("s"):
            dy += camera_speed
        if self.input_manager.isDown("d"):
            dx += camera_speed
        self.move_camera(dx, dy)

        FramerateCounter.frame()

        # Wait for the next frame at least 1ms
        millis_elapsed = (time.time_ns() - t) // 1_000_000
        time_to_next_frame = max(1, 1000 // Core._MAX_FRAMERATE - millis_elapsed)

        self.simulation_window.window.after(time_to_next_frame - 10, self._main_loop) # Very dirty, framerate is shitty :-(

    def _simulate_single_day(self):
        pass

    def move_camera(self, x: int, y: int) -> None:
        self.graphic_engine.camera_x += x
        self.graphic_engine.camera_y += y


def main():
    core = Core()
    core.begin_simulation()

if __name__ == "__main__":
    main()