from Core.ForwardModel import ForwardModel


# ---------------------------------------------------------------------------
# TicTacTow rules
# ---------------------------------------------------------------------------
class TicTacToeForwardModel(ForwardModel):
    # Update the board, change the turn, check winner and return reward according to heuristic
    def play(self, game_state, action, heuristic):
        player_id = game_state.turn
        game_state.board[action.row][action.column] = self.get_char(player_id)
        game_state.turn = self.next_turn(game_state.turn)
        game_state.winner = self.check_winner(game_state)
        return heuristic.get_score(game_state, player_id)

    def next_turn(self, turn):
        if turn == 0:
            return 1
        else:
            return 0

    # check if there is a winner
    def check_winner(self, gs):
        for player_id in range(0, 2):  # 0 and 1
            player_c = self.get_char(player_id)
            if (gs.board[0][0] == player_c and gs.board[0][1] == player_c and gs.board[0][2] == player_c) \
                    or (gs.board[1][0] == player_c and gs.board[1][1] == player_c and gs.board[1][2] == player_c) \
                    or (gs.board[2][0] == player_c and gs.board[2][1] == player_c and gs.board[2][2] == player_c) \
                    or (gs.board[0][0] == player_c and gs.board[1][0] == player_c and gs.board[2][0] == player_c) \
                    or (gs.board[0][1] == player_c and gs.board[1][1] == player_c and gs.board[2][1] == player_c) \
                    or (gs.board[0][2] == player_c and gs.board[1][2] == player_c and gs.board[2][2] == player_c) \
                    or (gs.board[0][0] == player_c and gs.board[1][1] == player_c and gs.board[2][2] == player_c) \
                    or (gs.board[0][2] == player_c and gs.board[1][1] == player_c and gs.board[2][0] == player_c):
                return player_id
        return -1

    def get_char(self, player_id):
        if player_id == 0:
            return "O"
        else:
            return "X"
