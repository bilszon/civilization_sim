"""Utilities for processing user input. Interface between keyboard events and the simulation."""


from core.window_creator import SimulationWindow


class InputManager():

    _INPUT_KEYS = ["w", "a", "s", "d"]

    def __init__(self, game_window: SimulationWindow):
        self.game_window = game_window
        self.game_window.window.bind("<KeyPress>", self.key_pressed)
        self.game_window.window.bind("<KeyRelease>", self.key_released)
        self.key_states = {}
        for key in InputManager._INPUT_KEYS:
            self.key_states[key] = False

    def key_pressed(self, event):
        if event.keysym in self.key_states.keys():
            self.key_states[event.keysym] = True

    def key_released(self, event):
        if event.keysym in self.key_states.keys():
            self.key_states[event.keysym] = False
    
    def isDown(self, key) -> bool:
        if key in self.key_states.keys():
            return self.key_states[key]
        return False