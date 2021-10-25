from Core.Heuristic import Heuristic


# TODO create a unit test
class TicTacToeHeuristic (Heuristic):
    def get_score(self, game_state, player_id):
        if game_state.winner == 0:               # no winner
            return 0
        elif game_state.winner == player_id:     # the player_id wins
            return 1.0
        else:                                    # the player_id loss
            return -1.0
