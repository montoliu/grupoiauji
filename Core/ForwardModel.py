# Abstract class for forward models
class ForwardModel:
    def play(self, game_state, action, heuristic):
        pass

    def check_winner(self, game_state):
        pass