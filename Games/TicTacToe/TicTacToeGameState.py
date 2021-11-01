from Core.GameState import GameState
from Games.TicTacToe.TicTacToeObservation import TicTacToeObservation


# ---------------------------------------------------------------------------
# TicTacToe Game state
# ---------------------------------------------------------------------------
class TicTacToeGameState(GameState):
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1
        self.winner = 0

    # Returns True if the game state is terminal (it is not possible to play more), False otherwise
    # This happend when there is a winner or when there is not free space to play
    def is_terminal(self):
        if self.winner != 0:
            return True
        # No cell is empty
        elif self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0 \
                and self.board[1][0] != 0 and self.board[1][1] != 0 and self.board[1][2] != 0 \
                and self.board[2][0] != 0 and self.board[2][1] != 0 and self.board[2][2] != 0:
            return True
        return False

    def reset_board(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Returns the observable (for the Player) version o f the game state
    def get_observation(self):
        obs = TicTacToeObservation(self.board, self.turn, self.winner)
        return obs

    def __str__(self):
        s = str(self.board[0][0]) + " " + str(self.board[0][1]) + " " + str(self.board[0][2]) + "\n"
        s += str(self.board[1][0]) + " " + str(self.board[1][1]) + " " + str(self.board[1][2]) + "\n"
        s += str(self.board[2][0]) + " " + str(self.board[2][1]) + " " + str(self.board[2][2])
        return s
