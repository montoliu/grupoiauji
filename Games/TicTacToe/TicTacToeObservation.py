from Core.Observation import Observation
from Games.TicTacToe.TicTacToeAction import TicTacToeAction


# ---------------------------------------------------------------------------
# In this game, all the parts of the game state are observable.
# Therefore, the observation is just a deep copy of the game state
# ---------------------------------------------------------------------------
class TicTacToeObservation(Observation):
    def __init__(self, gs_board, gs_turn, gs_winner):
        # deep copy of the board
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for r in range(3):
            for c in range(3):
                self.board[r][c] = gs_board[r][c]

        self.turn = gs_turn
        self.winner = gs_winner

    # Returns the list of possible actions that can be played from this state of the game
    def get_list_actions(self):
        l_actions = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    l_actions.append(TicTacToeAction(r, c))
        return l_actions

    # Returns a deep copy of the observation
    def clone(self):
        new_obs = TicTacToeObservation(self.board, self.turn, self.winner)
        return new_obs
