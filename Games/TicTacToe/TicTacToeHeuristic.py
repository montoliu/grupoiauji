from Core.Heuristic import Heuristic


class TicTacToeHeuristic (Heuristic):
    def get_score(self, observation, player_id):
        if observation.winner == 0:               # no winner
            return 0
        elif observation.winner == player_id:     # the player_id wins
            return 1.0
        else:                                    # the player_id loss
            return -1.0
