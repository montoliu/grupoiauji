from Core.Game import Game


class TicTacToeGame(Game):
    def reset(self, game_state, player_id_as_first):
        game_state.turn = player_id_as_first          # who plays as first
        game_state.reset_board()   # empty board
        game_state.winner = 0                         # no winner
