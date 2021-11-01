from Core.ForwardModel import ForwardModel


# ---------------------------------------------------------------------------
# TicTacTow rules
# ---------------------------------------------------------------------------
class TicTacToeForwardModel(ForwardModel):
    # Update the board, change the turn, check winner and return reward according to heuristic
    def play(self, game_state, action, heuristic):
        player_id = game_state.turn
        game_state.board[action.row][action.column] = player_id

        if game_state.turn == 1:
            game_state.turn = 2
        else:
            game_state.turn = 1

        game_state.winner = self.check_winner(game_state)

        return heuristic.get_score(game_state, player_id)

    # check if there is a winner
    def check_winner(self, gs):
        for player_id in range(1, 3):  # 1 and 2
            if (gs.board[0][0] == player_id and gs.board[0][1] == player_id and gs.board[0][2] == player_id) \
                    or (
                    gs.board[1][0] == player_id and gs.board[1][1] == player_id and gs.board[1][2] == player_id) \
                    or (
                    gs.board[2][0] == player_id and gs.board[2][1] == player_id and gs.board[2][2] == player_id) \
                    or (
                    gs.board[0][0] == player_id and gs.board[1][0] == player_id and gs.board[2][0] == player_id) \
                    or (
                    gs.board[0][1] == player_id and gs.board[1][1] == player_id and gs.board[2][1] == player_id) \
                    or (
                    gs.board[0][2] == player_id and gs.board[1][2] == player_id and gs.board[2][2] == player_id) \
                    or (
                    gs.board[0][0] == player_id and gs.board[1][1] == player_id and gs.board[2][2] == player_id) \
                    or (
                    gs.board[0][2] == player_id and gs.board[1][1] == player_id and gs.board[2][0] == player_id):
                return player_id
        return 0
