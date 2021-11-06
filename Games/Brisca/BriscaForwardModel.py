import math
from Core.ForwardModel import ForwardModel


class BriscaForwardModel(ForwardModel):
    def play(self, gs, action, heuristic):
        if action.get_type() == "PLAY_CARD":
            self.play_card(gs, action.get_card())


    def play_card(self, gs, card):
        # Remove card from player hand
        card_to_play = gs.hand[gs].remove(card)

        #

        # add to playing cards

        # if it is the fouth, check who is the winner of this play and move cards to won set

        # return reward
        pass

    def check_winner(self, game_state):

        if not game_state.is_terminal():
            return 0                   # no winner yet

        # the winner is the player with more points
        l_points = [0 for i in range(4)]

        best_points = -math.inf
        best_player = None
        for player in range(game_state.n_players):
            l_points[player] = self.calculate_points(game_state.l_won_cards[player])
            if l_points[player] > best_points:
                best_player = player
                best_points = l_points[player]

        return best_player + 1

    def calculate_points(self, l_cards):
        points = 0
        for card in l_cards:
            points += card.get_points()
        return points
