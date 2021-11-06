from Core.Game import Game
from Games.Brisca.BriscaCard import BriscaCard
from Games.Brisca.BriscaCardCollection import BriscaCardCollection


class BriscaGame(Game):
    def reset(self, game_state, player_id_as_first):
        self.create_main_deck(game_state.main_deck)
        game_state.n_players = 4

        for p in range(game_state.n_players):
            hand = BriscaCardCollection()
            game_state.hands.append(hand)

        # draw three cards to each player
        for i in range(3):
            for p in range(game_state.n_players):
                card = game_state.main_deck.draw()
                game_state.hands[p].add_card(card)

        # The last card on the main deck is the leader type
        game_state.trump_card = game_state.main_deck.get_last_card()

        # cleate empty won cards
        for p in range(game_state.n_players):
            won = BriscaCardCollection()
            game_state.won_cards.append(won)

        # who play as first
        game_state.turn = player_id_as_first

        game_state.played_cards.clear()

    def create_main_deck(self, deck):
        l_types = ["O", "E", "C", "B"]
        l_numbers = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        deck.clear()
        for card_type in l_types:
            for number in l_numbers:
                deck.add_card(BriscaCard(card_type, number))

        deck.shuffle()
