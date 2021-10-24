from Core.GameState import GameState
from Games.TicTacToe.TicTacToeAction import TicTacToeAction


class TicTacToeGameState(GameState):
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1
        self.winner = 0

    def get_list_actions(self):
        l_actions = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    l_actions.append(TicTacToeAction(r, c))
        return l_actions

    def is_terminal(self):
        # winner
        for player_id in range(1, 3):  # 1 and 2
            if (self.board[0][0] == player_id and self.board[0][1] == player_id and self.board[0][2] == player_id) \
                    or (
                    self.board[1][0] == player_id and self.board[1][1] == player_id and self.board[1][2] == player_id) \
                    or (
                    self.board[2][0] == player_id and self.board[2][1] == player_id and self.board[2][2] == player_id) \
                    or (
                    self.board[0][0] == player_id and self.board[1][0] == player_id and self.board[2][0] == player_id) \
                    or (
                    self.board[0][1] == player_id and self.board[1][1] == player_id and self.board[2][1] == player_id) \
                    or (
                    self.board[0][2] == player_id and self.board[1][2] == player_id and self.board[2][2] == player_id) \
                    or (
                    self.board[0][0] == player_id and self.board[1][1] == player_id and self.board[2][2] == player_id) \
                    or (
                    self.board[0][2] == player_id and self.board[1][1] == player_id and self.board[2][0] == player_id):
                self.winner = player_id
                return True

        # empty
        if self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0 \
                and self.board[1][0] != 0 and self.board[1][1] != 0 and self.board[1][2] != 0 \
                and self.board[2][0] != 0 and self.board[2][1] != 0 and self.board[2][2] != 0:
            return True
        return False

    def reset_board(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __str__(self):
        s = str(self.board[0][0]) + " " + str(self.board[0][1]) + " " + str(self.board[0][2]) + "\n"
        s += str(self.board[1][0]) + " " + str(self.board[1][1]) + " " + str(self.board[1][2]) + "\n"
        s += str(self.board[2][0]) + " " + str(self.board[2][1]) + " " + str(self.board[2][2])
        return s
