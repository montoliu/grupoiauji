from Core.ForwardModel import ForwardModel


class TicTacToeForwardModel(ForwardModel):
    # Uodate the board and change the turn
    def play(self, game_state, action, heuristic):
        player_id = game_state.turn
        game_state.board[action.row][action.column] = player_id
        if game_state.turn == 1:
            game_state.turn = 2
        else:
            game_state.turn = 1

        return heuristic.get_score(game_state, player_id)
