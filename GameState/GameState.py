

class GameState:
    def __init__(self):
        self.state = "menu"

    def change_state(self, new_state):
        self.state = new_state

game_state = GameState()