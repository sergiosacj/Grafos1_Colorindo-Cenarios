class Mouse:
    def __init__(self):
        self.state = False

    def set_state(self, state: bool) -> None:
        """state could be mouse pressed up or down

                Parameters:
                        state (bool=True): mouse button down
                        state (bool=False): mouse button up
                Returns:
                        None
        """
        self.state = state

    def is_mouse_button_down(self) -> bool:
        """check if state is True

                Returns:
                        True (bool): mouse button down
                        False (bool): mouse button up
        """
        return self.state
