from Core.Game import Game
from Games.Gwent.GwentCard import GwentCard
from Games.Gwent.GwentCardCollection import GwentCardCollection

class GwentGame(Game):

    # initialize game state
    def reset(self, game_state, player_id_as_first):
        self.create_main_deck_0(game_state.randomized_main_deck_0)
        self.create_main_deck_1(game_state.randomized_main_deck_1)

        # create empty hands
        for i in range(game_state.players):
            hands = GwentCardCollection()
            game_state.hands.append(hands)

        # draw three cards to player 1
        for j in range(3):
            card = game_state.randomized_main_deck_0.draw()
            game_state.hands.append(hands)

        # draw three cards to player 2
        for k in range(3):
            card = game_state.randomized_main_deck_1.draw()
            game_state.hands.append(hands)

        # reset board
        game_state.terrain_p1.clear()
        game_state.terrain_p2.clear()

        # reset lives nad points
        game_state.lives_p1 = 3
        game_state.lives_p2 = 3
        game_state.points_p1 = 0
        game_state.points_p2 = 0

        # who play as first
        game_state.turn = player_id_as_first

    def create_main_deck_0(self, deck):
        l_types = ["Melee", "Ranged", "Artillery"]
        deck.clear()
        for card_type in l_types:
            deck.add_card(GwentCard(card_type, 1, 0))

        deck.shuffle()

    def create_main_deck_1(self, deck):
        l_types = ["Melee", "Ranged", "Artillery"]
        deck.clear()
        for card_type in l_types:
            deck.add_card(GwentCard(card_type, 1, 0))

        deck.shuffle()