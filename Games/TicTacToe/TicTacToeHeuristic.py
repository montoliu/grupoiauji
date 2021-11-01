from Core.Heuristic import Heuristic


# ---------------------------------------------------------------------------
# If the player is the winner -> 1.0
# If the player is the losser -> -1
# Otherwise (no winner yet or Tie) -> 0.0
# ---------------------------------------------------------------------------
class TicTacToeHeuristic (Heuristic):
    def get_score(self, observation, player_id):
        if observation.winner == 0:               # no winner
            return 0
        elif observation.winner == player_id:     # the player_id wins
            return 1.0
        else:                                    # the player_id loss
            return -1.0
