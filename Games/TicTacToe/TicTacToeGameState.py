from Core.GameState import GameState
from Games.TicTacToe.TicTacToeObservation import TicTacToeObservation


class TicTacToeGameState(GameState):
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1
        self.winner = 0

    def is_terminal(self):
        if self.winner != 0:
            return True
        # empty
        elif self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0 \
                and self.board[1][0] != 0 and self.board[1][1] != 0 and self.board[1][2] != 0 \
                and self.board[2][0] != 0 and self.board[2][1] != 0 and self.board[2][2] != 0:
            return True
        return False

    def reset_board(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def get_observation(self):
        obs = TicTacToeObservation(self.board, self.turn, self.winner)
        return obs

    def __str__(self):
        s = str(self.board[0][0]) + " " + str(self.board[0][1]) + " " + str(self.board[0][2]) + "\n"
        s += str(self.board[1][0]) + " " + str(self.board[1][1]) + " " + str(self.board[1][2]) + "\n"
        s += str(self.board[2][0]) + " " + str(self.board[2][1]) + " " + str(self.board[2][2])
        return s
