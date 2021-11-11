import math
from Core.ForwardModel import ForwardModel


class BriscaForwardModel(ForwardModel):
    def play(self, gs, action, ht):
        card = action.get_card()

        # Remove card from player hand
        gs.hands[gs.turn].remove(card)

        # add to playing cards
        gs.playing_cards.add_card(card)

        # if it is the fouth, check who is the winner of this play and move cards to won set
        if gs.playing_cards.len() == 4:
            p = self.get_round_winner(gs.playing_cards, gs.trump_card, gs.turn)
            gs.won_cards[p].add_cards(gs.playing_cards.get_cards())
            gs.playing_cards.clear()
            gs.turn = p

            # draw new cards
            if not gs.main_deck.empty():
                for i in range(gs.n_players):
                    new_card = gs.main_deck.draw()
                    gs.hands[i].add_card(new_card)
        else:
            gs.turn = self.next_turn(gs.turn)



        # return reward
        return ht.get_score(gs, gs.turn)

    def next_turn(self, actual_turn):
        if actual_turn == 0:
            return 1
        elif actual_turn == 1:
            return 2
        elif actual_turn == 2:
            return 3
        elif actual_turn == 3:
            return 0

    def get_round_winner(self, playing_cards, trump_card, turn):
        winning_player = turn + 1
        if winning_player == 4:
            winning_player = 0
        best_card = playing_cards.get_card(0)

        p = winning_player
        for c in range(1, 4):
            p += 1
            if p == 4:
                p = 0

            card = playing_cards.get_card(c)

            if self.is_better_card(card, best_card, trump_card, playing_cards.get_card(0)):
                best_card = card
                winning_player = p

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
