import math
from Core.ForwardModel import ForwardModel


class BriscaForwardModel(ForwardModel):
    def play(self, gs, action, ht):
        card = action.get_action()
        # Remove card from player hand
        card_to_play = gs.hand[gs.turn].remove(card)

        # add to playing cards
        gs.playing_cards.add_card(card_to_play)

        # if it is the fouth, check who is the winner of this play and move cards to won set
        if gs.playing_cards.len() == 4:
            p = self.get_round_winner(gs.playing_cards, gs.trump_card, gs.turn)
            gs.won_cards[p].add_cards(gs.playing_cards.get_cards())

        # return reward
        return ht.get_score(gs, gs.turn)
        pass

    def get_round_winner(self, playing_cards, trump_card, turn):
        winning_player = turn
        best_card = playing_cards.get_card(0)

        for c in range(1,4):
            card = playing_cards.get_card(c)

            if self.is_better_card(card, best_card, trump_card, playing_cards.get_card(0)):
                best_card = card
                winning_player += 1
                if winning_player == 4:
                    winning_player = 0

        return winning_player

    def is_better_card(self, actual_card, prev_card, trump_card, round_card):
        # both cards are trump type
        if actual_card.get_type() == trump_card.get_type() and prev_card.get_type() == trump_card.get_type():
            if actual_card.get_value() > prev_card.get_value():
                return True
            else:
                return False
        elif actual_card.get_type() == trump_card.get_type():
            return True
        elif prev_card.get_type() == trump_card.get_type():
            return False
        elif actual_card.get_type() == round_card.get_type() and prev_card.get_type() == round_card.get_type():
            if actual_card.get_value() > prev_card.get_value():
                return True
            else:
                return False
        elif actual_card.get_type() == round_card.get_type():
            return True
        elif prev_card.get_type() == round_card.get_type():
            return False
        if actual_card.get_value() > prev_card.get_value():
            return True
        return False

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
