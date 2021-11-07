from Core.GameState import GameState
from Games.TicTacToe.TicTacToeObservation import TicTacToeObservation


# ---------------------------------------------------------------------------
# TicTacToe Game state
# ---------------------------------------------------------------------------
class TicTacToeGameState(GameState):
    def __init__(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.turn = 0
        self.winner = -1
        self.n_players = 2

    # Returns True if the game state is terminal (it is not possible to play more), False otherwise
    # This happend when there is a winner or when there is not free space to play
    def is_terminal(self):
        if self.winner != -1:
            return True
        # No cell is empty
        elif self.board[0][0] != "_" and self.board[0][1] != "_" and self.board[0][2] != "_" \
                and self.board[1][0] != "_" and self.board[1][1] != "_" and self.board[1][2] != "_" \
                and self.board[2][0] != "_" and self.board[2][1] != "_" and self.board[2][2] != "_":
            return True
        return False

    def reset_board(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    # Returns the observable (for the player) version of the game state
    def get_observation(self):
        obs = TicTacToeObservation(self.board, self.turn, self.winner)
        return obs

    def __str__(self):
        s = self.board[0][0] + " " + self.board[0][1] + " " + self.board[0][2] + "\n"
        s += self.board[1][0] + " " + self.board[1][1] + " " + self.board[1][2] + "\n"
        s += self.board[2][0] + " " + self.board[2][1] + " " + self.board[2][2]
        return s
