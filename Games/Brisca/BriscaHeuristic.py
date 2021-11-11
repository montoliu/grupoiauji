from Core.Heuristic import Heuristic


class BriscaHeuristic(Heuristic):

    # return the normalized difference between the points won by the actual player
    # and the maximum points of the opponent
    def get_score(self, observation, player_id):
        actual_player_points = 0
        best_points_opponents = 0
        for p in range(observation.n_players):
            points = 0
            cards = observation.won_cards[p].get_cards()
            for card in cards:
                points += card.get_value()

            if p == player_id:
                actual_player_points = points
            elif points > best_points_opponents:
                best_points_opponents = points

        return actual_player_points - best_points_opponents
