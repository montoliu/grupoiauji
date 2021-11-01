from Core.ForwardModel import ForwardModel


class BriscaForwardModel(ForwardModel):
    # TODO
    def play(self, game_state, action, heuristic):
        pass

    # TODO
    def check_winner(self, game_state):
        l_points = [0 for i in range(4)]

        for player in range(4):
            l_points[player] = self.calculate_points(game_state.l_won_cards[player])

    def calculate_points(self, l_cards):
        points = 0
        for card in l_cards:
            points += card.get_points()
        return points
