from Core.Game import Game
from Games.Brisca.BriscaCard import BriscaCard


class BriscaGame(Game):
    def reset(self, game_state, player_id_as_first):
        self.create_main_deck(game_state.main_deck)

        # draw three cards to each player
        for i in range(3):
            for j in range(4):
                card = game_state.main_deck.draw()
                game_state.l_hand[j].append(card)

        # type first card on the main deck is the leader type
        game_state.leader_type = game_state.main_deck.l_cards[0]

        # clear won cards for each player
        for j in range(4):
            game_state.l_won_cards.clear()

        game_state.turn = player_id_as_first

    def create_main_deck(self, deck):
        l_types = ["O", "E", "C", "B"]
        l_numbers = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

        for type in l_types:
            for number in l_numbers:
                deck.append(BriscaCard(type, number))
