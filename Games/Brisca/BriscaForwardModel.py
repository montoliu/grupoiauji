import math
from Core.ForwardModel import ForwardModel
from Games.Brisca.BriscaCommon import is_better_card, calculate_points


class BriscaForwardModel(ForwardModel):
    def play(self, gs, action, ht):
        actual_player = gs.turn

        card = action.get_card()

        # Remove card from player hand
        gs.hands[gs.turn].remove(card)

        # add to playing cards
        gs.playing_cards.add_card(card)

        # Estimate the reward
        reward = ht.get_score(gs, actual_player)

        # if it is the fouth, check who is the winner of this play and move cards to won set
        if gs.playing_cards.len() == 4:
            winner = self.get_round_winner(gs.playing_cards, gs.trump_card, gs.turn)
            gs.won_cards[winner].add_cards(gs.playing_cards.get_cards())
            gs.playing_cards.clear()
            gs.turn = winner

            # draw new cards starting by the winner
            if not gs.main_deck.empty():
                player_to_recieve_a_new_card = winner
                for i in range(gs.n_players):
                    new_card = gs.main_deck.draw()
                    gs.hands[player_to_recieve_a_new_card].add_card(new_card)
                    player_to_recieve_a_new_card += 1
                    if player_to_recieve_a_new_card == gs.n_players:
                        player_to_recieve_a_new_card = 0
        else:
            gs.turn = self.next_turn(gs.turn)

        return reward

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

            if is_better_card(card, best_card, trump_card, playing_cards.get_card(0)):
                best_card = card
                winning_player = p

        return winning_player

    # we assume 4 players
    def check_winner(self, game_state):
        if not game_state.is_terminal():
            return -1                   # no winner yet

        # the winner is the player with more points
        p0 = calculate_points(game_state.won_cards[0].get_cards()) + calculate_points(game_state.won_cards[2].get_cards())
        p1 = calculate_points(game_state.won_cards[1].get_cards()) + calculate_points(game_state.won_cards[3].get_cards())

        if p0 > p1:
            game_state.winner = 0
        else:
            game_state.winner = 1


